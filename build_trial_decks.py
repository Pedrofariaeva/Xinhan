#!/usr/bin/env python3
"""Transform static lesson decks into interactive trial-lesson decks."""
import os
import re

QUIZ_CSS = """
/* --- INTERACTIVE QUIZ STYLES --- */
.phone-row { display: flex; gap: 16px; flex-wrap: wrap; justify-content: flex-start; margin-bottom: 0.5rem; }
.phone-block { display: flex; flex-direction: column; gap: 0.55rem; width: 150px; }
.phone-block.wide { width: 200px; }
.phone-mock { width: 150px; border-radius: 16px; overflow: hidden; border: 3px solid var(--jade); box-shadow: 0 6px 16px rgba(45,106,79,0.25); position: relative; background: var(--cream); }
.phone-mock svg { width: 100%; display: block; }
.phone-step { font-size: 0.62rem; font-weight: 700; color: var(--gold); text-align: center; }
.quiz-q { background: var(--cream); border-radius: 8px; padding: 0.5rem 0.65rem; font-size: 0.66rem; color: var(--ink); line-height: 1.45; }
.quiz-q .py { display: block; color: var(--gold); font-size: 0.6rem; margin-top: 1px; }
.quiz-callout { position: absolute; border: 2px solid #f6e05e; border-radius: 6px; box-shadow: 0 0 0 3px rgba(246,224,94,0.35); pointer-events: none; animation: quiz-pulse 1.6s ease-in-out infinite; }
@keyframes quiz-pulse { 0%, 100% { opacity: 0.55; } 50% { opacity: 1; } }
.quiz-game { display: flex; flex-direction: column; gap: 0.3rem; }
.quiz-row { display: flex; gap: 0.3rem; }
.quiz-input { flex: 1; width: 100%; box-sizing: border-box; padding: 6px 8px; font-size: 0.66rem; font-family: inherit; border: 1px solid #d2d2d2; border-radius: 6px; background: var(--white); color: var(--ink); transition: border-color 0.15s, background 0.15s; }
.quiz-input:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.quiz-input:disabled { background: var(--cream); opacity: 0.85; }
.quiz-input.flash-correct { border-color: #2f7d52; background: #eaf7ef; animation: quiz-pop 0.4s ease; }
.quiz-input.flash-wrong { border-color: #c0392b; background: #fbeaea; animation: quiz-shake 0.4s ease; }
.quiz-check-btn { flex-shrink: 0; padding: 6px 10px; font-size: 0.62rem; font-weight: 700; border: none; border-radius: 6px; background: var(--gold); color: var(--jade); cursor: pointer; transition: background 0.15s, transform 0.15s; }
.quiz-check-btn:hover:not(:disabled) { transform: translateY(-1px); }
.quiz-check-btn:disabled { cursor: default; }
.quiz-check-btn.correct { background: #2f7d52; color: white; animation: quiz-pop 0.4s ease; }
.quiz-check-btn.wrong { background: #c0392b; color: white; animation: quiz-shake 0.4s ease; }
@keyframes quiz-pop { 0% { transform: scale(1); } 40% { transform: scale(1.12); } 100% { transform: scale(1); } }
@keyframes quiz-shake { 0%, 100% { transform: translateX(0); } 20% { transform: translateX(-5px); } 40% { transform: translateX(5px); } 60% { transform: translateX(-4px); } 80% { transform: translateX(4px); } }
.quiz-hint { font-size: 0.56rem; color: var(--ink-3); }
.quiz-feedback { font-size: 0.68rem; font-weight: 700; min-height: 1.1em; }
.quiz-feedback.correct { color: #2f7d52; }
.quiz-feedback.wrong { color: #c0392b; }
.quiz-feedback .reveal { display: block; font-weight: 500; color: var(--ink); margin-top: 2px; font-size: 0.62rem; }
.quiz-feedback .reveal .py { color: var(--gold); }
.quiz-score { display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.66rem; font-weight: 700; color: var(--jade); background: var(--cream); border-radius: 20px; padding: 0.3rem 0.8rem; margin-bottom: 0.8rem; }
.quiz-score .stars { color: var(--gold); letter-spacing: 1px; }
.learn-badge { display: inline-block; font-size: 0.6rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--jade); background: var(--jade-pale); border-radius: 20px; padding: 0.25rem 0.7rem; margin-bottom: 0.6rem; }
.test-badge { display: inline-block; font-size: 0.6rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--rust); background: #fbeaea; border-radius: 20px; padding: 0.25rem 0.7rem; margin-bottom: 0.6rem; }
.report-score { display: flex; align-items: baseline; gap: 0.6rem; margin: 0.5rem 0 1rem; }
.report-score .big { font-size: 2.4rem; font-weight: 800; color: var(--jade); }
.report-score .pct { font-size: 1rem; font-weight: 700; color: var(--gold); }
.report-groups { display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.2rem; }
.report-group-row { display: flex; align-items: center; gap: 0.6rem; font-size: 0.66rem; }
.report-group-name { width: 150px; flex-shrink: 0; color: var(--ink); }
.report-group-bar { flex: 1; height: 8px; border-radius: 5px; background: var(--cream); overflow: hidden; }
.report-group-fill { height: 100%; background: var(--jade-mid); border-radius: 5px; }
.report-group-fill.weak { background: var(--rust-light); }
.report-group-score { width: 36px; flex-shrink: 0; text-align: right; color: var(--ink-3); }
.report-missed { background: #fbeaea; border-radius: 8px; padding: 0.8rem 1rem; }
.report-missed h4 { margin: 0 0 0.5rem; font-size: 0.72rem; color: var(--rust); }
.report-missed-item { display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: baseline; font-size: 0.66rem; padding: 0.35rem 0; border-bottom: 1px solid rgba(155,34,38,0.12); }
.report-missed-item:last-child { border-bottom: none; }
.report-missed-q { color: var(--ink); flex: 1; min-width: 200px; }
.report-missed-you { color: #c0392b; text-decoration: line-through; }
.report-missed-correct { color: #2f7d52; font-weight: 600; }
.report-perfect { background: var(--jade-pale); border-radius: 8px; padding: 1rem; font-size: 0.72rem; color: var(--jade); font-weight: 600; text-align: center; }
.sidebar.dark { background: #1a3a2b; }
"""

