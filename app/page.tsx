import Link from 'next/link'
import { cookies } from 'next/headers'
import { verifyToken, COOKIE_NAME } from '@/lib/auth-edge'

async function getUser() {
  const cookieStore = await cookies()
  const token = cookieStore.get(COOKIE_NAME)?.value
  if (!token) return null
  return verifyToken(token)
}

export default async function HomePage() {
  const user = await getUser()

  return (
    <>
      {/* Navigation */}
      <nav>
        <div className="nav-inner">
          <Link href="/" className="logo">
            <div className="logo-mark">新</div>
            <div className="logo-text">
              Xinhan<span>Chinese Language School</span>
            </div>
          </Link>
          <div className="nav-links">
            <Link href="#curriculum">Curriculum</Link>
            <Link href="#themes">Themes</Link>
            <Link href="#featured">Featured</Link>
            {user ? (
              <Link href="/dashboard" className="btn">My Dashboard</Link>
            ) : (
              <>
                <Link href="/signin" className="btn-outline">Sign In</Link>
                <Link href="/signup" className="btn">Get Started</Link>
              </>
            )}
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="hero">
        <div className="hero-inner">
          <div className="hero-content">
            <div className="hero-eyebrow">Since 2018 &middot; Hainan, China</div>
            <h1>
              Master Mandarin.<br />
              <span className="chinese">掌握中文，</span><br />
              Unlock China.
            </h1>
            <p>
              Professional Chinese language education for global learners. From
              HSK&nbsp;1 foundations to advanced business Mandarin, guided by
              expert teachers with real classroom experience.
            </p>
            <div className="hero-buttons">
              <Link href="#curriculum" className="btn-primary">
                Explore Curriculum
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg>
              </Link>
              <Link href="/signup" className="btn-secondary">Start Free Trial</Link>
            </div>
          </div>

          <div className="hero-visual">
            <div className="hero-card">
              <div className="card-header">
                <div className="avatar">李</div>
                <div>
                  <div className="card-title">Your Learning Journey</div>
                  <div className="card-subtitle">Track progress across all levels</div>
                </div>
              </div>
              <div className="progress-list">
                <div className="progress-item">
                  <div className="progress-icon" style={{ background: '#d8f3dc', color: '#2d6a4f' }}>HSK1</div>
                  <div className="progress-info">
                    <div className="label">Greetings &amp; Basics</div>
                    <div className="progress-bar"><div className="fill" style={{ width: '100%', background: '#52b788' }} /></div>
                  </div>
                </div>
                <div className="progress-item">
                  <div className="progress-icon" style={{ background: '#fff3d0', color: '#b8860b' }}>HSK3</div>
                  <div className="progress-info">
                    <div className="label">Daily Life &amp; Travel</div>
                    <div className="progress-bar"><div className="fill" style={{ width: '72%', background: '#d4a574' }} /></div>
                  </div>
                </div>
                <div className="progress-item">
                  <div className="progress-icon" style={{ background: '#e9f5ee', color: '#40916c' }}>HSK5</div>
                  <div className="progress-info">
                    <div className="label">Advanced Oral Training</div>
                    <div className="progress-bar"><div className="fill" style={{ width: '45%', background: '#40916c' }} /></div>
                  </div>
                </div>
                <div className="progress-item">
                  <div className="progress-icon" style={{ background: '#f4f3fd', color: '#9f92ef' }}>BM</div>
                  <div className="progress-info">
                    <div className="label">Business Mandarin</div>
                    <div className="progress-bar"><div className="fill" style={{ width: '18%', background: '#9f92ef' }} /></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="scroll-indicator">
          <span>Scroll</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M12 5v14M5 12l7 7 7-7" />
          </svg>
        </div>
      </section>

      {/* Testimonials */}
      <section className="testimonials-section">
        <div className="testimonials-inner">
          <div className="section-header">
            <h2>Trusted by Students Worldwide</h2>
            <p>Real results from real learners — beginners, professionals, and HSK exam takers.</p>
            <div className="chinese-subtitle">学生好评 · 真实反馈</div>
          </div>

          <div className="testimonials-grid">
            {[
              {
                initials: 'SM',
                name: 'Sarah Mitchell',
                role: 'Business Professional · HSK 4',
                country: '🇬🇧',
                stars: 5,
                quote:
                  'Xinhan transformed how I approach Mandarin. After 8 months I passed HSK 4 on the first attempt. The structured curriculum and real exam papers made all the difference.',
              },
              {
                initials: 'MF',
                name: 'Marco Ferretti',
                role: 'Student · HSK 2 → HSK 3',
                country: '🇮🇹',
                stars: 5,
                quote:
                  'I struggled with tones for years before joining Xinhan. The teaching method here is unlike anything else — patient, systematic, and actually fun. My pronunciation improved in just weeks.',
              },
              {
                initials: 'JK',
                name: 'James Kim',
                role: 'Software Engineer · Business Mandarin',
                country: '🇺🇸',
                stars: 5,
                quote:
                  'The Business Mandarin program is exceptional. I now handle client calls in Chinese with confidence. The teachers understand professional contexts, not just textbook phrases.',
              },
              {
                initials: 'AP',
                name: 'Amélie Petit',
                role: 'Graduate Student · HSK 5',
                country: '🇫🇷',
                stars: 5,
                quote:
                  'Rigorous, authentic, and deeply engaging. The oral training modules at HSK 5 level pushed me further than any other program I tried. I finally feel fluent in real conversations.',
              },
            ].map((t) => (
              <div className="testimonial-card" key={t.name}>
                <div className="testimonial-stars">
                  {'★'.repeat(t.stars)}
                </div>
                <p className="testimonial-quote">&ldquo;{t.quote}&rdquo;</p>
                <div className="testimonial-author">
                  <div className="testimonial-avatar">{t.initials}</div>
                  <div>
                    <div className="testimonial-name">{t.country} {t.name}</div>
                    <div className="testimonial-role">{t.role}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Trustpilot bar */}
          <div className="trustpilot-bar">
            <div className="trustpilot-score">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <path d="M12 2l2.9 6.2L22 9.3l-5 5 1.2 7L12 18l-6.2 3.3L7 14.3 2 9.3l7.1-1.1z" fill="#00B67A" />
              </svg>
              <span className="trustpilot-label">
                <strong>Excellent</strong> · 4.9 out of 5
              </span>
              <span className="trustpilot-stars">★★★★★</span>
            </div>
            <a
              href="https://www.trustpilot.com/review/xinhan.org"
              target="_blank"
              rel="noopener noreferrer"
              className="trustpilot-link"
            >
              See all reviews on
              <svg width="90" height="22" viewBox="0 0 116 28" fill="none" style={{ display: 'inline-block', verticalAlign: 'middle', marginLeft: 6 }}>
                <text x="0" y="22" fontFamily="'Inter', sans-serif" fontWeight="700" fontSize="22" fill="#191919">Trustpilot</text>
              </svg>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{ marginLeft: 4 }}>
                <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3" />
              </svg>
            </a>
          </div>
        </div>
      </section>

      {/* Stats Bar */}
      <section className="stats-bar">
        <div className="stats-inner">
          <div className="stat-item">
            <div className="number">62</div>
            <div className="label">Unique Lessons</div>
          </div>
          <div className="stat-item">
            <div className="number">6</div>
            <div className="label">HSK Levels</div>
          </div>
          <div className="stat-item">
            <div className="number">15</div>
            <div className="label">Learning Themes</div>
          </div>
          <div className="stat-item">
            <div className="number">8+</div>
            <div className="label">Years Teaching</div>
          </div>
        </div>
      </section>

      {/* HSK Curriculum */}
      <section id="curriculum" className="section">
        <div className="section-header">
          <h2>Structured by HSK Level</h2>
          <p>A complete progression from beginner to advanced, aligned with the official Chinese Proficiency Test.</p>
          <div className="chinese-subtitle">汉语水平考试课程体系</div>
        </div>
        <div className="hsk-grid">
          <div className="hsk-card">
            <div className="level-badge">Beginner</div>
            <h3>HSK 1</h3>
            <div className="chinese-title">一级 · 起步</div>
            <p>Master pinyin, tones, and fundamental greetings. Build your first 150 words with dialogues on names, countries, and daily introductions.</p>
            <div className="topics">
              <span className="topic-tag">Greetings</span>
              <span className="topic-tag">Pinyin &amp; Tones</span>
              <span className="topic-tag">Question Words</span>
            </div>
            <div className="doc-count">3 lesson materials</div>
          </div>

          <div className="hsk-card">
            <div className="level-badge" style={{ background: '#fff3d0', color: '#b8860b' }}>Elementary</div>
            <h3>HSK 2</h3>
            <div className="chinese-title">二级 · 基础</div>
            <p>Expand to 300 words. Practice picture descriptions, true/false comprehension, and daily habits with structured speaking drills.</p>
            <div className="topics">
              <span className="topic-tag">Daily Habits</span>
              <span className="topic-tag">Time &amp; Numbers</span>
              <span className="topic-tag">Buying Fruit</span>
              <span className="topic-tag">Countries</span>
            </div>
            <div className="doc-count">8 lesson materials</div>
          </div>

          <div className="hsk-card">
            <div className="level-badge" style={{ background: '#e9f5ee', color: '#2d6a4f' }}>Intermediate</div>
            <h3>HSK 3</h3>
            <div className="chinese-title">三级 · 进阶</div>
            <p>Handle real-life situations: giving directions, describing places, talking about family and health with expanded vocabulary.</p>
            <div className="topics">
              <span className="topic-tag">Travel &amp; Places</span>
              <span className="topic-tag">Directions</span>
              <span className="topic-tag">Family</span>
              <span className="topic-tag">Health &amp; Body</span>
            </div>
            <div className="doc-count">6 lesson materials</div>
          </div>

          <div className="hsk-card">
            <div className="level-badge" style={{ background: '#e5e2fb', color: '#5e4fb8' }}>Upper-Int.</div>
            <h3>HSK 3–4</h3>
            <div className="chinese-title">三四级 · 提高</div>
            <p>Story-based learning with Chinese idioms, complex grammar (让/叫/被 structures), and rich reading passages on travel and education.</p>
            <div className="topics">
              <span className="topic-tag">Holiday Travel</span>
              <span className="topic-tag">Education Stories</span>
              <span className="topic-tag">Grammar Focus</span>
            </div>
            <div className="doc-count">5 mixed materials</div>
          </div>

          <div className="hsk-card">
            <div className="level-badge" style={{ background: '#dce5f3', color: '#225890' }}>Advanced</div>
            <h3>HSK 4</h3>
            <div className="chinese-title">四级 · 熟练</div>
            <p>The largest content bank: 6 real exam papers plus themed lessons on work, shopping, marriage, environment, art, and education.</p>
            <div className="topics">
              <span className="topic-tag">Work &amp; Career</span>
              <span className="topic-tag">Love &amp; Relationships</span>
              <span className="topic-tag">Environment</span>
              <span className="topic-tag">Beijing Opera</span>
              <span className="topic-tag">Exam Practice</span>
            </div>
            <div className="doc-count">18 lesson materials + 6 real exams</div>
          </div>

          <div className="hsk-card">
            <div className="level-badge" style={{ background: '#f1f8f4', color: '#1b4332' }}>Proficient</div>
            <h3>HSK 5</h3>
            <div className="chinese-title">五级 · 精通</div>
            <p>Polished oral training modules: 10-minute readings on reading culture, art, environment, and education with vocabulary and speaking prompts.</p>
            <div className="topics">
              <span className="topic-tag">Oral Training</span>
              <span className="topic-tag">Reading Culture</span>
              <span className="topic-tag">Art &amp; Environment</span>
              <span className="topic-tag">Real Exams</span>
            </div>
            <div className="doc-count">8 lesson materials</div>
          </div>
        </div>
      </section>

      {/* Themes */}
      <section id="themes" className="themes-section">
        <div className="section-inner">
          <div className="section-header">
            <h2>Explore by Theme</h2>
            <p>Cross-cutting topics that connect language to real Chinese life and culture.</p>
            <div className="chinese-subtitle">主题探索 · 文化之旅</div>
          </div>
          <div className="theme-grid">
            {[
              { bg: '#d8f3dc', emoji: '🏃', title: 'Health & Sports', desc: 'Body parts, illness, exercise dialogues' },
              { bg: '#fff3d0', emoji: '🏢', title: 'Work & Career', desc: 'Job interviews, office culture, business terms' },
              { bg: '#e5e2fb', emoji: '💏', title: 'Love & Relationships', desc: 'Marriage, friendship, social dynamics' },
              { bg: '#fedeca', emoji: '🎭', title: 'Art & Culture', desc: 'Beijing Opera, Chinese mythology, classics' },
              { bg: '#dce5f3', emoji: '🌍', title: 'Environment', desc: 'Pollution, forests, seasons, sustainability' },
              { bg: '#f1f8f4', emoji: '📚', title: 'Education', desc: 'Study habits, teaching, parenting approaches' },
              { bg: '#faf3e8', emoji: '✈️', title: 'Travel & Places', desc: 'Directions, holidays, countries & languages' },
              { bg: '#e9f5ee', emoji: '👩‍🏫', title: 'Business Mandarin', desc: 'Negotiations, appointments, email etiquette' },
            ].map((t) => (
              <div className="theme-card" key={t.title}>
                <div className="icon" style={{ background: t.bg }}>{t.emoji}</div>
                <h4>{t.title}</h4>
                <p>{t.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured */}
      <section id="featured" className="featured-section">
        <div className="section-header">
          <h2>Featured Content</h2>
          <p>Hand-picked premium materials from our teaching archive.</p>
          <div className="chinese-subtitle">精选课程 · 独家内容</div>
        </div>
        <div className="featured-grid">
          {[
            { bg: '#2d6a4f', emoji: '🎭', tag: 'HSK 4 · Culture', title: 'Beijing Opera Deep Dive', desc: 'Explore costume, performance, and music vocabulary through rich reading passages on 京剧.' },
            { bg: '#225890', emoji: '💬', tag: 'General · Culture', title: 'Chinese Non-Verbal Communication', desc: 'Lesson 14: posture, clothing, facial expressions, and gestures for Western business professionals.' },
            { bg: '#b8860b', emoji: '📜', tag: 'HSK 3–4 · Mythology', title: 'Graded Chinese Myths', desc: 'Jingwei fills the sea, Yugong moves mountains, and Straw Boat Arrows — with bilingual glossaries.' },
            { bg: '#5e4fb8', emoji: '🎙️', tag: 'HSK 5–6 · Speaking', title: '口语训练 Oral Training Series', desc: '10-minute readings + vocabulary + speaking prompts. Perfect love, true friends, work & interviews.' },
            { bg: '#40916c', emoji: '📝', tag: 'HSK 4 · Exam Prep', title: 'Official HSK 4 Real Exams', desc: '6 complete official exam papers with full listening, reading, and writing sections. Includes answer keys.' },
            { bg: '#1b4332', emoji: '🏢', tag: 'HSK 4–5 · Business', title: 'Business Mandarin Proposals', desc: '3–5 month speaking programs covering greetings, appointments, negotiations, and email writing.' },
          ].map((f) => (
            <div className="featured-card" key={f.title}>
              <div className="card-visual" data-emoji={f.emoji} style={{ background: f.bg }} />
              <div className="card-body">
                <span className="card-tag">{f.tag}</span>
                <h4>{f.title}</h4>
                <p>{f.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="cta-section">
        <h2>Start Your Mandarin Journey</h2>
        <p>Join professionals from around the world learning Chinese with Xinhan&apos;s proven curriculum.</p>
        <div className="hero-buttons" style={{ justifyContent: 'center' }}>
          <Link href="/signup" className="btn-primary">
            Create Free Account
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg>
          </Link>
          <Link href="/signin" className="btn-secondary">Already a student? Sign In</Link>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="footer-inner">
          <div className="footer-brand">
            <div className="logo-mark">新</div>
            <p>Xinhan Chinese Language School. Professional Mandarin education in Hainan, China since 2018.</p>
          </div>
          <div className="footer-col">
            <h5>Learn</h5>
            <Link href="#curriculum">HSK Curriculum</Link>
            <Link href="#themes">Themes</Link>
            <Link href="#featured">Featured</Link>
            <Link href="#">Business Mandarin</Link>
          </div>
          <div className="footer-col">
            <h5>Account</h5>
            <Link href="/signin">Sign In</Link>
            <Link href="/signup">Create Account</Link>
            <Link href="/dashboard">My Progress</Link>
            <Link href="#">Settings</Link>
          </div>
          <div className="footer-col">
            <h5>Contact</h5>
            <Link href="#">About Xinhan</Link>
            <Link href="#">Teachers</Link>
            <Link href="#">Hainan, China</Link>
          </div>
        </div>
        <div className="footer-bottom">
          <span>&copy; 2026 Xinhan Chinese Language School. All rights reserved.</span>
          <span>新汉中文学校</span>
        </div>
      </footer>
    </>
  )
}
