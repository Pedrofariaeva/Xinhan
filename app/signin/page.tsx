'use client'

import { Suspense, useState, useRef } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'
import Link from 'next/link'

export default function SignInPage() {
  return (
    <Suspense>
      <SignInForm />
    </Suspense>
  )
}

function SignInForm() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const next = searchParams.get('next') || '/dashboard'
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState('')
  const emailRef = useRef<HTMLInputElement>(null)
  const passwordRef = useRef<HTMLInputElement>(null)

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    setError('')
    setSuccess('')

    const email = emailRef.current?.value.trim() ?? ''
    const password = passwordRef.current?.value ?? ''

    if (!email) { setError('Please enter your email address.'); return }
    if (!password) { setError('Please enter your password.'); return }

    setLoading(true)

    try {
      const res = await fetch('/api/auth/signin', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      })

      const data: { ok?: boolean; error?: string; name?: string } = await res.json()

      if (!res.ok || !data.ok) {
        setError(data.error ?? `Sign in failed (${res.status}). Please try again.`)
        setLoading(false)
        return
      }

      setSuccess(`Welcome back, ${data.name ?? 'student'}! Redirecting…`)
      // Small delay so user sees the success message
      setTimeout(() => {
        router.push(next)
        router.refresh()
      }, 600)
    } catch (err) {
      console.error('[signin]', err)
      setError('Network error — check your connection and try again.')
      setLoading(false)
    }
  }

  return (
    <div className="auth-body">
      <Link href="/" className="back-link">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M19 12H5M12 19l-7-7 7-7" />
        </svg>
        Back to home
      </Link>

      <div className="auth-card">
        <div className="auth-card-inner">
          <div className="auth-header">
            <div className="auth-logo-mark">新</div>
            <h1>Welcome back</h1>
            <p>Sign in to continue your Mandarin journey</p>
          </div>

          {/* Error alert */}
          {error && (
            <div className="alert show">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10" />
                <path d="M12 8v4M12 16h.01" />
              </svg>
              <span>{error}</span>
            </div>
          )}

          {/* Success alert */}
          {success && (
            <div className="alert-success show">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 11.08V12a10 10 0 11-5.93-9.14" />
                <path d="M22 4L12 14.01l-3-3" />
              </svg>
              <span>{success}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} noValidate>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                ref={emailRef}
                type="email"
                id="email"
                name="email"
                placeholder="you@example.com"
                required
                autoComplete="email"
                autoFocus
                disabled={loading}
              />
            </div>

            <div className="form-group">
              <div className="password-row">
                <label htmlFor="password">Password</label>
                <a href="#">Forgot password?</a>
              </div>
              <input
                ref={passwordRef}
                type="password"
                id="password"
                name="password"
                placeholder="Enter your password"
                required
                autoComplete="current-password"
                disabled={loading}
              />
            </div>

            <button type="submit" className="btn-submit" disabled={loading}>
              {loading
                ? <><span className="spinner" /> Signing in…</>
                : 'Sign In'
              }
            </button>
          </form>

          <div className="auth-footer">
            Don&apos;t have an account?{' '}
            <Link href={`/signup${next !== '/dashboard' ? `?next=${encodeURIComponent(next)}` : ''}`}>Create one — it&apos;s free</Link>
          </div>
        </div>
      </div>
    </div>
  )
}
