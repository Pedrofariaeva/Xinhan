/**
 * Xinhan Lesson Catalog
 * Generated from CONTENT_AUDIT.md
 * English + Chinese only
 */

const LESSONS = [
  // === HSK 1 — Beginner ===
  {
    id: "hsk1-greetings",
    hsk: "HSK 1",
    level: 1,
    theme: "Greetings / Introductions",
    title: "Lesson 1: Hi, What's Your Name?",
    titleZh: "第一课：你好，你叫什么名字？",
    type: "Lesson",
    quality: 2,
    tags: ["pinyin", "tones", "dialogues", "bilingual"],
    description: "Complete Lesson 1: pinyin, tones, greetings dialogues, name/family name. Well structured. Bilingual EN/ZH.",
    slides: 12,
    source: "docs1/lesson 1 Mahima hi,what's your name.pptx"
  },
  {
    id: "hsk1-question-words",
    hsk: "HSK 1",
    level: 1,
    theme: "Grammar / Exercises",
    title: "Question Word Practice",
    titleZh: "疑问词练习",
    type: "Exercise",
    quality: 2,
    tags: ["grammar", "vocabulary"],
    description: "Question word practice (什么/哪里/怎么/etc.) with vocabulary table. Clean, beginner-focused.",
    slides: 8,
    source: "docs3/Level 1Sentence and practice.docx"
  },
  {
    id: "hsk1-dialogue-practice",
    hsk: "HSK 1–2",
    level: 1,
    theme: "Greetings / Daily Life",
    title: "Dialogue Practice: Lessons 1–15",
    titleZh: "对话练习：第1课至第15课",
    type: "Speaking Practice",
    quality: 2,
    tags: ["dialogue", "speaking", "progression"],
    description: "15 dialogue scripts using location, identity, time, and daily activity vocabulary. Good progression.",
    slides: 15,
    source: "docs3/dialogue practice lesson 1to 15.docx"
  },

  // === HSK 2 — Elementary ===
  {
    id: "hsk2-syllabus",
    hsk: "HSK 2",
    level: 2,
    theme: "HSK Exam Practice",
    title: "HSK 2 Official Syllabus",
    titleZh: "新HSK二级官方大纲",
    type: "Reference",
    quality: 1,
    tags: ["official", "syllabus", "vocabulary", "grammar"],
    description: "Official HSK 2 syllabus, sample exam, vocabulary list, grammar overview — published by Hanban/Confucius Institute.",
    slides: 20,
    source: "docs1/HSK2 (1).docx"
  },
  {
    id: "hsk2-daily-habits",
    hsk: "HSK 2",
    level: 2,
    theme: "Daily Life / Habits",
    title: "My Daily Habits",
    titleZh: "我的日常生活习惯",
    type: "Lesson",
    quality: 2,
    tags: ["habits", "frequency", "reading", "comprehension"],
    description: "Clean PPTX: vocabulary (often/rarely/always) + reading about 3 daily habits + comprehension exercises.",
    slides: 10,
    source: "docs1/My daily habbit.pptx"
  },
  {
    id: "hsk2-countries",
    hsk: "HSK 2",
    level: 2,
    theme: "Travel / Countries",
    title: "Countries and Languages",
    titleZh: "你想去哪一个国家？",
    type: "Lesson",
    quality: 2,
    tags: ["vocabulary", "countries", "languages", "bilingual", "pinyin"],
    description: "Vocabulary table (countries, languages, verbs) + dialogue questions. Bilingual ZH/EN with pinyin.",
    slides: 8,
    source: "docs1/你想去哪一个国家？ counrty and langugae (1).docx"
  },

  // === HSK 3 — Intermediate ===
  {
    id: "hsk3-places",
    hsk: "HSK 3",
    level: 3,
    theme: "Travel / Places",
    title: "Location Vocabulary",
    titleZh: "地点词汇",
    type: "Vocabulary",
    quality: 2,
    tags: ["vocabulary", "locations", "pinyin"],
    description: "~25 location words with characters + pinyin + English. Organized by suffix (店/站/室/馆).",
    slides: 6,
    source: "docs1/Hsk 3 练习 地点places .docx"
  },
  {
    id: "hsk3-health",
    hsk: "HSK 3",
    level: 3,
    theme: "Family / Health",
    title: "Family and Health",
    titleZh: "家和家人",
    type: "Lesson",
    quality: 2,
    tags: ["health", "body", "illness", "exercise", "pinyin"],
    description: "Health vocabulary (body parts, illness, exercise) with example sentences. Good pinyin support.",
    slides: 10,
    source: "docs1/家和家人.docx"
  },
  {
    id: "hsk3-directions",
    hsk: "HSK 3",
    level: 3,
    theme: "Travel / Directions",
    title: "How to Get to the Subway?",
    titleZh: "地铁站怎么走？",
    type: "Lesson",
    quality: 2,
    tags: ["directions", "vocabulary", "dialogues"],
    description: "Directions vocabulary with dialogues. Well formatted.",
    slides: 8,
    source: "docs1/地铁站怎么走 ppt.pdf"
  },
  {
    id: "hsk3-sports",
    hsk: "HSK 3",
    level: 3,
    theme: "Health & Sports",
    title: "Sports and Body",
    titleZh: "运动和身体",
    type: "Lesson",
    quality: 2,
    tags: ["sports", "health", "grammar", "dialogues", "exercises"],
    description: "Full lesson: grammar (verb+了+以后), vocabulary (throat/stomach/injury), 3 dialogues, sentence reordering exercises.",
    slides: 14,
    source: "docs1/运动和身体sports health.pptx"
  },

  // === HSK 3–4 — Mixed ===
  {
    id: "hsk34-travel",
    hsk: "HSK 3–4",
    level: 3.5,
    theme: "Travel / Holidays",
    title: "Holiday Travel & Art",
    titleZh: "玩：假期旅行 口语",
    type: "Speaking Practice",
    quality: 2,
    tags: ["travel", "holiday", "speaking", "vocabulary"],
    description: "Vocabulary list (~15+ travel/holiday words) + discussion questions. Good speaking activity.",
    slides: 8,
    source: "docs1/HSK3-4 玩：假期旅行 art 口语.docx"
  },
  {
    id: "hsk34-education",
    hsk: "HSK 3–4",
    level: 3.5,
    theme: "Education / Values",
    title: "The Education of Love",
    titleZh: "综合故事 第九课 爱的教育",
    type: "Reading",
    quality: 2,
    tags: ["story", "reading", "grammar", "comprehension"],
    description: "Story-based lesson about a Chinese teacher and students at graduation. Vocabulary, comprehension questions, grammar pattern (让/叫 + B + VERB).",
    slides: 12,
    source: "docs1/综合故事 第九课 爱的教育.docx"
  },

  // === HSK 4 — Advanced ===
  {
    id: "hsk4-exam-1",
    hsk: "HSK 4",
    level: 4,
    theme: "HSK Exam Practice",
    title: "HSK 4 Real Exam — H41332",
    titleZh: "HSK四级真题 H41332",
    type: "Exam",
    quality: 1,
    tags: ["official", "listening", "reading", "writing"],
    description: "Official HSK 4 full exam (H41332). Complete 3-part structure: listening, reading, writing. Authoritative.",
    slides: 40,
    source: "docs1/HSK4级全真题.docx"
  },
  {
    id: "hsk4-exam-2",
    hsk: "HSK 4",
    level: 4,
    theme: "HSK Exam Practice",
    title: "HSK 4 Real Exam — H41004",
    titleZh: "HSK四级真题 H41004",
    type: "Exam",
    quality: 1,
    tags: ["official", "listening", "reading", "writing"],
    description: "Official HSK 4 exam (H41004). Full paper.",
    slides: 40,
    source: "docs1/hsk四级真题4 (1).doc"
  },
  {
    id: "hsk4-work",
    hsk: "HSK 4",
    level: 4,
    theme: "Work & Career",
    title: "Work & Career Vocabulary",
    titleZh: "HSK4 话题工作",
    type: "Lesson",
    quality: 2,
    tags: ["work", "vocabulary", "reading", "speaking"],
    description: "17 work-related vocabulary items with example phrases + reading (mid-year work summary) + speaking frame.",
    slides: 12,
    source: "docs3/HSK4 话题工作&练习.doc"
  },
  {
    id: "hsk4-shopping",
    hsk: "HSK 4",
    level: 4,
    theme: "Daily Life / Shopping",
    title: "Buy Right, Not Expensive",
    titleZh: "不买贵的，只买对的",
    type: "Lesson",
    quality: 2,
    tags: ["shopping", "online", "vocabulary", "reading"],
    description: "Vocabulary for online shopping (19 items) + reading comprehensions + sentence completion. Practical daily life topic.",
    slides: 10,
    source: "docs3/HSK4不买贵的，只买对的&练习.doc"
  },
  {
    id: "hsk4-marriage",
    hsk: "HSK 4–5",
    level: 4,
    theme: "Love & Relationships",
    title: "Ideal Marriage",
    titleZh: "理想的婚姻",
    type: "Reading",
    quality: 2,
    tags: ["marriage", "reading", "vocabulary", "sentence-building"],
    description: "Vocabulary on marriage + reading comprehension passages (HSK 4 style) + sentence building.",
    slides: 12,
    source: "docs3/1理想的婚姻.doc"
  },
  {
    id: "hsk4-friends",
    hsk: "HSK 4",
    level: 4,
    theme: "Friends / Social",
    title: "Friendship",
    titleZh: "朋友",
    type: "Reading",
    quality: 2,
    tags: ["friendship", "reading", "sentence-reordering"],
    description: "5 HSK 4-style reading passages on friendship, communication, habits. Includes sentence reordering exercise.",
    slides: 10,
    source: "docs3/朋友.doc"
  },
  {
    id: "hsk4-opera",
    hsk: "HSK 4",
    level: 4,
    theme: "Art & Culture",
    title: "Beijing Opera",
    titleZh: "艺术-京剧",
    type: "Reading",
    quality: 2,
    tags: ["opera", "art", "culture", "reading"],
    description: "HSK 4 reading passages on art (performance, emotion, Beijing Opera setting).",
    slides: 10,
    source: "docs3/艺术-京剧.doc"
  },
  {
    id: "hsk4-environment",
    hsk: "HSK 4",
    level: 4,
    theme: "Environment",
    title: "Environment & Protection",
    titleZh: "环境与保护",
    type: "Reading",
    quality: 2,
    tags: ["environment", "pollution", "forests", "seasons"],
    description: "5 HSK 4 reading passages on environment: pollution, forests, seasons.",
    slides: 10,
    source: "docs3/环境与保护.doc"
  },

  // === HSK 5 — Proficient ===
  {
    id: "hsk5-reading",
    hsk: "HSK 5",
    level: 5,
    theme: "Education / Reading Culture",
    title: "Reading Makes One Happy",
    titleZh: "口语17 读书人是幸福的",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "reading", "vocabulary", "speaking"],
    description: "Oral training module: 10-minute reading on reading habits + vocabulary (15 words) + comprehension questions + speaking prompt. Excellent quality.",
    slides: 12,
    source: "docs3/口语17 读书人是幸福的.pdf"
  },
  {
    id: "hsk5-opera",
    hsk: "HSK 5",
    level: 5,
    theme: "Art & Culture",
    title: "Art & Beijing Opera",
    titleZh: "口语18 艺术",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "art", "opera", "vocabulary"],
    description: "Oral training: essay on Beijing Opera (京剧) with costume, performance, music description. Vocabulary + questions. Excellent.",
    slides: 12,
    source: "docs3/口语18 艺术.docx"
  },
  {
    id: "hsk5-environment",
    hsk: "HSK 5",
    level: 5,
    theme: "Environment",
    title: "Environment & Pollution",
    titleZh: "口语19 环境与污染",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "environment", "pollution", "vocabulary"],
    description: "Oral training: environmental pollution reading + vocabulary + questions + speaking prompt. Excellent structure.",
    slides: 12,
    source: "docs3/口语19 环境与污染.docx"
  },
  {
    id: "hsk5-education",
    hsk: "HSK 5",
    level: 5,
    theme: "Education",
    title: "Praise or Criticism?",
    titleZh: "口语20教育 表扬还批评",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "education", "vocabulary", "speaking"],
    description: "Oral training: praise vs. criticism in education + reading + vocabulary + speaking prompt. Excellent.",
    slides: 12,
    source: "docs3/口语20教育 表扬还批评.docx"
  },

  // === HSK 5–6 — Mixed / Advanced ===
  {
    id: "hsk56-love",
    hsk: "HSK 5–6",
    level: 5.5,
    theme: "Love & Relationships",
    title: "Perfect Love",
    titleZh: "口语5完美爱情",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "love", "reading", "speaking"],
    description: "Oral training: perfect love — reading + vocabulary + speaking prompts. Part of a numbered 口语训练 series.",
    slides: 10,
    source: "docs3/口语5完美爱情.docx"
  },
  {
    id: "hsk56-friendship",
    hsk: "HSK 5–6",
    level: 5.5,
    theme: "Friends / Social",
    title: "True Friendship",
    titleZh: "口语6真正的朋友",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "friendship", "reading", "speaking"],
    description: "Oral training: true friendship. Reading + vocabulary + speaking prompts.",
    slides: 10,
    source: "docs3/口语6真正的朋友.docx"
  },
  {
    id: "hsk56-work",
    hsk: "HSK 5–6",
    level: 5.5,
    theme: "Work & Career",
    title: "Work and Interviews",
    titleZh: "口语7工作和面试",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "work", "interview", "speaking"],
    description: "Oral training: work and interviews. Reading + vocabulary + speaking prompts.",
    slides: 10,
    source: "docs3/口语7工作和面试.docx"
  },
  {
    id: "hsk56-shopping",
    hsk: "HSK 5–6",
    level: 5.5,
    theme: "Daily Life / Shopping",
    title: "Buy Right, Not Expensive",
    titleZh: "口语9 只买对的，不买贵的",
    type: "Speaking Practice",
    quality: 1,
    tags: ["oral", "shopping", "speaking"],
    description: "Oral training: buying wisely, not expensively. Reading + vocabulary + speaking prompts.",
    slides: 10,
    source: "docs3/口语9 只买对的，不买贵的.docx"
  },

  // === Chinese Characters — Graded Stories ===
  {
    id: "chars-jingwei",
    hsk: "HSK 3–4",
    level: 3.5,
    theme: "Art & Culture (Mythology)",
    title: "Jingwei Fills the Sea",
    titleZh: "汉字认读短文6 精卫填海",
    type: "Reading",
    quality: 1,
    tags: ["mythology", "characters", "bilingual", "graded"],
    description: "Graded story: Chinese myth — Jingwei fills the sea. Simple poetic style, bilingual ZH/EN glossary. Excellent cultural content.",
    slides: 8,
    source: "docs3/汉字认读短文6 精卫填海.docx"
  },
  {
    id: "chars-yugong",
    hsk: "HSK 3–4",
    level: 3.5,
    theme: "Art & Culture (Mythology)",
    title: "The Foolish Old Man Removes the Mountain",
    titleZh: "汉字认读短文7 愚公移山",
    type: "Reading",
    quality: 1,
    tags: ["mythology", "characters", "bilingual", "graded"],
    description: "Graded story: Chinese myth — The Foolish Old Man removes the mountain. Warm storytelling style. Bilingual glossary.",
    slides: 8,
    source: "docs3/汉字认读短文7 愚公移山.docx"
  },
  {
    id: "chars-haier",
    hsk: "HSK 4–5",
    level: 4.5,
    theme: "Work & Career (Business)",
    title: "Haier's Corporate Transformation",
    titleZh: "汉字认读短文3 另一种发展",
    type: "Reading",
    quality: 2,
    tags: ["business", "characters", "bilingual", "graded"],
    description: "Graded story: Haier's corporate transformation. Business vocabulary. Bilingual ZH/EN glossary.",
    slides: 8,
    source: "docs3/汉字认读短文3 另一种发展.docx"
  },
  {
    id: "chars-zhuge",
    hsk: "HSK 4–5",
    level: 4.5,
    theme: "Art & Culture (History)",
    title: "Zhuge Liang Borrows Arrows",
    titleZh: "汉字认读短文11 草船借箭",
    type: "Reading",
    quality: 1,
    tags: ["history", "characters", "bilingual", "graded", "three-kingdoms"],
    description: "Graded story: Zhuge Liang borrows arrows with straw boats (Three Kingdoms). Rich vocabulary. Excellent cultural material.",
    slides: 10,
    source: "docs3/汉字认读短文11 草船借箭.docx"
  },

  // === Culture / Non-Verbal Communication ===
  {
    id: "culture-nonverbal",
    hsk: "General",
    level: 0,
    theme: "Art & Culture / Business",
    title: "Chinese Non-Verbal Communication",
    titleZh: "中国非语言交际",
    type: "Lesson",
    quality: 1,
    tags: ["culture", "business", "gestures", "posture", "scenarios"],
    description: "Lesson 14: Chinese non-verbal communication (posture, clothing, facial expressions, gestures). Targeted at Western business professionals. Scenarios, case studies, Q&A. Excellent quality.",
    slides: 20,
    source: "docs1/Chinese Non-Verbal Communication in China Lesson 14 _2026.pptx"
  },

  // === Business Mandarin ===
  {
    id: "business-proposal",
    hsk: "HSK 3–4",
    level: 3.5,
    theme: "Business Mandarin",
    title: "Business Mandarin: Better Career in China",
    titleZh: "商务汉语：更好的职业与生活",
    type: "Proposal",
    quality: 2,
    tags: ["business", "speaking", "curriculum", "proposal"],
    description: "Course proposal: Business Chinese speaking, 3–5 months, 30 lessons. Covers business greetings, appointments, negotiations, email. Good curriculum overview.",
    slides: 8,
    source: "docs3/Business Mandarin Better Carreer Life In China 2018.doc"
  }
];

// Group lessons by HSK level
function groupByHsk() {
  const groups = {};
  LESSONS.forEach(l => {
    if (!groups[l.hsk]) groups[l.hsk] = [];
    groups[l.hsk].push(l);
  });
  return groups;
}

// Group lessons by theme
function groupByTheme() {
  const groups = {};
  LESSONS.forEach(l => {
    if (!groups[l.theme]) groups[l.theme] = [];
    groups[l.theme].push(l);
  });
  return groups;
}

// Get assigned lessons for a student (simulated)
function getAssignedLessons(studentId) {
  const data = JSON.parse(localStorage.getItem('assignments') || '{}');
  return data[studentId] || [];
}

// Assign lessons to a student (teacher action)
function assignLessons(studentId, lessonIds) {
  const data = JSON.parse(localStorage.getItem('assignments') || '{}');
  data[studentId] = lessonIds;
  localStorage.setItem('assignments', JSON.stringify(data));
}

// Search lessons
function searchLessons(query) {
  const q = query.toLowerCase();
  return LESSONS.filter(l =>
    l.title.toLowerCase().includes(q) ||
    l.titleZh.includes(q) ||
    l.theme.toLowerCase().includes(q) ||
    l.tags.some(t => t.toLowerCase().includes(q))
  );
}
