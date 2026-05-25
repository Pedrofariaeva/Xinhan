/**
 * Xinhan Progress Tracking
 * LocalStorage-based progress per user
 */

const PROGRESS_KEY = 'xinhan_progress';

function getProgressData() {
  return JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
}

function saveProgressData(data) {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(data));
}

function getUserProgress(userId) {
  const data = getProgressData();
  return data[userId] || { completed: [], lastAccessed: {}, totalTime: 0 };
}

function markLessonComplete(userId, lessonId) {
  const data = getProgressData();
  if (!data[userId]) data[userId] = { completed: [], lastAccessed: {}, totalTime: 0 };
  if (!data[userId].completed.includes(lessonId)) {
    data[userId].completed.push(lessonId);
  }
  data[userId].lastAccessed[lessonId] = Date.now();
  saveProgressData(data);
}

function isLessonComplete(userId, lessonId) {
  const prog = getUserProgress(userId);
  return prog.completed.includes(lessonId);
}

function getCompletionRate(userId, lessonIds) {
  if (!lessonIds || lessonIds.length === 0) return 0;
  const prog = getUserProgress(userId);
  const completed = lessonIds.filter(id => prog.completed.includes(id)).length;
  return Math.round((completed / lessonIds.length) * 100);
}

function recordLessonAccess(userId, lessonId) {
  const data = getProgressData();
  if (!data[userId]) data[userId] = { completed: [], lastAccessed: {}, totalTime: 0 };
  data[userId].lastAccessed[lessonId] = Date.now();
  saveProgressData(data);
}

function getLastAccessed(userId, lessonId) {
  const prog = getUserProgress(userId);
  return prog.lastAccessed[lessonId] || null;
}

function getStudentStats(studentId) {
  const user = getAuth().users.find(u => u.id === studentId);
  if (!user) return null;
  const assigned = getAssignedLessons(studentId);
  const progress = getUserProgress(studentId);
  const completed = assigned.filter(id => progress.completed.includes(id));
  return {
    name: user.name,
    assigned: assigned.length,
    completed: completed.length,
    rate: assigned.length > 0 ? Math.round((completed.length / assigned.length) * 100) : 0
  };
}
