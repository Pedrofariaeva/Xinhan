import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import Link from 'next/link'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

async function getUser() {
  const cookieStore = await cookies()
  const token = cookieStore.get(COOKIE_NAME)?.value
  if (!token) redirect('/signin?next=/trial-lesson')
  const user = await verifyToken(token)
  if (!user) redirect('/signin?next=/trial-lesson')
  return user
}

const LESSONS = [
  {
    id: 'luckin-coffee',
    titleZh: '点咖啡',
    titlePy: 'Diǎn Kāfēi',
    titleEn: 'Ordering Coffee',
    level: 'HSK 2–3',
    icon: '☕',
    color: '#4a3b32',
    desc: 'The original Luckin Coffee trial lesson — ordering in a Chinese café.',
  },
  {
    id: 'mood-weather',
    titleZh: '心情和天气',
    titlePy: 'Xīnqíng hé Tiānqì',
    titleEn: 'Mood & Weather',
    level: 'HSK 2–3',
    icon: '🌤️',
    color: '#e8f4fd',
    desc: 'Talk about how weather affects the way you feel.',
  },
  {
    id: 'banjia',
    titleZh: '搬家',
    titlePy: 'Bānjiā',
    titleEn: 'Moving House',
    level: 'HSK 2–3',
    icon: '🏠',
    color: '#d8f3dc',
    desc: 'Learn vocabulary and sentences for moving house and describing a new home.',
  },
  {
    id: 'many-ways',
    titleZh: '一句话，几种说法？',
    titlePy: 'Yí Jù Huà, Jǐ Zhǒng Shuōfǎ?',
    titleEn: 'One Idea, Many Sentences',
    level: 'HSK 3',
    icon: '🗣️',
    color: '#fff5eb',
    desc: 'Discover how native speakers say the same thing in many different ways.',
  },
  {
    id: 'mood-weather-v2',
    titleZh: '心情和天气',
    titlePy: 'Xīnqíng hé Tiānqì v2',
    titleEn: 'Mood & Weather (new version)',
    level: 'HSK 2–3',
    icon: '☀️',
    color: '#e8f4fd',
    desc: 'A fresh take on weather and mood with drawings and pictures.',
  },
]

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
          Pick a topic below. Each lesson ends with a short quiz and saves your score so you can track progress.
        </div>

        <div className="dashboard-grid">
          {LESSONS.map((lesson, index) => (
            <Link
              key={lesson.id}
              href={`/trial-lesson/${lesson.id}`}
              style={{ textDecoration: 'none', color: 'inherit' }}
            >
              <div className="dash-card" style={{ cursor: 'pointer', height: '100%' }}>
                <div
                  className="dash-card-icon"
                  style={{ background: lesson.color }}
                >
                  {lesson.icon}
                </div>
                <div style={{ fontSize: '12px', color: '#7a7a7a', marginBottom: '6px' }}>
                  Step {index + 1} · {lesson.level}
                </div>
                <h3>{lesson.titleZh}</h3>
                <p style={{ marginBottom: '4px' }}>{lesson.titleEn}</p>
                <p style={{ fontSize: '13px', color: '#b7791f' }}>{lesson.titlePy}</p>
                <p>{lesson.desc}</p>
                <span className="dash-card-link">Start lesson →</span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
