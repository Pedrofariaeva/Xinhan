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

const HSK_CYCLE = [
  {
    id: 'hsk-1',
    titleZh: '你好！',
    titlePy: 'Nǐ hǎo!',
    titleEn: 'Hello!',
    level: 'HSK 1',
    icon: '👋',
    color: '#d8f3dc',
    desc: 'Greetings & self-introduction with only HSK 1 words.',
  },
  {
    id: 'hsk-2',
    titleZh: '我要一杯咖啡',
    titlePy: 'Wǒ yào yì bēi kāfēi',
    titleEn: 'I Want a Cup of Coffee',
    level: 'HSK 2',
    icon: '☕',
    color: '#fff5eb',
    desc: 'Order drinks and food with HSK 2 vocabulary.',
  },
  {
    id: 'hsk-3',
    titleZh: '你的爱好是什么？',
    titlePy: 'Nǐ de àihào shì shénme?',
    titleEn: 'What Are Your Hobbies?',
    level: 'HSK 3',
    icon: '🎸',
    color: '#e8f4fd',
    desc: 'Talk about hobbies and weekend plans at HSK 3.',
  },
  {
    id: 'hsk-4',
    titleZh: '旅行计划',
    titlePy: 'Lǚxíng jìhuà',
    titleEn: 'Travel Plans',
    level: 'HSK 4',
    icon: '✈️',
    color: '#fff0ee',
    desc: 'Plan trips, compare options, and book at HSK 4.',
  },
  {
    id: 'hsk-5',
    titleZh: '职业与发展',
    titlePy: 'Zhíyè yǔ fāzhǎn',
    titleEn: 'Career & Development',
    level: 'HSK 5',
    icon: '💼',
    color: '#f3e8ff',
    desc: 'Discuss work, goals, and professional choices at HSK 5.',
  },
  {
    id: 'hsk-6',
    titleZh: '科技与社会',
    titlePy: 'Kējì yǔ shèhuì',
    titleEn: 'Technology & Society',
    level: 'HSK 6',
    icon: '🌐',
    color: '#ede9fe',
    desc: 'Debate technology, social change, and future trends at HSK 6.',
  },
]

const EXTRA_LESSONS = [
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

function LessonCard({ lesson }: { lesson: (typeof HSK_CYCLE)[0] }) {
  return (
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
          {lesson.level}
        </div>
        <h3>{lesson.titleZh}</h3>
        <p style={{ marginBottom: '4px' }}>{lesson.titleEn}</p>
        <p style={{ fontSize: '13px', color: '#b7791f' }}>{lesson.titlePy}</p>
        <p>{lesson.desc}</p>
        <span className="dash-card-link">Start lesson →</span>
      </div>
    </Link>
  )
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
          Pick a topic below. Each lesson ends with a short quiz and saves your score so you can track progress.
        </div>

        <h2 style={{ margin: '2rem 0 1rem', fontSize: '1.1rem', color: '#3d3d3d' }}>
          Progressive HSK Cycle · 渐进式 HSK 课程
        </h2>
        <div className="dashboard-grid">
          {HSK_CYCLE.map((lesson) => (
            <LessonCard key={lesson.id} lesson={lesson} />
          ))}
        </div>

        <h2 style={{ margin: '2.5rem 0 1rem', fontSize: '1.1rem', color: '#3d3d3d' }}>
          More Trial Lessons · 更多试听课
        </h2>
        <div className="dashboard-grid">
          {EXTRA_LESSONS.map((lesson) => (
            <LessonCard key={lesson.id} lesson={lesson} />
          ))}
        </div>
      </div>
    </div>
  )
}
