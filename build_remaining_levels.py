#!/usr/bin/env python3
"""Generate missing HSK 1/2/4/5/6 variants for mood-weather, many-ways, and mood-weather-v2."""
import os, json, html

ROOT = "/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson"


def esc(s):
    return html.escape(str(s))


def attr_esc(s):
    return str(s).replace('"', '&quot;')


def sidebar(icon, label, active=0, total=7, bg_class=""):
    dots = []
    for i in range(total):
        if i < active:
            dots.append('<div class="dot done"></div>')
        elif i == active:
            dots.append('<div class="dot active"></div>')
        else:
            dots.append('<div class="dot"></div>')
    cls = ("sidebar " + bg_class).strip()
    return f'''<div class="{cls}">
    <div class="sb-icon">{icon}<div class="sb-label">{label}</div></div>
    <div class="sb-prog">{"".join(dots)}</div>
  </div>'''


ICON_WARMUP = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="14" cy="14" r="10" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
      <circle cx="14" cy="11" r="3" fill="rgba(255,255,255,0.85)"/>
      <path d="M9 19c0-2.8 2.2-5 5-5s5 2.2 5 5" fill="rgba(255,255,255,0.5)" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    </svg>'''

ICON_VOCAB = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="4" y="3" width="20" height="22" rx="2" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
      <line x1="8" y1="9" x2="20" y2="9" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="8" y1="14" x2="20" y2="14" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="8" y1="19" x2="15" y2="19" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
    </svg>'''

ICON_TEST = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="14" cy="14" r="6" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
      <path d="M14 6v2M14 20v2M6 14h2M20 14h2" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
    </svg>'''

ICON_REPORT = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M5 21 L5 13 M12 21 L12 8 M19 21 L19 16 M23 21 L23 11" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" stroke-linecap="round"/>
    </svg>'''


def cover(story, level, level_label, word_count, grammar_count, theme):
    accent = theme["accent"]
    eyebrow = story.get("eyebrow", "Daily life · 日常生活")
    return f'''<!-- COVER -->
<div class="slide slide-cover">
  <div class="sidebar" style="background:{accent['dark']};justify-content:center;align-items:center;min-height:300px;">
    {story['cover_icon']}
  </div>
  <div class="cover-content">
    <div class="cover-eyebrow">{eyebrow} · {level_label}</div>
    <div class="cover-zh">{story['title_zh']}</div>
    <div class="cover-py">{story['title_py']}</div>
    <div class="cover-en">{story['title_en']}</div>
    <div class="cover-tags">
      <span class="tag">{level_label}</span>
      <span class="tag">{word_count} new words</span>
      <span class="tag">{grammar_count} grammar points</span>
    </div>
  </div>
</div>'''


def warm_up_slide(level_data, theme, active=0):
    chips = ''.join([f'<div class="chip"><span class="ch">{esc(z)}</span><span class="py">{esc(e)}</span></div>' for z, e in level_data['warm_chips']])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_WARMUP, "warm up", active=active, bg_class="")}
  <div class="content">
    <div class="sec-label">Warm-up · 热身</div>
    <h2>{level_data['warm_title']}</h2>
    <div class="tip"><strong>Practice:</strong> {level_data['warm_tip']}</div>
    <div class="chip-row">{chips}</div>
  </div>
</div>'''


def vocab_slide(level_data, theme, active=1):
    cards = '\n'.join([f'<div class="vc {cat}"><div class="vc-zh">{esc(z)}</div><div class="vc-py">{esc(p)}</div><div class="vc-en">{esc(e)}</div></div>' for z, p, e, cat in level_data['vocab']])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_VOCAB, "vocab", active=active, bg_class=theme['accent']['mid'])}
  <div class="content">
    <div class="sec-label">New Words · 新词 — {len(level_data['vocab'])} words</div>
    <div class="vocab-grid">{cards}</div>
    <div class="tip"><strong>Tip:</strong> Focus on the highlighted grammar words.</div>
  </div>
</div>'''


def grammar_strip(parts, en, theme):
    items = []
    for p in parts:
        if len(p) == 3:
            zh, py, cls = p
            items.append(f'<div class="gs-part colored {cls}"><div class="gs-zh">{esc(zh)}</div><div class="gs-py">{esc(py)}</div></div>')
        else:
            zh, py = p
            items.append(f'<div class="gs-part"><div class="gs-plain-zh">{esc(zh)}</div><div class="gs-plain-py">{esc(py)}</div></div>')
    return f'<div class="grammar-strip">{"".join(items)}<div class="gs-en">{esc(en)}</div></div>'


def ex(zh, py, en, cls=""):
    return f'<div class="ex {cls}"><div class="ex-zh">{zh}</div><div class="ex-py">{esc(py)}</div><div class="ex-en">{esc(en)}</div></div>'


def grammar_slide(idx, g, theme, active):
    cls = theme['grammar_classes'][idx % len(theme['grammar_classes'])]
    examples = '\n'.join([ex(*e) if len(e) == 3 else ex(*e) for e in g['ex']])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_VOCAB, f"G{idx+1} · {g['label']}", active=active, bg_class=cls)}
  <div class="content">
    <div class="sec-label">Grammar {idx+1} · 语法{idx+1}</div>
    {grammar_strip(g['strip'], g['en'], theme)}
    <div class="ex-block">{examples}</div>
  </div>
</div>'''


def dialogue_slide(level_data, theme, active):
    bubbles = '\n'.join([f'<div class="dial-{who}"><div class="dial-label">{esc(label)}</div><div class="dial-zh">{esc(zh)}</div><div class="dial-py">{esc(py)}</div><div class="dial-en">{esc(en)}</div></div>' for who, label, zh, py, en in level_data['dialogue']])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_WARMUP, "dialogue", active=active, bg_class=theme['accent']['mid'])}
  <div class="content">
    <div class="sec-label">Dialogue · 对话</div>
    <h2>{level_data['dialogue_title']}</h2>
    <div class="dial-grid">{bubbles}</div>
  </div>
</div>'''


def quiz_item(qzh, qpy, answers, reveal):
    ans = "|".join(answers)
    return f'''<div class="phone-block wide">
    <div class="quiz-q">{qzh}<span class="py">{qpy}</span></div>
    <div class="quiz-game">
      <div class="quiz-row">
        <input type="text" class="quiz-input" placeholder="Type your answer…" data-answer="{attr_esc(ans)}" data-reveal="{attr_esc(reveal)}"/>
        <button type="button" class="quiz-check-btn">检查</button>
      </div>
      <div class="quiz-feedback"></div>
    </div>
  </div>'''


def quiz_slide(num, total, label, group, title, items, theme, active):
    items_html = '\n'.join([quiz_item(*i) for i in items])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_TEST, f"test {num}/{total}", active=active, bg_class="rust")}
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">{label}</div>
    <h2>{title}</h2>
    <div class="quiz-score" data-quiz-score data-group="{group}" data-total="{len(items)}">✅ <span class="score-correct">0</span>/<span class="score-total">{len(items)}</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type your answer</strong> in Chinese, pinyin, or English. Hit Enter or tap 检查.</div>
    <div class="phone-row">{items_html}</div>
  </div>
</div>'''


def review_slide(level_data, theme, active):
    chips = ''.join([f'<div class="chip"><span class="ch">{esc(z)}</span><span class="py">{esc(e)}</span></div>' for z, e in level_data['review_chips']])
    sentences = '\n'.join([f'<div class="practice-item"><div class="practice-num">{i+1}</div><div class="practice-text"><span class="zh">{esc(zh)}</span></div></div>' for i, (zh,) in enumerate(level_data['review_sentences'])])
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_VOCAB, "review", active=active, bg_class="dark")}
  <div class="content">
    <div class="sec-label">Review · 复习</div>
    <h2>Useful phrases · 常用语</h2>
    <div class="chip-row">{chips}</div>
    <div class="practice">
      <div class="practice-title">Key sentences · 重点句</div>
      {sentences}
    </div>
  </div>
</div>'''


def report_slide(active, total):
    return f'''<div class="slide" id="lesson-report-slide" style="grid-template-columns:64px 1fr; display:none;">
  {sidebar(ICON_REPORT, "your report", active=active, bg_class="dark")}
  <div class="content">
    <div class="sec-label">Lesson Report · 学习报告</div>
    <h2>你的学习报告 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Nǐ de xuéxí bàogào.</span></h2>
    <div id="report-score" class="report-score"></div>
    <div id="report-groups" class="report-groups"></div>
    <div id="report-missed"></div>
  </div>
</div>'''


def closing(story, level_label, theme):
    return f'''<div class="slide slide-close">
  <div class="close-inner">
    <div class="close-zh">{story['close_zh']}</div>
    <div class="close-detail">
      <div class="py">{story['close_py']}</div>
      <div class="en">{story['close_en']}</div>
      <div class="sub">{level_label} · {story['title_en']}</div>
    </div>
  </div>
</div>'''


def build_lesson(story, level, level_data, theme):
    level_label = level.replace('hsk-', 'HSK ')
    slides = []
    slides.append(cover(story, level, level_label, len(level_data['vocab']), len(level_data['grammar']), theme))
    slides.append(warm_up_slide(level_data, theme, active=0))
    slides.append(vocab_slide(level_data, theme, active=1))
    for i, g in enumerate(level_data['grammar']):
        slides.append(grammar_slide(i, g, theme, active=2 + i))
    dia_active = 2 + len(level_data['grammar'])
    slides.append(dialogue_slide(level_data, theme, active=dia_active))
    for i, (label, group, title, items) in enumerate(level_data['quizzes']):
        slides.append(quiz_slide(i + 1, len(level_data['quizzes']), label, group, title, items, theme, active=dia_active + 1 + i))
    report_active = dia_active + 1 + len(level_data['quizzes'])
    slides.append(report_slide(active=report_active, total=report_active + 2))
    slides.append(review_slide(level_data, theme, active=report_active + 1))
    slides.append(closing(story, level_label, theme))

    group_names = json.dumps({q[1]: q[0] for q in level_data['quizzes']}, ensure_ascii=False)
    body_id = f"{level}/{story['id']}"

    return HEAD_TEMPLATE(theme) + f'<body data-lesson-id="{body_id}">\n<div class="deck">\n<div class="deck-brand"><span class="brand-name">新汉 Xīnhàn</span><span class="brand-sub">{level_label} · {story["title_en"]}</span></div>\n' + '\n'.join(slides) + '\n</div>\n' + FOOT_TEMPLATE(group_names) + '</body>\n</html>'