REPORT_SLIDE = """
<!-- LESSON REPORT -->
<div class="slide" id="lesson-report-slide" style="grid-template-columns:64px 1fr; display:none;">
  <div class="sidebar dark">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 21 L5 13 M12 21 L12 8 M19 21 L19 16 M23 21 L23 11" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">your report</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div></div>
  </div>
  <div class="content">
    <div class="sec-label">Lesson Report · 学习报告</div>
    <h2>你的学习报告 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Nǐ de xuéxí bàogào.</span></h2>
    <div id="report-score" class="report-score"></div>
    <div id="report-groups" class="report-groups"></div>
    <div id="report-missed"></div>
  </div>
</div>
"""


def quiz_block(question, answers, reveal, placeholder=""):
    safe_reveal = reveal.replace('"', '&quot;')
    safe_answers = answers.replace('"', '&quot;')
    safe_placeholder = placeholder.replace('"', '&quot;')
    return f"""<div class="phone-block wide">
        <div class="quiz-q">{question}</div>
        <div class="quiz-game">
          <div class="quiz-row">
            <input type="text" class="quiz-input" placeholder="{safe_placeholder}" data-answer="{safe_answers}" data-reveal="{safe_reveal}"/>
            <button type="button" class="quiz-check-btn">检查</button>
          </div>
          <div class="quiz-feedback"></div>
        </div>
      </div>"""


