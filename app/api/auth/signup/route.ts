import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { hashPassword } from '@/lib/auth'
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

    const { name, email, password, role } = body as {
      name: string
      email: string
      password: string
      role?: string
    }

    // Field-level validation with specific messages
    if (!name?.trim()) {
      return NextResponse.json({ error: 'Full name is required.' }, { status: 400 })
    }
    if (!email?.trim()) {
      return NextResponse.json({ error: 'Email address is required.' }, { status: 400 })
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim())) {
      return NextResponse.json({ error: 'Please enter a valid email address.' }, { status: 400 })
    }
    if (!password) {
      return NextResponse.json({ error: 'Password is required.' }, { status: 400 })
    }
    if (password.length < 6) {
      return NextResponse.json(
        { error: 'Password must be at least 6 characters long.' },
        { status: 400 }
      )
    }

    const db = await getDb()
    const users = db.collection('users')

    const existing = await users.findOne({ email: email.toLowerCase().trim() })
    if (existing) {
      return NextResponse.json(
        { error: 'An account with this email already exists. Try signing in instead.' },
        { status: 409 }
      )
    }

    const hashedPassword = await hashPassword(password)
    const result = await users.insertOne({
      name: name.trim(),
      email: email.toLowerCase().trim(),
      password: hashedPassword,
      role: role || 'student',
      createdAt: new Date(),
      updatedAt: new Date(),
    })

    const token = await signToken({
      userId: result.insertedId.toString(),
      email: email.toLowerCase().trim(),
      name: name.trim(),
      role: role || 'student',
    })

    const response = NextResponse.json({
      ok: true,
      message: 'Account created successfully!',
      name: name.trim(),
      role: role || 'student',
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
    console.error('[signup] Unexpected error:', err)
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
