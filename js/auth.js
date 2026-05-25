/**
 * Xinhan Auth Simulation
 * LocalStorage-based auth with role support
 */

const AUTH_KEY = 'xinhan_auth';

function initAuth() {
  if (!localStorage.getItem(AUTH_KEY)) {
    // Seed demo data
    localStorage.setItem(AUTH_KEY, JSON.stringify({
      currentUser: null,
      users: [
        { id: 'u1', name: 'Teacher Pedro', email: 'pedro@xinhan.org', role: 'teacher', password: 'demo' },
        { id: 'u2', name: 'Student Chloe', email: 'chloe@student.com', role: 'student', password: 'demo' },
        { id: 'u3', name: 'Student Khush', email: 'khush@student.com', role: 'student', password: 'demo' },
        { id: 'u4', name: 'Student Mahima', email: 'mahima@student.com', role: 'student', password: 'demo' }
      ]
    }));
    // Seed assignments
    localStorage.setItem('assignments', JSON.stringify({
      'u2': ['hsk1-greetings', 'hsk1-question-words', 'hsk2-daily-habits'],
      'u3': ['hsk3-sports', 'hsk34-travel', 'hsk4-opera'],
      'u4': ['hsk1-greetings', 'hsk2-countries', 'hsk3-places']
    }));
  }
}

function getAuth() {
  initAuth();
  return JSON.parse(localStorage.getItem(AUTH_KEY));
}

function saveAuth(auth) {
  localStorage.setItem(AUTH_KEY, JSON.stringify(auth));
}

function getCurrentUser() {
  const auth = getAuth();
  return auth.currentUser;
}

function isLoggedIn() {
  return !!getCurrentUser();
}

function isTeacher() {
  const user = getCurrentUser();
  return user && user.role === 'teacher';
}

function isStudent() {
  const user = getCurrentUser();
  return user && user.role === 'student';
}

function login(email, password) {
  const auth = getAuth();
  const user = auth.users.find(u => u.email === email && u.password === password);
  if (!user) return { ok: false, error: 'Invalid email or password' };
  auth.currentUser = user;
  saveAuth(auth);
  return { ok: true, user };
}

function register(name, email, password, role = 'student') {
  const auth = getAuth();
  if (auth.users.find(u => u.email === email)) {
    return { ok: false, error: 'An account with this email already exists' };
  }
  const user = { id: 'u' + Date.now(), name, email, role, password };
  auth.users.push(user);
  auth.currentUser = user;
  saveAuth(auth);
  return { ok: true, user };
}

function logout() {
  const auth = getAuth();
  auth.currentUser = null;
  saveAuth(auth);
  window.location.href = 'signin.html';
}

function requireAuth() {
  if (!isLoggedIn()) {
    window.location.href = 'signin.html';
    return false;
  }
  return true;
}

function requireTeacher() {
  if (!requireAuth()) return false;
  if (!isTeacher()) {
    window.location.href = 'dashboard.html';
    return false;
  }
  return true;
}

function requireStudent() {
  if (!requireAuth()) return false;
  if (!isStudent()) {
    window.location.href = 'teacher.html';
    return false;
  }
  return true;
}

// Init on load
initAuth();