BANJIA_QUIZZES = """
<!-- ⑩ VOCAB TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4" y="3" width="20" height="22" rx="2" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <line x1="8" y1="9" x2="20" y2="9" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="8" y1="14" x2="20" y2="14" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="8" y1="19" x2="15" y2="19" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">test 1/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Vocabulary · 词汇</div>
    <h2>写出中文 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Xiě chū Zhōngwén.</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-1" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type the Chinese word</strong> for each English meaning.</div>
    <div class="phone-row">
      """ + quiz_block("'move house' 的中文是什么？<span class=\"py\">What is 'move house' in Chinese?</span>",
                       "搬家|bān jiā|ban jia", "搬家 <span class=\"py\">bān jiā · move house</span>", "搬家...") + """
      """ + quiz_block("'convenient' 的中文是什么？<span class=\"py\">What is 'convenient' in Chinese?</span>",
                       "方便|fāng biàn|fang bian", "方便 <span class=\"py\">fāng biàn · convenient</span>", "方便...") + """
      """ + quiz_block("'expensive' 的中文是什么？<span class=\"py\">What is 'expensive' in Chinese?</span>",
                       "贵|guì|gui", "贵 <span class=\"py\">guì · expensive</span>", "贵...") + """
    </div>
  </div>
</div>

<!-- ⑪ GRAMMAR TEST 比/更 -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <line x1="14" y1="5" x2="14" y2="24" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <line x1="5" y1="11" x2="23" y2="11" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
        <circle cx="5" cy="17" r="4" fill="rgba(255,255,255,0.7)"/>
        <circle cx="23" cy="8" r="4" fill="rgba(255,255,255,0.5)"/>
      </svg>
      <div class="sb-label">test 2/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Grammar · 语法</div>
    <h2>比 / 更 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">bǐ / gèng</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-2" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Fill in the blank</strong> with the right word.</div>
    <div class="phone-row">
      """ + quiz_block("深圳的工资____这里高。 <span class=\"py\">Shēnzhèn de gōngzī ___ zhèlǐ gāo.</span>",
                       "比|bǐ|bi", "比 <span class=\"py\">bǐ · than</span>", "比...") + """
      """ + quiz_block("住在城市，买东西____方便。 <span class=\"py\">Zhù zài chéngshì, mǎi dōngxi ___ fāngbiàn.</span>",
                       "更|gèng|geng", "更 <span class=\"py\">gèng · even more</span>", "更...") + """
      """ + quiz_block("猫____狗小。 <span class=\"py\">Māo ___ gǒu xiǎo.</span>",
                       "比|bǐ|bi", "比 <span class=\"py\">bǐ · than</span>", "比...") + """
    </div>
  </div>
</div>

<!-- ⑫ GRAMMAR TEST 离/先然后 -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="7" cy="10" r="4" fill="none" stroke="rgba(255,255,255,0.9)" stroke-width="1.5"/>
        <circle cx="21" cy="18" r="4" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
        <path d="M7 18 Q14 22 21 18" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" stroke-dasharray="3,2"/>
      </svg>
      <div class="sb-label">test 3/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Grammar · 语法</div>
    <h2>离 / 先…然后 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">lí / xiān…ránhòu</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-3" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Fill in the blank.</strong></div>
    <div class="phone-row">
      """ + quiz_block("我的家____超市很近。 <span class=\"py\">Wǒ de jiā ___ chāoshì hěn jìn.</span>",
                       "离|lí|li", "离 <span class=\"py\">lí · away from</span>", "离...") + """
      """ + quiz_block("你____在网上找到工作，然后搬家。 <span class=\"py\">Nǐ ___ zài wǎngshàng zhǎodào gōngzuò, ránhòu bānjiā.</span>",
                       "先|xiān|xian", "先 <span class=\"py\">xiān · first</span>", "先...") + """
      """ + quiz_block("他的办公室____家很远。 <span class=\"py\">Tā de bàngōngshì ___ jiā hěn yuǎn.</span>",
                       "离|lí|li", "离 <span class=\"py\">lí · away from</span>", "离...") + """
    </div>
  </div>
</div>

<!-- ⑬ FINAL TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 14 L12 20 L22 8" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="sb-label">final test</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Final Challenge · 综合挑战</div>
    <h2>搬家大挑战 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Moving House Challenge</span></h2>
    <div class="quiz-score" data-quiz-score data-group="final" data-total="4">✅ <span class="score-correct">0</span>/<span class="score-total">4</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Answer in Chinese, pinyin, or English.</strong></div>
    <div class="phone-row">
      """ + quiz_block("'find' 的中文是什么？<span class=\"py\">What is 'find' in Chinese?</span>",
                       "找到|zhǎo dào|zhao dao", "找到 <span class=\"py\">zhǎo dào · find</span>", "找到...") + """
      """ + quiz_block("'opportunity' 的中文是什么？<span class=\"py\">What is 'opportunity' in Chinese?</span>",
                       "机会|jī huì|ji hui", "机会 <span class=\"py\">jī huì · opportunity</span>", "机会...") + """
      """ + quiz_block("'far' 的反义词是什么？<span class=\"py\">What is the opposite of 'far'?</span>",
                       "近|jìn|jin|close|near", "近 <span class=\"py\">jìn · close / near</span>", "近...") + """
      """ + quiz_block("'first…then…' 用中文怎么说？<span class=\"py\">How do you say 'first…then…'?</span>",
                       "先然后|xiān rán hòu|xian ran hou|先…然后", "先…然后 <span class=\"py\">xiān…rán hòu · first…then…</span>", "先...然后...") + """
    </div>
  </div>
</div>
"""

