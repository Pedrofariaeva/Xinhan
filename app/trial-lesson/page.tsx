import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import Link from 'next/link'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'
import { existsSync } from 'fs'
import { join } from 'path'

async function getUser() {
  const cookieStore = await cookies()
  const token = cookieStore.get(COOKIE_NAME)?.value
  if (!token) redirect('/signin?next=/trial-lesson')
  const user = await verifyToken(token)
  if (!user) redirect('/signin?next=/trial-lesson')
  return user
}

const LEVELS = [
  { id: 'hsk-1', label: 'HSK 1', desc: 'Start here — basic words and short sentences.' },
  { id: 'hsk-2', label: 'HSK 2', desc: 'Simple daily conversations.' },
  { id: 'hsk-3', label: 'HSK 3', desc: 'Original lesson difficulty.' },
  { id: 'hsk-4', label: 'HSK 4', desc: 'Longer dialogues and more grammar.' },
  { id: 'hsk-5', label: 'HSK 5', desc: 'Natural, nuanced Chinese.' },
  { id: 'hsk-6', label: 'HSK 6', desc: 'Fluent, idiomatic, and formal language.' },
]

const STORIES = [
  { id: 'luckin-coffee', titleZh: '点咖啡', titleEn: 'Ordering Coffee', icon: '☕', color: '#4a3b32' },
  { id: 'mood-weather', titleZh: '心情和天气', titleEn: 'Mood & Weather', icon: '🌤️', color: '#e8f4fd' },
  { id: 'banjia', titleZh: '搬家', titleEn: 'Moving House', icon: '🏠', color: '#d8f3dc' },
  { id: 'many-ways', titleZh: '一句话，几种说法？', titleEn: 'One Idea, Many Sentences', icon: '🗣️', color: '#fff5eb' },
  { id: 'mood-weather-v2', titleZh: '心情和天气', titleEn: 'Mood & Weather (new version)', icon: '☀️', color: '#e8f4fd' },
  { id: 'party-game', titleZh: '是还是不是？', titleEn: 'Yes or No? Party Game', icon: '🎉', color: '#312e81' },
]

function deckExists(level: string, storyId: string) {
  const path = join(process.cwd(), 'public', 'trial-lesson', level, storyId, 'index.html')
  return existsSync(path)
}

export default async function TrialLessonHubPage() {
  const user = await getUser()

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
          <Link href="/dashboard" className="btn-outline">Back to dashboard</Link>
        </div>
      </div>

      <div className="dashboard-body">
        <div className="dashboard-welcome">Free Trial Lessons 👋 {user.name.split(' ')[0]}</div>
        <div className="dashboard-sub">
          Pick your HSK level, then choose a story. Each lesson ends with a short quiz and saves your score.
        </div>

        {LEVELS.map((level) => (
          <div key={level.id} style={{ marginTop: '2.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: '0.75rem', marginBottom: '0.5rem' }}>
              <h2 style={{ fontSize: '1.35rem', margin: 0 }}>{level.label}</h2>
              <span style={{ color: '#7a7a7a', fontSize: '14px' }}>{level.desc}</span>
            </div>
            <div className="dashboard-grid">
              {STORIES.map((story) => {
                const hasDeck = deckExists(level.id, story.id)
                return (
                  <Link
                    key={`${level.id}-${story.id}`}
                    href={`/trial-lesson/${level.id}/${story.id}`}
                    style={{ textDecoration: 'none', color: 'inherit' }}
                  >
                    <div
                      className="dash-card"
                      style={{
                        cursor: 'pointer',
                        height: '100%',
                        opacity: hasDeck ? 1 : 0.72,
                        position: 'relative',
                      }}
                    >
                      {!hasDeck && (
                        <span
                          style={{
                            position: 'absolute',
                            top: '0.75rem',
                            right: '0.75rem',
                            fontSize: '0.55rem',
                            fontWeight: 700,
                            textTransform: 'uppercase',
                            letterSpacing: '0.06em',
                            color: '#9b2226',
                            background: '#fff0ee',
                            padding: '0.2rem 0.5rem',
                            borderRadius: '999px',
                          }}
                        >
                          Soon
                        </span>
                      )}
                      <div className="dash-card-icon" style={{ background: story.color }}>
                        {story.icon}
                      </div>
                      <div style={{ fontSize: '12px', color: '#7a7a7a', marginBottom: '6px' }}>
                        {level.label}
                      </div>
                      <h3>{story.titleZh}</h3>
                      <p>{story.titleEn}</p>
                      <span className="dash-card-link">
                        {hasDeck ? 'Start lesson →' : 'Preview page →'}
                      </span>
                    </div>
                  </Link>
                )
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
