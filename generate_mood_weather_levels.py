#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re

ROOT = "/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson"
STORY = "mood-weather"
SRC = os.path.join(ROOT, "hsk-3", STORY, "index.html")

with open(SRC, "r", encoding="utf-8") as f:
    src_html = f.read()
css_match = re.search(r"<style>(.*?)</style>", src_html, re.S)
CSS = css_match.group(1) if css_match else ""


def attr_esc(s):
    return s.replace('"', '&quot;')


def dots(active=0, total=7):
    out = []
    for i in range(total):
        if i < active:
            out.append('<div class="dot done"></div>')
        elif i == active:
            out.append('<div class="dot active"></div>')
        else:
            out.append('<div class="dot"></div>')
    return "\n".join(out)


def sidebar(icon_svg, label, active=0, bg_class=""):
    cls = ("sidebar " + bg_class).strip()
    return f'''<div class="{cls}">
    <div class="sb-icon">
      {icon_svg}
      <div class="sb-label">{label}</div>
    </div>
    <div class="sb-prog">
      {dots(active)}
    </div>
  </div>'''


ICON_COVER = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <circle cx="16" cy="16" r="5" fill="rgba(255,255,255,0.9)"/>
      <path d="M16 5v3M16 24v3M5 16h3M24 16h3M8.3 8.3l2.1 2.1M21.6 21.6l2.1 2.1M8.3 23.7l2.1-2.1M21.6 10.4l2.1-2.1" stroke="rgba(255,255,255,0.85)" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M10 26c0-3.3 2.7-6 6-6s6 2.7 6 6" fill="rgba(255,255,255,0.4)" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    </svg>'''

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

ICON_GRAMMAR = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 16c0-4.4 3.6-8 8-8s8 3.6 8 8" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <path d="M9 16h10M11 20h6M13 24h2" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>'''

ICON_DIALOGUE = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 20h16M6 20v-8c0-3.3 2.7-6 6-6h4c3.3 0 6 2.7 6 6v8" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <circle cx="11" cy="14" r="1.5" fill="rgba(255,255,255,0.85)"/><circle cx="17" cy="14" r="1.5" fill="rgba(255,255,255,0.85)"/>
      </svg>'''

ICON_REVIEW = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 14 L12 20 L22 8" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>'''