MOOD_WEATHER_QUIZZES = """
<!-- ⑧ WEATHER TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="14" cy="14" r="6" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <path d="M14 6v2M14 20v2M6 14h2M20 14h2" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">test 1/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot active"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Weather · 天气</div>
    <h2>天气词 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Tiānqì cí</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-1" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type the Chinese word.</strong></div>
    <div class="phone-row">
      """ + quiz_block("'sunny / clear' 用中文怎么说？<span class=\"py\">How do you say 'sunny / clear'?</span>",
                       "晴|qíng|qing|晴天|qíngtiān", "晴 / 晴天 <span class=\"py\">qíng / qíngtiān · sunny</span>", "晴...") + """
      """ + quiz_block("'snow / snowy' 用中文怎么说？<span class=\"py\">How do you say 'snow / snowy'?</span>",
                       "下雪|xià xuě|xia xue|雪|xuě", "下雪 <span class=\"py\">xià xuě · snow / snowy</span>", "下雪...") + """
      """ + quiz_block("'warm' 用中文怎么说？<span class=\"py\">How do you say 'warm'?</span>",
                       "暖和|nuǎn huo|nuan huo", "暖和 <span class=\"py\">nuǎn huo · warm</span>", "暖和...") + """
    </div>
  </div>
</div>

<!-- ⑨ MOOD TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="14" cy="14" r="9" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <circle cx="11" cy="13" r="1.5" fill="rgba(255,255,255,0.85)"/>
        <circle cx="17" cy="13" r="1.5" fill="rgba(255,255,255,0.85)"/>
        <path d="M10 17 Q14 21 18 17" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">test 2/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Mood · 心情</div>
    <h2>心情词 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Xīnqíng cí</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-2" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type the Chinese word.</strong></div>
    <div class="phone-row">
      """ + quiz_block("'happy' 用中文怎么说？<span class=\"py\">How do you say 'happy'?</span>",
                       "开心|kāi xīn|kai xin", "开心 <span class=\"py\">kāi xīn · happy</span>", "开心...") + """
      """ + quiz_block("'down / low' 用中文怎么说？<span class=\"py\">How do you say 'down / low'?</span>",
                       "低落|dī luò|di luo", "低落 <span class=\"py\">dī luò · down / low</span>", "低落...") + """
      """ + quiz_block("'mood / feeling' 用中文怎么说？<span class=\"py\">How do you say 'mood / feeling'?</span>",
                       "心情|xīn qíng|xin qing", "心情 <span class=\"py\">xīn qíng · mood</span>", "心情...") + """
    </div>
  </div>
</div>

<!-- ⑩ GRAMMAR TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M7 14 Q14 8 21 14 L19 23 Q14 26 9 23 Z" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none"/>
        <line x1="10" y1="16" x2="18" y2="16" stroke="rgba(255,255,255,0.6)" stroke-width="1.5"/>
      </svg>
      <div class="sb-label">test 3/4</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Grammar · 语法</div>
    <h2>让 / 的时候 / 看起来 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">ràng / de shíhòu / kàn qǐlái</span></h2>
    <div class="quiz-score" data-quiz-score data-group="group-3" data-total="3">✅ <span class="score-correct">0</span>/<span class="score-total">3</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Fill in the blank.</strong></div>
    <div class="phone-row">
      """ + quiz_block("晴天____我的心情很好。 <span class=\"py\">Qíngtiān ___ wǒ de xīnqíng hěn hǎo.</span>",
                       "让|ràng|rang|使", "让 <span class=\"py\">ràng · make / let</span>", "让...") + """
      """ + quiz_block("天气好的时候，我喜欢去公园____。 <span class=\"py\">Tiānqì hǎo de shíhòu, wǒ xǐhuan qù gōngyuán ___.</span>",
                       "散步|sàn bù|san bu", "散步 <span class=\"py\">sàn bù · take a walk</span>", "散步...") + """
      """ + quiz_block("你____很开心！ <span class=\"py\">Nǐ ___ hěn kāixīn!</span>",
                       "看起来|kàn qǐ lái|kan qi lai", "看起来 <span class=\"py\">kàn qǐlái · look</span>", "看起来...") + """
    </div>
  </div>
</div>

<!-- ⑪ FINAL TEST -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar rust">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 14 L12 20 L22 8" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="sb-label">final test</div>
    </div>
    <div class="sb-prog"><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div><div class="dot done"></div></div>
  </div>
  <div class="content">
    <div class="test-badge">Test · 小测验</div>
    <div class="sec-label">Final Challenge · 综合挑战</div>
    <h2>心情和天气大挑战 <span style="font-family:'Inter';font-weight:300;font-size:0.78rem;color:var(--gold);letter-spacing:0.07em;">Mood &amp; Weather Challenge</span></h2>
    <div class="quiz-score" data-quiz-score data-group="final" data-total="4">✅ <span class="score-correct">0</span>/<span class="score-total">4</span> <span class="stars">★</span></div>
    <div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Answer in Chinese, pinyin, or English.</strong></div>
    <div class="phone-row">
      """ + quiz_block("'cloudy' 用中文怎么说？<span class=\"py\">How do you say 'cloudy'?</span>",
                       "阴|yīn|yin|阴天|yīntiān", "阴 / 阴天 <span class=\"py\">yīn / yīntiān · cloudy</span>", "阴...") + """
      """ + quiz_block("'rain / rainy' 用中文怎么说？<span class=\"py\">How do you say 'rain / rainy'?</span>",
                       "下雨|xià yǔ|xia yu|雨|yǔ", "下雨 <span class=\"py\">xià yǔ · rain / rainy</span>", "下雨...") + """
      """ + quiz_block("今天天气____阴____冷。 <span class=\"py\">Jīntiān tiānqì ___ yīn ___ lěng.</span>",
                       "又|yòu|you", "又…又… <span class=\"py\">yòu…yòu… · both…and…</span>", "又...") + """
      """ + quiz_block("'when…' 用中文怎么说？<span class=\"py\">How do you say 'when…'?</span>",
                       "的时候|de shí hòu|de shi hou", "的时候 <span class=\"py\">de shíhòu · when…</span>", "的时候...") + """
    </div>
  </div>
</div>
"""


