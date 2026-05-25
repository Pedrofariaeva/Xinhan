import { jwtVerify, SignJWT } from 'jose'

const getSecret = () =>
  new TextEncoder().encode(
    process.env.JWT_SECRET ?? 'dev-secret-change-in-production'
  )

export const COOKIE_NAME = 'xinhan_token'
export const COOKIE_MAX_AGE = 60 * 60 * 24 * 7

export interface TokenPayload {
  userId: string
  email: string
  name: string
  role: string
}

export async function signToken(payload: TokenPayload): Promise<string> {
  return new SignJWT({ ...payload })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(getSecret())
}

export async function verifyToken(token: string): Promise<TokenPayload | null> {
  try {
    const { payload } = await jwtVerify(token, getSecret())
    return payload as unknown as TokenPayload
  } catch {
    return null
  }
}