ICON_TEST = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="14" cy="14" r="6" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <path d="M14 6v2M14 20v2M6 14h2M20 14h2" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>'''

ICON_REPORT = '''<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 21 L5 13 M12 21 L12 8 M19 21 L19 16 M23 21 L23 11" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" stroke-linecap="round"/>
      </svg>'''

SCENE_WEATHER = '''<svg viewBox="0 0 740 190" xmlns="http://www.w3.org/2000/svg">
        <defs><linearGradient id="wuSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#dff0fb"/><stop offset="100%" stop-color="#f5f9fc"/></linearGradient></defs>
        <rect width="740" height="190" fill="url(#wuSky)" rx="8"/>
        <circle cx="95" cy="65" r="28" fill="#f6e05e"/>
        <path d="M95 24v10M95 96v10M54 65h-10M136 65h-10M68 38l-8-8M122 38l8-8M68 92l-8 8M122 92l8 8" stroke="#f6d05e" stroke-width="4" stroke-linecap="round"/>
        <circle cx="95" cy="130" r="18" fill="#74c69d"/>
        <ellipse cx="280" cy="68" rx="42" ry="22" fill="#8aaec0"/>
        <path d="M262 90l-8 18M280 90l-6 20M298 90l-3 16" stroke="#4a9ec7" stroke-width="3" stroke-linecap="round"/>
        <circle cx="280" cy="132" r="18" fill="#e76f51"/>
        <ellipse cx="460" cy="65" rx="40" ry="21" fill="#b8d0e0"/>
        <circle cx="448" cy="86" r="3" fill="#a0c0d8"/><circle cx="465" cy="93" r="3" fill="#a0c0d8"/><circle cx="478" cy="80" r="3" fill="#a0c0d8"/>
        <circle cx="460" cy="132" r="18" fill="#9b2226"/>
        <ellipse cx="640" cy="68" rx="44" ry="22" fill="#d8c8a8"/>
        <circle cx="640" cy="60" r="18" fill="#f6d77a" opacity="0.7"/>
        <circle cx="640" cy="132" r="18" fill="#74c69d"/>
      </svg>'''

SCENE_GRAMMAR = '''<svg viewBox="0 0 720 160" xmlns="http://www.w3.org/2000/svg">
        <rect width="720" height="160" fill="#f0ebe1" rx="8"/>
        <circle cx="120" cy="60" r="28" fill="#f6e05e"/>
        <path d="M120 20v10M120 100v10M80 60h-10M160 60h-10" stroke="#d69e2e" stroke-width="4" stroke-linecap="round"/>
        <ellipse cx="360" cy="60" rx="44" ry="22" fill="#8aaec0"/>
        <path d="M340 84l-8 18M360 84l-6 20M380 84l-3 16" stroke="#4a9ec7" stroke-width="3" stroke-linecap="round"/>
        <circle cx="600" cy="60" r="24" fill="#74c69d"/>
        <path d="M180 120h120M420 120h120" stroke="#d8c8a8" stroke-width="3" stroke-linecap="round"/>
        <polygon points="170,120 180,115 180,125" fill="#d69e2e"/>
        <polygon points="410,120 420,115 420,125" fill="#d69e2e"/>
      </svg>'''

SCENE_VOCAB = '''<svg viewBox="0 0 720 56" xmlns="http://www.w3.org/2000/svg">
        <rect width="720" height="56" fill="#f0ebe1" rx="8"/>
        <rect x="0" y="0" width="240" height="56" fill="#e8f4fd" rx="8 0 0 8"/>
        <rect x="240" y="0" width="240" height="56" fill="#fff0ee"/>
        <rect x="480" y="0" width="240" height="56" fill="#fffff0" rx="0 8 8 0"/>
        <circle cx="55" cy="22" r="9" fill="#f6e05e"/>
        <text x="95" y="28" font-family="Noto Serif SC,serif" font-size="9" fill="#1d5f8a" font-weight="700">Weather 天气</text>
        <text x="95" y="44" font-family="Inter,sans-serif" font-size="7.5" fill="#1d5f8a">sunny · rainy · cloudy · snowy</text>
        <circle cx="295" cy="22" r="8" fill="#e76f51"/>
        <text x="325" y="28" font-family="Noto Serif SC,serif" font-size="9" fill="#9b2226" font-weight="700">Mood 心情</text>
        <text x="325" y="44" font-family="Inter,sans-serif" font-size="7.5" fill="#e76f51">happy · sad · relaxed · down</text>
        <path d="M520 18h10v8h-10zM535 14h12v12h-12zM552 20h8v6h-8z" fill="#d69e2e" opacity="0.85"/>
        <text x="575" y="28" font-family="Noto Serif SC,serif" font-size="9" fill="#7b5a1a" font-weight="700">Activities 活动</text>
        <text x="575" y="44" font-family="Inter,sans-serif" font-size="7.5" fill="#b7791f">walk · swim · shop · read</text>
      </svg>'''


def chip(ch, py, en=None):
    extra = f" · {en}" if en else ""
    return f'<div class="chip"><span class="ch">{ch}</span><span class="py">{py}{extra}</span></div>'


def vc(zh, py, en, cat):
    return f'<div class="vc {cat}"><div class="vc-zh">{zh}</div><div class="vc-py">{py}</div><div class="vc-en">{en}</div></div>'


def ex(zh, py, en, cls=""):
    return f'''<div class="ex {cls}">
        <div class="ex-zh">{zh}</div>
        <div class="ex-py">{py}</div>
        <div class="ex-en">{en}</div>
      </div>'''


def practice_item(num, html):
    return f'''<div class="practice-item">
        <div class="practice-num">{num}</div>
        <div class="practice-text">{html}</div>
      </div>'''


def photo_slot(img, cap, sub=""):
    sub_html = f"<small>{sub}</small>" if sub else ""
    return f'''<div class="photo-slot">
        <img src="{img}" alt="" onerror="this.style.display='none'"/>
        <div class="photo-cap">{cap}{sub_html}</div>
      </div>'''


def photo_wide(img, cap):
    return f'''<div class="photo-wide">
      <img src="{img}" alt="" onerror="this.style.display='none'"/>
      <div class="photo-cap">{cap}</div>
    </div>'''


def quiz_item(prompt_zh, prompt_py, placeholder, answers, reveal):
    ans = "|".join(answers)
    rev = attr_esc(reveal)
    return f'''<div class="phone-block wide">
        <div class="quiz-q">{prompt_zh}<span class="py">{prompt_py}</span></div>
        <div class="quiz-game">
          <div class="quiz-row">
            <input type="text" class="quiz-input" placeholder="{placeholder}..." data-answer="{ans}" data-reveal="{rev}"/>
            <button type="button" class="quiz-check-btn">检查</button>
          </div>
          <div class="quiz-feedback"></div>
        </div>
      </div>'''


def quiz_group_slide(level, num, total, label, group_id, title, sub, tip, items):
    items_html = "\n".join(items)
    return f'''<div class="slide" style="grid-template-columns:64px 1fr">
  {sidebar(ICON_TEST, f"test {num}/{total}", active=6, bg_class="rust")}
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">{label}</div>
    <h2>{title} <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">{sub}</span></h2>
    <div class="quiz-score" data-quiz-score data-group="{group_id}" data-total="{len(items)}">✅ <span class="score-correct">0</span>/<span class="score-total">{len(items)}</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>{tip}</strong></div>
    <div class="phone-row">
      {items_html}
    </div>
  </div>
