import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { comparePassword } from '@/lib/auth'
import { signToken, COOKIE_NAME, COOKIE_MAX_AGE } from '@/lib/auth-edge'

export async function POST(req: NextRequest) {
  try {
    const body = await req.json().catch(() => null)

    if (!body) {
      return NextResponse.json(
        { error: 'Invalid request body.' },
        { status: 400 }
      )
    }

    const { email, password } = body as { email: string; password: string }

    if (!email?.trim()) {
      return NextResponse.json({ error: 'Email is required.' }, { status: 400 })
    }
    if (!password) {
      return NextResponse.json({ error: 'Password is required.' }, { status: 400 })
    }

    const db = await getDb()
    const users = db.collection('users')
    const user = await users.findOne({ email: email.toLowerCase().trim() })

    if (!user) {
      return NextResponse.json(
        { error: 'No account found with this email address.' },
        { status: 404 }
      )
    }

    const isMatch = await comparePassword(password, user.password as string)
    if (!isMatch) {
      return NextResponse.json(
        { error: 'Incorrect password. Please try again.' },
        { status: 401 }
      )
    }

    const token = await signToken({
      userId: user._id.toString(),
      email: user.email as string,
      name: user.name as string,
      role: user.role as string,
    })

    const response = NextResponse.json({
      ok: true,
      message: 'Signed in successfully.',
      name: user.name,
      role: user.role,
    })

    response.cookies.set(COOKIE_NAME, token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: COOKIE_MAX_AGE,
      path: '/',
    })

    return response
  } catch (err) {
    console.error('[signin] Unexpected error:', err)
    return NextResponse.json(
      {
        error:
          err instanceof Error
            ? err.message
            : 'An unexpected error occurred. Please try again.',
      },
      { status: 500 }
    )
  }
}
