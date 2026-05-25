/**
 * Xinhan Auth — Real API Version
 * Calls Next.js API routes with JWT cookie auth
 */

const API_BASE = '';

async function api(endpoint, opts = {}) {
  const res = await fetch(API_BASE + endpoint, {
    credentials: 'include',
    headers: { 'Content-Type': 'application/json', ...opts.headers },
    ...opts,
  });
  const data = await res.json().catch(() => ({}));
  return { ok: res.ok, status: res.status, data };
}

let currentUser = null;
let userPromise = null;

async function fetchUser() {
  if (userPromise) return userPromise;
  userPromise = api('/api/auth/me').then(r => {
    currentUser = r.data?.user || null;
    return currentUser;
  });
  return userPromise;
}

function getCurrentUser() {
  return currentUser;
}

function isLoggedIn() {
  return !!currentUser;
}

function isTeacher() {
  return currentUser?.role === 'teacher';
}

function isStudent() {
  return currentUser?.role === 'student';
}

async function login(email, password) {
  const r = await api('/api/auth/signin', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
  if (r.ok && r.data?.ok) {
    currentUser = await fetchUser();
    return { ok: true, user: currentUser };
  }
  return { ok: false, error: r.data?.error || 'Login failed' };
}

async function register(name, email, password, role = 'student') {
  const r = await api('/api/auth/signup', {
    method: 'POST',
    body: JSON.stringify({ name, email, password, role }),
  });
  if (r.ok && r.data?.ok) {
    currentUser = await fetchUser();
    return { ok: true, user: currentUser };
  }
  return { ok: false, error: r.data?.error || 'Registration failed' };
}

async function logout() {
  await api('/api/auth/signout', { method: 'POST' });
  currentUser = null;
  window.location.href = '/signin.html';
}

async function requireAuth() {
  await fetchUser();
  if (!isLoggedIn()) {
    window.location.href = '/signin.html';
    return false;
  }
  return true;
}

async function requireTeacher() {
  if (!(await requireAuth())) return false;
  if (!isTeacher()) {
    window.location.href = '/dashboard.html';
    return false;
  }
  return true;
}

async function requireStudent() {
  if (!(await requireAuth())) return false;
  if (!isStudent()) {
    window.location.href = '/teacher.html';
    return false;
  }
  return true;
}

// Init: prefetch user on every page
fetchUser();
