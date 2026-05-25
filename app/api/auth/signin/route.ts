import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { comparePassword } from '@/lib/auth'
import { signToken, COOKIE_NAME, COOKIE_MAX_AGE } from '@/lib/auth-edge'

export async function POST(req: NextRequest) {
  try {
    const { email, password } = await req.json() as {
      email: string
      password: string
    }

    if (!email?.trim() || !password) {
      return NextResponse.json(
        { error: 'Email and password are required.' },
        { status: 400 }
      )
    }

    const db = await getDb()
    const users = db.collection('users')
    const user = await users.findOne({ email: email.toLowerCase().trim() })

    if (!user || !(await comparePassword(password, user.password as string))) {
      return NextResponse.json(
        { error: 'Invalid email or password.' },
        { status: 401 }
      )
    }

    const token = await signToken({
      userId: user._id.toString(),
      email: user.email as string,
      name: user.name as string,
      role: user.role as string,
    })

    const response = NextResponse.json({ ok: true, name: user.name })
    response.cookies.set(COOKIE_NAME, token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: COOKIE_MAX_AGE,
      path: '/',
    })
    return response
  } catch (err) {
    console.error('[signin]', err)
    return NextResponse.json(
      { error: 'Something went wrong. Please try again.' },
      { status: 500 }
    )
  }
}
