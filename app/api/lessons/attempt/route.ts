import { NextRequest, NextResponse } from 'next/server'
import { getDb } from '@/lib/mongodb'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

// Logs a single answer for any lesson. Generic across lessons — lessonId
// identifies which lesson, groupId identifies which learn/test block within it.
// Never blocks the lesson UI: the deck fires this and ignores failures.
export async function POST(req: NextRequest) {
  try {
    const token = req.cookies.get(COOKIE_NAME)?.value
    if (!token) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })
    const payload = await verifyToken(token)
    if (!payload) return NextResponse.json({ error: 'Not authenticated' }, { status: 401 })

    const body = await req.json().catch(() => null)
    if (!body) return NextResponse.json({ error: 'Invalid request body.' }, { status: 400 })

    const { lessonId, groupId, questionIndex, questionText, userAnswer, correct } = body as {
      lessonId: string
      groupId: string
      questionIndex: number
      questionText: string
      userAnswer: string
      correct: boolean
    }

    if (!lessonId || !groupId || typeof correct !== 'boolean') {
      return NextResponse.json({ error: 'Missing lessonId, groupId, or correct.' }, { status: 400 })
    }

    const db = await getDb()
    await db.collection('lesson_attempts').insertOne({
      userId: payload.userId,
      lessonId,
      groupId,
      questionIndex: questionIndex ?? null,
      questionText: questionText ?? '',
      userAnswer: userAnswer ?? '',
      correct,
      answeredAt: new Date(),
    })

    return NextResponse.json({ ok: true })
  } catch (err) {
    return NextResponse.json(
      { error: err instanceof Error ? err.message : 'Unexpected error.' },
      { status: 500 }
    )
  }
}
