import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import Link from 'next/link'
import { verifyToken, COOKIE_NAME } from '@/lib/auth'
import SignOutButton from './SignOutButton'

async function getUser() {
  const cookieStore = await cookies()
  const token = cookieStore.get(COOKIE_NAME)?.value
  if (!token) redirect('/signin')
  const user = await verifyToken(token)
  if (!user) redirect('/signin')
  return user
}

export default async function DashboardPage() {
  const user = await getUser()

  return (
    <div className="dashboard-wrapper">
      {/* Dashboard Nav */}
      <div className="dashboard-nav">
        <div className="dashboard-nav-inner">
          <Link href="/" className="logo">
            <div className="logo-mark">新</div>
            <div className="logo-text">
              Xinhan<span>Chinese Language School</span>
            </div>
          </Link>
          <SignOutButton />
        </div>
      </div>

      {/* Dashboard Content */}
      <div className="dashboard-body">
        <div className="dashboard-welcome">
          Welcome back, {user.name.split(' ')[0]} 👋
        </div>
        <div className="dashboard-sub">
          {user.role === 'teacher'
            ? 'Manage your classes and student progress.'
            : "Here's your learning journey at a glance."}
        </div>

        <div className="dashboard-grid">
          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#d8f3dc' }}>📚</div>
            <h3>My Lessons</h3>
            <p>Browse and continue your HSK lessons across all 6 levels.</p>
            <Link href="#" className="dash-card-link">
              Browse lessons →
            </Link>
          </div>

          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#fff3d0' }}>🎯</div>
            <h3>Vocabulary Practice</h3>
            <p>Review HSK vocabulary with flashcards and matching games.</p>
            <Link href="#" className="dash-card-link">
              Start practice →
            </Link>
          </div>

          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#dce5f3' }}>📝</div>
            <h3>Exam Prep</h3>
            <p>Practice with 6 official HSK 4 real exam papers, complete with answer keys.</p>
            <Link href="#" className="dash-card-link">
              Open exams →
            </Link>
          </div>

          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#e5e2fb' }}>🎙️</div>
            <h3>Oral Training</h3>
            <p>HSK 5 oral training modules with 10-minute readings and speaking prompts.</p>
            <Link href="#" className="dash-card-link">
              Start speaking →
            </Link>
          </div>

          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#fedeca' }}>🎭</div>
            <h3>Culture &amp; Stories</h3>
            <p>Chinese myths, Beijing Opera, and non-verbal communication guides.</p>
            <Link href="#" className="dash-card-link">
              Explore →
            </Link>
          </div>

          <div className="dash-card">
            <div className="dash-card-icon" style={{ background: '#faf3e8' }}>📊</div>
            <h3>My Progress</h3>
            <p>Track your completion across levels and themes. Coming soon.</p>
            <Link href="#" className="dash-card-link" style={{ opacity: 0.4, pointerEvents: 'none' }}>
              Coming soon →
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
