import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

// Upserts the final grade for one (user, lesson) pair. Called once when a
// learner finishes every test block in a lesson. Generic across lessons.
export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get(COOKIE_NAME)?.value
    if (!token) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })
    const payload = await verifyToken(token)
    if (!payload) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })

    const body = await req.json().catch(() => null)
    if (!body) return NextResponse.json({ error: 'Invalid request body.' }, { status: 400 })

    const { lessonId, score, total, groups } = body as {
      lessonId: string
      score: number
      total: number
      groups: { groupId: string; score: number; total: number }[]
    }

    if (!lessonId || typeof score !== 'number' || typeof total !== 'number') {
      return NextResponse.json({ error: 'Missing lessonId, score, or total.' }, { status: 400 })
    }

    const db = await getDb()
    await db.collection('lesson_results').updateOne(
      { userId: payload.userId, lessonId },
      {
        $set: {
          userId: payload.userId,
          lessonId,
          score,
          total,
          percentage: total > 0 ? Math.round((score / total) * 100) : 0,
          groups: groups ?? [],
          completedAt: new Date(),
        },
      },
      { upsert: true }
    )

    return NextResponse.json({ ok: true })
  } catch (err) {
    return NextResponse.json(
      { error: err instanceof Error ? err.message : 'Unexpected error.' },
      { status: 500 }
    )
  }
}
