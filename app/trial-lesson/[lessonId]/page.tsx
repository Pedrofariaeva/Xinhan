import { cookies } from 'next/headers'
import { redirect, notFound } from 'next/navigation'
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

const LESSONS: Record<string, { titleZh: string; titleEn: string; level: string }> = {
  // Progressive HSK cycle
  'hsk-1': { titleZh: '你好！', titleEn: 'Hello!', level: 'HSK 1' },
  'hsk-2': { titleZh: '我要一杯咖啡', titleEn: 'I Want a Cup of Coffee', level: 'HSK 2' },
  'hsk-3': { titleZh: '你的爱好是什么？', titleEn: 'What Are Your Hobbies?', level: 'HSK 3' },
  'hsk-4': { titleZh: '旅行计划', titleEn: 'Travel Plans', level: 'HSK 4' },
  'hsk-5': { titleZh: '职业与发展', titleEn: 'Career & Development', level: 'HSK 5' },
  'hsk-6': { titleZh: '科技与社会', titleEn: 'Technology & Society', level: 'HSK 6' },
  // Extra trial lessons
  'luckin-coffee': { titleZh: '点咖啡', titleEn: 'Ordering Coffee', level: 'HSK 2–3' },
  banjia: { titleZh: '搬家', titleEn: 'Moving House', level: 'HSK 2–3' },
  'mood-weather': { titleZh: '心情和天气', titleEn: 'Mood & Weather', level: 'HSK 2–3' },
  'many-ways': { titleZh: '一句话，几种说法？', titleEn: 'One Idea, Many Sentences', level: 'HSK 3' },
  'mood-weather-v2': { titleZh: '心情和天气', titleEn: 'Mood & Weather (new version)', level: 'HSK 2–3' },
}

interface PageProps {
  params: Promise<{ lessonId: string }>
}

export default async function TrialLessonPlayerPage({ params }: PageProps) {
  const user = await getUser()
  const { lessonId } = await params
  const lesson = LESSONS[lessonId]
  if (!lesson) notFound()

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
        <div className="dashboard-welcome">{lesson.titleZh} · {lesson.titleEn}</div>
        <div className="dashboard-sub">
          {lesson.level} free trial lesson — scroll through the slides, then take the quiz at the end. Your score will be saved.
        </div>

        <iframe
          src={`/trial-lesson/${lessonId}/index.html`}
          title={`${lesson.titleZh} — ${lesson.titleEn} trial lesson`}
          style={{
            width: '100%',
            height: '85vh',
            border: '1px solid #e5e0d8',
            borderRadius: '12px',
            marginTop: '1.5rem',
          }}
        />
      </div>
    </div>
  )
}