def HEAD_TEMPLATE(theme):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{theme['title_zh']} — {theme['title_en']} · Xinhan Chinese</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --jade: #2d6a4f; --jade-mid: #40916c; --jade-light: #74c69d; --jade-pale: #d8f3dc;
  --gold: #b7791f; --gold-mid: #d69e2e; --gold-pale: #fffff0;
  --rust: #9b2226; --rust-light: #e76f51; --rust-pale: #fff0ee;
  --accent: {theme['accent']['main']};
  --accent-mid: {theme['accent']['mid']};
  --accent-dark: {theme['accent']['dark']};
  --accent-pale: {theme['accent']['pale']};
  --cream: #faf7f2; --cream-dark: #ede8df;
  --ink: #1a1a1a; --ink-2: #3d3d3d; --ink-3: #7a7a7a;
  --white: #fff;
}}
body {{ font-family: 'Inter', sans-serif; background: #d6cfc4; color: var(--ink); padding: 2.5rem 1rem 5rem; }}
.deck {{ max-width: 940px; margin: 0 auto; }}
.deck-brand {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }}
.brand-name {{ font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--accent); }}
.brand-sub  {{ font-size: 0.68rem; color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.12em; }}
.slide {{ display: grid; background: var(--white); overflow: hidden; margin-bottom: 3px; }}
.slide:first-of-type {{ border-radius: 14px 14px 0 0; }}
.slide:last-of-type  {{ border-radius: 0 0 14px 14px; }}
.sidebar {{
  display: flex; flex-direction: column;
  padding: 1.5rem 0.65rem 1.5rem 0.9rem;
  background: var(--accent);
  gap: 1.8rem; min-width: 64px;
  position: relative;
}}
.sidebar::after {{
  content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 2px;
  background: linear-gradient(to bottom, rgba(255,255,255,0.25), transparent);
}}
.sb-icon {{ display: flex; flex-direction: column; align-items: center; gap: 0.3rem; }}
.sb-icon svg {{ width: 28px; height: 28px; }}
.sb-label {{ font-size: 0.48rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.55); text-align: center; line-height: 1.2; }}
.sb-prog {{ display: flex; flex-direction: column; align-items: center; gap: 5px; margin-top: auto; }}
.dot {{ width: 7px; height: 7px; border-radius: 50%; background: rgba(255,255,255,0.2); }}
.dot.active {{ background: #f6e05e; }}
.dot.done   {{ background: var(--accent-mid); }}
.sidebar.rust  {{ background: var(--rust); }}
.sidebar.gold  {{ background: #7b5a1a; }}
.sidebar.jade  {{ background: var(--jade-mid); }}
.sidebar.dark  {{ background: {theme['accent']['dark']}; }}
.content {{ padding: 2rem 2.5rem 2rem 2rem; flex: 1; }}
.sec-label {{ font-size: 0.6rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent-mid); margin-bottom: 0.9rem; }}
.content h2 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 600; margin-bottom: 1.25rem; line-height: 1.3; }}
.zh-inline {{ font-family: 'Noto Serif SC', serif; color: var(--accent); }}
.py-inline {{ font-size: 0.72rem; font-family: 'Inter', sans-serif; font-weight: 400; color: var(--gold); letter-spacing: 0.07em; }}
.scene {{ width: 100%; border-radius: 10px; overflow: hidden; margin-bottom: 1.25rem; }}
.scene svg {{ display: block; width: 100%; }}
.slide-cover {{ grid-template-columns: 90px 1fr; }}
.cover-content {{ background: var(--accent); padding: 2.5rem 2.5rem 2rem; position: relative; min-height: 300px; display: flex; flex-direction: column; justify-content: flex-end; overflow: hidden; }}
.cover-eyebrow {{ font-size: 0.65rem; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; color: var(--accent-pale); margin-bottom: 0.7rem; position: relative; }}
.cover-zh {{ font-family: 'Noto Serif SC', serif; font-size: 5.8rem; font-weight: 700; color: var(--white); line-height: 1; letter-spacing: -0.02em; position: relative; }}
.cover-py {{ font-size: 1.25rem; font-weight: 300; color: var(--accent-pale); letter-spacing: 0.18em; margin: 0.3rem 0; position: relative; }}
.cover-en {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.45rem; color: #f6e05e; position: relative; margin-bottom: 1.5rem; }}
.cover-tags {{ display: flex; gap: 0.5rem; flex-wrap: wrap; position: relative; }}
.tag {{ padding: 0.22rem 0.8rem; border-radius: 999px; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9); }}
.grammar-strip {{ display: flex; align-items: center; gap: 0; background: var(--cream); border-radius: 10px; overflow: hidden; margin-bottom: 1.4rem; }}
.gs-part {{ padding: 0.75rem 1rem; display: flex; flex-direction: column; align-items: center; }}
.gs-part.colored {{ background: var(--accent); }}
.gs-part.colored.rust {{ background: var(--rust); }}
.gs-part.colored.jade {{ background: var(--jade-mid); }}
.gs-part.colored.gold {{ background: #7b5a1a; }}
.gs-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1.5rem; font-weight: 700; color: var(--white); line-height: 1; }}
.gs-py {{ font-size: 0.58rem; color: rgba(255,255,255,0.7); letter-spacing: 0.06em; margin-top: 2px; }}
.gs-sep {{ font-size: 1.1rem; color: var(--ink-3); padding: 0 0.3rem; }}
.gs-plain-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1.1rem; font-weight: 500; color: var(--accent); }}
.gs-plain-py {{ font-size: 0.58rem; color: var(--gold); margin-top: 2px; }}
.gs-en {{ margin-left: auto; padding: 0.75rem 1.25rem; font-size: 0.72rem; color: var(--ink-3); font-style: italic; border-left: 1px solid var(--cream-dark); }}
.ex-block {{ display: flex; flex-direction: column; gap: 0.65rem; margin-bottom: 1.25rem; }}
.ex {{ background: var(--cream); border-radius: 8px; padding: 0.8rem 1rem; border-left: 3px solid var(--accent-mid); }}
.ex.rust {{ border-left-color: var(--rust-light); }}
.ex.jade {{ border-left-color: var(--jade-mid); }}
.ex-zh {{ font-family: 'Noto Serif SC', serif; font-size: 0.98rem; color: var(--ink); margin-bottom: 0.15rem; }}
.key  {{ color: var(--accent); font-weight: 700; }}
.key-r{{ color: var(--rust); font-weight: 700; }}
.key-j{{ color: var(--jade-mid); font-weight: 700; }}
.key-g{{ color: var(--gold); font-weight: 700; }}
.ex-py {{ font-size: 0.63rem; color: var(--gold); letter-spacing: 0.03em; margin-bottom: 0.1rem; }}
.ex-en {{ font-size: 0.69rem; color: var(--ink-3); font-style: italic; }}
.chip-row {{ display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem; }}
.chip {{ padding: 0.25rem 0.75rem; border-radius: 999px; font-size: 0.7rem; background: var(--cream); border: 1.5px solid var(--cream-dark); }}
.chip .ch {{ font-family: 'Noto Serif SC', serif; font-size: 0.85rem; color: var(--accent); font-weight: 500; }}
.chip .py {{ font-size: 0.58rem; color: var(--gold); margin-left: 0.25rem; }}
.vocab-grid {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 6px; }}
.vc {{ background: var(--white); border: 1px solid var(--cream-dark); border-radius: 7px; padding: 0.55rem 0.7rem; border-top: 3px solid var(--accent-mid); }}
.vc.cat-mood {{ border-top-color: var(--rust-light); }}
.vc.cat-weather {{ border-top-color: #1d5f8a; }}
.vc.cat-act {{ border-top-color: var(--gold-mid); }}
.vc.cat-gram {{ border-top-color: var(--jade); }}
.vc-zh {{ font-family: 'Noto Serif SC', serif; font-size: 1rem; font-weight: 500; color: var(--accent); }}
.vc-py {{ font-size: 0.58rem; color: var(--gold); margin: 2px 0 1px; }}
.vc-en {{ font-size: 0.62rem; color: var(--ink-3); }}
.tip {{ background: var(--accent-pale); border-radius: 7px; padding: 0.65rem 0.95rem; font-size: 0.7rem; color: var(--accent-dark); line-height: 1.55; margin-top: 0.9rem; }}
.tip strong {{ font-weight: 600; }}
.practice {{ background: linear-gradient(135deg, var(--accent-pale), #e8f4fd); border-radius: 10px; padding: 1rem 1.2rem; margin-top: 1rem; border-left: 4px solid var(--accent-mid); }}
.practice-title {{ font-size: 0.58rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin-bottom: 0.5rem; }}
.practice-item {{ display: flex; gap: 0.6rem; align-items: flex-start; margin-bottom: 0.45rem; }}
.practice-item:last-child {{ margin-bottom: 0; }}
.practice-num {{ min-width: 20px; height: 20px; border-radius: 50%; background: var(--accent); color: white; font-size: 0.65rem; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-top: 1px; }}
.practice-text {{ font-size: 0.82rem; color: var(--ink-2); line-height: 1.45; }}
.practice-text .zh {{ font-family: 'Noto Serif SC', serif; color: var(--accent); font-weight: 500; }}
.dial-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0.7rem; margin-bottom: 1.25rem; }}
.dial-a, .dial-b {{ border-radius: 10px; padding: 0.85rem 1rem; }}
.dial-a {{ background: #e8f4fd; border-left: 3px solid #1d5f8a; }}
.dial-b {{ background: var(--accent-pale); border-left: 3px solid var(--accent-mid); }}
.dial-label {{ font-size: 0.55rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 0.35rem; color: var(--accent); }}
.dial-zh {{ font-family: 'Noto Serif SC', serif; font-size: 0.92rem; margin-bottom: 0.15rem; }}
.dial-py {{ font-size: 0.6rem; color: var(--gold); margin-bottom: 0.1rem; }}
.dial-en {{ font-size: 0.66rem; color: var(--ink-3); font-style: italic; }}
.phone-row {{ display: flex; gap: 16px; flex-wrap: wrap; justify-content: flex-start; margin-bottom: 0.5rem; }}
.phone-block {{ display: flex; flex-direction: column; gap: 0.55rem; width: 150px; }}
.phone-block.wide {{ width: 200px; }}
.quiz-q {{ background: var(--cream); border-radius: 8px; padding: 0.5rem 0.65rem; font-size: 0.66rem; color: var(--ink); line-height: 1.45; }}
.quiz-q .py {{ display: block; color: var(--gold); font-size: 0.6rem; margin-top: 1px; }}
.quiz-game {{ display: flex; flex-direction: column; gap: 0.3rem; }}
.quiz-row {{ display: flex; gap: 0.3rem; }}
.quiz-input {{ flex: 1; width: 100%; box-sizing: border-box; padding: 6px 8px; font-size: 0.66rem; font-family: inherit; border: 1px solid #d2d2d2; border-radius: 6px; background: var(--white); color: var(--ink); transition: border-color 0.15s, background 0.15s; }}
.quiz-input:focus {{ outline: 2px solid var(--gold); outline-offset: 1px; }}
.quiz-input:disabled {{ background: var(--cream); opacity: 0.85; }}
.quiz-input.flash-correct {{ border-color: #2f7d52; background: #eaf7ef; animation: quiz-pop 0.4s ease; }}
.quiz-input.flash-wrong {{ border-color: #c0392b; background: #fbeaea; animation: quiz-shake 0.4s ease; }}
.quiz-check-btn {{ flex-shrink: 0; padding: 6px 10px; font-size: 0.62rem; font-weight: 700; border: none; border-radius: 6px; background: var(--gold); color: var(--accent-dark); cursor: pointer; transition: background 0.15s, transform 0.15s; }}
.quiz-check-btn:hover:not(:disabled) {{ transform: translateY(-1px); }}
.quiz-check-btn:disabled {{ cursor: default; }}
.quiz-check-btn.correct {{ background: #2f7d52; color: white; animation: quiz-pop 0.4s ease; }}
.quiz-check-btn.wrong {{ background: #c0392b; color: white; animation: quiz-shake 0.4s ease; }}
@keyframes quiz-pop {{ 0% {{ transform: scale(1); }} 40% {{ transform: scale(1.12); }} 100% {{ transform: scale(1); }} }}
@keyframes quiz-shake {{ 0%, 100% {{ transform: translateX(0); }} 20% {{ transform: translateX(-5px); }} 40% {{ transform: translateX(5px); }} 60% {{ transform: translateX(-4px); }} 80% {{ transform: translateX(4px); }} }}
.quiz-feedback {{ font-size: 0.68rem; font-weight: 700; min-height: 1.1em; }}
.quiz-feedback.correct {{ color: #2f7d52; }}
.quiz-feedback.wrong {{ color: #c0392b; }}
.quiz-feedback .reveal {{ display: block; font-weight: 500; color: var(--ink); margin-top: 2px; font-size: 0.62rem; }}
.quiz-feedback .reveal .py {{ color: var(--gold); }}
.quiz-score {{ display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.66rem; font-weight: 700; color: var(--accent); background: var(--cream); border-radius: 20px; padding: 0.3rem 0.8rem; margin-bottom: 0.8rem; }}
.quiz-score .stars {{ color: var(--gold); letter-spacing: 1px; }}
.learn-badge {{ display: inline-block; font-size: 0.6rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--jade); background: var(--jade-pale); border-radius: 20px; padding: 0.25rem 0.7rem; margin-bottom: 0.6rem; }}
.test-badge {{ display: inline-block; font-size: 0.6rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--rust); background: #fbeaea; border-radius: 20px; padding: 0.25rem 0.7rem; margin-bottom: 0.6rem; }}
.report-score {{ display: flex; align-items: baseline; gap: 0.6rem; margin: 0.5rem 0 1rem; }}
.report-score .big {{ font-size: 2.4rem; font-weight: 800; color: var(--jade); }}
.report-score .pct {{ font-size: 1rem; font-weight: 700; color: var(--gold); }}
.report-groups {{ display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.2rem; }}
.report-group-row {{ display: flex; align-items: center; gap: 0.6rem; font-size: 0.66rem; }}
.report-group-name {{ width: 150px; flex-shrink: 0; color: var(--ink); }}
.report-group-bar {{ flex: 1; height: 8px; border-radius: 5px; background: var(--cream); overflow: hidden; }}
.report-group-fill {{ height: 100%; background: var(--jade-mid); border-radius: 5px; }}
.report-group-fill.weak {{ background: var(--rust-light); }}
.report-group-score {{ width: 36px; flex-shrink: 0; text-align: right; color: var(--ink-3); }}
.report-missed {{ background: #fbeaea; border-radius: 8px; padding: 0.8rem 1rem; }}
.report-missed h4 {{ margin: 0 0 0.5rem; font-size: 0.72rem; color: var(--rust); }}
.report-missed-item {{ display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: baseline; font-size: 0.66rem; padding: 0.35rem 0; border-bottom: 1px solid rgba(155,34,38,0.12); }}
.report-missed-item:last-child {{ border-bottom: none; }}
.report-missed-q {{ color: var(--ink); flex: 1; min-width: 200px; }}
.report-missed-you {{ color: #c0392b; text-decoration: line-through; }}
.report-missed-correct {{ color: #2f7d52; font-weight: 600; }}
.report-perfect {{ background: var(--jade-pale); border-radius: 8px; padding: 1rem; font-size: 0.72rem; color: var(--jade); font-weight: 600; text-align: center; }}
.slide-close {{ display: block; background: {theme['accent']['dark']}; border-radius: 0 0 14px 14px; }}
.close-inner {{ padding: 3rem 3.5rem; display: flex; align-items: center; justify-content: space-between; }}
.close-zh {{ font-family: 'Noto Serif SC', serif; font-size: 5rem; font-weight: 700; color: var(--white); }}
.close-detail .py {{ font-size: 1rem; color: var(--accent-pale); letter-spacing: 0.2em; }}
.close-detail .en {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.9rem; color: #f6e05e; margin-top: 0.2rem; }}
.close-detail .sub {{ font-size: 0.62rem; color: rgba(255,255,255,0.3); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 1rem; }}
@media print {{
  body {{ background: white; padding: 0; }}
  .deck {{ max-width: 100%; }}
  .slide {{ break-inside: avoid; break-after: page; margin-bottom: 0; }}
  .slide:last-of-type {{ break-after: auto; }}
  .deck-brand {{ display: none; }}
}}
@media (max-width: 640px) {{
  .slide {{ grid-template-columns: 48px 1fr !important; }}
  .sidebar {{ padding: 1rem 0.4rem; }}
  .content {{ padding: 1.25rem; }}
  .vocab-grid {{ grid-template-columns: repeat(2,1fr); }}
  .cover-zh {{ font-size: 3.5rem; }}
}}
</style>
</head>
'''


def FOOT_TEMPLATE(group_names_json):
    return f'''<script>
(function () {{
  var lessonId = document.body.dataset.lessonId || '';
  var allInputs = Array.prototype.slice.call(document.querySelectorAll('.quiz-input'));
  var reportShown = false;
  var wrongAnswers = [];
  var GROUP_NAMES = {group_names_json};
  function escapeHtml(s) {{
    return String(s).replace(/[&<>"]/g, function (c) {{
      return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }}[c];
    }});
  }}
  function logAttempt(payload) {{
    if (!lessonId) return;
    fetch('/api/lessons/attempt', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }}, body: JSON.stringify(payload) }}).catch(function () {{}});
  }}
  function logCompletion(score, total, groupList) {{
    if (!lessonId) return;
    fetch('/api/lessons/complete', {{ method: 'POST', headers: {{ 'Content-Type': 'application/json' }}, body: JSON.stringify({{ lessonId: lessonId, score: score, total: total, groups: groupList }}) }}).catch(function () {{}});
  }}
  function buildReport() {{
    var groups = {{}};
    document.querySelectorAll('[data-quiz-score]').forEach(function (box) {{
      var groupId = box.dataset.group || 'default';
      groups[groupId] = {{ groupId: groupId, score: Number(box.querySelector('.score-correct').textContent), total: Number(box.dataset.total) }};
    }});
    var groupList = Object.keys(groups).map(function (k) {{ return groups[k]; }});
    var score = groupList.reduce(function (s, g) {{ return s + g.score; }}, 0);
    var total = groupList.reduce(function (s, g) {{ return s + g.total; }}, 0);
    var pct = total > 0 ? Math.round((score / total) * 100) : 0;
    var scoreBox = document.getElementById('report-score');
    if (scoreBox) {{ scoreBox.innerHTML = '<span class="big">' + score + '/' + total + '</span><span class="pct">' + pct + '%</span>'; }}
    var groupsBox = document.getElementById('report-groups');
    if (groupsBox) {{
      groupsBox.innerHTML = groupList.map(function (g) {{
        var p = g.total > 0 ? (g.score / g.total) * 100 : 0;
        var weak = p < 100 ? ' weak' : '';
        return '<div class="report-group-row"><div class="report-group-name">' + (GROUP_NAMES[g.groupId] || g.groupId) + '</div><div class="report-group-bar"><div class="report-group-fill' + weak + '" style="width:' + p + '%"></div></div><div class="report-group-score">' + g.score + '/' + g.total + '</div></div>';
      }}).join('');
    }}
    var missedBox = document.getElementById('report-missed');
    if (missedBox) {{
      if (wrongAnswers.length === 0) {{ missedBox.innerHTML = '<div class="report-perfect">完美！Perfect score — every answer right. 🎉</div>'; }}
      else {{
        missedBox.innerHTML = '<div class="report-missed"><h4>Words & phrases to review · 需要复习的词</h4>' + wrongAnswers.map(function (w) {{
          return '<div class="report-missed-item"><span class="report-missed-q">' + escapeHtml(w.questionText) + '</span><span class="report-missed-you">' + escapeHtml(w.userAnswer || '(blank)') + '</span><span class="report-missed-correct">' + w.reveal + '</span></div>';
        }}).join('') + '</div>';
      }}
    }}
    var slide = document.getElementById('lesson-report-slide');
    if (slide) {{ slide.style.display = 'grid'; slide.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
    logCompletion(score, total, groupList);
  }}
  function maybeShowReport() {{
    if (reportShown) return;
    var allDone = allInputs.every(function (i) {{ return i.disabled; }});
    if (!allDone) return;
    reportShown = true; buildReport();
  }}
  allInputs.forEach(function (input, globalIndex) {{
    var row = input.closest('.quiz-game');
    var feedback = row.querySelector('.quiz-feedback');
    var checkBtn = row.querySelector('.quiz-check-btn');
    var answers = (input.dataset.answer || '').split('|').map(function (a) {{ return a.trim().toLowerCase(); }});
    var reveal = input.dataset.reveal || '';
    var scoreBox = input.closest('.content') ? input.closest('.content').querySelector('[data-quiz-score]') : null;
    var questionText = input.closest('.phone-block') ? input.closest('.phone-block').querySelector('.quiz-q').textContent.trim() : '';
    function check() {{
      if (input.disabled) return;
      var val = input.value.trim().toLowerCase();
      if (!val) return;
      var correct = answers.indexOf(val) !== -1;
      feedback.className = 'quiz-feedback ' + (correct ? 'correct' : 'wrong');
      feedback.innerHTML = (correct ? '对! Duì! Right!' : '错! Cuò! Wrong!') + (reveal ? '<span class="reveal">' + reveal + '</span>' : '');
      input.classList.add(correct ? 'flash-correct' : 'flash-wrong');
      if (checkBtn) {{ checkBtn.classList.add(correct ? 'correct' : 'wrong'); checkBtn.textContent = correct ? '✓' : '✗'; checkBtn.disabled = true; }}
      input.disabled = true;
      if (correct && scoreBox) {{ var counter = scoreBox.querySelector('.score-correct'); counter.textContent = String(Number(counter.textContent) + 1); }}
      if (!correct) {{ wrongAnswers.push({{ questionText: questionText, userAnswer: input.value.trim(), reveal: reveal }}); }}
      logAttempt({{ lessonId: lessonId, groupId: scoreBox ? scoreBox.dataset.group : 'default', questionIndex: globalIndex, questionText: questionText, userAnswer: input.value.trim(), correct: correct }});
      maybeShowReport();
    }}
    input.addEventListener('keydown', function (e) {{ if (e.key === 'Enter') check(); }});
    if (checkBtn) checkBtn.addEventListener('click', check);
  }});
}})();
</script>
'''


# ---------------------------------------------------------------------------
# STORY DATA
# ---------------------------------------------------------------------------

SUN_ICON = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <circle cx="16" cy="16" r="5" fill="rgba(255,255,255,0.9)"/>
      <path d="M16 5v3M16 24v3M5 16h3M24 16h3M8.3 8.3l2.1 2.1M21.6 21.6l2.1 2.1M8.3 23.7l2.1-2.1M21.6 10.4l2.1-2.1" stroke="rgba(255,255,255,0.85)" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M10 26c0-3.3 2.7-6 6-6s6 2.7 6 6" fill="rgba(255,255,255,0.4)" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    </svg>'''

TALK_ICON = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <path d="M8 22h16M8 22v-8c0-3.3 2.7-6 6-6h4c3.3 0 6 2.7 6 6v8" stroke="rgba(255,255,255,0.9)" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="13" cy="15" r="1.5" fill="rgba(255,255,255,0.9)"/>
      <circle cx="19" cy="15" r="1.5" fill="rgba(255,255,255,0.9)"/>
    </svg>'''

WEATHER_V2_ICON = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <circle cx="22" cy="12" r="5" fill="rgba(255,255,255,0.9)"/>
      <path d="M22 5v2M22 17v2M15 12h2M27 12h2" stroke="rgba(255,255,255,0.85)" stroke-width="1.8" stroke-linecap="round"/>
      <ellipse cx="14" cy="22" rx="9" ry="5" fill="rgba(255,255,255,0.4)"/>
      <path d="M9 27l-2 3M14 27l0 3M19 27l2 3" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" stroke-linecap="round"/>
    </svg>'''


STORIES = {
    "mood-weather": {
        "id": "mood-weather",
        "title_zh": "心情和天气",
        "title_py": "xīn qíng hé tiān qì",
        "title_en": "Mood & Weather",
        "eyebrow": "Daily life · 日常生活",
        "close_zh": "再见",
        "close_py": "Zàijiàn",
        "close_en": "See you next time — stay happy, rain or shine",
        "cover_icon": SUN_ICON,
        "theme": {
            "title_zh": "心情和天气",
            "title_en": "Mood & Weather",
            "accent": {"main": "#1d5f8a", "mid": "#4a9ec7", "dark": "#153d5c", "pale": "#e8f4fd"},
            "grammar_classes": ["rust", "gold", "jade"],
        },
        "levels": {
            "hsk-1": {
                "warm_title": "你好吗？今天天气怎么样？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ hǎo ma? Jīntiān tiānqì zěnmeyàng?</span>",
                "warm_tip": "Point to the sky and say: 今天天气很好。 / 我不开心。",
                "warm_chips": [("太阳", "sun"), ("雨", "rain"), ("雪", "snow"), ("云", "cloud"), ("开心", "happy"), ("好", "good")],
                "vocab": [
                    ("天气", "tiān qì", "weather", "cat-weather"),
                    ("太阳", "tài yáng", "sun", "cat-weather"),
                    ("云", "yún", "cloud", "cat-weather"),
                    ("雨", "yǔ", "rain", "cat-weather"),
                    ("雪", "xuě", "snow", "cat-weather"),
                    ("冷", "lěng", "cold", "cat-weather"),
                    ("热", "rè", "hot", "cat-weather"),
                    ("开心", "kāi xīn", "happy", "cat-mood"),
                    ("好", "hǎo", "good", "cat-mood"),
                    ("不好", "bù hǎo", "not good", "cat-mood"),
                    ("很", "hěn", "very", "cat-gram"),
                    ("吗", "ma", "question particle", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "很",
                        "strip": [("noun", "e.g. 天气"), ("很", "hěn"), ("adj", "good / hot")],
                        "en": "A is very + adjective",
                        "ex": [
                            ("天气<span class=\"key\">很</span>好。", "Tiānqì hěn hǎo.", "The weather is very good."),
                            ("我<span class=\"key\">很</span>开心。", "Wǒ hěn kāixīn.", "I am very happy."),
                            ("太阳<span class=\"key\">很</span>大。", "Tàiyáng hěn dà.", "The sun is very big."),
                        ],
                    },
                    {
                        "label": "吗",
                        "strip": [("statement", "e.g. 你好"), ("吗", "ma"), ("?", "")],
                        "en": "Yes / no question",
                        "ex": [
                            ("你开心<span class=\"key\">吗</span>？", "Nǐ kāixīn ma?", "Are you happy?"),
                            ("今天天气好<span class=\"key\">吗</span>？", "Jīntiān tiānqì hǎo ma?", "Is the weather good today?"),
                        ],
                    },
                    {
                        "label": "不",
                        "strip": [("不", "bù"), ("adj / verb", "good / like")],
                        "en": "not + adj / verb",
                        "ex": [
                            ("今天天气<span class=\"key\">不</span>好。", "Jīntiān tiānqì bù hǎo.", "Today's weather is not good."),
                            ("我<span class=\"key\">不</span>开心。", "Wǒ bù kāixīn.", "I am not happy."),
                        ],
                    },
                ],
                "dialogue_title": "你好吗？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ hǎo ma?</span>",
                "dialogue": [
                    ("a", "A — Ask", "你好！你好吗？", "Nǐ hǎo! Nǐ hǎo ma?", "Hello! How are you?"),
                    ("b", "B — Answer", "我很好。谢谢你。", "Wǒ hěn hǎo. Xièxie nǐ.", "I'm very good. Thank you."),
                    ("a", "A — Ask", "今天天气好吗？", "Jīntiān tiānqì hǎo ma?", "Is the weather good today?"),
                    ("b", "B — Answer", "很好。太阳很大。", "Hěn hǎo. Tàiyáng hěn dà.", "Very good. The sun is big."),
                ],
                "review_chips": [("太阳", "sun"), ("雨", "rain"), ("雪", "snow"), ("云", "cloud"), ("冷", "cold"), ("热", "hot"), ("开心", "happy"), ("很好", "very good")],
                "review_sentences": [("今天天气很好。",), ("你开心吗？",), ("我很开心。/ 我不开心。",)],
                "quizzes": [
                    ("Weather · 天气", "group-1", "天气词", [
                        ("'sun' 用中文怎么说？", "How do you say 'sun'?", ["太阳", "tài yáng", "tai yang"], '太阳 <span class="py">tài yáng · sun</span>'),
                        ("'rain' 用中文怎么说？", "How do you say 'rain'?", ["雨", "yǔ", "yu", "下雨"], '雨 / 下雨 <span class="py">yǔ / xià yǔ · rain</span>'),
                        ("'cold' 用中文怎么说？", "How do you say 'cold'?", ["冷", "lěng", "leng"], '冷 <span class="py">lěng · cold</span>'),
                    ]),
                    ("Mood · 心情", "group-2", "心情词", [
                        ("'happy' 用中文怎么说？", "How do you say 'happy'?", ["开心", "kāi xīn", "kai xin"], '开心 <span class="py">kāi xīn · happy</span>'),
                        ("'good' 用中文怎么说？", "How do you say 'good'?", ["好", "hǎo", "hao"], '好 <span class="py">hǎo · good</span>'),
                        ("'not good' 用中文怎么说？", "How do you say 'not good'?", ["不好", "bù hǎo", "bu hao"], '不好 <span class="py">bù hǎo · not good</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "很 / 吗 / 不", [
                        ("天气____好。", "Tiānqì ___ hǎo.", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
                        ("你开心____？", "Nǐ kāixīn ___?", ["吗", "ma"], '吗 <span class="py">ma · question particle</span>'),
                        ("今天天气不____。", "Jīntiān tiānqì bù ___.", ["好", "hǎo", "hao"], '好 <span class="py">hǎo · good</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'weather' 用中文怎么说？", "How do you say 'weather'?", ["天气", "tiān qì", "tian qi"], '天气 <span class="py">tiān qì · weather</span>'),
                        ("'snow' 用中文怎么说？", "How do you say 'snow'?", ["雪", "xuě", "xue"], '雪 <span class="py">xuě · snow</span>'),
                        ("我____开心。", "Wǒ ___ kāixīn.", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
                    ]),
                ],
            },
            "hsk-2": {
                "warm_title": "你喜欢什么天气？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ xǐhuan shénme tiānqì?</span>",
                "warm_tip": "Tell your partner what weather you like and what you do.",
                "warm_chips": [("晴天", "sunny"), ("阴天", "cloudy"), ("下雨", "rainy"), ("下雪", "snowy"), ("暖和", "warm"), ("散步", "walk")],
                "vocab": [
                    ("天气", "tiān qì", "weather", "cat-weather"),
                    ("晴天", "qíng tiān", "sunny day", "cat-weather"),
                    ("阴天", "yīn tiān", "cloudy day", "cat-weather"),
                    ("下雨", "xià yǔ", "rain / rainy", "cat-weather"),
                    ("下雪", "xià xuě", "snow / snowy", "cat-weather"),
                    ("暖和", "nuǎn huo", "warm", "cat-weather"),
                    ("冷", "lěng", "cold", "cat-weather"),
                    ("热", "rè", "hot", "cat-weather"),
                    ("心情", "xīn qíng", "mood", "cat-mood"),
                    ("开心", "kāi xīn", "happy", "cat-mood"),
                    ("难过", "nán guò", "sad", "cat-mood"),
                    ("不错", "bú cuò", "not bad", "cat-mood"),
                    ("喜欢", "xǐ huan", "like", "cat-act"),
                    ("散步", "sàn bù", "take a walk", "cat-act"),
                    ("在家", "zài jiā", "at home", "cat-act"),
                    ("看书", "kàn shū", "read a book", "cat-act"),
                    ("让", "ràng", "make / let", "cat-gram"),
                    ("的时候", "de shí hòu", "when", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "让",
                        "strip": [("weather", "e.g. 晴天"), ("让", "ràng"), ("person + 心情", "me happy")],
                        "en": "A makes B's mood good / bad",
                        "ex": [
                            ("<span class=\"key-r\">晴天</span><span class=\"key\">让</span>我<span class=\"key-r\">开心</span>。", "Qíngtiān ràng wǒ kāixīn.", "Sunny weather makes me happy."),
                            ("<span class=\"key-r\">下雨</span><span class=\"key\">让</span>我<span class=\"key-r\">难过</span>。", "Xià yǔ ràng wǒ nánguò.", "Rain makes me sad."),
                        ],
                    },
                    {
                        "label": "的时候",
                        "strip": [("situation", "e.g. 天气好"), ("的时候", "de shíhòu"), ("I like / do…", "")],
                        "en": "When…, I like / do…",
                        "ex": [
                            ("<span class=\"key\">天气好的时候</span>，我喜欢去公园散步。", "Tiānqì hǎo de shíhòu, wǒ xǐhuan qù gōngyuán sànbù.", "When the weather is good, I like walking in the park."),
                            ("<span class=\"key\">下雨的时候</span>，我在家看书。", "Xià yǔ de shíhòu, wǒ zài jiā kànshū.", "When it rains, I read at home."),
                        ],
                    },
                    {
                        "label": "也",
                        "strip": [("A", "person"), ("也", "yě"), ("verb / adj", "like / happy")],
                        "en": "A also…",
                        "ex": [
                            ("我<span class=\"key\">也</span>喜欢晴天。", "Wǒ yě xǐhuan qíngtiān.", "I also like sunny weather."),
                            ("他<span class=\"key\">也</span>不开心。", "Tā yě bù kāixīn.", "He is also unhappy."),
                        ],
                    },
                ],
                "dialogue_title": "今天天气怎么样？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Jīntiān tiānqì zěnme yàng?</span>",
                "dialogue": [
                    ("a", "A — Ask", "你住的地方天气怎么样？", "Nǐ zhù de dìfāng tiānqì zěnme yàng?", "How is the weather where you live?"),
                    ("b", "B — Answer", "今天晴天，不太冷，也不太热。", "Jīntiān qíngtiān, bú tài lěng, yě bú tài rè.", "It's sunny today, not too cold or too hot."),
                    ("a", "A — Ask", "天气好的时候，你喜欢做什么？", "Tiānqì hǎo de shíhòu, nǐ xǐhuan zuò shénme?", "What do you like to do when the weather is good?"),
                    ("b", "B — Answer", "我喜欢去公园散步。下雨的时候，我在家看书。", "Wǒ xǐhuan qù gōngyuán sànbù. Xià yǔ de shíhòu, wǒ zài jiā kànshū.", "I like walking in the park. When it rains, I read at home."),
                ],
                "review_chips": [("天气怎么样？", "how's weather?"), ("不太冷也不太热", "not too cold/hot"), ("天气好的时候", "when weather is good"), ("让", "make"), ("的时候", "when"), ("也", "also")],
                "review_sentences": [("晴天让我开心。",), ("天气好的时候，我喜欢去公园散步。",), ("我也喜欢在家看书。",)],
                "quizzes": [
                    ("Weather · 天气", "group-1", "天气词", [
                        ("'sunny day' 用中文怎么说？", "How do you say 'sunny day'?", ["晴天", "qíng tiān", "qing tian"], '晴天 <span class="py">qíng tiān · sunny day</span>'),
                        ("'cloudy day' 用中文怎么说？", "How do you say 'cloudy day'?", ["阴天", "yīn tiān", "yin tian"], '阴天 <span class="py">yīn tiān · cloudy day</span>'),
                        ("'warm' 用中文怎么说？", "How do you say 'warm'?", ["暖和", "nuǎn huo", "nuan huo"], '暖和 <span class="py">nuǎn huo · warm</span>'),
                    ]),
                    ("Mood · 心情", "group-2", "心情词", [
                        ("'mood' 用中文怎么说？", "How do you say 'mood'?", ["心情", "xīn qíng", "xin qing"], '心情 <span class="py">xīn qíng · mood</span>'),
                        ("'sad' 用中文怎么说？", "How do you say 'sad'?", ["难过", "nán guò", "nan guo"], '难过 <span class="py">nán guò · sad</span>'),
                        ("'not bad' 用中文怎么说？", "How do you say 'not bad'?", ["不错", "bú cuò", "bu cuo"], '不错 <span class="py">bú cuò · not bad</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "让 / 的时候 / 也", [
                        ("晴天____我开心。", "Qíngtiān ___ wǒ kāixīn.", ["让", "ràng", "rang"], '让 <span class="py">ràng · make</span>'),
                        ("天气好的时候，我喜欢____。", "Tiānqì hǎo de shíhòu, wǒ xǐhuan ___.", ["散步", "sàn bù", "san bu"], '散步 <span class="py">sàn bù · take a walk</span>'),
                        ("我____喜欢晴天。", "Wǒ ___ xǐhuan qíngtiān.", ["也", "yě", "ye"], '也 <span class="py">yě · also</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'take a walk' 用中文怎么说？", "How do you say 'take a walk'?", ["散步", "sàn bù", "san bu"], '散步 <span class="py">sàn bù · take a walk</span>'),
                        ("下雨的时候，我在家____。", "Xià yǔ de shíhòu, wǒ zài jiā ___.", ["看书", "kàn shū", "kan shu"], '看书 <span class="py">kàn shū · read</span>'),
                        ("阴天让我的心情____。", "Yīntiān ràng wǒ de xīnqíng ___.", ["不好", "bù hǎo", "bu hao"], '不好 <span class="py">bù hǎo · not good</span>'),
                    ]),
                ],
            },

            "hsk-4": {
                "warm_title": "天气和心情有什么关系？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiānqì hé xīnqíng yǒu shénme guānxi?</span>",
                "warm_tip": "Discuss how weather affects your mood and daily plans.",
                "warm_chips": [("晴朗", "sunny/clear"), ("潮湿", "humid"), ("干燥", "dry"), ("郁闷", "depressed"), ("放松", "relaxed"), ("影响", "influence")],
                "vocab": [
                    ("天气", "tiān qì", "weather", "cat-weather"),
                    ("气候", "qì hòu", "climate", "cat-weather"),
                    ("晴朗", "qíng lǎng", "sunny and clear", "cat-weather"),
                    ("阴天", "yīn tiān", "cloudy day", "cat-weather"),
                    ("下雨", "xià yǔ", "rain / rainy", "cat-weather"),
                    ("下雪", "xià xuě", "snow / snowy", "cat-weather"),
                    ("潮湿", "cháo shī", "humid", "cat-weather"),
                    ("干燥", "gān zào", "dry", "cat-weather"),
                    ("心情", "xīn qíng", "mood", "cat-mood"),
                    ("开心", "kāi xīn", "happy", "cat-mood"),
                    ("难过", "nán guò", "sad", "cat-mood"),
                    ("郁闷", "yù mèn", "depressed / gloomy", "cat-mood"),
                    ("放松", "fàng sōng", "relaxed", "cat-mood"),
                    ("影响", "yǐng xiǎng", "influence / affect", "cat-act"),
                    ("改变", "gǎi biàn", "change", "cat-act"),
                    ("决定", "jué dìng", "decide", "cat-act"),
                    ("不但", "bù dàn", "not only", "cat-gram"),
                    ("而且", "ér qiě", "but also", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "不但…而且…",
                        "strip": [("不但", "bùdàn"), ("A", ""), ("而且", "érqiě"), ("B", "")],
                        "en": "Not only A but also B",
                        "ex": [
                            ("<span class=\"key\">不但</span>天气好，<span class=\"key\">而且</span>我的心情也很好。", "Bùdàn tiānqì hǎo, érqiě wǒ de xīnqíng yě hěn hǎo.", "Not only is the weather good, but my mood is also good."),
                            ("下雨<span class=\"key\">不但</span>让我难过，<span class=\"key\">而且</span>让我不想出门。", "Xià yǔ bùdàn ràng wǒ nánguò, érqiě ràng wǒ bù xiǎng chūmén.", "Rain not only makes me sad, but also makes me not want to go out."),
                        ],
                    },
                    {
                        "label": "对…有影响",
                        "strip": [("weather / thing", ""), ("对", "duì"), ("mood", ""), ("有影响", "yǒu yǐngxiǎng")],
                        "en": "has an influence on…",
                        "ex": [
                            ("天气<span class=\"key\">对</span>我的心情<span class=\"key\">有影响</span>。", "Tiānqì duì wǒ de xīnqíng yǒu yǐngxiǎng.", "The weather has an influence on my mood."),
                            ("音乐<span class=\"key\">对</span>他的心情<span class=\"key\">有很大的影响</span>。", "Yīnyuè duì tā de xīnqíng yǒu hěn dà de yǐngxiǎng.", "Music has a big influence on his mood."),
                        ],
                    },
                    {
                        "label": "因为…所以…",
                        "strip": [("因为", "yīnwèi"), ("reason", ""), ("所以", "suǒyǐ"), ("result", "")],
                        "en": "Because…, therefore…",
                        "ex": [
                            ("<span class=\"key\">因为</span>今天下雨，<span class=\"key\">所以</span>我的心情不太好。", "Yīnwèi jīntiān xià yǔ, suǒyǐ wǒ de xīnqíng bú tài hǎo.", "Because it's raining today, my mood isn't very good."),
                            ("<span class=\"key\">因为</span>天气晴朗，<span class=\"key\">所以</span>我想去散步。", "Yīnwèi tiānqì qínglǎng, suǒyǐ wǒ xiǎng qù sànbù.", "Because the weather is sunny and clear, I want to go for a walk."),
                        ],
                    },
                ],
                "dialogue_title": "天气影响心情 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiānqì yǐngxiǎng xīnqíng</span>",
                "dialogue": [
                    ("a", "A — Ask", "你觉得天气会影响心情吗？", "Nǐ juéde tiānqì huì yǐngxiǎng xīnqíng ma?", "Do you think weather affects mood?"),
                    ("b", "B — Answer", "当然会。晴朗的天气让我开心，阴雨天让我有点郁闷。", "Dāngrán huì. Qínglǎng de tiānqì ràng wǒ kāixīn, yīnyǔ tiān ràng wǒ yǒudiǎn yùmèn.", "Of course. Sunny weather makes me happy, rainy days make me a bit gloomy."),
                    ("a", "A — Ask", "那你下雨天一般做什么？", "Nà nǐ xià yǔ tiān yìbān zuò shénme?", "Then what do you usually do on rainy days?"),
                    ("b", "B — Answer", "因为下雨天不能出门，所以我在家听音乐、看电影，让自己放松。", "Yīnwèi xià yǔ tiān bù néng chūmén, suǒyǐ wǒ zài jiā tīng yīnyuè, kàn diànyǐng, ràng zìjǐ fàngsōng.", "Because I can't go out on rainy days, I listen to music and watch movies at home to relax."),
                ],
                "review_chips": [("晴朗", "clear"), ("潮湿", "humid"), ("干燥", "dry"), ("郁闷", "gloomy"), ("放松", "relax"), ("影响", "influence"), ("不但…而且…", "not only…but also"), ("对…有影响", "influence on")],
                "review_sentences": [("天气对我的心情有影响。",), ("下雨不但让我难过，而且让我不想出门。",), ("因为天气晴朗，所以我想去散步。",)],
                "quizzes": [
                    ("Weather · 天气", "group-1", "天气词", [
                        ("'humid' 用中文怎么说？", "How do you say 'humid'?", ["潮湿", "cháo shī", "chao shi"], '潮湿 <span class="py">cháoshī · humid</span>'),
                        ("'dry' 用中文怎么说？", "How do you say 'dry'?", ["干燥", "gān zào", "gan zao"], '干燥 <span class="py">gānzào · dry</span>'),
                        ("'sunny and clear' 用中文怎么说？", "How do you say 'sunny and clear'?", ["晴朗", "qíng lǎng", "qing lang"], '晴朗 <span class="py">qínglǎng · sunny and clear</span>'),
                    ]),
                    ("Mood · 心情", "group-2", "心情词", [
                        ("'depressed / gloomy' 用中文怎么说？", "How do you say 'depressed'?", ["郁闷", "yù mèn", "yu men"], '郁闷 <span class="py">yùmèn · gloomy</span>'),
                        ("'relaxed' 用中文怎么说？", "How do you say 'relaxed'?", ["放松", "fàng sōng", "fang song"], '放松 <span class="py">fàngsōng · relaxed</span>'),
                        ("'influence / affect' 用中文怎么说？", "How do you say 'influence'?", ["影响", "yǐng xiǎng", "ying xiang"], '影响 <span class="py">yǐngxiǎng · influence</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "不但 / 对…有影响 / 因为…所以…", [
                        ("今天____天气好，____我的心情也很好。", "Jīntiān ___ tiānqì hǎo, ___ wǒ de xīnqíng yě hěn hǎo.", ["不但...而且", "不但...而且...", "bùdàn...érqiě"], '不但…而且… <span class="py">bùdàn…érqiě… · not only…but also</span>'),
                        ("天气____我的心情有影响。", "Tiānqì ___ wǒ de xīnqíng yǒu yǐngxiǎng.", ["对", "duì"], '对 <span class="py">duì · toward</span>'),
                        ("____今天下雨，____我想在家。", "___ jīntiān xià yǔ, ___ wǒ xiǎng zài jiā.", ["因为...所以", "因为...所以...", "yīnwèi...suǒyǐ"], '因为…所以… <span class="py">yīnwèi…suǒyǐ… · because…so…</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'climate' 用中文怎么说？", "How do you say 'climate'?", ["气候", "qì hòu", "qi hou"], '气候 <span class="py">qìhòu · climate</span>'),
                        ("'change' 用中文怎么说？", "How do you say 'change'?", ["改变", "gǎi biàn", "gai bian"], '改变 <span class="py">gǎibiàn · change</span>'),
                        ("天气____我的心情有很大的影响。", "Tiānqì ___ wǒ de xīnqíng yǒu hěn dà de yǐngxiǎng.", ["对", "duì"], '对 <span class="py">duì · has influence on</span>'),
                    ]),
                ],
            },
            "hsk-5": {
                "warm_title": "为什么有些人更喜欢某一种天气？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Wèishénme yǒuxiē rén gèng xǐhuan mǒu yì zhǒng tiānqì?</span>",
                "warm_tip": "Give reasons for your weather preferences using 之所以…是因为…",
                "warm_chips": [("季节", "season"), ("温度", "temperature"), ("适应", "adapt"), ("情绪", "emotion"), ("效率", "efficiency"), ("因人而异", "vary by person")],
                "vocab": [
                    ("季节", "jì jié", "season", "cat-weather"),
                    ("温度", "wēn dù", "temperature", "cat-weather"),
                    ("适应", "shì yìng", "adapt", "cat-weather"),
                    ("变化", "biàn huà", "change", "cat-weather"),
                    ("情绪", "qíng xù", "emotion", "cat-mood"),
                    ("状态", "zhuàng tài", "state", "cat-mood"),
                    ("积极", "jī jí", "positive / active", "cat-mood"),
                    ("消极", "xiāo jí", "negative / passive", "cat-mood"),
                    ("效率", "xiào lǜ", "efficiency", "cat-act"),
                    ("取决于", "qǔ jué yú", "depend on", "cat-act"),
                    ("随着", "suí zhe", "along with", "cat-gram"),
                    ("之所以", "zhī suǒ yǐ", "the reason why", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "之所以…是因为…",
                        "strip": [("之所以", "zhīsuǒyǐ"), ("result", ""), ("是因为", "shì yīnwèi"), ("reason", "")],
                        "en": "The reason why… is that…",
                        "ex": [
                            ("我<span class=\"key\">之所以</span>喜欢晴天，<span class=\"key\">是因为</span>它让我情绪积极。", "Wǒ zhīsuǒyǐ xǐhuan qíngtiān, shì yīnwèi tā ràng wǒ qíngxù jījí.", "The reason I like sunny days is that they make me emotionally positive."),
                            ("他<span class=\"key\">之所以</span>冬天效率高，<span class=\"key\">是因为</span>他适应了冷天气。", "Tā zhīsuǒyǐ dōngtiān xiàolǜ gāo, shì yīnwèi tā shìyìng le lěng tiānqì.", "The reason he is efficient in winter is that he has adapted to cold weather."),
                        ],
                    },
                    {
                        "label": "随着…",
                        "strip": [("随着", "suízhe"), ("change", ""), ("也 / 越来越", "")],
                        "en": "As… (changes), …",
                        "ex": [
                            ("<span class=\"key\">随着</span>季节变化，我的心情<span class=\"key\">也</span>会变化。", "Suízhe jìjié biànhuà, wǒ de xīnqíng yě huì biànhuà.", "As the seasons change, my mood also changes."),
                            ("<span class=\"key\">随着</span>温度升高，人变得越来越懒。", "Suízhe wēndù shēnggāo, rén biàn de yuè lái yuè lǎn.", "As the temperature rises, people become lazier and lazier."),
                        ],
                    },
                    {
                        "label": "取决于",
                        "strip": [("result", ""), ("取决于", "qǔjuéyú"), ("factor", "")],
                        "en": "depends on",
                        "ex": [
                            ("心情好不好，<span class=\"key\">取决于</span>你怎麼想。", "Xīnqíng hǎo bu hǎo, qǔjuéyú nǐ zěnme xiǎng.", "Whether your mood is good depends on how you think."),
                            ("工作效率<span class=\"key\">取决于</span>天气和身体状况。", "Gōngzuò xiàolǜ qǔjuéyú tiānqì hé shēntǐ zhuàngkuàng.", "Work efficiency depends on the weather and physical condition."),
                        ],
                    },
                ],
                "dialogue_title": "天气与个人状态 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiānqì yǔ gèrén zhuàngtài</span>",
                "dialogue": [
                    ("a", "A — Ask", "你发现自己会因为天气改变心情吗？", "Nǐ fāxiàn zìjǐ huì yīnwèi tiānqì gǎibiàn xīnqíng ma?", "Do you find that your mood changes because of the weather?"),
                    ("b", "B — Answer", "会。我之所以喜欢秋天，是因为温度合适，让我既放松又有效率。", "Huì. Wǒ zhīsuǒyǐ xǐhuan qiūtiān, shì yīnwèi wēndù héshì, ràng wǒ jì fàngsōng yòu yǒu xiàolǜ.", "Yes. The reason I like autumn is that the temperature is suitable, making me both relaxed and efficient."),
                    ("a", "A — Ask", "那夏天呢？高温会不会影响你？", "Nà xiàtiān ne? Gāowēn huì bu huì yǐngxiǎng nǐ?", "What about summer? Does high temperature affect you?"),
                    ("b", "B — Answer", "随着温度升高，我确实会变得有点消极，所以我会开空调、多喝水。", "Suízhe wēndù shēnggāo, wǒ quèshí huì biàn de yǒudiǎn xiāojí, suǒyǐ wǒ huì kāi kōngtiáo, duō hē shuǐ.", "As the temperature rises, I do become a bit negative, so I turn on the AC and drink more water."),
                ],
                "review_chips": [("季节", "season"), ("温度", "temperature"), ("适应", "adapt"), ("情绪", "emotion"), ("效率", "efficiency"), ("取决于", "depend on"), ("随着", "along with"), ("之所以", "the reason why")],
                "review_sentences": [("我之所以喜欢晴天，是因为它让我情绪积极。",), ("随着季节变化，我的心情也会变化。",), ("心情好不好，取决于你怎么想。",)],
                "quizzes": [
                    ("Weather & State · 天气与状态", "group-1", "词汇", [
                        ("'temperature' 用中文怎么说？", "How do you say 'temperature'?", ["温度", "wēn dù", "wen du"], '温度 <span class="py">wēndù · temperature</span>'),
                        ("'adapt' 用中文怎么说？", "How do you say 'adapt'?", ["适应", "shì yìng", "shi ying"], '适应 <span class="py">shìyìng · adapt</span>'),
                        ("'efficiency' 用中文怎么说？", "How do you say 'efficiency'?", ["效率", "xiào lǜ", "xiao lü"], '效率 <span class="py">xiàolǜ · efficiency</span>'),
                    ]),
                    ("Mood · 心情", "group-2", "心情词", [
                        ("'emotion' 用中文怎么说？", "How do you say 'emotion'?", ["情绪", "qíng xù", "qing xu"], '情绪 <span class="py">qíngxù · emotion</span>'),
                        ("'positive' 用中文怎么说？", "How do you say 'positive'?", ["积极", "jī jí", "ji ji"], '积极 <span class="py">jījí · positive</span>'),
                        ("'negative' 用中文怎么说？", "How do you say 'negative'?", ["消极", "xiāo jí", "xiao ji"], '消极 <span class="py">xiāojí · negative</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "之所以 / 随着 / 取决于", [
                        ("我____喜欢秋天，____温度合适。", "Wǒ ___ xǐhuan qiūtiān, ___ wēndù héshì.", ["之所以...是因为", "之所以...是因为...", "zhīsuǒyǐ...shìyīnwèi"], '之所以…是因为… <span class="py">zhīsuǒyǐ…shìyīnwèi…</span>'),
                        ("____温度升高，人变得越来越懒。", "___ wēndù shēnggāo, rén biàn de yuè lái yuè lǎn.", ["随着", "suí zhe", "sui zhe"], '随着 <span class="py">suízhe · along with</span>'),
                        ("心情好不好____你怎么想。", "Xīnqíng hǎo bu hǎo ___ nǐ zěnme xiǎng.", ["取决于", "qǔ jué yú", "qu jue yu"], '取决于 <span class="py">qǔjuéyú · depend on</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'season' 用中文怎么说？", "How do you say 'season'?", ["季节", "jì jié", "ji jie"], '季节 <span class="py">jìjié · season</span>'),
                        ("'state / condition' 用中文怎么说？", "How do you say 'state'?", ["状态", "zhuàng tài", "zhuang tai"], '状态 <span class="py">zhuàngtài · state</span>'),
                        ("工作效率____天气和身体状况。", "Gōngzuò xiàolǜ ___ tiānqì hé shēntǐ zhuàngkuàng.", ["取决于", "qǔ jué yú", "qu jue yu"], '取决于 <span class="py">qǔjuéyú · depend on</span>'),
                    ]),
                ],
            },
            "hsk-6": {
                "warm_title": "气候如何塑造人的情绪与文化？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Qìhòu rúhé sùzào rén de qíngxù yǔ wénhuà?</span>",
                "warm_tip": "Discuss the deeper relationship between climate, emotion, and culture.",
                "warm_chips": [("潜移默化", "subtly influence"), ("根深蒂固", "deep-rooted"), ("因地制宜", "adapt locally"), ("气候带", "climate zone"), ("心态", "mindset"), ("生活方式", "lifestyle")],
                "vocab": [
                    ("气候", "qì hòu", "climate", "cat-weather"),
                    ("气候带", "qì hòu dài", "climate zone", "cat-weather"),
                    ("温带", "wēn dài", "temperate zone", "cat-weather"),
                    ("热带", "rè dài", "tropical zone", "cat-weather"),
                    ("潜移默化", "qián yí mò huà", "subtly influence", "cat-weather"),
                    ("根深蒂固", "gēn shēn dì gù", "deep-rooted", "cat-mood"),
                    ("心态", "xīn tài", "mindset", "cat-mood"),
                    ("乐观", "lè guān", "optimistic", "cat-mood"),
                    ("悲观", "bēi guān", "pessimistic", "cat-mood"),
                    ("塑造", "sù zào", "shape / mold", "cat-act"),
                    ("因地制宜", "yīn dì zhì yí", "adapt to local conditions", "cat-act"),
                    ("换言之", "huàn yán zhī", "in other words", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "潜移默化地…",
                        "strip": [("潜移默化", "qiányímòhuà"), ("地", "de"), ("verb", "influence")],
                        "en": "subtly influence…",
                        "ex": [
                            ("气候会<span class=\"key\">潜移默化地</span>影响人的心态。", "Qìhòu huì qiányímòhuà de yǐngxiǎng rén de xīntài.", "Climate will subtly influence people's mindset."),
                            ("文化习惯<span class=\"key\">潜移默化地</span>塑造了我们的生活方式。", "Wénhuà xíguàn qiányímòhuà de sùzào le wǒmen de shēnghuó fāngshì.", "Cultural habits subtly shape our lifestyle."),
                        ],
                    },
                    {
                        "label": "之所以…究其原因为…",
                        "strip": [("之所以", "zhīsuǒyǐ"), ("result", ""), ("究其原因为", "qiū jí qí yuán wéi"), ("root cause", "")],
                        "en": "The reason why… is rooted in…",
                        "ex": [
                            ("北方人之所以更乐观，<span class=\"key\">究其原因为</span>阳光充足。", "Běifāng rén zhīsuǒyǐ gèng lèguān, qiū jí qí yuán wéi yángguāng chōngzú.", "The reason northerners are more optimistic is rooted in ample sunshine."),
                            ("他们之所以适应寒冷，<span class=\"key\">究其原因为</span>根深蒂固的生活习惯。", "Tāmen zhīsuǒyǐ shìyìng hánlěng, qiū jí qí yuán wéi gēnshēndìgù de shēnghuó xíguàn.", "The reason they adapt to cold is rooted in deep-rooted living habits."),
                        ],
                    },
                    {
                        "label": "换言之",
                        "strip": [("换言之", "huànyánzhī"), ("restatement", "")],
                        "en": "in other words",
                        "ex": [
                            ("天气影响情绪；<span class=\"key\">换言之</span>，环境塑造心态。", "Tiānqì yǐngxiǎng qíngxù; huànyánzhī, huánjìng sùzào xīntài.", "Weather affects emotion; in other words, environment shapes mindset."),
                            ("他们因地制宜；<span class=\"key\">换言之</span>，他们根据环境调整生活方式。", "Tāmen yīndìzhìyí; huànyánzhī, tāmen gēnjù huánjìng tiáozhěng shēnghuó fāngshì.", "They adapt to local conditions; in other words, they adjust their lifestyle according to the environment."),
                        ],
                    },
                ],
                "dialogue_title": "气候与文化心态 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Qìhòu yǔ wénhuà xīntài</span>",
                "dialogue": [
                    ("a", "A — Analyst", "有研究指出，阳光充足地区的人更乐观。你觉得原因是什么？", "Yǒu yánjiū zhǐchū, yángguāng chōngzú dìqū de rén gèng lèguān. Nǐ juéde yuányīn shì shénme?", "Some studies show people in sunny regions are more optimistic. What do you think is the reason?"),
                    ("b", "B — Expert", "究其原因为气候潜移默化地影响了心态。阳光让人积极，阴雨则容易让人低落。", "Qiū jí qí yuán wéi qìhòu qiányímòhuà de yǐngxiǎng le xīntài. Yángguāng ràng rén jījí, yīnyǔ zé róngyì ràng rén dīluò.", "The root cause is that climate subtly influences mindset. Sunshine makes people positive, while rain tends to make people low."),
                    ("a", "A — Analyst", "那不同气候带的人生活方式也不同吗？", "Nà bùtóng qìhòudài de rén shēnghuó fāngshì yě bùtóng ma?", "Do people in different climate zones also have different lifestyles?"),
                    ("b", "B — Expert", "当然。热带地区的人生活节奏较慢；换言之，他们更懂得因地制宜，适应环境。", "Dāngrán. Rèdài dìqū de rén shēnghuó jiézòu jiào màn; huànyánzhī, tāmen gèng dǒngde yīndìzhìyí, shìyìng huánjìng.", "Of course. People in tropical regions have a slower pace of life; in other words, they better understand adapting to local conditions."),
                ],
                "review_chips": [("潜移默化", "subtly"), ("根深蒂固", "deep-rooted"), ("因地制宜", "adapt locally"), ("换言之", "in other words"), ("究其原因为", "root cause"), ("心态", "mindset")],
                "review_sentences": [("气候会潜移默化地影响人的心态。",), ("北方人之所以更乐观，究其原因为阳光充足。",), ("天气影响情绪；换言之，环境塑造心态。",)],
                "quizzes": [
                    ("Climate · 气候", "group-1", "气候词", [
                        ("'climate zone' 用中文怎么说？", "How do you say 'climate zone'?", ["气候带", "qì hòu dài", "qi hou dai"], '气候带 <span class="py">qìhòudài · climate zone</span>'),
                        ("'temperate zone' 用中文怎么说？", "How do you say 'temperate zone'?", ["温带", "wēn dài", "wen dai"], '温带 <span class="py">wēndài · temperate zone</span>'),
                        ("'subtly influence' 用中文怎么说？", "How do you say 'subtly influence'?", ["潜移默化", "qián yí mò huà", "qian yi mo hua"], '潜移默化 <span class="py">qiányímòhuà · subtly influence</span>'),
                    ]),
                    ("Mindset · 心态", "group-2", "心态词", [
                        ("'mindset' 用中文怎么说？", "How do you say 'mindset'?", ["心态", "xīn tài", "xin tai"], '心态 <span class="py">xīntài · mindset</span>'),
                        ("'optimistic' 用中文怎么说？", "How do you say 'optimistic'?", ["乐观", "lè guān", "le guan"], '乐观 <span class="py">lèguān · optimistic</span>'),
                        ("'deep-rooted' 用中文怎么说？", "How do you say 'deep-rooted'?", ["根深蒂固", "gēn shēn dì gù", "gen shen di gu"], '根深蒂固 <span class="py">gēnshēndìgù · deep-rooted</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "潜移默化 / 究其原因为 / 换言之", [
                        ("气候会____地影响人的心态。", "Qìhòu huì ___ de yǐngxiǎng rén de xīntài.", ["潜移默化", "qiányímòhuà", "qian yi mo hua"], '潜移默化 <span class="py">qiányímòhuà · subtly</span>'),
                        ("他们之所以适应寒冷，____根深蒂固的生活习惯。", "Tāmen zhīsuǒyǐ shìyìng hánlěng, ___ gēnshēndìgù de shēnghuó xíguàn.", ["究其原因为", "qiū jí qí yuán wéi", "qiu ji qi yuan wei"], '究其原因为 <span class="py">qiūjíqíyuánwéi · root cause is</span>'),
                        ("他们因地制宜；____，他们根据环境调整生活方式。", "Tāmen yīndìzhìyí; ___, tāmen gēnjù huánjìng tiáozhěng shēnghuó fāngshì.", ["换言之", "huàn yán zhī", "huan yan zhi"], '换言之 <span class="py">huànyánzhī · in other words</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'shape / mold' 用中文怎么说？", "How do you say 'shape'?", ["塑造", "sù zào", "su zao"], '塑造 <span class="py">sùzào · shape</span>'),
                        ("'pessimistic' 用中文怎么说？", "How do you say 'pessimistic'?", ["悲观", "bēi guān", "bei guan"], '悲观 <span class="py">bēiguān · pessimistic</span>'),
                        ("天气影响情绪；____，环境塑造心态。", "Tiānqì yǐngxiǎng qíngxù; ___, huánjìng sùzào xīntài.", ["换言之", "huàn yán zhī", "huan yan zhi"], '换言之 <span class="py">huànyánzhī · in other words</span>'),
                    ]),
                ],
            },
        },
    },

    "many-ways": {
        "id": "many-ways",
        "title_zh": "一句话，几种说法？",
        "title_py": "yí jù huà, jǐ zhǒng shuōfǎ?",
        "title_en": "One Idea, Many Sentences",
        "eyebrow": "Speaking · 口语",
        "close_zh": "多说",
        "close_py": "Duō shuō",
        "close_en": "The more ways you can say it, the more Chinese you are",
        "cover_icon": TALK_ICON,
        "theme": {
            "title_zh": "一句话，几种说法？",
            "title_en": "One Idea, Many Sentences",
            "accent": {"main": "#c05621", "mid": "#dd6b20", "dark": "#7c2d12", "pale": "#fff5eb"},
            "grammar_classes": ["jade", "rust", "gold"],
        },
        "levels": {
            "hsk-1": {
                "warm_title": "你会怎么说？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ huì zěnme shuō?</span>",
                "warm_tip": "One idea can be said in different ways. Try these.",
                "warm_chips": [("我饿了", "I'm hungry"), ("我想吃", "I want to eat"), ("我很好", "I'm fine"), ("谢谢", "thanks")],
                "vocab": [
                    ("饿", "è", "hungry", "cat-gram"),
                    ("想", "xiǎng", "want / think", "cat-gram"),
                    ("吃", "chī", "eat", "cat-act"),
                    ("喝", "hē", "drink", "cat-act"),
                    ("好", "hǎo", "good", "cat-mood"),
                    ("谢谢", "xiè xie", "thanks", "cat-mood"),
                    ("我", "wǒ", "I", "cat-gram"),
                    ("你", "nǐ", "you", "cat-gram"),
                    ("很", "hěn", "very", "cat-gram"),
                    ("不", "bù", "not", "cat-gram"),
                    ("了", "le", "particle", "cat-gram"),
                    ("要", "yào", "want", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "我饿了 / 我想吃",
                        "strip": [("我", "wǒ"), ("饿", "è"), ("了", "le")],
                        "en": "I'm hungry. / I want to eat.",
                        "ex": [
                            ("<span class=\"key\">我饿了</span>。", "Wǒ è le.", "I'm hungry."),
                            ("<span class=\"key\">我想吃</span>东西。", "Wǒ xiǎng chī dōngxi.", "I want to eat something."),
                            ("<span class=\"key\">我要</span>吃饭。", "Wǒ yào chī fàn.", "I want to eat."),
                        ],
                    },
                    {
                        "label": "我很好 / 我不错",
                        "strip": [("我", "wǒ"), ("很", "hěn"), ("好", "hǎo")],
                        "en": "I'm very good. / I'm fine.",
                        "ex": [
                            ("<span class=\"key\">我很好</span>。", "Wǒ hěn hǎo.", "I'm very good."),
                            ("<span class=\"key\">我不错</span>。", "Wǒ bú cuò.", "I'm not bad."),
                            ("<span class=\"key\">我还好</span>。", "Wǒ hái hǎo.", "I'm okay."),
                        ],
                    },
                    {
                        "label": "谢谢 / 谢谢你",
                        "strip": [("谢谢", "xièxie"), ("你", "nǐ")],
                        "en": "Thanks. / Thank you.",
                        "ex": [
                            ("<span class=\"key\">谢谢</span>。", "Xièxie.", "Thanks."),
                            ("<span class=\"key\">谢谢你</span>。", "Xièxie nǐ.", "Thank you."),
                            ("<span class=\"key\">多谢</span>。", "Duōxiè.", "Many thanks."),
                        ],
                    },
                ],
                "dialogue_title": "你想吃什么？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ xiǎng chī shénme?</span>",
                "dialogue": [
                    ("a", "A — Ask", "你饿了吗？", "Nǐ è le ma?", "Are you hungry?"),
                    ("b", "B — Answer", "我饿了。我想吃面条。", "Wǒ è le. Wǒ xiǎng chī miàntiáo.", "I'm hungry. I want to eat noodles."),
                    ("a", "A — Ask", "你好吗？", "Nǐ hǎo ma?", "How are you?"),
                    ("b", "B — Answer", "我很好，谢谢！", "Wǒ hěn hǎo, xièxie!", "I'm very good, thanks!"),
                ],
                "review_chips": [("我饿了", "I'm hungry"), ("我想吃", "I want to eat"), ("我很好", "I'm good"), ("谢谢", "thanks"), ("我不错", "not bad")],
                "review_sentences": [("我饿了。 / 我想吃东西。 / 我要吃饭。",), ("我很好。 / 我不错。 / 我还好。",), ("谢谢。 / 谢谢你。 / 多谢。",)],
                "quizzes": [
                    ("Ideas · 说法", "group-1", "同义表达", [
                        ("'I'm hungry' 有几种说法？", "How do you say 'I'm hungry'?", ["我饿了", "我想吃东西", "我要吃饭", "wo e le", "wo xiang chi"], '我饿了 / 我想吃东西 / 我要吃饭'),
                        ("'I'm fine' 有几种说法？", "How do you say 'I'm fine'?", ["我很好", "我不错", "我还好", "wo hen hao", "wo bu cuo"], '我很好 / 我不错 / 我还好'),
                        ("'Thanks' 有几种说法？", "How do you say 'thanks'?", ["谢谢", "谢谢你", "多谢", "xie xie", "xie xie ni"], '谢谢 / 谢谢你 / 多谢'),
                    ]),
                    ("Fill in · 填空", "group-2", "填空", [
                        ("我____了。（hungry）", "Wǒ ___ le.", ["饿", "è", "e"], '饿 <span class="py">è · hungry</span>'),
                        ("我____吃面条。", "Wǒ ___ chī miàntiáo.", ["想", "xiǎng", "xiang"], '想 <span class="py">xiǎng · want</span>'),
                        ("____你。", "___ nǐ.", ["谢谢", "xiè xie", "xie xie"], '谢谢 <span class="py">xièxie · thanks</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "了 / 想 / 很", [
                        ("我饿____。", "Wǒ è ___.", ["了", "le"], '了 <span class="py">le · completed</span>'),
                        ("我____很好。", "Wǒ ___ hěn hǎo.", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
                        ("我不____。", "Wǒ bù ___.", ["饿", "è", "e"], '饿 <span class="py">è · hungry</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'I want to eat' 用中文怎么说？", "How do you say 'I want to eat'?", ["我想吃东西", "我要吃饭", "我饿了", "wo xiang chi dongxi"], '我想吃东西 / 我要吃饭'),
                        ("'Thank you' 用中文怎么说？", "How do you say 'thank you'?", ["谢谢你", "谢谢", "多谢", "xie xie ni"], '谢谢你 / 谢谢 / 多谢'),
                        ("'I'm not bad' 用中文怎么说？", "How do you say 'I'm not bad'?", ["我不错", "我还好", "wo bu cuo"], '我不错 / 我还好'),
                    ]),
                ],
            },

            "hsk-2": {
                "warm_title": "同一种意思，不同说法 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tóng yì zhǒng yìsi, bùtóng shuōfǎ</span>",
                "warm_tip": "Use different words to say the same thing.",
                "warm_chips": [("我累了", "I'm tired"), ("我想休息", "I want to rest"), ("我不舒服", "I don't feel well"), ("我需要睡觉", "I need sleep")],
                "vocab": [
                    ("累", "lèi", "tired", "cat-mood"),
                    ("休息", "xiū xi", "rest", "cat-act"),
                    ("睡觉", "shuì jiào", "sleep", "cat-act"),
                    ("舒服", "shū fu", "comfortable", "cat-mood"),
                    ("需要", "xū yào", "need", "cat-act"),
                    ("一会儿", "yí huìr", "a while", "cat-act"),
                    ("想", "xiǎng", "want", "cat-gram"),
                    ("要", "yào", "want / need", "cat-gram"),
                    ("应该", "yīng gāi", "should", "cat-gram"),
                    ("可以", "kě yǐ", "can / may", "cat-gram"),
                    ("太", "tài", "too", "cat-gram"),
                    ("了", "le", "particle", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "我累了 / 我想休息",
                        "strip": [("我", "wǒ"), ("累", "lèi"), ("了", "le")],
                        "en": "I'm tired. / I want to rest.",
                        "ex": [
                            ("<span class=\"key\">我累了</span>。", "Wǒ lèi le.", "I'm tired."),
                            ("<span class=\"key\">我想休息</span>一会儿。", "Wǒ xiǎng xiūxi yíhuìr.", "I want to rest for a while."),
                            ("<span class=\"key\">我需要睡觉</span>。", "Wǒ xūyào shuìjiào.", "I need to sleep."),
                        ],
                    },
                    {
                        "label": "我太累了 / 我不舒服",
                        "strip": [("我", "wǒ"), ("太", "tài"), ("累", "lèi"), ("了", "le")],
                        "en": "I'm too tired. / I'm not comfortable.",
                        "ex": [
                            ("我<span class=\"key\">太</span>累了。", "Wǒ tài lèi le.", "I'm too tired."),
                            ("我<span class=\"key\">不太舒服</span>。", "Wǒ bú tài shūfu.", "I'm not very comfortable."),
                            ("我<span class=\"key\">应该</span>休息一下。", "Wǒ yīnggāi xiūxi yíxià.", "I should rest a bit."),
                        ],
                    },
                    {
                        "label": "我可以休息吗？",
                        "strip": [("我", "wǒ"), ("可以", "kěyǐ"), ("verb", "rest")],
                        "en": "Can I…?",
                        "ex": [
                            ("我<span class=\"key\">可以</span>休息吗？", "Wǒ kěyǐ xiūxi ma?", "Can I rest?"),
                            ("你<span class=\"key\">可以</span>帮我吗？", "Nǐ kěyǐ bāng wǒ ma?", "Can you help me?"),
                            ("我们<span class=\"key\">可以</span>走了吗？", "Wǒmen kěyǐ zǒu le ma?", "Can we leave?"),
                        ],
                    },
                ],
                "dialogue_title": "你累了吗？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ lèi le ma?</span>",
                "dialogue": [
                    ("a", "A — Ask", "你累了吗？", "Nǐ lèi le ma?", "Are you tired?"),
                    ("b", "B — Answer", "我有点累。我想休息一会儿。", "Wǒ yǒudiǎn lèi. Wǒ xiǎng xiūxi yíhuìr.", "I'm a bit tired. I want to rest for a while."),
                    ("a", "A — Ask", "你可以睡觉吗？", "Nǐ kěyǐ shuìjiào ma?", "Can you sleep?"),
                    ("b", "B — Answer", "现在不行。我应该先工作。", "Xiànzài bù xíng. Wǒ yīnggāi xiān gōngzuò.", "Not now. I should work first."),
                ],
                "review_chips": [("我累了", "tired"), ("我想休息", "want rest"), ("我需要睡觉", "need sleep"), ("我不太舒服", "not comfortable"), ("我可以", "I can"), ("我应该", "I should")],
                "review_sentences": [("我累了。 / 我想休息。 / 我需要睡觉。",), ("我太累了。 / 我不太舒服。",), ("我可以休息吗？ / 我应该先工作。",)],
                "quizzes": [
                    ("Ideas · 说法", "group-1", "同义表达", [
                        ("'I'm tired' 有几种说法？", "How do you say 'I'm tired'?", ["我累了", "我想休息", "我太累了", "wo lei le", "wo xiang xiuxi"], '我累了 / 我想休息 / 我太累了'),
                        ("'I want to rest' 用中文怎么说？", "How do you say 'I want to rest'?", ["我想休息", "我要休息", "wo xiang xiuxi"], '我想休息 / 我要休息'),
                        ("'Can I…?' 用中文怎么说？", "How do you say 'Can I…?'?", ["我可以...吗", "我可以休息吗", "wo keyi...ma"], '我可以…吗？'),
                    ]),
                    ("Fill in · 填空", "group-2", "填空", [
                        ("我____了。（tired）", "Wǒ ___ le.", ["累", "lèi", "lei"], '累 <span class="py">lèi · tired</span>'),
                        ("我____休息一会儿。", "Wǒ ___ xiūxi yíhuìr.", ["想", "xiǎng", "xiang"], '想 <span class="py">xiǎng · want</span>'),
                        ("我____先工作。", "Wǒ ___ xiān gōngzuò.", ["应该", "yīng gāi", "ying gai"], '应该 <span class="py">yīnggāi · should</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "太 / 可以 / 应该", [
                        ("我太____了。", "Wǒ tài ___ le.", ["累", "lèi", "lei"], '累 <span class="py">lèi · tired</span>'),
                        ("我____休息吗？", "Wǒ ___ xiūxi ma?", ["可以", "kě yǐ", "ke yi"], '可以 <span class="py">kěyǐ · can</span>'),
                        ("我不太____。", "Wǒ bú tài ___.", ["舒服", "shū fu", "shu fu"], '舒服 <span class="py">shūfu · comfortable</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'I need sleep' 用中文怎么说？", "How do you say 'I need sleep'?", ["我需要睡觉", "wo xuyao shuijiao"], '我需要睡觉'),
                        ("'I should work first' 用中文怎么说？", "How do you say 'I should work first'?", ["我应该先工作", "wo yinggai xian gongzuo"], '我应该先工作'),
                        ("'Can you help me?' 用中文怎么说？", "How do you say 'Can you help me?'?", ["你可以帮我吗", "ni keyi bang wo ma"], '你可以帮我吗？'),
                    ]),
                ],
            },
            "hsk-4": {
                "warm_title": "正式一点还是随便一点？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Zhèngshì yìdiǎn háishi suíbiàn yìdiǎn?</span>",
                "warm_tip": "Choose formal or casual ways to express yourself depending on the situation.",
                "warm_chips": [("打扰一下", "excuse me"), ("请问", "may I ask"), ("不好意思", "sorry"), ("麻烦你", "trouble you")],
                "vocab": [
                    ("打扰", "dǎ rǎo", "disturb", "cat-act"),
                    ("请问", "qǐng wèn", "may I ask", "cat-act"),
                    ("不好意思", "bù hǎo yì si", "sorry / excuse me", "cat-mood"),
                    ("麻烦", "má fan", "trouble", "cat-act"),
                    ("正式", "zhèng shì", "formal", "cat-mood"),
                    ("随便", "suí biàn", "casual", "cat-mood"),
                    ("根据", "gēn jù", "according to", "cat-act"),
                    ("情况", "qíng kuàng", "situation", "cat-act"),
                    ("决定", "jué dìng", "decide", "cat-act"),
                    ("合适", "hé shì", "suitable", "cat-mood"),
                    ("对…说", "duì...shuō", "say to…", "cat-gram"),
                    ("看情况", "kàn qíng kuàng", "see the situation", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "请问 / 打扰一下",
                        "strip": [("请问", "qǐngwèn"), ("打扰一下", "dǎrǎo yíxià")],
                        "en": "Polite ways to get attention",
                        "ex": [
                            ("<span class=\"key\">请问</span>，现在几点？", "Qǐngwèn, xiànzài jǐ diǎn?", "Excuse me, what time is it now?"),
                            ("<span class=\"key\">打扰一下</span>，我能问你一个问题吗？", "Dǎrǎo yíxià, wǒ néng wèn nǐ yí gè wèntí ma?", "Sorry to bother you, can I ask you a question?"),
                        ],
                    },
                    {
                        "label": "不好意思 / 麻烦你",
                        "strip": [("不好意思", "bùhǎoyìsi"), ("麻烦你", "máfan nǐ")],
                        "en": "Softening requests",
                        "ex": [
                            ("<span class=\"key\">不好意思</span>，请让一下。", "Bùhǎoyìsi, qǐng ràng yíxià.", "Excuse me, please make way."),
                            ("<span class=\"key\">麻烦你</span>帮我拿一下。", "Máfan nǐ bāng wǒ ná yíxià.", "Could you please help me take it?"),
                        ],
                    },
                    {
                        "label": "根据…决定…",
                        "strip": [("根据", "gēnjù"), ("situation", ""), ("决定", "juédìng"), ("action", "")],
                        "en": "Decide based on…",
                        "ex": [
                            ("<span class=\"key\">根据</span>情况<span class=\"key\">决定</span>怎么说。", "Gēnjù qíngkuàng juédìng zěnme shuō.", "Decide how to say it based on the situation."),
                            ("<span class=\"key\">看情况</span>吧。", "Kàn qíngkuàng ba.", "Let's see the situation."),
                        ],
                    },
                ],
                "dialogue_title": "怎么问时间？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Zěnme wèn shíjiān?</span>",
                "dialogue": [
                    ("a", "A — Formal", "打扰一下，请问现在几点？", "Dǎrǎo yíxià, qǐngwèn xiànzài jǐ diǎn?", "Excuse me, may I ask what time it is?"),
                    ("b", "B — Answer", "现在三点半。", "Xiànzài sān diǎn bàn.", "It's half past three now."),
                    ("a", "A — Casual", "哎，现在几点了？", "Āi, xiànzài jǐ diǎn le?", "Hey, what time is it?"),
                    ("b", "B — Answer", "三点半。", "Sān diǎn bàn.", "Half past three."),
                ],
                "review_chips": [("请问", "formal ask"), ("打扰一下", "excuse me"), ("不好意思", "sorry"), ("麻烦你", "trouble you"), ("根据情况", "based on situation"), ("看情况", "see situation")],
                "review_sentences": [("请问，现在几点？ / 打扰一下，请问现在几点？",), ("不好意思，请让一下。 / 麻烦你帮我拿一下。",), ("根据情况决定怎么说。 / 看情况吧。",)],
                "quizzes": [
                    ("Politeness · 礼貌", "group-1", "礼貌用语", [
                        ("'may I ask' 用中文怎么说？", "How do you say 'may I ask'?", ["请问", "qing wen", "qingwen"], '请问 <span class="py">qǐngwèn · may I ask</span>'),
                        ("'excuse me (soft)' 用中文怎么说？", "How do you say 'excuse me'?", ["打扰一下", "da rao yi xia", "daraoyixia"], '打扰一下 <span class="py">dǎrǎo yíxià · excuse me</span>'),
                        ("'sorry / excuse me' 用中文怎么说？", "How do you say 'sorry'?", ["不好意思", "bu hao yi si", "buhaoyisi"], '不好意思 <span class="py">bùhǎoyìsi · sorry</span>'),
                    ]),
                    ("Requests · 请求", "group-2", "请求表达", [
                        ("'trouble you' 用中文怎么说？", "How do you say 'trouble you'?", ["麻烦你", "ma fan ni", "mafanni"], '麻烦你 <span class="py">máfan nǐ · trouble you</span>'),
                        ("'formal' 用中文怎么说？", "How do you say 'formal'?", ["正式", "zheng shi", "zhengshi"], '正式 <span class="py">zhèngshì · formal</span>'),
                        ("'casual' 用中文怎么说？", "How do you say 'casual'?", ["随便", "sui bian", "suibian"], '随便 <span class="py">suíbiàn · casual</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "根据 / 看情况", [
                        ("____情况决定怎么说。", "___ qíngkuàng juédìng zěnme shuō.", ["根据", "gēn jù", "gen ju"], '根据 <span class="py">gēnjù · according to</span>'),
                        ("____吧。", "___ ba.", ["看情况", "kàn qíng kuàng", "kan qing kuang"], '看情况 <span class="py">kàn qíngkuàng · see the situation</span>'),
                        ("____你帮我拿一下。", "___ nǐ bāng wǒ ná yíxià.", ["麻烦", "má fan", "ma fan"], '麻烦 <span class="py">máfan · trouble</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'suitable' 用中文怎么说？", "How do you say 'suitable'?", ["合适", "hé shì", "he shi"], '合适 <span class="py">héshì · suitable</span>'),
                        ("'situation' 用中文怎么说？", "How do you say 'situation'?", ["情况", "qíng kuàng", "qing kuang"], '情况 <span class="py">qíngkuàng · situation</span>'),
                        ("'decide' 用中文怎么说？", "How do you say 'decide'?", ["决定", "jué dìng", "jue ding"], '决定 <span class="py">juédìng · decide</span>'),
                    ]),
                ],
            },
            "hsk-5": {
                "warm_title": "表达同一件事，语气可以有多不同？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Biǎodá tóng yí jiàn shì, yǔqì kěyǐ yǒu duō bùtóng?</span>",
                "warm_tip": "Use stronger, softer, or more indirect expressions depending on your relationship with the listener.",
                "warm_chips": [("我认为", "I think"), ("我觉得", "I feel"), ("在我看来", "in my view"), ("说实话", "to be honest")],
                "vocab": [
                    ("认为", "rèn wéi", "think / consider", "cat-act"),
                    ("觉得", "jué de", "feel / think", "cat-act"),
                    ("看法", "kàn fǎ", "opinion", "cat-act"),
                    ("观点", "guān diǎn", "viewpoint", "cat-act"),
                    ("态度", "tài du", "attitude", "cat-mood"),
                    ("语气", "yǔ qì", "tone", "cat-mood"),
                    ("直接", "zhí jiē", "direct", "cat-mood"),
                    ("委婉", "wěi wǎn", "indirect / tactful", "cat-mood"),
                    ("强烈", "qiáng liè", "strong / intense", "cat-mood"),
                    ("温和", "wēn hé", "mild / gentle", "cat-mood"),
                    ("说实话", "shuō shí huà", "to be honest", "cat-gram"),
                    ("在我看来", "zài wǒ kàn lái", "in my opinion", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "我认为 / 我觉得 / 在我看来",
                        "strip": [("I think", ""), ("认为", "rènwéi"), ("觉得", "juéde"), ("在我看来", "zài wǒ kàn lái")],
                        "en": "Different ways to give opinions",
                        "ex": [
                            ("<span class=\"key\">我认为</span>这个办法更好。", "Wǒ rènwéi zhège bànfǎ gèng hǎo.", "I think this way is better."),
                            ("<span class=\"key\">我觉得</span>天气不错。", "Wǒ juéde tiānqì búcuò.", "I feel the weather is not bad."),
                            ("<span class=\"key\">在我看来</span>，学习需要耐心。", "Zài wǒ kàn lái, xuéxí xūyào nàixīn.", "In my opinion, learning requires patience."),
                        ],
                    },
                    {
                        "label": "说实话 / 老实说",
                        "strip": [("说实话", "shuō shíhuà"), ("老实说", "lǎo shí shuō")],
                        "en": "To be honest…",
                        "ex": [
                            ("<span class=\"key\">说实话</span>，我不太喜欢下雨天。", "Shuō shíhuà, wǒ bú tài xǐhuan xià yǔ tiān.", "To be honest, I don't really like rainy days."),
                            ("<span class=\"key\">老实说</span>，这个观点有问题。", "Lǎo shí shuō, zhège guāndiǎn yǒu wèntí.", "Honestly speaking, this viewpoint has problems."),
                        ],
                    },
                    {
                        "label": "直接 vs 委婉",
                        "strip": [("直接", "zhíjiē"), ("vs", ""), ("委婉", "wěiwǎn")],
                        "en": "Direct vs tactful",
                        "ex": [
                            ("<span class=\"key\">直接</span>说：我不喜欢。", "Zhíjiē shuō: Wǒ bù xǐhuan.", "Say directly: I don't like it."),
                            ("<span class=\"key\">委婉</span>地说：这个可能不太适合我。", "Wěiwǎn de shuō: Zhège kěnéng bú tài shìhé wǒ.", "Say tactfully: This may not be very suitable for me."),
                        ],
                    },
                ],
                "dialogue_title": "表达不同意见 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Biǎodá bùtóng yìjiàn</span>",
                "dialogue": [
                    ("a", "A — Direct", "我觉得这个计划不好。", "Wǒ juéde zhège jìhuà bù hǎo.", "I feel this plan is not good."),
                    ("b", "B — Tactful", "在我看来，这个计划可能还需要再讨论。", "Zài wǒ kàn lái, zhège jìhuà kěnéng hái xūyào zài tǎolùn.", "In my opinion, this plan may need further discussion."),
                    ("a", "A — Honest", "说实话，我没有信心。", "Shuō shíhuà, wǒ méiyǒu xìnxīn.", "To be honest, I don't have confidence."),
                    ("b", "B — Encourage", "没关系，我们可以一起想办法。", "Méi guānxi, wǒmen kěyǐ yìqǐ xiǎng bànfǎ.", "It's okay, we can think of a solution together."),
                ],
                "review_chips": [("我认为", "I think"), ("我觉得", "I feel"), ("在我看来", "in my view"), ("说实话", "honestly"), ("直接", "direct"), ("委婉", "tactful")],
                "review_sentences": [("我认为这个办法更好。 / 我觉得天气不错。",), ("说实话，我不太喜欢下雨天。",), ("委婉地说：这个可能不太适合我。",)],
                "quizzes": [
                    ("Opinion · 观点", "group-1", "表达观点", [
                        ("'in my opinion' 用中文怎么说？", "How do you say 'in my opinion'?", ["在我看来", "zai wo kan lai", "zài wǒ kàn lái"], '在我看来 <span class="py">zài wǒ kàn lái · in my opinion</span>'),
                        ("'viewpoint' 用中文怎么说？", "How do you say 'viewpoint'?", ["观点", "guān diǎn", "guan dian"], '观点 <span class="py">guāndiǎn · viewpoint</span>'),
                        ("'opinion' 用中文怎么说？", "How do you say 'opinion'?", ["看法", "kàn fǎ", "kan fa"], '看法 <span class="py">kànfǎ · opinion</span>'),
                    ]),
                    ("Tone · 语气", "group-2", "语气词", [
                        ("'tone' 用中文怎么说？", "How do you say 'tone'?", ["语气", "yǔ qì", "yu qi"], '语气 <span class="py">yǔqì · tone</span>'),
                        ("'direct' 用中文怎么说？", "How do you say 'direct'?", ["直接", "zhí jiē", "zhi jie"], '直接 <span class="py">zhíjiē · direct</span>'),
                        ("'tactful' 用中文怎么说？", "How do you say 'tactful'?", ["委婉", "wěi wǎn", "wei wan"], '委婉 <span class="py">wěiwǎn · tactful</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "认为 / 觉得 / 说实话", [
                        ("我____这个计划不好。", "Wǒ ___ zhège jìhuà bù hǎo.", ["觉得", "jué de", "jue de"], '觉得 <span class="py">juéde · feel</span>'),
                        ("____，我不太喜欢下雨天。", "___, wǒ bú tài xǐhuan xià yǔ tiān.", ["说实话", "shuō shí huà", "shuo shi hua"], '说实话 <span class="py">shuō shíhuà · to be honest</span>'),
                        ("____，这个计划可能还需要再讨论。", "___, zhège jìhuà kěnéng hái xūyào zài tǎolùn.", ["在我看来", "zài wǒ kàn lái", "zai wo kan lai"], '在我看来 <span class="py">zài wǒ kàn lái · in my opinion</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'attitude' 用中文怎么说？", "How do you say 'attitude'?", ["态度", "tài du", "tai du"], '态度 <span class="py">tàidu · attitude</span>'),
                        ("'strong / intense' 用中文怎么说？", "How do you say 'strong'?", ["强烈", "qiáng liè", "qiang lie"], '强烈 <span class="py">qiángliè · strong</span>'),
                        ("'mild / gentle' 用中文怎么说？", "How do you say 'mild'?", ["温和", "wēn hé", "wen he"], '温和 <span class="py">wēnhé · mild</span>'),
                    ]),
                ],
            },
            "hsk-6": {
                "warm_title": "同一个意思，如何说得更有层次？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tóng yí gè yìsi, rúhé shuō de gèng yǒu céngcì?</span>",
                "warm_tip": "Use idioms, literary expressions, and nuanced phrasing to add depth.",
                "warm_chips": [("不言而喻", "self-evident"), ("各有千秋", "each has merits"), ("见仁见智", "opinions differ"), ("言之有理", "makes sense")],
                "vocab": [
                    ("层次", "céng cì", "layer / level", "cat-mood"),
                    ("内涵", "nèi hán", "connotation", "cat-mood"),
                    ("韵味", "yùn wèi", "charm / flavor", "cat-mood"),
                    ("风格", "fēng gé", "style", "cat-mood"),
                    ("修辞", "xiū cí", "rhetoric", "cat-act"),
                    ("比喻", "bǐ yù", "metaphor", "cat-act"),
                    ("夸张", "kuā zhāng", "exaggeration", "cat-act"),
                    ("反语", "fǎn yǔ", "irony", "cat-act"),
                    ("不言而喻", "bù yán ér yù", "self-evident", "cat-gram"),
                    ("各有千秋", "gè yǒu qiān qiū", "each has its merits", "cat-gram"),
                    ("见仁见智", "jiàn rén jiàn zhì", "opinions differ", "cat-gram"),
                    ("言之有理", "yán zhī yǒu lǐ", "makes sense", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "不言而喻",
                        "strip": [("不言而喻", "bù yán ér yù")],
                        "en": "self-evident / it goes without saying",
                        "ex": [
                            ("好的表达能让人印象深刻，这<span class=\"key\">不言而喻</span>。", "Hǎo de biǎodá néng ràng rén yìnxiàng shēnkè, zhè bù yán ér yù.", "Good expression leaves a deep impression — it goes without saying."),
                            ("天气影响心情，<span class=\"key\">不言而喻</span>。", "Tiānqì yǐngxiǎng xīnqíng, bù yán ér yù.", "Weather affects mood — it goes without saying."),
                        ],
                    },
                    {
                        "label": "各有千秋",
                        "strip": [("各有千秋", "gè yǒu qiān qiū")],
                        "en": "Each has its own merits",
                        "ex": [
                            ("直白的表达和含蓄的表达<span class=\"key\">各有千秋</span>。", "Zhíbái de biǎodá hé hánxù de biǎodá gè yǒu qiān qiū.", "Direct and implicit expressions each have their own merits."),
                            ("口语和书面语<span class=\"key\">各有千秋</span>。", "Kǒuyǔ hé shūmiànyǔ gè yǒu qiān qiū.", "Spoken and written language each have their own merits."),
                        ],
                    },
                    {
                        "label": "见仁见智",
                        "strip": [("见仁见智", "jiàn rén jiàn zhì")],
                        "en": "Opinions differ",
                        "ex": [
                            ("哪种说法最好，<span class=\"key\">见仁见智</span>。", "Nǎ zhǒng shuōfǎ zuì hǎo, jiàn rén jiàn zhì.", "Which way of saying it is best — opinions differ."),
                            ("对这个观点，大家<span class=\"key\">见仁见智</span>。", "Duì zhège guāndiǎn, dàjiā jiàn rén jiàn zhì.", "Everyone has different opinions on this viewpoint."),
                        ],
                    },
                ],
                "dialogue_title": "文学化的表达 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Wénxué huà de biǎodá</span>",
                "dialogue": [
                    ("a", "A — Ask", "你觉得口语表达和书面表达最大的区别是什么？", "Nǐ juéde kǒuyǔ biǎodá hé shūmiàn biǎodá zuì dà de qūbié shì shénme?", "What do you think is the biggest difference between spoken and written expression?"),
                    ("b", "B — Answer", "各有千秋。口语更直接，书面语更有韵味和层次。", "Gè yǒu qiān qiū. Kǒuyǔ gèng zhíjiē, shūmiànyǔ gèng yǒu yùnwèi hé céngcì.", "Each has its merits. Spoken is more direct; written has more charm and depth."),
                    ("a", "A — Ask", "那用修辞是不是一定更好？", "Nà yòng xiūcí shì bùshì yídìng gèng hǎo?", "Then is using rhetoric always better?"),
                    ("b", "B — Answer", "见仁见智。恰当才有内涵，过度反而显得夸张。", "Jiàn rén jiàn zhì. Qiàdàng cái yǒu nèihán, guòdù fǎn'ér xiǎnde kuāzhāng.", "Opinions differ. Only when appropriate does it have connotation; overuse appears exaggerated."),
                ],
                "review_chips": [("不言而喻", "self-evident"), ("各有千秋", "each has merits"), ("见仁见智", "opinions differ"), ("言之有理", "makes sense"), ("层次", "layer"), ("内涵", "connotation")],
                "review_sentences": [("好的表达能让人印象深刻，这不言而喻。",), ("口语和书面语各有千秋。",), ("哪种说法最好，见仁见智。",)],
                "quizzes": [
                    ("Idioms · 成语", "group-1", "成语表达", [
                        ("'self-evident' 用中文怎么说？", "How do you say 'self-evident'?", ["不言而喻", "bu yan er yu", "bù yán ér yù"], '不言而喻 <span class="py">bù yán ér yù · self-evident</span>'),
                        ("'each has its merits' 用中文怎么说？", "How do you say 'each has merits'?", ["各有千秋", "ge you qian qiu", "gè yǒu qiān qiū"], '各有千秋 <span class="py">gè yǒu qiān qiū · each has merits</span>'),
                        ("'opinions differ' 用中文怎么说？", "How do you say 'opinions differ'?", ["见仁见智", "jian ren jian zhi", "jiàn rén jiàn zhì"], '见仁见智 <span class="py">jiàn rén jiàn zhì · opinions differ</span>'),
                    ]),
                    ("Rhetoric · 修辞", "group-2", "修辞手法", [
                        ("'metaphor' 用中文怎么说？", "How do you say 'metaphor'?", ["比喻", "bǐ yù", "bi yu"], '比喻 <span class="py">bǐyù · metaphor</span>'),
                        ("'exaggeration' 用中文怎么说？", "How do you say 'exaggeration'?", ["夸张", "kuā zhāng", "kua zhang"], '夸张 <span class="py">kuāzhāng · exaggeration</span>'),
                        ("'irony' 用中文怎么说？", "How do you say 'irony'?", ["反语", "fǎn yǔ", "fan yu"], '反语 <span class="py">fǎnyǔ · irony</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "成语填空", [
                        ("天气影响心情，____。", "Tiānqì yǐngxiǎng xīnqíng, ___.", ["不言而喻", "bù yán ér yù", "bu yan er yu"], '不言而喻 <span class="py">bù yán ér yù · self-evident</span>'),
                        ("直白的表达和含蓄的表达____。", "Zhíbái de biǎodá hé hánxù de biǎodá ___.", ["各有千秋", "gè yǒu qiān qiū", "ge you qian qiu"], '各有千秋 <span class="py">gè yǒu qiān qiū · each has merits</span>'),
                        ("哪种说法最好，____。", "Nǎ zhǒng shuōfǎ zuì hǎo, ___.", ["见仁见智", "jiàn rén jiàn zhì", "jian ren jian zhi"], '见仁见智 <span class="py">jiàn rén jiàn zhì · opinions differ</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'connotation' 用中文怎么说？", "How do you say 'connotation'?", ["内涵", "nèi hán", "nei han"], '内涵 <span class="py">nèihán · connotation</span>'),
                        ("'charm / flavor' 用中文怎么说？", "How do you say 'charm'?", ["韵味", "yùn wèi", "yun wei"], '韵味 <span class="py">yùnwèi · charm</span>'),
                        ("'style' 用中文怎么说？", "How do you say 'style'?", ["风格", "fēng gé", "feng ge"], '风格 <span class="py">fēnggé · style</span>'),
                    ]),
                ],
            },
        },
    },

    "mood-weather-v2": {
        "id": "mood-weather-v2",
        "title_zh": "心情和天气",
        "title_py": "xīn qíng hé tiān qì",
        "title_en": "Mood & Weather (new version)",
        "eyebrow": "Daily life · 日常生活",
        "close_zh": "再见",
        "close_py": "Zàijiàn",
        "close_en": "See you next time — stay happy, rain or shine",
        "cover_icon": WEATHER_V2_ICON,
        "theme": {
            "title_zh": "心情和天气",
            "title_en": "Mood & Weather",
            "accent": {"main": "#1d5f8a", "mid": "#4a9ec7", "dark": "#153d5c", "pale": "#e8f4fd"},
            "grammar_classes": ["rust", "gold", "jade"],
        },
        "levels": {
            "hsk-1": {
                "warm_title": "今天天气好吗？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Jīntiān tiānqì hǎo ma?</span>",
                "warm_tip": "Look outside and describe the weather and your feeling.",
                "warm_chips": [("晴天", "sunny"), ("下雨", "rain"), ("冷", "cold"), ("热", "hot"), ("开心", "happy"), ("累", "tired")],
                "vocab": [
                    ("今天", "jīn tiān", "today", "cat-weather"),
                    ("天气", "tiān qì", "weather", "cat-weather"),
                    ("晴天", "qíng tiān", "sunny day", "cat-weather"),
                    ("下雨", "xià yǔ", "rain", "cat-weather"),
                    ("冷", "lěng", "cold", "cat-weather"),
                    ("热", "rè", "hot", "cat-weather"),
                    ("开心", "kāi xīn", "happy", "cat-mood"),
                    ("累", "lèi", "tired", "cat-mood"),
                    ("好", "hǎo", "good", "cat-mood"),
                    ("不好", "bù hǎo", "not good", "cat-mood"),
                    ("吗", "ma", "question particle", "cat-gram"),
                    ("很", "hěn", "very", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "今天天气很好",
                        "strip": [("今天", "jīntiān"), ("天气", "tiānqì"), ("很", "hěn"), ("好", "hǎo")],
                        "en": "Today's weather is very good.",
                        "ex": [
                            ("<span class=\"key\">今天天气很好</span>。", "Jīntiān tiānqì hěn hǎo.", "Today's weather is very good."),
                            ("<span class=\"key\">今天很热</span>。", "Jīntiān hěn rè.", "Today is very hot."),
                            ("<span class=\"key\">今天很冷</span>。", "Jīntiān hěn lěng.", "Today is very cold."),
                        ],
                    },
                    {
                        "label": "你开心吗？",
                        "strip": [("你", "nǐ"), ("开心", "kāixīn"), ("吗", "ma")],
                        "en": "Are you happy?",
                        "ex": [
                            ("你<span class=\"key\">开心吗</span>？", "Nǐ kāixīn ma?", "Are you happy?"),
                            ("今天天气好<span class=\"key\">吗</span>？", "Jīntiān tiānqì hǎo ma?", "Is the weather good today?"),
                            ("你累<span class=\"key\">吗</span>？", "Nǐ lèi ma?", "Are you tired?"),
                        ],
                    },
                    {
                        "label": "我很开心 / 我不开心",
                        "strip": [("我", "wǒ"), ("很", "hěn"), ("开心", "kāixīn")],
                        "en": "I am very happy. / I am not happy.",
                        "ex": [
                            ("我<span class=\"key\">很开心</span>。", "Wǒ hěn kāixīn.", "I am very happy."),
                            ("我<span class=\"key\">不开心</span>。", "Wǒ bù kāixīn.", "I am not happy."),
                            ("我<span class=\"key\">很累</span>。", "Wǒ hěn lèi.", "I am very tired."),
                        ],
                    },
                ],
                "dialogue_title": "今天怎么样？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Jīntiān zěnme yàng?</span>",
                "dialogue": [
                    ("a", "A — Ask", "今天天气好吗？", "Jīntiān tiānqì hǎo ma?", "Is the weather good today?"),
                    ("b", "B — Answer", "很好，是晴天。", "Hěn hǎo, shì qíngtiān.", "Very good, it's sunny."),
                    ("a", "A — Ask", "你开心吗？", "Nǐ kāixīn ma?", "Are you happy?"),
                    ("b", "B — Answer", "我很开心！", "Wǒ hěn kāixīn!", "I am very happy!"),
                ],
                "review_chips": [("今天天气很好", "weather good"), ("晴天", "sunny"), ("下雨", "rain"), ("冷", "cold"), ("热", "hot"), ("开心", "happy")],
                "review_sentences": [("今天天气很好。",), ("你开心吗？",), ("我很开心。 / 我不开心。",)],
                "quizzes": [
                    ("Weather · 天气", "group-1", "天气词", [
                        ("'sunny day' 用中文怎么说？", "How do you say 'sunny day'?", ["晴天", "qíng tiān", "qing tian"], '晴天 <span class="py">qíng tiān · sunny day</span>'),
                        ("'rain' 用中文怎么说？", "How do you say 'rain'?", ["下雨", "xià yǔ", "xia yu", "雨"], '下雨 <span class="py">xià yǔ · rain</span>'),
                        ("'cold' 用中文怎么说？", "How do you say 'cold'?", ["冷", "lěng", "leng"], '冷 <span class="py">lěng · cold</span>'),
                    ]),
                    ("Mood · 心情", "group-2", "心情词", [
                        ("'happy' 用中文怎么说？", "How do you say 'happy'?", ["开心", "kāi xīn", "kai xin"], '开心 <span class="py">kāi xīn · happy</span>'),
                        ("'tired' 用中文怎么说？", "How do you say 'tired'?", ["累", "lèi", "lei"], '累 <span class="py">lèi · tired</span>'),
                        ("'not good' 用中文怎么说？", "How do you say 'not good'?", ["不好", "bù hǎo", "bu hao"], '不好 <span class="py">bù hǎo · not good</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "很 / 吗 / 不", [
                        ("今天天气____好。", "Jīntiān tiānqì ___ hǎo.", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
                        ("你开心____？", "Nǐ kāixīn ___?", ["吗", "ma"], '吗 <span class="py">ma · question particle</span>'),
                        ("我____开心。", "Wǒ ___ kāixīn.", ["不", "bù", "bu"], '不 <span class="py">bù · not</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'today' 用中文怎么说？", "How do you say 'today'?", ["今天", "jīn tiān", "jin tian"], '今天 <span class="py">jīntiān · today</span>'),
                        ("'hot' 用中文怎么说？", "How do you say 'hot'?", ["热", "rè", "re"], '热 <span class="py">rè · hot</span>'),
                        ("今天____晴天。", "Jīntiān ___ qíngtiān.", ["是", "shì", "shi"], '是 <span class="py">shì · is</span>'),
                    ]),
                ],
            },
            "hsk-2": {
                "warm_title": "你喜欢什么季节？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ xǐhuan shénme jìjié?</span>",
                "warm_tip": "Talk about seasons and how they make you feel.",
                "warm_chips": [("春天", "spring"), ("夏天", "summer"), ("秋天", "autumn"), ("冬天", "winter"), ("舒服", "comfortable"), ("喜欢", "like")],
                "vocab": [
                    ("春天", "chūn tiān", "spring", "cat-weather"),
                    ("夏天", "xià tiān", "summer", "cat-weather"),
                    ("秋天", "qiū tiān", "autumn", "cat-weather"),
                    ("冬天", "dōng tiān", "winter", "cat-weather"),
                    ("季节", "jì jié", "season", "cat-weather"),
                    ("舒服", "shū fu", "comfortable", "cat-mood"),
                    ("难过", "nán guò", "sad", "cat-mood"),
                    ("不错", "bú cuò", "not bad", "cat-mood"),
                    ("喜欢", "xǐ huan", "like", "cat-act"),
                    ("游泳", "yóu yǒng", "swim", "cat-act"),
                    ("堆雪人", "duī xuě rén", "make a snowman", "cat-act"),
                    ("最", "zuì", "most", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "我最喜欢…",
                        "strip": [("我", "wǒ"), ("最", "zuì"), ("喜欢", "xǐhuan"), ("season", "")],
                        "en": "I like … the most.",
                        "ex": [
                            ("我<span class=\"key\">最喜欢</span>秋天。", "Wǒ zuì xǐhuan qiūtiān.", "I like autumn the most."),
                            ("我<span class=\"key\">最不喜欢</span>夏天。", "Wǒ zuì bù xǐhuan xiàtiān.", "I like summer the least."),
                        ],
                    },
                    {
                        "label": "…的时候，我…",
                        "strip": [("season", ""), ("的时候", "de shíhòu"), ("I…", "")],
                        "en": "When it's…, I…",
                        "ex": [
                            ("<span class=\"key\">夏天的时候</span>，我喜欢游泳。", "Xiàtiān de shíhòu, wǒ xǐhuan yóuyǒng.", "In summer, I like swimming."),
                            ("<span class=\"key\">冬天的时候</span>，我堆雪人。", "Dōngtiān de shíhòu, wǒ duī xuěrén.", "In winter, I make a snowman."),
                        ],
                    },
                    {
                        "label": "因为…所以…",
                        "strip": [("因为", "yīnwèi"), ("reason", ""), ("所以", "suǒyǐ"), ("result", "")],
                        "en": "Because…, so…",
                        "ex": [
                            ("<span class=\"key\">因为</span>秋天很舒服，<span class=\"key\">所以</span>我最喜欢它。", "Yīnwèi qiūtiān hěn shūfu, suǒyǐ wǒ zuì xǐhuan tā.", "Because autumn is very comfortable, I like it the most."),
                            ("<span class=\"key\">因为</span>夏天很热，<span class=\"key\">所以</span>我不开心。", "Yīnwèi xiàtiān hěn rè, suǒyǐ wǒ bù kāixīn.", "Because summer is very hot, I am not happy."),
                        ],
                    },
                ],
                "dialogue_title": "你最喜欢哪个季节？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Nǐ zuì xǐhuan nǎge jìjié?</span>",
                "dialogue": [
                    ("a", "A — Ask", "你最喜欢哪个季节？", "Nǐ zuì xǐhuan nǎge jìjié?", "Which season do you like the most?"),
                    ("b", "B — Answer", "我最喜欢秋天，因为天气很舒服。", "Wǒ zuì xǐhuan qiūtiān, yīnwèi tiānqì hěn shūfu.", "I like autumn the most because the weather is very comfortable."),
                    ("a", "A — Ask", "夏天的时候你喜欢做什么？", "Xiàtiān de shíhòu nǐ xǐhuan zuò shénme?", "What do you like to do in summer?"),
                    ("b", "B — Answer", "夏天的时候，我喜欢游泳。", "Xiàtiān de shíhòu, wǒ xǐhuan yóuyǒng.", "In summer, I like swimming."),
                ],
                "review_chips": [("春天", "spring"), ("夏天", "summer"), ("秋天", "autumn"), ("冬天", "winter"), ("最喜欢", "like most"), ("的时候", "when")],
                "review_sentences": [("我最喜欢秋天。",), ("夏天的时候，我喜欢游泳。",), ("因为秋天很舒服，所以我最喜欢它。",)],
                "quizzes": [
                    ("Seasons · 季节", "group-1", "季节词", [
                        ("'spring' 用中文怎么说？", "How do you say 'spring'?", ["春天", "chūn tiān", "chun tian"], '春天 <span class="py">chūntiān · spring</span>'),
                        ("'autumn' 用中文怎么说？", "How do you say 'autumn'?", ["秋天", "qiū tiān", "qiu tian"], '秋天 <span class="py">qiūtiān · autumn</span>'),
                        ("'winter' 用中文怎么说？", "How do you say 'winter'?", ["冬天", "dōng tiān", "dong tian"], '冬天 <span class="py">dōngtiān · winter</span>'),
                    ]),
                    ("Activities · 活动", "group-2", "活动", [
                        ("'swim' 用中文怎么说？", "How do you say 'swim'?", ["游泳", "yóu yǒng", "you yong"], '游泳 <span class="py">yóuyǒng · swim</span>'),
                        ("'make a snowman' 用中文怎么说？", "How do you say 'make a snowman'?", ["堆雪人", "duī xuě rén", "dui xue ren"], '堆雪人 <span class="py">duī xuěrén · make a snowman</span>'),
                        ("'comfortable' 用中文怎么说？", "How do you say 'comfortable'?", ["舒服", "shū fu", "shu fu"], '舒服 <span class="py">shūfu · comfortable</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "最 / 的时候 / 因为…所以…", [
                        ("我____喜欢秋天。", "Wǒ ___ xǐhuan qiūtiān.", ["最", "zuì", "zui"], '最 <span class="py">zuì · most</span>'),
                        ("____的时候，我喜欢游泳。", "___ de shíhòu, wǒ xǐhuan yóuyǒng.", ["夏天", "xià tiān", "xia tian"], '夏天 <span class="py">xiàtiān · summer</span>'),
                        ("____秋天很舒服，____我最喜欢它。", "___ qiūtiān hěn shūfu, ___ wǒ zuì xǐhuan tā.", ["因为...所以", "因为...所以...", "yīnwèi...suǒyǐ"], '因为…所以… <span class="py">yīnwèi…suǒyǐ…</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'season' 用中文怎么说？", "How do you say 'season'?", ["季节", "jì jié", "ji jie"], '季节 <span class="py">jìjié · season</span>'),
                        ("'summer' 用中文怎么说？", "How do you say 'summer'?", ["夏天", "xià tiān", "xia tian"], '夏天 <span class="py">xiàtiān · summer</span>'),
                        ("____的时候，我堆雪人。", "___ de shíhòu, wǒ duī xuěrén.", ["冬天", "dōng tiān", "dong tian"], '冬天 <span class="py">dōngtiān · winter</span>'),
                    ]),
                ],
            },

            "hsk-4": {
                "warm_title": "天气变化时，你的计划会怎么变？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiānqì biànhuà shí, nǐ de jìhuà huì zěnme biàn?</span>",
                "warm_tip": "Talk about how weather changes affect your plans and mood.",
                "warm_chips": [("预报", "forecast"), ("突然", "suddenly"), ("取消", "cancel"), ("改变", "change"), ("带伞", "bring umbrella"), ("穿外套", "wear coat")],
                "vocab": [
                    ("预报", "yù bào", "forecast", "cat-weather"),
                    ("突然", "tū rán", "suddenly", "cat-weather"),
                    ("变化", "biàn huà", "change", "cat-weather"),
                    ("取消", "qǔ xiāo", "cancel", "cat-act"),
                    ("改变", "gǎi biàn", "change", "cat-act"),
                    ("计划", "jì huà", "plan", "cat-act"),
                    ("带伞", "dài sǎn", "bring umbrella", "cat-act"),
                    ("穿外套", "chuān wài tào", "wear coat", "cat-act"),
                    ("心情", "xīn qíng", "mood", "cat-mood"),
                    ("郁闷", "yù mèn", "gloomy", "cat-mood"),
                    ("不但", "bù dàn", "not only", "cat-gram"),
                    ("而且", "ér qiě", "but also", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "天气预报说…",
                        "strip": [("天气预报", "tiānqì yùbào"), ("说", "shuō"), ("content", "")],
                        "en": "The weather forecast says…",
                        "ex": [
                            ("<span class=\"key\">天气预报说</span>今天会下雨。", "Tiānqì yùbào shuō jīntiān huì xià yǔ.", "The weather forecast says it will rain today."),
                            ("<span class=\"key\">天气预报说</span>明天晴天。", "Tiānqì yùbào shuō míngtiān qíngtiān.", "The weather forecast says tomorrow will be sunny."),
                        ],
                    },
                    {
                        "label": "突然…",
                        "strip": [("突然", "tūrán"), ("verb", "rain / change")],
                        "en": "Suddenly…",
                        "ex": [
                            ("天气<span class=\"key\">突然</span>变了。", "Tiānqì tūrán biàn le.", "The weather suddenly changed."),
                            ("<span class=\"key\">突然</span>下雨了。", "Tūrán xià yǔ le.", "It suddenly rained."),
                        ],
                    },
                    {
                        "label": "不但…而且…",
                        "strip": [("不但", "bùdàn"), ("A", ""), ("而且", "érqiě"), ("B", "")],
                        "en": "Not only… but also…",
                        "ex": [
                            ("下雨<span class=\"key\">不但</span>让我难过，<span class=\"key\">而且</span>让我取消计划。", "Xià yǔ bùdàn ràng wǒ nánguò, érqiě ràng wǒ qǔxiāo jìhuà.", "Rain not only makes me sad but also makes me cancel plans."),
                            ("晴天<span class=\"key\">不但</span>舒服，<span class=\"key\">而且</span>让我心情好。", "Qíngtiān bùdàn shūfu, érqiě ràng wǒ xīnqíng hǎo.", "Sunny days are not only comfortable but also put me in a good mood."),
                        ],
                    },
                ],
                "dialogue_title": "天气变化影响计划 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiānqì biànhuà yǐngxiǎng jìhuà</span>",
                "dialogue": [
                    ("a", "A — Ask", "你看天气预报了吗？", "Nǐ kàn tiānqì yùbào le ma?", "Did you check the weather forecast?"),
                    ("b", "B — Answer", "看了。天气预报说明天会下雨，所以我打算带伞。", "Kàn le. Tiānqì yùbào shuō míngtiān huì xià yǔ, suǒyǐ wǒ dǎsuàn dài sǎn.", "Yes. The forecast says it will rain tomorrow, so I plan to bring an umbrella."),
                    ("a", "A — Ask", "如果天气突然变冷怎么办？", "Rúguǒ tiānqì tūrán biàn lěng zěnme bàn?", "What if the weather suddenly gets cold?"),
                    ("b", "B — Answer", "我会穿外套。天气变冷不但影响心情，而且影响计划。", "Wǒ huì chuān wàitào. Tiānqì biàn lěng bùdàn yǐngxiǎng xīnqíng, érqiě yǐngxiǎng jìhuà.", "I'll wear a coat. Cold weather not only affects mood but also affects plans."),
                ],
                "review_chips": [("天气预报", "forecast"), ("突然", "suddenly"), ("取消", "cancel"), ("改变", "change"), ("带伞", "bring umbrella"), ("不但…而且…", "not only…but also")],
                "review_sentences": [("天气预报说明天会下雨。",), ("天气突然变了。",), ("下雨不但让我难过，而且让我取消计划。",)],
                "quizzes": [
                    ("Weather · 天气", "group-1", "天气词", [
                        ("'forecast' 用中文怎么说？", "How do you say 'forecast'?", ["预报", "yù bào", "yu bao"], '预报 <span class="py">yùbào · forecast</span>'),
                        ("'suddenly' 用中文怎么说？", "How do you say 'suddenly'?", ["突然", "tū rán", "tu ran"], '突然 <span class="py">tūrán · suddenly</span>'),
                        ("'cancel' 用中文怎么说？", "How do you say 'cancel'?", ["取消", "qǔ xiāo", "qu xiao"], '取消 <span class="py">qǔxiāo · cancel</span>'),
                    ]),
                    ("Plans · 计划", "group-2", "计划相关", [
                        ("'plan' 用中文怎么说？", "How do you say 'plan'?", ["计划", "jì huà", "ji hua"], '计划 <span class="py">jìhuà · plan</span>'),
                        ("'change' 用中文怎么说？", "How do you say 'change'?", ["改变", "gǎi biàn", "gai bian"], '改变 <span class="py">gǎibiàn · change</span>'),
                        ("'wear coat' 用中文怎么说？", "How do you say 'wear coat'?", ["穿外套", "chuān wài tào", "chuan wai tao"], '穿外套 <span class="py">chuān wàitào · wear coat</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "预报 / 突然 / 不但…而且…", [
                        ("天气____说明天会下雨。", "Tiānqì ___ shuō míngtiān huì xià yǔ.", ["预报", "yù bào", "yu bao"], '预报 <span class="py">yùbào · forecast</span>'),
                        ("____下雨了。", "___ xià yǔ le.", ["突然", "tū rán", "tu ran"], '突然 <span class="py">tūrán · suddenly</span>'),
                        ("晴天____舒服，____让我心情好。", "Qíngtiān ___ shūfu, ___ ràng wǒ xīnqíng hǎo.", ["不但...而且", "不但...而且...", "bùdàn...érqiě"], '不但…而且… <span class="py">bùdàn…érqiě…</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'bring umbrella' 用中文怎么说？", "How do you say 'bring umbrella'?", ["带伞", "dài sǎn", "dai san"], '带伞 <span class="py">dài sǎn · bring umbrella</span>'),
                        ("'gloomy' 用中文怎么说？", "How do you say 'gloomy'?", ["郁闷", "yù mèn", "yu men"], '郁闷 <span class="py">yùmèn · gloomy</span>'),
                        ("天气变冷____影响心情，____影响计划。", "Tiānqì biàn lěng ___ yǐngxiǎng xīnqíng, ___ yǐngxiǎng jìhuà.", ["不但...而且", "不但...而且...", "bùdàn...érqiě"], '不但…而且… <span class="py">bùdàn…érqiě…</span>'),
                    ]),
                ],
            },
            "hsk-5": {
                "warm_title": "现代人如何根据天气调整生活？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Xiàndài rén rúhé gēnjù tiānqì tiáozhěng shēnghuó?</span>",
                "warm_tip": "Discuss how people adapt their lifestyle to weather.",
                "warm_chips": [("适应", "adapt"), ("调整", "adjust"), ("节奏", "pace"), ("效率", "efficiency"), ("户外活动", "outdoor activity"), ("室内", "indoor")],
                "vocab": [
                    ("适应", "shì yìng", "adapt", "cat-act"),
                    ("调整", "tiáo zhěng", "adjust", "cat-act"),
                    ("节奏", "jié zòu", "pace / rhythm", "cat-act"),
                    ("效率", "xiào lǜ", "efficiency", "cat-act"),
                    ("户外", "hù wài", "outdoor", "cat-weather"),
                    ("室内", "shì nèi", "indoor", "cat-weather"),
                    ("活动", "huó dòng", "activity", "cat-act"),
                    ("安排", "ān pái", "arrange", "cat-act"),
                    ("心态", "xīn tài", "mindset", "cat-mood"),
                    ("平衡", "píng héng", "balance", "cat-mood"),
                    ("随着", "suí zhe", "along with", "cat-gram"),
                    ("取决于", "qǔ jué yú", "depend on", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "随着…调整…",
                        "strip": [("随着", "suízhe"), ("change", ""), ("调整", "tiáozhěng"), ("life", "")],
                        "en": "Adjust… as… changes",
                        "ex": [
                            ("<span class=\"key\">随着</span>季节变化，人们会<span class=\"key\">调整</span>生活节奏。", "Suízhe jìjié biànhuà, rénmen huì tiáozhěng shēnghuó jiézòu.", "As seasons change, people adjust their pace of life."),
                            ("<span class=\"key\">随着</span>天气变冷，户外活动减少了。", "Suízhe tiānqì biàn lěng, hùwài huódòng jiǎnshǎo le.", "As the weather gets cold, outdoor activities decrease."),
                        ],
                    },
                    {
                        "label": "取决于",
                        "strip": [("result", ""), ("取决于", "qǔjuéyú"), ("factor", "")],
                        "en": "depends on",
                        "ex": [
                            ("我的心情<span class=\"key\">取决于</span>天气。", "Wǒ de xīnqíng qǔjuéyú tiānqì.", "My mood depends on the weather."),
                            ("生活安排<span class=\"key\">取决于</span>季节和工作。", "Shēnghuó ānpái qǔjuéyú jìjié hé gōngzuò.", "Life arrangements depend on season and work."),
                        ],
                    },
                    {
                        "label": "在…和…之间保持平衡",
                        "strip": [("在", "zài"), ("A", ""), ("和", "hé"), ("B", ""), ("之间", "zhījiān"), ("保持平衡", "bǎochí pínghéng")],
                        "en": "keep a balance between A and B",
                        "ex": [
                            ("我们要<span class=\"key\">在室内和户外活动之间保持平衡</span>。", "Wǒmen yào zài shìnèi hé hùwài huódòng zhījiān bǎochí pínghéng.", "We should keep a balance between indoor and outdoor activities."),
                            ("<span class=\"key\">在工作和休息之间保持平衡</span>很重要。", "Zài gōngzuò hé xiūxi zhījiān bǎochí pínghéng hěn zhòngyào.", "Keeping a balance between work and rest is important."),
                        ],
                    },
                ],
                "dialogue_title": "调整生活节奏 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Tiáozhěng shēnghuó jiézòu</span>",
                "dialogue": [
                    ("a", "A — Ask", "你冬天和夏天的生活节奏一样吗？", "Nǐ dōngtiān hé xiàtiān de shēnghuó jiézòu yíyàng ma?", "Is your pace of life the same in winter and summer?"),
                    ("b", "B — Answer", "不一样。随着天气变冷，我的效率会变低，所以我会调整安排。", "Bù yíyàng. Suízhe tiānqì biàn lěng, wǒ de xiàolǜ huì biàn dī, suǒyǐ wǒ huì tiáozhěng ānpái.", "Not the same. As the weather gets cold, my efficiency drops, so I adjust my schedule."),
                    ("a", "A — Ask", "你心态好不好，取决于什么？", "Nǐ xīntài hǎo bu hǎo, qǔjuéyú shénme?", "What does your mindset depend on?"),
                    ("b", "B — Answer", "取决于我能不能在室内和户外活动之间保持平衡。", "Qǔjuéyú wǒ néng bu néng zài shìnèi hé hùwài huódòng zhījiān bǎochí pínghéng.", "It depends on whether I can keep a balance between indoor and outdoor activities."),
                ],
                "review_chips": [("适应", "adapt"), ("调整", "adjust"), ("节奏", "pace"), ("效率", "efficiency"), ("取决于", "depend on"), ("保持平衡", "keep balance")],
                "review_sentences": [("随着季节变化，人们会调整生活节奏。",), ("我的心情取决于天气。",), ("我们要在室内和户外活动之间保持平衡。",)],
                "quizzes": [
                    ("Lifestyle · 生活", "group-1", "生活词", [
                        ("'pace / rhythm' 用中文怎么说？", "How do you say 'pace'?", ["节奏", "jié zòu", "jie zou"], '节奏 <span class="py">jiézòu · pace</span>'),
                        ("'adjust' 用中文怎么说？", "How do you say 'adjust'?", ["调整", "tiáo zhěng", "tiao zheng"], '调整 <span class="py">tiáozhěng · adjust</span>'),
                        ("'indoor' 用中文怎么说？", "How do you say 'indoor'?", ["室内", "shì nèi", "shi nei"], '室内 <span class="py">shìnèi · indoor</span>'),
                    ]),
                    ("Mood · 心态", "group-2", "心态词", [
                        ("'mindset' 用中文怎么说？", "How do you say 'mindset'?", ["心态", "xīn tài", "xin tai"], '心态 <span class="py">xīntài · mindset</span>'),
                        ("'balance' 用中文怎么说？", "How do you say 'balance'?", ["平衡", "píng héng", "ping heng"], '平衡 <span class="py">pínghéng · balance</span>'),
                        ("'outdoor' 用中文怎么说？", "How do you say 'outdoor'?", ["户外", "hù wài", "hu wai"], '户外 <span class="py">hùwài · outdoor</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "随着 / 取决于 / 保持平衡", [
                        ("____天气变冷，户外活动减少了。", "___ tiānqì biàn lěng, hùwài huódòng jiǎnshǎo le.", ["随着", "suí zhe", "sui zhe"], '随着 <span class="py">suízhe · along with</span>'),
                        ("我的心情____天气。", "Wǒ de xīnqíng ___ tiānqì.", ["取决于", "qǔ jué yú", "qu jue yu"], '取决于 <span class="py">qǔjuéyú · depend on</span>'),
                        ("我们要在室内和户外活动之间____。", "Wǒmen yào zài shìnèi hé hùwài huódòng zhījiān ___.", ["保持平衡", "bǎo chí píng héng", "bao chi ping heng"], '保持平衡 <span class="py">bǎochí pínghéng · keep balance</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'arrange' 用中文怎么说？", "How do you say 'arrange'?", ["安排", "ān pái", "an pai"], '安排 <span class="py">ānpái · arrange</span>'),
                        ("'activity' 用中文怎么说？", "How do you say 'activity'?", ["活动", "huó dòng", "huo dong"], '活动 <span class="py">huódòng · activity</span>'),
                        ("'adapt' 用中文怎么说？", "How do you say 'adapt'?", ["适应", "shì yìng", "shi ying"], '适应 <span class="py">shìyìng · adapt</span>'),
                    ]),
                ],
            },
            "hsk-6": {
                "warm_title": "气候差异如何塑造不同的生活方式？ <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Qìhòu chāyì rúhé sùzào bùtóng de shēnghuó fāngshì?</span>",
                "warm_tip": "Discuss how climate shapes culture and lifestyle.",
                "warm_chips": [("气候差异", "climate difference"), ("塑造", "shape"), ("因地制宜", "adapt locally"), ("潜移默化", "subtly"), ("生活方式", "lifestyle"), ("文化习惯", "cultural habit")],
                "vocab": [
                    ("气候差异", "qì hòu chā yì", "climate difference", "cat-weather"),
                    ("塑造", "sù zào", "shape / mold", "cat-act"),
                    ("因地制宜", "yīn dì zhì yí", "adapt to local conditions", "cat-act"),
                    ("潜移默化", "qián yí mò huà", "subtly influence", "cat-act"),
                    ("生活方式", "shēng huó fāng shì", "lifestyle", "cat-act"),
                    ("文化习惯", "wén huà xí guàn", "cultural habit", "cat-act"),
                    ("气候带", "qì hòu dài", "climate zone", "cat-weather"),
                    ("温带", "wēn dài", "temperate zone", "cat-weather"),
                    ("热带", "rè dài", "tropical zone", "cat-weather"),
                    ("心态", "xīn tài", "mindset", "cat-mood"),
                    ("换言之", "huàn yán zhī", "in other words", "cat-gram"),
                    ("究其原因为", "qiū jí qí yuán wéi", "the root cause is", "cat-gram"),
                ],
                "grammar": [
                    {
                        "label": "潜移默化地塑造",
                        "strip": [("潜移默化", "qiányímòhuà"), ("地", "de"), ("塑造", "sùzào")],
                        "en": "subtly shape",
                        "ex": [
                            ("气候<span class=\"key\">潜移默化地塑造</span>了当地人的生活方式。", "Qìhòu qiányímòhuà de sùzào le dāngdì rén de shēnghuó fāngshì.", "Climate subtly shapes the lifestyle of local people."),
                            ("文化习惯<span class=\"key\">潜移默化地影响</span>了人们的心态。", "Wénhuà xíguàn qiányímòhuà de yǐngxiǎng le rénmen de xīntài.", "Cultural habits subtly influence people's mindset."),
                        ],
                    },
                    {
                        "label": "究其原因为…",
                        "strip": [("之所以", "zhīsuǒyǐ"), ("result", ""), ("究其原因为", "qiū jí qí yuán wéi"), ("root cause", "")],
                        "en": "The reason… is rooted in…",
                        "ex": [
                            ("南方人之所以饮食清淡，<span class=\"key\">究其原因为</span>气候炎热。", "Nánfāng rén zhīsuǒyǐ yǐnshí qīngdàn, qiū jí qí yuán wéi qìhòu yánrè.", "The reason southerners have a light diet is rooted in the hot climate."),
                            ("北方人之所以性格直爽，<span class=\"key\">究其原因为</span>地理与气候的影响。", "Běifāng rén zhīsuǒyǐ xìnggé zhíshuǎng, qiū jí qí yuán wéi dìlǐ yǔ qìhòu de yǐngxiǎng.", "The reason northerners are straightforward is rooted in geography and climate influences."),
                        ],
                    },
                    {
                        "label": "换言之",
                        "strip": [("换言之", "huànyánzhī"), ("restatement", "")],
                        "en": "in other words",
                        "ex": [
                            ("人们因地制宜地生活；<span class=\"key\">换言之</span>，环境塑造了文化。", "Rénmen yīndìzhìyí de shēnghuó; huànyánzhī, huánjìng sùzào le wénhuà.", "People live according to local conditions; in other words, environment shapes culture."),
                            ("气候影响心态；<span class=\"key\">换言之</span>，天气也是文化的一部分。", "Qìhòu yǐngxiǎng xīntài; huànyánzhī, tiānqì yě shì wénhuà de yí bùfèn.", "Climate affects mindset; in other words, weather is also part of culture."),
                        ],
                    },
                ],
                "dialogue_title": "气候与文化 <span style=\"font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;\">Qìhòu yǔ wénhuà</span>",
                "dialogue": [
                    ("a", "A — Analyst", "为什么不同气候带的人生活方式差异这么大？", "Wèishénme bùtóng qìhòudài de rén shēnghuó fāngshì chāyì zhème dà?", "Why do people in different climate zones have such different lifestyles?"),
                    ("b", "B — Expert", "究其原因为气候潜移默化地塑造了文化习惯。热带地区的人生活节奏较慢，温带地区的人则更注重效率。", "Qiū jí qí yuán wéi qìhòu qiányímòhuà de sùzào le wénhuà xíguàn. Rèdài dìqū de rén shēnghuó jiézòu jiào màn, wēndài dìqū de rén zé gèng zhùzhòng xiàolǜ.", "The root cause is that climate subtly shapes cultural habits. People in tropical regions have a slower pace of life, while those in temperate zones focus more on efficiency."),
                    ("a", "A — Analyst", "那我们可以说环境决定了一切吗？", "Nà wǒmen kěyǐ shuō huánjìng juédìng le yíqiè ma?", "Can we then say environment determines everything?"),
                    ("b", "B — Expert", "不能这么说。环境只是重要因素之一；换言之，个人选择和心态也同样重要。", "Bùnéng zhème shuō. Huánjìng zhǐshì zhòngyào yīnsù zhī yī; huànyánzhī, gèrén xuǎnzé hé xīntài yě tóngyàng zhòngyào.", "We can't say that. Environment is only one important factor; in other words, personal choice and mindset are equally important."),
                ],
                "review_chips": [("潜移默化", "subtly"), ("究其原因为", "root cause"), ("换言之", "in other words"), ("因地制宜", "adapt locally"), ("塑造", "shape"), ("生活方式", "lifestyle")],
                "review_sentences": [("气候潜移默化地塑造了当地人的生活方式。",), ("南方人之所以饮食清淡，究其原因为气候炎热。",), ("人们因地制宜地生活；换言之，环境塑造了文化。",)],
                "quizzes": [
                    ("Climate · 气候", "group-1", "气候词", [
                        ("'climate difference' 用中文怎么说？", "How do you say 'climate difference'?", ["气候差异", "qì hòu chā yì", "qi hou cha yi"], '气候差异 <span class="py">qìhòu chāyì · climate difference</span>'),
                        ("'tropical zone' 用中文怎么说？", "How do you say 'tropical zone'?", ["热带", "rè dài", "re dai"], '热带 <span class="py">rèdài · tropical zone</span>'),
                        ("'temperate zone' 用中文怎么说？", "How do you say 'temperate zone'?", ["温带", "wēn dài", "wen dai"], '温带 <span class="py">wēndài · temperate zone</span>'),
                    ]),
                    ("Culture · 文化", "group-2", "文化词", [
                        ("'shape / mold' 用中文怎么说？", "How do you say 'shape'?", ["塑造", "sù zào", "su zao"], '塑造 <span class="py">sùzào · shape</span>'),
                        ("'cultural habit' 用中文怎么说？", "How do you say 'cultural habit'?", ["文化习惯", "wén huà xí guàn", "wen hua xi guan"], '文化习惯 <span class="py">wénhuà xíguàn · cultural habit</span>'),
                        ("'lifestyle' 用中文怎么说？", "How do you say 'lifestyle'?", ["生活方式", "shēng huó fāng shì", "sheng huo fang shi"], '生活方式 <span class="py">shēnghuó fāngshì · lifestyle</span>'),
                    ]),
                    ("Grammar · 语法", "group-3", "潜移默化 / 究其原因为 / 换言之", [
                        ("气候____地塑造了当地人的生活方式。", "Qìhòu ___ de sùzào le dāngdì rén de shēnghuó fāngshì.", ["潜移默化", "qián yí mò huà", "qian yi mo hua"], '潜移默化 <span class="py">qiányímòhuà · subtly</span>'),
                        ("南方人之所以饮食清淡，____气候炎热。", "Nánfāng rén zhīsuǒyǐ yǐnshí qīngdàn, ___ qìhòu yánrè.", ["究其原因为", "qiū jí qí yuán wéi", "qiu ji qi yuan wei"], '究其原因为 <span class="py">qiūjíqíyuánwéi · root cause is</span>'),
                        ("环境只是重要因素之一；____，个人选择和心态也同样重要。", "Huánjìng zhǐshì zhòngyào yīnsù zhī yī; ___, gèrén xuǎnzé hé xīntài yě tóngyàng zhòngyào.", ["换言之", "huàn yán zhī", "huan yan zhi"], '换言之 <span class="py">huànyánzhī · in other words</span>'),
                    ]),
                    ("Final Challenge · 综合挑战", "final", "小挑战", [
                        ("'adapt to local conditions' 用中文怎么说？", "How do you say 'adapt to local conditions'?", ["因地制宜", "yīn dì zhì yí", "yin di zhi yi"], '因地制宜 <span class="py">yīndìzhìyí · adapt locally</span>'),
                        ("'subtly influence' 用中文怎么说？", "How do you say 'subtly influence'?", ["潜移默化", "qián yí mò huà", "qian yi mo hua"], '潜移默化 <span class="py">qiányímòhuà · subtly influence</span>'),
                        ("'in other words' 用中文怎么说？", "How do you say 'in other words'?", ["换言之", "huàn yán zhī", "huan yan zhi"], '换言之 <span class="py">huànyánzhī · in other words</span>'),
                    ]),
                ],
            },
        },
    },
}


def main():
    for story_id, story in STORIES.items():
        theme = story["theme"]
        for level in ["hsk-1", "hsk-2", "hsk-4", "hsk-5", "hsk-6"]:
            if level not in story["levels"]:
                continue
            level_data = story["levels"][level]
            html = build_lesson(story, level, level_data, theme)
            out_dir = os.path.join(ROOT, level, story_id)
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, "index.html")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Wrote {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