</div>'''


LEVELS = {}

# -----------------------------------------------------------------------------
# HSK 1
# -----------------------------------------------------------------------------
warm1_title = "你好！今天怎么样？"
warm1_py = "Nǐ hǎo! Jīntiān zěnme yàng?"
warm1_chips_w = [chip("太阳", "tài yáng", "sun"), chip("雨", "yǔ", "rain"), chip("雪", "xuě", "snow"), chip("云", "yún", "cloud")]
warm1_chips_m = [chip("开心", "kāi xīn", "happy"), chip("好", "hǎo", "good"), chip("不好", "bù hǎo", "not good")]
warm1_practice = "".join([
    practice_item("1", '<span class="zh">你好吗？</span> <span class="py">Nǐ hǎo ma?</span>'),
    practice_item("2", '<span class="zh">今天天气好吗？</span> <span class="py">Jīntiān tiānqì hǎo ma?</span>'),
    practice_item("3", '<span class="zh">你开心吗？</span> <span class="py">Nǐ kāixīn ma?</span>')
])

vocab1_words = [
    vc("天气", "tiān qì", "weather", "cat-weather"),
    vc("太阳", "tài yáng", "sun", "cat-weather"),
    vc("云", "yún", "cloud", "cat-weather"),
    vc("雨", "yǔ", "rain", "cat-weather"),
    vc("雪", "xuě", "snow", "cat-weather"),
    vc("冷", "lěng", "cold", "cat-weather"),
    vc("热", "rè", "hot", "cat-weather"),
    vc("开心", "kāi xīn", "happy", "cat-mood"),
    vc("好", "hǎo", "good", "cat-mood"),
    vc("不好", "bù hǎo", "not good", "cat-mood"),
    vc("很", "hěn", "very", "cat-gram"),
    vc("吗", "ma", "question particle", "cat-gram"),
]
vocab1_ex = ex("今天天气<span class=\"key-s\">很</span>好。", "Jīntiān tiānqì hěn hǎo.", "Today the weather is very good.") + \
            ex("我不<span class=\"key-r\">开心</span>。", "Wǒ bù kāixīn.", "I am not happy.", "rust")
vocab1_practice = "".join([
    practice_item("1", 'Use <span class="zh">很</span>: <em>e.g. 天气很好。</em>'),
    practice_item("2", 'Use <span class="zh">吗</span>: <em>e.g. 你好吗？</em>'),
    practice_item("3", 'Use <span class="zh">不</span>: <em>e.g. 不好。</em>')
])

gram1_g1 = '''<div class="grammar-strip">
      <div class="gs-part colored rust"><div class="gs-zh">A</div><div class="gs-py">noun</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part colored rust"><div class="gs-zh">很</div><div class="gs-py">hěn</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part"><div class="gs-plain-zh">adj</div><div class="gs-plain-py">good / hot</div></div>
      <div class="gs-en">A is very + adjective</div>
    </div>'''
gram1_g1_ex = ex("天气<span class=\"key\">很</span>好。", "Tiānqì hěn hǎo.", "The weather is very good.", "rust") + \
              ex("太阳<span class=\"key\">很</span>大。", "Tàiyáng hěn dà.", "The sun is very big.", "rust") + \
              ex("我<span class=\"key\">很</span>开心。", "Wǒ hěn kāixīn.", "I am very happy.", "rust")
gram1_g1_practice = "".join([
    practice_item("1", '<span class="zh">天气很好。</span> <span class="py">Tiānqì hěn hǎo.</span>'),
    practice_item("2", '<span class="zh">我很开心。</span> <span class="py">Wǒ hěn kāixīn.</span>'),
    practice_item("3", '<span class="zh">太阳很大。</span> <span class="py">Tàiyáng hěn dà.</span>')
])

gram1_g2 = '''<div class="grammar-strip">
      <div class="gs-part colored sky"><div class="gs-zh">statement</div><div class="gs-py">e.g. 你好</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part colored sky"><div class="gs-zh">吗</div><div class="gs-py">ma</div></div>
      <div class="gs-sep">?</div>
      <div class="gs-en">Yes / no question</div>
    </div>'''
gram1_g2_ex = ex("你开心<span class=\"key-s\">吗</span>？", "Nǐ kāixīn ma?", "Are you happy?", "sky") + \
              ex("今天天气好<span class=\"key-s\">吗</span>？", "Jīntiān tiānqì hǎo ma?", "Is the weather good today?", "sky") + \
              ex("你好吗？", "Nǐ hǎo ma?", "How are you?", "sky")
gram1_g2_practice = "".join([
    practice_item("1", '<span class="zh">你好吗？</span>'),
    practice_item("2", '<span class="zh">今天冷吗？</span>'),
    practice_item("3", '<span class="zh">你开心吗？</span>')
])

gram1_g3 = '''<div class="grammar-strip">
      <div class="gs-part colored gold"><div class="gs-zh">不</div><div class="gs-py">bù</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part"><div class="gs-plain-zh">adj / verb</div><div class="gs-plain-py">good / like</div></div>
      <div class="gs-en">not + adj / verb</div>
    </div>'''
gram1_g3_ex = ex("今天天气<span class=\"key-g\">不</span>好。", "Jīntiān tiānqì bù hǎo.", "Today's weather is not good.", "") + \
              ex("我<span class=\"key-g\">不</span>开心。", "Wǒ bù kāixīn.", "I am not happy.", "") + \
              ex("今天<span class=\"key-g\">不</span>冷。", "Jīntiān bù lěng.", "Today it is not cold.", "")
gram1_g3_practice = "".join([
    practice_item("1", '<span class="zh">今天不好。</span>'),
    practice_item("2", '<span class="zh">我不热。</span>'),
    practice_item("3", '<span class="zh">天气不好，我不开心。</span>')
])

dial1 = '''<div class="dial-grid">
      <div class="dial-a"><div class="dial-label">A — 问 Ask</div><div class="dial-zh">你好！你好吗？</div><div class="dial-py">Nǐ hǎo! Nǐ hǎo ma?</div><div class="dial-en">Hello! How are you?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答 Answer</div><div class="dial-zh">我很好。谢谢你。</div><div class="dial-py">Wǒ hěn hǎo. Xièxie nǐ.</div><div class="dial-en">I'm very good. Thank you.</div></div>
      <div class="dial-a"><div class="dial-label">A — 问</div><div class="dial-zh">今天天气好吗？</div><div class="dial-py">Jīntiān tiānqì hǎo ma?</div><div class="dial-en">Is the weather good today?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答</div><div class="dial-zh">很好。太阳很大。</div><div class="dial-py">Hěn hǎo. Tàiyáng hěn dà.</div><div class="dial-en">Very good. The sun is big.</div></div>
      <div class="dial-a"><div class="dial-label">A — 问</div><div class="dial-zh">你开心吗？</div><div class="dial-py">Nǐ kāixīn ma?</div><div class="dial-en">Are you happy?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答</div><div class="dial-zh">我很开心！</div><div class="dial-py">Wǒ hěn kāixīn!</div><div class="dial-en">I'm very happy!</div></div>
    </div>'''

review1 = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.7rem;margin-bottom:1rem;">
      <div style="background:var(--cream);border-radius:9px;padding:0.85rem 1rem;">
        <div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--jade);margin-bottom:0.5rem;">Weather words 天气词</div>
        <div class="chip-row" style="margin:0;gap:0.35rem;">
          <div class="chip"><span class="ch">太阳</span><span class="py">sun</span></div>
          <div class="chip"><span class="ch">雨</span><span class="py">rain</span></div>
          <div class="chip"><span class="ch">雪</span><span class="py">snow</span></div>
          <div class="chip"><span class="ch">云</span><span class="py">cloud</span></div>
          <div class="chip"><span class="ch">冷</span><span class="py">cold</span></div>
          <div class="chip"><span class="ch">热</span><span class="py">hot</span></div>
        </div>
      </div>
      <div style="background:var(--cream);border-radius:9px;padding:0.85rem 1rem;">
        <div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--jade);margin-bottom:0.5rem;">Mood words 心情词</div>
        <div class="chip-row" style="margin:0;gap:0.35rem;">
          <div class="chip"><span class="ch">开心</span><span class="py">happy</span></div>
          <div class="chip"><span class="ch">好</span><span class="py">good</span></div>
          <div class="chip"><span class="ch">不好</span><span class="py">not good</span></div>
        </div>
      </div>
    </div>
    <div class="practice">
      <div class="practice-title">Key sentences · 重点句</div>
      <div class="practice-item"><div class="practice-num">1</div><div class="practice-text"><span class="zh">今天天气很好。</span></div></div>
      <div class="practice-item"><div class="practice-num">2</div><div class="practice-text"><span class="zh">你开心吗？</span></div></div>
      <div class="practice-item"><div class="practice-num">3</div><div class="practice-text"><span class="zh">我很开心！/ 我不开心。</span></div></div>
    </div>'''

