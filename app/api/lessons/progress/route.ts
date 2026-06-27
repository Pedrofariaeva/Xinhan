import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

// Returns the signed-in user's final grades across all lessons (or one
// lesson via ?lessonId=). For future use by a student dashboard.
export async function GET(req: NextRequest) {
  const token = req.cookies.get(COOKIE_NAME)?.value
  if (!token) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })
  const payload = await verifyToken(token)
  if (!payload) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })

  const lessonId = req.nextUrl.searchParams.get('lessonId')
  const db = await getDb()
  const query: Record<string, unknown> = { userId: payload.userId }
  if (lessonId) query.lessonId = lessonId

  const results = await db
    .collection('lesson_results')
    .find(query)
    .sort({ completedAt: -1 })
    .toArray()

  return NextResponse.json({ results })
}
