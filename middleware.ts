import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

const PUBLIC_PATHS = ['/signin.html', '/signup.html', '/index.html', '/']

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl

  // Allow public paths
  if (PUBLIC_PATHS.some(p => pathname === p || pathname.startsWith(p + '/'))) {
    return NextResponse.next()
  }

  // Allow API routes
  if (pathname.startsWith('/api/')) {
    return NextResponse.next()
  }

  // Check auth
  const token = request.cookies.get(COOKIE_NAME)?.value
  if (!token) {
    return NextResponse.redirect(new URL('/signin.html', request.url))
  }

  const payload = await verifyToken(token)
  if (!payload) {
    const response = NextResponse.redirect(new URL('/signin.html', request.url))
    response.cookies.delete(COOKIE_NAME)
    return response
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico|api/).*)'],
}
