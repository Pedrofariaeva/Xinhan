import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import Link from 'next/link'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'
import { getDb } from '@/lib/mongodb'

async function getUser() {
  const cookieStore = await cookies()
  const token = cookieStore.get(COOKIE_NAME)?.value
  if (!token) redirect('/signin?next=/dashboard/progress')
  const user = await verifyToken(token)
  if (!user) redirect('/signin?next=/dashboard/progress')
  return user
}

interface LessonResult {
  lessonId: string
  score: number
  total: number
  percentage: number
  completedAt: string
  groups?: { groupId: string; score: number; total: number }[]
}

const STORY_TITLES: Record<string, { zh: string; en: string }> = {
  'banjia': { zh: '搬家', en: 'Moving House' },
  'luckin-coffee': { zh: '点咖啡', en: 'Ordering Coffee' },
  'mood-weather': { zh: '心情和天气', en: 'Mood & Weather' },
  'many-ways': { zh: '一句话，几种说法？', en: 'One Idea, Many Sentences' },
  'mood-weather-v2': { zh: '心情和天气', en: 'Mood & Weather (new version)' },
}

function parseLessonId(lessonId: string) {
  const parts = lessonId.split('/')
  if (parts.length !== 2) return null
  const [level, storyId] = parts
  const story = STORY_TITLES[storyId]
  if (!story) return null
  const levelLabel = level.replace('hsk-', 'HSK ')
  return { level, levelLabel, storyId, ...story }
}

export default async function ProgressPage() {
  const user = await getUser()
  const db = await getDb()

  const results = await db
    .collection('lesson_results')
    .find({ userId: user.userId })
    .sort({ completedAt: -1 })
    .toArray()

  const typedResults: LessonResult[] = results.map((r) => ({
    lessonId: r.lessonId,
    score: r.score,
    total: r.total,
    percentage: r.percentage,
    completedAt: r.completedAt,
    groups: r.groups,
  }))

  const completedLessons = typedResults.length
  const totalScore = typedResults.reduce((sum, r) => sum + r.score, 0)
  const totalQuestions = typedResults.reduce((sum, r) => sum + r.total, 0)
  const overallPct = totalQuestions > 0 ? Math.round((totalScore / totalQuestions) * 100) : 0

  return (
    <div className="dashboard-wrapper">
      <div className="dashboard-nav">
        <div className="dashboard-nav-inner">
          <Link href="/" className="logo">
            <div className="logo-mark">新</div>
            <div className="logo-text">
              Xinhan<span>Chinese Language School</span>
            </div>
          </Link>
          <Link href="/dashboard" className="btn-outline">← Back to dashboard</Link>
        </div>
      </div>

      <div className="dashboard-body">
        <div className="dashboard-welcome">My Progress 📊 {user.name.split(' ')[0]}</div>
        <div className="dashboard-sub">
          Track your completed trial lessons and scores across all HSK levels.
        </div>

        <div className="dashboard-grid" style={{ marginBottom: '2.5rem' }}>
          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#d8f3dc' }}>📚</div>
            <h3>{completedLessons}</h3>
            <p>Lessons completed</p>
          </div>
          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#fff3d0' }}>🎯</div>
            <h3>{overallPct}%</h3>
            <p>Overall accuracy</p>
          </div>
          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#dce5f3' }}>✅</div>
            <h3>{totalScore}/{totalQuestions}</h3>
            <p>Total correct answers</p>
          </div>
        </div>

        {typedResults.length === 0 ? (
          <div
            style={{
              background: '#faf7f2',
              border: '1px dashed #d6cfc4',
              borderRadius: '12px',
              padding: '2rem',
              textAlign: 'center',
            }}
          >
            <div style={{ fontSize: '2.5rem', marginBottom: '0.75rem' }}>📝</div>
            <h3 style={{ marginBottom: '0.5rem' }}>No scores yet</h3>
            <p style={{ color: '#7a7a7a', marginBottom: '1.25rem' }}>
              Complete a trial lesson and your score will appear here.
            </p>
            <Link href="/trial-lesson" className="btn-primary">Start a trial lesson →</Link>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {typedResults.map((result) => {
              const parsed = parseLessonId(result.lessonId)
              const pct = result.percentage ?? (result.total > 0 ? Math.round((result.score / result.total) * 100) : 0)
              const color = pct >= 80 ? '#2d6a4f' : pct >= 60 ? '#b7791f' : '#9b2226'
              const bg = pct >= 80 ? '#d8f3dc' : pct >= 60 ? '#fff3d0' : '#fff0ee'

              return (
                <div
                  key={result.lessonId}
                  style={{
                    background: '#fff',
                    border: '1px solid #e5e0d8',
                    borderRadius: '12px',
                    padding: '1.25rem 1.5rem',
                    display: 'flex',
                    flexWrap: 'wrap',
                    gap: '1rem',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                  }}
                >
                  <div style={{ flex: 1, minWidth: '220px' }}>
                    <div style={{ fontSize: '0.7rem', color: '#7a7a7a', marginBottom: '0.25rem' }}>
                      {parsed?.levelLabel ?? result.lessonId}
                    </div>
                    <div style={{ fontWeight: 600, fontSize: '1.1rem' }}>
                      {parsed ? `${parsed.zh} · ${parsed.en}` : result.lessonId}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#7a7a7a', marginTop: '0.25rem' }}>
                      Completed {new Date(result.completedAt).toLocaleString()}
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
                    {result.groups && result.groups.length > 0 && (
                      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                        {result.groups.map((g) => (
                          <span
                            key={g.groupId}
                            style={{
                              fontSize: '0.65rem',
                              background: '#faf7f2',
                              padding: '0.25rem 0.5rem',
                              borderRadius: '999px',
                              color: '#3d3d3d',
                            }}
                          >
                            {g.groupId}: {g.score}/{g.total}
                          </span>
                        ))}
                      </div>
                    )}
                    <div
                      style={{
                        background: bg,
                        color: color,
                        padding: '0.5rem 1rem',
                        borderRadius: '999px',
                        fontWeight: 700,
                        fontSize: '0.9rem',
                        minWidth: '70px',
                        textAlign: 'center',
                      }}
                    >
                      {pct}%
                    </div>
                    <div style={{ color: '#3d3d3d', fontSize: '0.85rem', minWidth: '60px', textAlign: 'right' }}>
                      {result.score}/{result.total}
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}
