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

export default async function TrialLessonPage() {
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
        <div className="dashboard-welcome">点咖啡 · Ordering Coffee 👋 {user.name.split(' ')[0]}</div>
        <div className="dashboard-sub">
          A free trial lesson — vocabulary, dialogue, and a real-screenshot interface quiz from the Luckin Coffee app.
        </div>

        <iframe
          src="/trial-lesson/index.html"
          title="点咖啡 — Ordering Coffee trial lesson"
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