def make_js(group_names):
    entries = ",\n    ".join(f"'{k}': '{v}'" for k, v in group_names.items())
    return f"""<script>
(function () {{
  var lessonId = document.body.dataset.lessonId || '';
  var allInputs = Array.prototype.slice.call(document.querySelectorAll('.quiz-input'));
  var reportShown = false;
  var wrongAnswers = [];

  var GROUP_NAMES = {{
    {entries}
  }};

  function escapeHtml(s) {{
    return String(s).replace(/[&<>"]/g, function (c) {{
      return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }}[c];
    }});
  }}

  function logAttempt(payload) {{
    if (!lessonId) return;
    fetch('/api/lessons/attempt', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify(payload),
    }}).catch(function () {{}});
  }}

  function logCompletion(score, total, groupList) {{
    if (!lessonId) return;
    fetch('/api/lessons/complete', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ lessonId: lessonId, score: score, total: total, groups: groupList }}),
    }}).catch(function () {{}});
  }}

  function buildReport() {{
    var groups = {{}};
    document.querySelectorAll('[data-quiz-score]').forEach(function (box) {{
      var groupId = box.dataset.group || 'default';
      groups[groupId] = {{
        groupId: groupId,
        score: Number(box.querySelector('.score-correct').textContent),
        total: Number(box.dataset.total),
      }};
    }});
    var groupList = Object.keys(groups).map(function (k) {{ return groups[k]; }});
    var score = groupList.reduce(function (s, g) {{ return s + g.score; }}, 0);
    var total = groupList.reduce(function (s, g) {{ return s + g.total; }}, 0);
    var pct = total > 0 ? Math.round((score / total) * 100) : 0;

    var scoreBox = document.getElementById('report-score');
    if (scoreBox) {{
      scoreBox.innerHTML =
        '<span class="big">' + score + '/' + total + '</span>' +
        '<span class="pct">' + pct + '%</span>';
    }}

    var groupsBox = document.getElementById('report-groups');
    if (groupsBox) {{
      groupsBox.innerHTML = groupList.map(function (g) {{
        var p = g.total > 0 ? (g.score / g.total) * 100 : 0;
        var weak = p < 100 ? ' weak' : '';
        return '<div class="report-group-row">' +
          '<div class="report-group-name">' + (GROUP_NAMES[g.groupId] || g.groupId) + '</div>' +
          '<div class="report-group-bar"><div class="report-group-fill' + weak + '" style="width:' + p + '%"></div></div>' +
          '<div class="report-group-score">' + g.score + '/' + g.total + '</div>' +
          '</div>';
      }}).join('');
    }}

    var missedBox = document.getElementById('report-missed');
    if (missedBox) {{
      if (wrongAnswers.length === 0) {{
        missedBox.innerHTML = '<div class="report-perfect">完美！Perfect score — every answer right. 🎉</div>';
      }} else {{
        missedBox.innerHTML = '<div class="report-missed"><h4>Words &amp; phrases to review · 需要复习的词</h4>' +
          wrongAnswers.map(function (w) {{
            return '<div class="report-missed-item">' +
              '<span class="report-missed-q">' + escapeHtml(w.questionText) + '</span>' +
              '<span class="report-missed-you">' + escapeHtml(w.userAnswer || '(blank)') + '</span>' +
              '<span class="report-missed-correct">' + w.reveal + '</span>' +
              '</div>';
          }}).join('') +
          '</div>';
      }}
    }}

    var slide = document.getElementById('lesson-report-slide');
    if (slide) {{
      slide.style.display = 'grid';
      slide.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}

    logCompletion(score, total, groupList);
  }}

  function maybeShowReport() {{
    if (reportShown) return;
    var allDone = allInputs.every(function (i) {{ return i.disabled; }});
    if (!allDone) return;
    reportShown = true;
    buildReport();
  }}

  allInputs.forEach(function (input, globalIndex) {{
    var row = input.closest('.quiz-game');
    var feedback = row.querySelector('.quiz-feedback');
    var checkBtn = row.querySelector('.quiz-check-btn');
    var answers = (input.dataset.answer || '').split('|').map(function (a) {{
      return a.trim().toLowerCase();
    }});
    var reveal = input.dataset.reveal || '';
    var scoreBox = input.closest('.content') ? input.closest('.content').querySelector('[data-quiz-score]') : null;
    var questionText = input.closest('.phone-block') ? input.closest('.phone-block').querySelector('.quiz-q').textContent.trim() : '';

    function check() {{
      if (input.disabled) return;
      var val = input.value.trim().toLowerCase();
      if (!val) return;
      var correct = answers.indexOf(val) !== -1;

      feedback.className = 'quiz-feedback ' + (correct ? 'correct' : 'wrong');
      feedback.innerHTML = (correct ? '对! Duì! Right!' : '错! Cuò! Wrong!') +
        (reveal ? '<span class="reveal">' + reveal + '</span>' : '');

      input.classList.add(correct ? 'flash-correct' : 'flash-wrong');
      if (checkBtn) {{
        checkBtn.classList.add(correct ? 'correct' : 'wrong');
        checkBtn.textContent = correct ? '✓' : '✗';
        checkBtn.disabled = true;
      }}
      input.disabled = true;

      if (correct && scoreBox) {{
        var counter = scoreBox.querySelector('.score-correct');
        counter.textContent = String(Number(counter.textContent) + 1);
      }}
      if (!correct) {{
        wrongAnswers.push({{
          questionText: questionText,
          userAnswer: input.value.trim(),
          reveal: reveal,
        }});
      }}

      logAttempt({{
        lessonId: lessonId,
        groupId: scoreBox ? scoreBox.dataset.group : 'default',
        questionIndex: globalIndex,
        questionText: questionText,
        userAnswer: input.value.trim(),
        correct: correct,
      }});
      maybeShowReport();
    }}

    input.addEventListener('keydown', function (e) {{
      if (e.key === 'Enter') check();
    }});
    if (checkBtn) checkBtn.addEventListener('click', check);
  }});
}})();
</script>"""


