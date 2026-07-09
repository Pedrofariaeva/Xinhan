import { cookies } from 'next/headers'
import { redirect, notFound } from 'next/navigation'
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

const LEVELS = ['hsk-1', 'hsk-2', 'hsk-3', 'hsk-4', 'hsk-5', 'hsk-6']

const STORIES: Record<string, { titleZh: string; titleEn: string }> = {
  'luckin-coffee': { titleZh: '点咖啡', titleEn: 'Ordering Coffee' },
  'mood-weather': { titleZh: '心情和天气', titleEn: 'Mood & Weather' },
  'banjia': { titleZh: '搬家', titleEn: 'Moving House' },
  'many-ways': { titleZh: '一句话，几种说法？', titleEn: 'One Idea, Many Sentences' },
  'mood-weather-v2': { titleZh: '心情和天气', titleEn: 'Mood & Weather (new version)' },
  'party-game': { titleZh: '是还是不是？', titleEn: 'Yes or No? Party Game' },
}

function deckFile(storyId: string) {
  return storyId === 'party-game' ? 'game.html' : 'index.html'
}

function deckExists(level: string, storyId: string) {
  const path = join(process.cwd(), 'public', 'trial-lesson', level, storyId, deckFile(storyId))
  return existsSync(path)
}

interface PageProps {
  params: Promise<{ level: string; storyId: string }>
}

export default async function TrialLessonStoryLevelPage({ params }: PageProps) {
  const user = await getUser()
  const { level, storyId } = await params

  if (!LEVELS.includes(level) || !STORIES[storyId]) {
    notFound()
  }

  const story = STORIES[storyId]
  const levelLabel = level.replace('hsk-', 'HSK ')
  const hasDeck = deckExists(level, storyId)

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
          <Link href="/trial-lesson" className="btn-outline">← Choose another lesson</Link>
        </div>
      </div>

      <div className="dashboard-body">
        <div className="dashboard-welcome">{story.titleZh} · {story.titleEn}</div>
        <div className="dashboard-sub">
          {levelLabel} free trial lesson — scroll through the slides, then take the quiz at the end. Your score will be saved.
        </div>

        {hasDeck ? (
          <iframe
            src={`/trial-lesson/${level}/${storyId}/${deckFile(storyId)}`}
            title={`${story.titleZh} — ${story.titleEn} ${levelLabel} trial lesson`}
            style={{
              width: '100%',
              height: '85vh',
              border: '1px solid #e5e0d8',
              borderRadius: '12px',
              marginTop: '1.5rem',
            }}
          />
        ) : (
          <div
            style={{
              marginTop: '1.5rem',
              padding: '3rem 2rem',
              background: '#faf7f2',
              border: '1px dashed #d6cfc4',
              borderRadius: '12px',
              textAlign: 'center',
            }}
          >
            <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🚧</div>
            <h3 style={{ marginBottom: '0.5rem' }}>{levelLabel} version coming soon</h3>
            <p style={{ color: '#7a7a7a', maxWidth: '520px', margin: '0 auto 1.5rem' }}>
              We are still preparing the {levelLabel} adaptation of this lesson.
              Try the HSK 3 version below, or choose another level.
            </p>
            <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'center', flexWrap: 'wrap' }}>
              <Link href={`/trial-lesson/hsk-3/${storyId}`} className="btn-primary">
                Try HSK 3 version →
              </Link>
              <Link href="/trial-lesson" className="btn-outline">
                ← Back to lessons
              </Link>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