quiz1_1 = quiz_group_slide(1, "1", "4", "Weather · 天气", "group-1", "天气词", "Tiānqì cí", "Type the Chinese word.", [
    quiz_item("'sun' 用中文怎么说？", "How do you say 'sun'?", "太阳", ["太阳", "tài yáng", "tai yang"], '太阳 <span class="py">tài yáng · sun</span>'),
    quiz_item("'rain' 用中文怎么说？", "How do you say 'rain'?", "雨", ["雨", "yǔ", "yu", "下雨", "xià yǔ"], '雨 / 下雨 <span class="py">yǔ / xià yǔ · rain</span>'),
    quiz_item("'cold' 用中文怎么说？", "How do you say 'cold'?", "冷", ["冷", "lěng", "leng"], '冷 <span class="py">lěng · cold</span>'),
])
quiz1_2 = quiz_group_slide(1, "2", "4", "Mood · 心情", "group-2", "心情词", "Xīnqíng cí", "Type the Chinese word.", [
    quiz_item("'happy' 用中文怎么说？", "How do you say 'happy'?", "开心", ["开心", "kāi xīn", "kai xin"], '开心 <span class="py">kāi xīn · happy</span>'),
    quiz_item("'good' 用中文怎么说？", "How do you say 'good'?", "好", ["好", "hǎo", "hao"], '好 <span class="py">hǎo · good</span>'),
    quiz_item("'not good' 用中文怎么说？", "How do you say 'not good'?", "不好", ["不好", "bù hǎo", "bu hao"], '不好 <span class="py">bù hǎo · not good</span>'),
])
quiz1_3 = quiz_group_slide(1, "3", "4", "Grammar · 语法", "group-3", "很 / 吗 / 不", "hěn / ma / bù", "Fill in the blank.", [
    quiz_item("天气____好。", "Tiānqì ___ hǎo.", "很", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
    quiz_item("你开心____？", "Nǐ kāixīn ___?", "吗", ["吗", "ma"], '吗 <span class="py">ma · question particle</span>'),
    quiz_item("今天天气不____。", "Jīntiān tiānqì bù ___.", "好", ["好", "hǎo", "hao"], '好 <span class="py">hǎo · good</span>'),
])
quiz1_4 = quiz_group_slide(1, "4", "4", "Final Challenge · 综合挑战", "final", "小挑战", "Challenge", "Answer in Chinese, pinyin, or English.", [
    quiz_item("'weather' 用中文怎么说？", "How do you say 'weather'?", "天气", ["天气", "tiān qì", "tian qi"], '天气 <span class="py">tiān qì · weather</span>'),
    quiz_item("'snow' 用中文怎么说？", "How do you say 'snow'?", "雪", ["雪", "xuě", "xue", "下雪"], '雪 / 下雪 <span class="py">xuě / xià xuě · snow</span>'),
    quiz_item("我____开心。", "Wǒ ___ kāixīn.", "很", ["很", "hěn", "hen"], '很 <span class="py">hěn · very</span>'),
])

LEVELS[1] = {
    "tags": ["HSK 1", "12 new words", "3 grammar points"],
    "eyebrow": "Daily life · 日常生活 · Level 1",
    "warmup": {"title": warm1_title, "py": warm1_py, "chips_w": warm1_chips_w, "chips_m": warm1_chips_m, "practice": warm1_practice},
    "vocab": {"count": "12 words", "words": vocab1_words, "ex": vocab1_ex, "practice": vocab1_practice},
    "grammar": [
        {"label": "G1 · 很", "bg": "rust", "strip": gram1_g1, "ex": gram1_g1_ex, "practice": gram1_g1_practice},
        {"label": "G2 · 吗", "bg": "sky", "strip": gram1_g2, "ex": gram1_g2_ex, "practice": gram1_g2_practice},
        {"label": "G3 · 不", "bg": "gold", "strip": gram1_g3, "ex": gram1_g3_ex, "practice": gram1_g3_practice},
    ],
    "dialogue": dial1,
    "review": review1,
    "quizzes": [quiz1_1, quiz1_2, quiz1_3, quiz1_4],
}

# -----------------------------------------------------------------------------
# HSK 2
# -----------------------------------------------------------------------------
warm2_title = "今天天气怎么样？"
warm2_py = "Jīntiān tiānqì zěnme yàng?"
warm2_chips_w = [chip("晴天", "qíng tiān", "sunny"), chip("阴天", "yīn tiān", "cloudy"), chip("下雨", "xià yǔ", "rainy"), chip("下雪", "xià xuě", "snowy"), chip("暖和", "nuǎn huo", "warm")]
warm2_chips_m = [chip("开心", "kāi xīn", "happy"), chip("难过", "nán guò", "sad"), chip("不错", "bú cuò", "not bad"), chip("好", "hǎo", "good")]
warm2_practice = "".join([
    practice_item("1", '<span class="zh">今天天气怎么样？</span> <span class="py">Jīntiān tiānqì zěnme yàng?</span>'),
    practice_item("2", '<span class="zh">你开心吗？</span> <span class="py">Nǐ kāixīn ma?</span>'),
    practice_item("3", '<span class="zh">你喜欢什么天气？</span> <span class="py">Nǐ xǐhuan shénme tiānqì?</span>')
])

vocab2_words = [
    vc("天气", "tiān qì", "weather", "cat-weather"),
    vc("晴天", "qíng tiān", "sunny day", "cat-weather"),
    vc("阴天", "yīn tiān", "cloudy day", "cat-weather"),
    vc("下雨", "xià yǔ", "rain / rainy", "cat-weather"),
    vc("下雪", "xià xuě", "snow / snowy", "cat-weather"),
    vc("暖和", "nuǎn huo", "warm", "cat-weather"),
    vc("冷", "lěng", "cold", "cat-weather"),
    vc("热", "rè", "hot", "cat-weather"),
    vc("心情", "xīn qíng", "mood", "cat-mood"),
    vc("开心", "kāi xīn", "happy", "cat-mood"),
    vc("难过", "nán guò", "sad", "cat-mood"),
    vc("不错", "bú cuò", "not bad", "cat-mood"),
    vc("喜欢", "xǐ huan", "like", "cat-act"),
    vc("散步", "sàn bù", "take a walk", "cat-act"),
    vc("在家", "zài jiā", "at home", "cat-act"),
    vc("看书", "kàn shū", "read a book", "cat-act"),
    vc("听音乐", "tīng yīn yuè", "listen to music", "cat-act"),
    vc("让", "ràng", "make / let", "cat-gram"),
]
vocab2_ex = ex("今天天气<span class=\"key-s\">很暖和</span>。", "Jīntiān tiānqì hěn nuǎnhuo.", "Today's weather is very warm.") + \
            ex("下雨<span class=\"key\">让</span>我难过。", "Xià yǔ ràng wǒ nánguò.", "Rain makes me sad.")
vocab2_practice = "".join([
    practice_item("1", 'Use <span class="zh">天气</span> + <span class="zh">让</span> + <span class="zh">心情</span>: <em>e.g. 晴天让我开心。</em>'),
    practice_item("2", 'Use <span class="zh">的时候</span>: <em>e.g. 天气好的时候，我喜欢散步。</em>'),
    practice_item("3", 'Use <span class="zh">也</span>: <em>e.g. 我也喜欢晴天。</em>')
])

gram2_g1 = '''<div class="grammar-strip">
      <div class="gs-part colored rust"><div class="gs-zh">weather / thing</div><div class="gs-py">e.g. 晴天</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part colored rust"><div class="gs-zh">让</div><div class="gs-py">ràng</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part"><div class="gs-plain-zh">person + 心情 + adj</div><div class="gs-plain-py">me happy</div></div>
      <div class="gs-en">A makes B's mood good / bad</div>
    </div>'''
gram2_g1_ex = ex("<span class=\"key-r\">晴天</span><span class=\"key\">让</span>我<span class=\"key-r\">开心</span>。", "Qíngtiān ràng wǒ kāixīn.", "Sunny weather makes me happy.", "rust") + \
              ex("<span class=\"key-r\">下雨</span><span class=\"key\">让</span>我<span class=\"key-r\">难过</span>。", "Xià yǔ ràng wǒ nánguò.", "Rain makes me sad.", "rust") + \
              ex("<span class=\"key-r\">阴天</span><span class=\"key\">让</span>我的心情<span class=\"key-r\">不好</span>。", "Yīntiān ràng wǒ de xīnqíng bù hǎo.", "Cloudy weather makes me feel bad.", "rust")
gram2_g1_practice = "".join([
    practice_item("1", '<span class="zh">什么让你开心？</span> <span class="py">Shénme ràng nǐ kāixīn?</span>'),
    practice_item("2", '<span class="zh">什么让你难过？</span> <span class="py">Shénme ràng nǐ nánguò?</span>'),
    practice_item("3", '<span class="zh">天气好的时候，你的心情怎么样？</span>')
])

gram2_g2 = '''<div class="grammar-strip">
      <div class="gs-part colored sky"><div class="gs-zh">situation / time</div><div class="gs-py">e.g. 天气好</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part colored sky"><div class="gs-zh">的时候</div><div class="gs-py">de shí hòu</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part"><div class="gs-plain-zh">I like / do…</div><div class="gs-plain-py">action</div></div>
      <div class="gs-en">When…, I like / do…</div>
    </div>'''
gram2_g2_ex = ex("<span class=\"key-s\">天气好的时候</span>，我喜欢去公园散步。", "Tiānqì hǎo de shíhòu, wǒ xǐhuan qù gōngyuán sànbù.", "When the weather is good, I like walking in the park.", "sky") + \
              ex("<span class=\"key-s\">下雨的时候</span>，我在家看书。", "Xià yǔ de shíhòu, wǒ zài jiā kànshū.", "When it rains, I read at home.", "sky") + \
              ex("<span class=\"key-s\">心情不好的时候</span>，我听音乐。", "Xīnqíng bù hǎo de shíhòu, wǒ tīng yīnyuè.", "When I'm in a bad mood, I listen to music.", "sky")
gram2_g2_practice = "".join([
    practice_item("1", '<span class="zh">天气好的时候，你喜欢做什么？</span>'),
    practice_item("2", '<span class="zh">下雨的时候，你做什么？</span>'),
    practice_item("3", '<span class="zh">你难过的时候，喜欢做什么？</span>')
])

gram2_g3 = '''<div class="grammar-strip">
      <div class="gs-part colored gold"><div class="gs-zh">A</div><div class="gs-py">person / thing</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part colored gold"><div class="gs-zh">也</div><div class="gs-py">yě</div></div>
      <div class="gs-sep">+</div>
      <div class="gs-part"><div class="gs-plain-zh">verb / adj</div><div class="gs-plain-py">like / happy</div></div>
      <div class="gs-en">A also…</div>
    </div>'''
gram2_g3_ex = ex("我<span class=\"key-g\">也</span>喜欢晴天。", "Wǒ yě xǐhuan qíngtiān.", "I also like sunny weather.", "") + \
              ex("他<span class=\"key-g\">也</span>不开心。", "Tā yě bù kāixīn.", "He is also unhappy.", "") + \
              ex("天气好的时候，我<span class=\"key-g\">也</span>喜欢去海边。", "Tiānqì hǎo de shíhòu, wǒ yě xǐhuan qù hǎibiān.", "When the weather is good, I also like going to the beach.", "")
gram2_g3_practice = "".join([
    practice_item("1", '<span class="zh">我也喜欢下雨。</span>'),
    practice_item("2", '<span class="zh">他也不难过。</span>'),
    practice_item("3", '<span class="zh">天气冷的时候，我也喜欢在家。</span>')
])

dial2 = '''<div class="dial-grid">
      <div class="dial-a"><div class="dial-label">A — 问 Ask</div><div class="dial-zh">你住的地方天气怎么样？</div><div class="dial-py">Nǐ zhù de dìfāng tiānqì zěnme yàng?</div><div class="dial-en">How is the weather where you live?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答 Answer</div><div class="dial-zh">今天晴天，不太冷，也不太热。</div><div class="dial-py">Jīntiān qíngtiān, bú tài lěng, yě bú tài rè.</div><div class="dial-en">It's sunny today, not too cold or too hot.</div></div>
      <div class="dial-a"><div class="dial-label">A — 问</div><div class="dial-zh">天气好的时候，你喜欢做什么？</div><div class="dial-py">Tiānqì hǎo de shíhòu, nǐ xǐhuan zuò shénme?</div><div class="dial-en">What do you like to do when the weather is good?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答</div><div class="dial-zh">我喜欢去公园散步。你呢？</div><div class="dial-py">Wǒ xǐhuan qù gōngyuán sànbù. Nǐ ne?</div><div class="dial-en">I like walking in the park. What about you?</div></div>
      <div class="dial-a"><div class="dial-label">A — 问</div><div class="dial-zh">下雨的时候你做什么？</div><div class="dial-py">Xià yǔ de shíhòu nǐ zuò shénme?</div><div class="dial-en">What do you do when it rains?</div></div>
      <div class="dial-b"><div class="dial-label">B — 答</div><div class="dial-zh">下雨的时候，我在家看书、听音乐。</div><div class="dial-py">Xià yǔ de shíhòu, wǒ zài jiā kànshū, tīng yīnyuè.</div><div class="dial-en">When it rains, I read and listen to music at home.</div></div>
    </div>'''

review2 = '''<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.7rem;margin-bottom:1rem;">
      <div style="background:var(--cream);border-radius:9px;padding:0.85rem 1rem;">
        <div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--jade);margin-bottom:0.5rem;">Useful phrases 常用语</div>
        <div class="chip-row" style="margin:0;gap:0.35rem;">
          <div class="chip"><span class="ch">天气怎么样？</span></div>
          <div class="chip"><span class="ch">不太冷也不太热</span></div>
          <div class="chip"><span class="ch">天气好的时候</span></div>
          <div class="chip"><span class="ch">下雨的时候</span></div>
        </div>
      </div>
      <div style="background:var(--cream);border-radius:9px;padding:0.85rem 1rem;">
        <div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--jade);margin-bottom:0.5rem;">Grammar 语法</div>
        <div class="chip-row" style="margin:0;gap:0.35rem;">
          <div class="chip"><span class="ch">A 让 B + 心情</span></div>
          <div class="chip"><span class="ch">...的时候</span></div>
          <div class="chip"><span class="ch">也</span></div>
        </div>
      </div>
    </div>
    <div class="practice">
      <div class="practice-title">Key sentences · 重点句</div>
      <div class="practice-item"><div class="practice-num">1</div><div class="practice-text"><span class="zh">晴天让我开心。</span></div></div>
      <div class="practice-item"><div class="practice-num">2</div><div class="practice-text"><span class="zh">天气好的时候，我喜欢去公园散步。</span></div></div>
      <div class="practice-item"><div class="practice-num">3</div><div class="practice-text"><span class="zh">我也喜欢在家看书。</span></div></div>
    </div>'''

quiz2_1 = quiz_group_slide(2, "1", "4", "Weather · 天气", "group-1", "天气词", "Tiānqì cí", "Type the Chinese word.", [
    quiz_item("'sunny day' 用中文怎么说？", "How do you say 'sunny day'?", "晴天", ["晴天", "qíng tiān", "qing tian"], '晴天 <span class="py">qíng tiān · sunny day</span>'),
    quiz_item("'cloudy day' 用中文怎么说？", "How do you say 'cloudy day'?", "阴天", ["阴天", "yīn tiān", "yin tian"], '阴天 <span class="py">yīn tiān · cloudy day</span>'),
    quiz_item("'warm' 用中文怎么说？", "How do you say 'warm'?", "暖和", ["暖和", "nuǎn huo", "nuan huo"], '暖和 <span class="py">nuǎn huo · warm</span>'),
])
quiz2_2 = quiz_group_slide(2, "2", "4", "Mood · 心情", "group-2", "心情词", "Xīnqíng cí", "Type the Chinese word.", [
    quiz_item("'mood' 用中文怎么说？", "How do you say 'mood'?", "心情", ["心情", "xīn qíng", "xin qing"], '心情 <span class="py">xīn qíng · mood</span>'),
    quiz_item("'sad' 用中文怎么说？", "How do you say 'sad'?", "难过", ["难过", "nán guò", "nan guo"], '难过 <span class="py">nán guò · sad</span>'),
    quiz_item("'not bad' 用中文怎么说？", "How do you say 'not bad'?", "不错", ["不错", "bú cuò", "bu cuo"], '不错 <span class="py">bú cuò · not bad</span>'),
])
quiz2_3 = quiz_group_slide(2, "3", "4", "Grammar · 语法", "group-3", "让 / 的时候 / 也", "ràng / de shíhòu / yě", "Fill in the blank.", [
    quiz_item("晴天____我开心。", "Qíngtiān ___ wǒ kāixīn.", "让", ["让", "ràng", "rang"], '让 <span class="py">ràng · make</span>'),
    quiz_item("天气好的时候，我喜欢____。", "Tiānqì hǎo de shíhòu, wǒ xǐhuan ___.", "散步", ["散步", "sàn bù", "san bu"], '散步 <span class="py">sàn bù · take a walk</span>'),
    quiz_item("我____喜欢晴天。", "Wǒ ___ xǐhuan qíngtiān.", "也", ["也", "yě", "ye"], '也 <span class="py">yě · also</span>'),
])
quiz2_4 = quiz_group_slide(2, "4", "4", "Final Challenge · 综合挑战", "final", "小挑战", "Challenge", "Answer in Chinese, pinyin, or English.", [
    quiz_item("'take a walk' 用中文怎么说？", "How do you say 'take a walk'?", "散步", ["散步", "sàn bù", "san bu"], '散步 <span class="py">sàn bù · take a walk</span>'),
    quiz_item("下雨的时候，我在家____。", "Xià yǔ de shíhòu, wǒ zài jiā ___.", "看书", ["看书", "kàn shū", "kan shu"], '看书 <span class="py">kàn shū · read</span>'),
    quiz_item("阴天让我的心情____。", "Yīntiān ràng wǒ de xīnqíng ___.", "不好", ["不好", "bù hǎo", "bu hao"], '不好 <span class="py">bù hǎo · not good</span>'),
])

LEVELS[2] = {
    "tags": ["HSK 2", "18 new words", "3 grammar points"],
    "eyebrow": "Daily life · 日常生活 · Level 2",
    "warmup": {"title": warm2_title, "py": warm2_py, "chips_w": warm2_chips_w, "chips_m": warm2_chips_m, "practice": warm2_practice},
    "vocab": {"count": "18 words", "words": vocab2_words, "ex": vocab2_ex, "practice": vocab2_practice},
    "grammar": [
        {"label": "G1 · 让", "bg": "rust", "strip": gram2_g1, "ex": gram2_g1_ex, "practice": gram2_g1_practice},
        {"label": "G2 · 的时候", "bg": "sky", "strip": gram2_g2, "ex": gram2_g2_ex, "practice": gram2_g2_practice},
        {"label": "G3 · 也", "bg": "gold", "strip": gram2_g3, "ex": gram2_g3_ex, "practice": gram2_g3_practice},
    ],
    "dialogue": dial2,
    "review": review2,
    "quizzes": [quiz2_1, quiz2_2, quiz2_3, quiz2_4],
}