LESSONS = {
    'banjia': {
        'source': '/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/13 banjia/ban-jia-lesson-deck.html',
        'target': '/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson/banjia/index.html',
        'lesson_id': 'banjia',
        'quiz_css_extra': '',
        'quizzes': BANJIA_QUIZZES,
        'group_names': {
            'group-1': 'Vocabulary · 词汇',
            'group-2': 'Grammar 比/更',
            'group-3': 'Grammar 离/先然后',
            'final': 'Final Test · 综合挑战',
        },
    },
    'mood-weather': {
        'source': '/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/14 Mood and Weather/xin-qing-tian-qi-lesson-deck.html',
        'target': '/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson/mood-weather/index.html',
        'lesson_id': 'mood-weather',
        'quiz_css_extra': '.vc.cat-weather { border-top-color: #1d5f8a; }\n.vc.cat-mood { border-top-color: #9b2226; }\n.vc.cat-act { border-top-color: #7b5a1a; }\n.vc.cat-gram { border-top-color: #2d6a4f; }',
        'quizzes': MOOD_WEATHER_QUIZZES,
        'group_names': {
            'group-1': 'Weather · 天气',
            'group-2': 'Mood · 心情',
            'group-3': 'Grammar · 语法',
            'final': 'Final Test · 综合挑战',
        },
    },
}


def transform(lesson):
    with open(lesson['source'], 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject quiz CSS before closing </style>
    css = QUIZ_CSS
    if lesson['quiz_css_extra']:
        css += '\n' + lesson['quiz_css_extra']
    html = html.replace('</style>', css + '\n</style>')

    # Set body data-lesson-id
    html = re.sub(r'<body([^>]*)>', r'<body data-lesson-id="' + lesson['lesson_id'] + r'"\1>', html)

    # Replace closing tags with quizzes, report, JS, and closing tags
    closing = '</div>\n</body>\n</html>'
    replacement = lesson['quizzes'] + REPORT_SLIDE + make_js(lesson['group_names']) + '\n</body>\n</html>'
    if html.endswith(closing):
        html = html[:-len(closing)] + replacement
    else:
        # Fallback: replace the last occurrence
        html = html.rsplit('</div>', 1)[0] + replacement

    os.makedirs(os.path.dirname(lesson['target']), exist_ok=True)
    with open(lesson['target'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote {lesson['target']} ({len(html)} bytes)")


if __name__ == '__main__':
    for key in LESSONS:
        transform(LESSONS[key])
