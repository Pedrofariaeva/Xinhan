'use client'

import { useState, useRef } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

export default function SignUpPage() {
  const router = useRouter()
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const [loading, setLoading] = useState(false)

  const nameRef = useRef<HTMLInputElement>(null)
  const emailRef = useRef<HTMLInputElement>(null)
  const passwordRef = useRef<HTMLInputElement>(null)
  const confirmRef = useRef<HTMLInputElement>(null)
  const roleRef = useRef<HTMLSelectElement>(null)

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    setError('')
    setSuccess('')

    const name = nameRef.current?.value.trim() ?? ''
    const email = emailRef.current?.value.trim() ?? ''
    const password = passwordRef.current?.value ?? ''
    const confirmPassword = confirmRef.current?.value ?? ''
    const role = roleRef.current?.value ?? 'student'

    // Client-side validation — fast, no round trip
    if (!name) { setError('Please enter your full name.'); return }
    if (!email) { setError('Please enter your email address.'); return }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setError('Please enter a valid email address.')
      return
    }
    if (!password) { setError('Please choose a password.'); return }
    if (password.length < 6) {
      setError('Password must be at least 6 characters long.')
      return
    }
    if (password !== confirmPassword) {
      setError('Passwords do not match. Please check and try again.')
      return
    }

    setLoading(true)

    try {
      const res = await fetch('/api/auth/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password, role }),
      })

      const data: { ok?: boolean; error?: string; name?: string } = await res.json()

      if (!res.ok || !data.ok) {
        setError(data.error ?? `Registration failed (${res.status}). Please try again.`)
        setLoading(false)
        return
      }

      setSuccess(`Account created! Welcome, ${data.name ?? name}. Taking you to your dashboard…`)
      setTimeout(() => {
        router.push('/dashboard')
        router.refresh()
      }, 800)
    } catch (err) {
      console.error('[signup]', err)
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
            <h1>Create your account</h1>
            <p>Start learning Mandarin with Xinhan</p>
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
              <label htmlFor="name">Full Name</label>
              <input
                ref={nameRef}
                type="text"
                id="name"
                name="name"
                placeholder="Your full name"
                required
                autoComplete="name"
                autoFocus
                disabled={loading}
              />
            </div>

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
                disabled={loading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="role">I am a</label>
              <div className="select-wrapper">
                <select ref={roleRef} id="role" name="role" required disabled={loading}>
                  <option value="student">Student</option>
                  <option value="teacher">Teacher</option>
                  <option value="business">Business Professional</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                ref={passwordRef}
                type="password"
                id="password"
                name="password"
                placeholder="At least 6 characters"
                required
                autoComplete="new-password"
                disabled={loading}
              />
              <div className="hint">Must be at least 6 characters</div>
            </div>

            <div className="form-group">
              <label htmlFor="confirmPassword">Confirm Password</label>
              <input
                ref={confirmRef}
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                placeholder="Repeat your password"
                required
                autoComplete="new-password"
                disabled={loading}
              />
            </div>

            <button type="submit" className="btn-submit" disabled={loading}>
              {loading
                ? <><span className="spinner" /> Creating account…</>
                : 'Create Account'
              }
            </button>
          </form>

          <div className="auth-footer">
            Already have an account?{' '}
            <Link href="/signin">Sign in</Link>
          </div>
        </div>
      </div>
    </div>
  )
}
