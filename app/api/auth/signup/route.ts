import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { hashPassword } from '@/lib/auth'
import { signToken, COOKIE_NAME, COOKIE_MAX_AGE } from '@/lib/auth-edge'

export async function POST(req: NextRequest) {
  try {
    const body = await req.json()
    const { name, email, password, role } = body as {
      name: string
      email: string
      password: string
      role?: string
    }

    if (!name?.trim() || !email?.trim() || !password) {
      return NextResponse.json(
        { error: 'All fields are required.' },
        { status: 400 }
      )
    }

    if (password.length < 6) {
      return NextResponse.json(
        { error: 'Password must be at least 6 characters.' },
        { status: 400 }
      )
    }

    const db = await getDb()
    const users = db.collection('users')

    const existing = await users.findOne({ email: email.toLowerCase().trim() })
    if (existing) {
      return NextResponse.json(
        { error: 'An account with this email already exists.' },
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
    })

    const token = await signToken({
      userId: result.insertedId.toString(),
      email: email.toLowerCase().trim(),
      name: name.trim(),
      role: role || 'student',
    })

    const response = NextResponse.json({ ok: true, name: name.trim() })
    response.cookies.set(COOKIE_NAME, token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: COOKIE_MAX_AGE,
      path: '/',
    })
    return response
  } catch (err) {
    console.error('[signup]', err)
    return NextResponse.json(
      { error: 'Something went wrong. Please try again.' },
      { status: 500 }
    )
  }
}
