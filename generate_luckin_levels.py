#!/usr/bin/env python3
"""Generate HSK 1, 2, 4, 5, 6 adaptations of the luckin-coffee lesson."""
import os, json

ROOT = "/Users/pedro/Documents/GitHub/Xinhan/public/trial-lesson"
SCREEN_BASE = "../../hsk-3/luckin-coffee/screens"

HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>点咖啡 — Ordering Coffee · Xinhan Chinese</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --jade: #2d6a4f; --jade-mid: #40916c; --jade-light: #74c69d; --jade-pale: #d8f3dc;
  --gold: #b7791f; --gold-mid: #d69e2e; --gold-pale: #fffff0;
  --rust: #9b2226; --rust-light: #e76f51; --rust-pale: #fff0ee;
  --sky: #1d5f8a; --sky-pale: #e8f4fd;
  --coffee: #4a3b32; --coffee-mid: #6f5b4d; --coffee-light: #a1887f;
  --cream: #faf7f2; --cream-dark: #ede8df;
  --ink: #1a1a1a; --ink-2: #3d3d3d; --ink-3: #7a7a7a;
  --white: #fff;
}
body { font-family: 'Inter', sans-serif; background: #d6cfc4; color: var(--ink); padding: 2.5rem 1rem 5rem; }
.deck { max-width: 940px; margin: 0 auto; }
.deck-brand { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
.brand-name { font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--coffee); }
.brand-sub  { font-size: 0.68rem; color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.12em; }
.slide { display: grid; background: var(--white); overflow: hidden; margin-bottom: 3px; }
.slide:first-of-type { border-radius: 14px 14px 0 0; }
.slide:last-of-type  { border-radius: 0 0 14px 14px; }
.sidebar { display: flex; flex-direction: column; padding: 1.5rem 0.65rem 1.5rem 0.9rem; background: var(--coffee); gap: 1.8rem; min-width: 64px; position: relative; }
.sidebar::after { content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(to bottom, rgba(255,255,255,0.25), transparent); }
.sb-icon { display: flex; flex-direction: column; align-items: center; gap: 0.3rem; }
.sb-icon svg { width: 28px; height: 28px; }
.sb-label { font-size: 0.48rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.55); text-align: center; line-height: 1.2; }
.sb-prog { display: flex; flex-direction: column; align-items: center; gap: 5px; margin-top: auto; }
.dot { width: 7px; height: 7px; border-radius: 50%; background: rgba(255,255,255,0.2); }
.dot.active { background: #d69e2e; }
.dot.done   { background: var(--coffee-light); }
.sidebar.rust  { background: var(--rust); }
.sidebar.sky   { background: var(--sky); }
.sidebar.gold  { background: #7b5a1a; }
.sidebar.cream { background: var(--cream-dark); }
.sidebar.cream::after { display:none; }
.sidebar.cream .sb-label { color: var(--coffee); }
.sidebar.dark  { background: #2d241f; }
.content { padding: 2rem 2.5rem 2rem 2rem; flex: 1; }
.sec-label { font-size: 0.6rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--coffee-mid); margin-bottom: 0.9rem; }
.content h2 { font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 600; margin-bottom: 1.25rem; line-height: 1.3; }
.zh-inline { font-family: 'Noto Serif SC', serif; color: var(--coffee); }
.py-inline { font-size: 0.72rem; font-family: 'Inter', sans-serif; font-weight: 400; color: var(--gold); letter-spacing: 0.07em; }
.scene { width: 100%; border-radius: 10px; overflow: hidden; margin-bottom: 1.25rem; }
.scene svg { display: block; width: 100%; }
.slide-cover { grid-template-columns: 90px 1fr; }
.cover-content { background: var(--coffee); padding: 2.5rem 2.5rem 2rem; position: relative; min-height: 300px; display: flex; flex-direction: column; justify-content: flex-end; overflow: hidden; }
.cover-scene { position: absolute; top: 0; right: 0; left: 0; bottom: 0; opacity: 0.15; }
.cover-eyebrow { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; color: var(--coffee-light); margin-bottom: 0.7rem; position: relative; }
.cover-zh { font-family: 'Noto Serif SC', serif; font-size: 5.8rem; font-weight: 700; color: var(--white); line-height: 1; letter-spacing: -0.02em; position: relative; }
.cover-py { font-size: 1.25rem; font-weight: 300; color: var(--coffee-light); letter-spacing: 0.18em; margin: 0.3rem 0; position: relative; }
.cover-en { font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.45rem; color: #f6e05e; position: relative; margin-bottom: 1.5rem; }
.cover-tags { display: flex; gap: 0.5rem; flex-wrap: wrap; position: relative; }
.tag { padding: 0.22rem 0.8rem; border-radius: 999px; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9); }
.grammar-strip { display: flex; align-items: center; gap: 0; background: var(--cream); border-radius: 10px; overflow: hidden; margin-bottom: 1.4rem; }
.gs-part { padding: 0.75rem 1rem; display: flex; flex-direction: column; align-items: center; }
.gs-part.colored { background: var(--coffee); }
.gs-part.colored.rust { background: var(--rust); }
.gs-part.colored.sky  { background: var(--sky); }
.gs-part.colored.gold { background: #7b5a1a; }
.gs-zh { font-family: 'Noto Serif SC', serif; font-size: 1.5rem; font-weight: 700; color: var(--white); line-height: 1; }
.gs-py { font-size: 0.58rem; color: rgba(255,255,255,0.7); letter-spacing: 0.06em; margin-top: 2px; }
.gs-sep { font-size: 1.1rem; color: var(--ink-3); padding: 0 0.3rem; }
.gs-plain-zh { font-family: 'Noto Serif SC', serif; font-size: 1.1rem; font-weight: 500; color: var(--coffee); }
.gs-plain-py { font-size: 0.58rem; color: var(--gold); margin-top: 2px; }
.gs-en { margin-left: auto; padding: 0.75rem 1.25rem; font-size: 0.72rem; color: var(--ink-3); font-style: italic; border-left: 1px solid var(--cream-dark); }
.ex-block { display: flex; flex-direction: column; gap: 0.65rem; margin-bottom: 1.25rem; }
.ex { background: var(--cream); border-radius: 8px; padding: 0.8rem 1rem; border-left: 3px solid var(--coffee-mid); }
.ex.rust { border-left-color: var(--rust-light); }
.ex.sky  { border-left-color: #4a9ec7; }
.ex-zh { font-family: 'Noto Serif SC', serif; font-size: 0.98rem; color: var(--ink); margin-bottom: 0.15rem; }
.key  { color: var(--coffee); font-weight: 700; }
.key-r{ color: var(--rust); font-weight: 700; }
.key-s{ color: var(--sky); font-weight: 700; }
.ex-py { font-size: 0.63rem; color: var(--gold); letter-spacing: 0.03em; margin-bottom: 0.1rem; }
.ex-en { font-size: 0.69rem; color: var(--ink-3); font-style: italic; }
.chip-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem; }
.chip { padding: 0.25rem 0.75rem; border-radius: 999px; font-size: 0.7rem; background: var(--cream); border: 1.5px solid var(--cream-dark); }
.chip .ch { font-family: 'Noto Serif SC', serif; font-size: 0.85rem; color: var(--coffee); font-weight: 500; }
.chip .py { font-size: 0.58rem; color: var(--gold); margin-left: 0.25rem; }
.vocab-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 6px; }
.vc { background: var(--white); border: 1px solid var(--cream-dark); border-radius: 7px; padding: 0.55rem 0.7rem; border-top: 3px solid var(--coffee-mid); }
.vc.cat-drink { border-top-color: var(--coffee-mid); }
.vc.cat-size  { border-top-color: var(--sky); }
.vc.cat-temp  { border-top-color: var(--gold-mid); }
.vc.cat-action{ border-top-color: var(--jade-mid); }
.vc-zh { font-family: 'Noto Serif SC', serif; font-size: 1rem; font-weight: 500; color: var(--coffee); }
.vc-py { font-size: 0.58rem; color: var(--gold); margin: 2px 0 1px; }
.vc-en { font-size: 0.62rem; color: var(--ink-3); }
.tip { background: var(--jade-pale); border-radius: 7px; padding: 0.65rem 0.95rem; font-size: 0.7rem; color: var(--jade); line-height: 1.55; margin-top: 0.9rem; }
.tip strong { font-weight: 600; }
.activities { display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: 0.75rem; }
.act { background: var(--cream); border-radius: 8px; padding: 0.55rem 0.8rem; text-align: center; flex: 1; min-width: 90px; }
.act-zh { font-family: 'Noto Serif SC', serif; font-size: 0.88rem; color: var(--coffee); font-weight: 500; }
.act-py { font-size: 0.58rem; color: var(--gold); margin-top: 2px; }
.slide-close { display: block; background: #2d241f; border-radius: 0 0 14px 14px; }
.close-inner { padding: 3rem 3.5rem; display: flex; align-items: center; justify-content: space-between; }
.close-zh { font-family: 'Noto Serif SC', serif; font-size: 5rem; font-weight: 700; color: var(--white); }
.close-detail .py { font-size: 1rem; color: var(--coffee-light); letter-spacing: 0.2em; }
.close-detail .en { font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.9rem; color: #f6e05e; margin-top: 0.2rem; }
.close-detail .sub { font-size: 0.62rem; color: rgba(255,255,255,0.3); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 1rem; }
.photo-row { display:flex; gap:8px; margin-bottom:1rem; }
.photo-slot { flex:1; border-radius:9px; overflow:hidden; position:relative; min-height:110px; background:linear-gradient(135deg,var(--jade-pale),var(--cream-dark)); }
.photo-slot img { width:100%; height:100%; object-fit:cover; display:block; }
.photo-cap { position:absolute; bottom:0; left:0; right:0; background:linear-gradient(transparent,rgba(0,0,0,0.58)); color:white; font-size:0.68rem; font-family:'Noto Serif SC',serif; padding:14px 9px 6px; font-weight:700; letter-spacing:0.04em; }
.photo-cap small { display:block; font-family:'Inter',sans-serif; font-size:0.56rem; color:rgba(255,255,255,0.72); font-weight:400; }
.photo-wide { border-radius:10px; overflow:hidden; position:relative; margin-bottom:1rem; height:130px; background:linear-gradient(135deg,var(--sky-pale),var(--cream-dark)); }
.photo-wide img { width:100%; height:100%; object-fit:cover; display:block; }
.phone-row { display: flex; gap: 16px; flex-wrap: wrap; justify-content: flex-start; margin-bottom: 0.5rem; }
.phone-block { display: flex; flex-direction: column; gap: 0.55rem; width: 150px; }
.phone-mock { width: 150px; border-radius: 16px; overflow: hidden; border: 3px solid #2d241f; box-shadow: 0 6px 16px rgba(45,36,31,0.25); position: relative; }
.phone-mock img { width: 100%; display: block; }
.phone-step { font-size: 0.62rem; font-weight: 700; color: var(--gold); text-align: center; }
.quiz-q { background: var(--cream); border-radius: 8px; padding: 0.5rem 0.65rem; font-size: 0.66rem; color: var(--ink); line-height: 1.45; }
.quiz-q .py { display: block; color: var(--gold); font-size: 0.6rem; margin-top: 1px; }
.quiz-callout { position: absolute; border: 2px solid #d69e2e; border-radius: 6px; box-shadow: 0 0 0 3px rgba(214,158,46,0.35); pointer-events: none; animation: quiz-pulse 1.6s ease-in-out infinite; }
@keyframes quiz-pulse { 0%, 100% { opacity: 0.55; } 50% { opacity: 1; } }
.quiz-game { display: flex; flex-direction: column; gap: 0.3rem; }
.quiz-row { display: flex; gap: 0.3rem; }
.quiz-input { flex: 1; width: 100%; box-sizing: border-box; padding: 6px 8px; font-size: 0.66rem; font-family: inherit; border: 1px solid #cbb8a0; border-radius: 6px; background: var(--white); color: var(--ink); transition: border-color 0.15s, background 0.15s; }
.quiz-input:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.quiz-input:disabled { background: var(--cream); opacity: 0.85; }
.quiz-input.flash-correct { border-color: #2f7d52; background: #eaf7ef; animation: quiz-pop 0.4s ease; }
.quiz-input.flash-wrong { border-color: #c0392b; background: #fbeaea; animation: quiz-shake 0.4s ease; }
.quiz-check-btn { flex-shrink: 0; padding: 6px 10px; font-size: 0.62rem; font-weight: 700; border: none; border-radius: 6px; background: var(--gold); color: #2d241f; cursor: pointer; transition: background 0.15s, transform 0.15s; }
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
.quiz-score { display: inline-flex; align-items: center; gap: 0.4rem; font-size: 0.66rem; font-weight: 700; color: var(--coffee); background: var(--cream); border-radius: 20px; padding: 0.3rem 0.8rem; margin-bottom: 0.8rem; }
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
.dialogue-exchange { display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1rem; }
.bubble { display: flex; gap: 0.75rem; align-items: flex-start; }
.bubble.bubble-b { flex-direction: row-reverse; }
.bubble-avatar { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Noto Serif SC', serif; font-size: 0.75rem; font-weight: 700; flex-shrink: 0; }
.avatar-a { background: var(--coffee); color: white; }
.avatar-b { background: #fff7e6; color: var(--gold); }
.bubble-content { max-width: 75%; }
.bubble-role { font-size: 0.58rem; font-weight: 700; color: var(--ink-3); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.2rem; }
.bubble-b .bubble-role { text-align: right; }
.bubble-text { background: var(--cream); border-radius: 0 10px 10px 10px; padding: 0.7rem 0.9rem; }
.bubble-b .bubble-text { background: var(--jade-pale); border-radius: 10px 0 10px 10px; }
.bubble-zh { font-family: 'Noto Serif SC', serif; font-size: 1rem; color: var(--ink); }
.bubble-py { font-size: 0.65rem; color: var(--gold); margin-top: 0.2rem; }
.bubble-en { font-size: 0.7rem; color: var(--ink-3); font-style: italic; margin-top: 0.15rem; }
@media print {
  body { background: white; padding: 0; }
  .deck { max-width: 100%; }
  .slide { break-inside: avoid; margin-bottom: 0; }
  .deck-brand { display: none; }
}
@media (max-width: 640px) {
  .slide { grid-template-columns: 48px 1fr !important; }
  .sidebar { padding: 1rem 0.4rem; }
  .content { padding: 1.25rem; }
  .vocab-grid { grid-template-columns: repeat(2,1fr); }
  .cover-zh { font-size: 3.5rem; }
}
</style>
</head>
"""

FOOT = """</div>

<script>
(function () {
  var lessonId = document.body.dataset.lessonId || '';
  var allInputs = Array.prototype.slice.call(document.querySelectorAll('.quiz-input'));
  var reportShown = false;
  var wrongAnswers = [];
  var GROUP_NAMES = {GROUP_NAMES_JSON};
  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function logAttempt(payload) {
    if (!lessonId) return;
    fetch('/api/lessons/attempt', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) }).catch(function () {});
  }
  function logCompletion(score, total, groupList) {
    if (!lessonId) return;
    fetch('/api/lessons/complete', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ lessonId: lessonId, score: score, total: total, groups: groupList }) }).catch(function () {});
  }
  function buildReport() {
    var groups = {};
    document.querySelectorAll('[data-quiz-score]').forEach(function (box) {
      var groupId = box.dataset.group || 'default';
      groups[groupId] = { groupId: groupId, score: Number(box.querySelector('.score-correct').textContent), total: Number(box.dataset.total) };
    });
    var groupList = Object.keys(groups).map(function (k) { return groups[k]; });
    var score = groupList.reduce(function (s, g) { return s + g.score; }, 0);
    var total = groupList.reduce(function (s, g) { return s + g.total; }, 0);
    var pct = total > 0 ? Math.round((score / total) * 100) : 0;
    var scoreBox = document.getElementById('report-score');
    if (scoreBox) { scoreBox.innerHTML = '<span class="big">' + score + '/' + total + '</span><span class="pct">' + pct + '%</span>'; }
    var groupsBox = document.getElementById('report-groups');
    if (groupsBox) {
      groupsBox.innerHTML = groupList.map(function (g) {
        var p = g.total > 0 ? (g.score / g.total) * 100 : 0;
        var weak = p < 100 ? ' weak' : '';
        return '<div class="report-group-row"><div class="report-group-name">' + (GROUP_NAMES[g.groupId] || g.groupId) + '</div><div class="report-group-bar"><div class="report-group-fill' + weak + '" style="width:' + p + '%"></div></div><div class="report-group-score">' + g.score + '/' + g.total + '</div></div>';
      }).join('');
    }
    var missedBox = document.getElementById('report-missed');
    if (missedBox) {
      if (wrongAnswers.length === 0) { missedBox.innerHTML = '<div class="report-perfect">完美！Perfect score — every screen, right answer. 🎉</div>'; }
      else {
        missedBox.innerHTML = '<div class="report-missed"><h4>Words & screens to review · 需要复习的词</h4>' + wrongAnswers.map(function (w) {
          return '<div class="report-missed-item"><span class="report-missed-q">' + escapeHtml(w.questionText) + '</span><span class="report-missed-you">' + escapeHtml(w.userAnswer || '(blank)') + '</span><span class="report-missed-correct">' + w.reveal + '</span></div>';
        }).join('') + '</div>';
      }
    }
    var slide = document.getElementById('lesson-report-slide');
    if (slide) { slide.style.display = 'grid'; slide.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    logCompletion(score, total, groupList);
  }
  function maybeShowReport() {
    if (reportShown) return;
    var allDone = allInputs.every(function (i) { return i.disabled; });
    if (!allDone) return;
    reportShown = true; buildReport();
  }
  allInputs.forEach(function (input, globalIndex) {
    var row = input.closest('.quiz-game');
    var feedback = row.querySelector('.quiz-feedback');
    var checkBtn = row.querySelector('.quiz-check-btn');
    var answers = (input.dataset.answer || '').split('|').map(function (a) { return a.trim().toLowerCase(); });
    var reveal = input.dataset.reveal || '';
    var scoreBox = input.closest('.content') ? input.closest('.content').querySelector('[data-quiz-score]') : null;
    var questionText = input.closest('.phone-block') ? input.closest('.phone-block').querySelector('.quiz-q').textContent.trim() : '';
    function check() {
      if (input.disabled) return;
      var val = input.value.trim().toLowerCase();
      if (!val) return;
      var correct = answers.indexOf(val) !== -1;
      feedback.className = 'quiz-feedback ' + (correct ? 'correct' : 'wrong');
      feedback.innerHTML = (correct ? '对! Duì! Right!' : '错! Cuò! Wrong!') + (reveal ? '<span class="reveal">' + reveal + '</span>' : '');
      input.classList.add(correct ? 'flash-correct' : 'flash-wrong');
      if (checkBtn) { checkBtn.classList.add(correct ? 'correct' : 'wrong'); checkBtn.textContent = correct ? '✓' : '✗'; checkBtn.disabled = true; }
      input.disabled = true;
      if (correct && scoreBox) { var counter = scoreBox.querySelector('.score-correct'); counter.textContent = String(Number(counter.textContent) + 1); }
      if (!correct) { wrongAnswers.push({ questionText: questionText, userAnswer: input.value.trim(), reveal: reveal }); }
      logAttempt({ lessonId: lessonId, groupId: scoreBox ? scoreBox.dataset.group : 'default', questionIndex: globalIndex, questionText: questionText, userAnswer: input.value.trim(), correct: correct });
      maybeShowReport();
    }
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') check(); });
    if (checkBtn) checkBtn.addEventListener('click', check);
  });
})();
</script>
</body>
</html>
"""


def cover(level_tag, word_count, sub):
    return f"""<!-- ① COVER -->
<div class="slide slide-cover">
  <div class="sidebar" style="background:#2d241f;justify-content:center;align-items:center;min-height:300px;">
    <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:38px;height:38px;">
      <path d="M8 8 Q16 4 24 8 L22 24 Q16 28 10 24 Z" stroke="rgba(255,255,255,0.9)" stroke-width="1.5" fill="none"/>
      <path d="M10 12 Q16 14 22 12" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" fill="none"/>
      <line x1="12" y1="8" x2="12" y2="5" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="20" y1="8" x2="20" y2="5" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="cover-content">
    <div class="cover-scene">
      <svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
        <circle cx="580" cy="70" r="35" fill="white" opacity="0.1"/>
        <circle cx="120" cy="220" r="45" fill="white" opacity="0.08"/>
        <ellipse cx="350" cy="260" rx="180" ry="30" fill="white" opacity="0.05"/>
        <rect x="450" y="80" width="70" height="110" rx="6" fill="white" opacity="0.12"/>
        <rect x="460" y="95" width="50" height="8" rx="2" fill="white" opacity="0.2"/>
        <rect x="460" y="110" width="50" height="8" rx="2" fill="white" opacity="0.2"/>
        <rect x="460" y="125" width="30" height="8" rx="2" fill="white" opacity="0.2"/>
        <rect x="180" y="100" width="90" height="120" rx="8" fill="white" opacity="0.1"/>
        <rect x="195" y="120" width="60" height="10" rx="2" fill="white" opacity="0.15"/>
        <rect x="195" y="140" width="60" height="10" rx="2" fill="white" opacity="0.15"/>
        <rect x="195" y="170" width="60" height="30" rx="2" fill="white" opacity="0.12"/>
        <circle cx="600" cy="200" r="25" fill="white" opacity="0.08"/>
      </svg>
    </div>
    <div class="cover-eyebrow">Ordering Coffee · 点咖啡 · {level_tag}</div>
    <div class="cover-zh">点咖啡</div>
    <div class="cover-py">diǎn kāfēi</div>
    <div class="cover-en">Ordering Coffee</div>
    <div class="cover-tags">
      <span class="tag">{level_tag}</span>
      <span class="tag">{word_count} new words</span>
      <span class="tag">Luckin Coffee</span>
    </div>
  </div>
</div>"""


def slide(num, total, label, sidebar_class="", done=None, active=None):
    if done is None: done = num - 1
    if active is None: active = num
    dots = []
    for i in range(1, total + 1):
        if i <= done: dots.append('<div class="dot done"></div>')
        elif i == active: dots.append('<div class="dot active"></div>')
        else: dots.append('<div class="dot"></div>')
    return f"""<!-- {num} -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar {sidebar_class}">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 14 L12 20 L22 8" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="sb-label">{label}</div>
    </div>
    <div class="sb-prog">{''.join(dots)}</div>
  </div>
  <div class="content">"""


def end_slide(): return "  </div>\n</div>"


def grammar_strip(parts, en):
    items = []
    for p in parts:
        if len(p) == 3:
            zh, py, cls = p
            items.append(f'<div class="gs-part colored {cls}"><div class="gs-zh">{zh}</div><div class="gs-py">{py}</div></div>')
        else:
            zh, py = p
            items.append(f'<div class="gs-part"><div class="gs-plain-zh">{zh}</div><div class="gs-plain-py">{py}</div></div>')
    return f'<div class="grammar-strip">{"".join(items)}<div class="gs-en">{en}</div></div>'


def ex(zh, py, en, cls=""):
    return f'<div class="ex {cls}"><div class="ex-zh">{zh}</div><div class="ex-py">{py}</div><div class="ex-en">{en}</div></div>'


def vc(zh, py, en, cat="drink"):
    return f'<div class="vc cat-{cat}"><div class="vc-zh">{zh}</div><div class="vc-py">{py}</div><div class="vc-en">{en}</div></div>'


def bubble(who, role, zh, py, en):
    side = "bubble-a" if who == "a" else "bubble-b"
    avatar = "店" if who == "a" else "我"
    avcls = "avatar-a" if who == "a" else "avatar-b"
    return f'<div class="bubble {side}"><div class="bubble-avatar {avcls}">{avatar}</div><div class="bubble-content"><div class="bubble-role">{role}</div><div class="bubble-text"><div class="bubble-zh">{zh}</div><div class="bubble-py">{py}</div><div class="bubble-en">{en}</div></div></div></div>'


def quiz_score(group, total):
    return f'<div class="quiz-score" data-quiz-score data-group="{group}" data-total="{total}">✅ <span class="score-correct">0</span>/<span class="score-total">{total}</span> <span class="stars">★</span></div>'


def phone_block(img, alt, callout, qzh, qpy, ans, reveal):
    c = f'<div class="quiz-callout" style="{callout}"></div>' if callout else ''
    return f'<div class="phone-block"><div class="phone-mock"><img src="{SCREEN_BASE}/{img}" alt="{alt}"/>{c}</div><div class="quiz-q">{qzh}<span class="py">{qpy}</span></div><div class="quiz-game"><div class="quiz-row"><input type="text" class="quiz-input" placeholder="打字猜猜看…" data-answer="{ans}" data-reveal="{reveal}"/><button type="button" class="quiz-check-btn">检查</button></div><div class="quiz-feedback"></div></div></div>'


def learn_slide(num, total, title, title_py, tip, phones):
    phone_html = '\n'.join([f'<div class="phone-block"><div class="phone-mock"><img src="{SCREEN_BASE}/{img}" alt="{alt}"/></div><div class="phone-step">{label} <span style="color:var(--ink-3);font-weight:400;">{label_py}</span></div></div>' for img, alt, label, label_py in phones])
    return slide(num, total, f"learn {num-6}/{total-6}", "gold") + f'<div class="learn-badge">Learn · 学习</div><div class="sec-label">How It Really Works · 手机点单</div><h2>{title} <span class="py-inline">{title_py}</span></h2><div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Reality check:</strong> {tip}</div><div class="phone-row">{phone_html}</div>' + end_slide()


def test_slide(num, total, title, title_py, group, total_q, questions):
    qhtml = '\n'.join([phone_block(*q) for q in questions])
    return slide(num, total, f"test {num-7}/{total-7}", "rust") + f'<div class="test-badge">Test · 小测验</div><div class="sec-label">Interface Check · 看懂界面</div><h2>{title} <span class="py-inline">{title_py}</span></h2>{quiz_score(group, total_q)}<div class="tip" style="margin-top:0;margin-bottom:1rem;"><strong>Type your answer:</strong> Chinese, pinyin, or English. Hit Enter or tap 检查.</div><div class="phone-row">{qhtml}</div>' + end_slide()


def report_slide(total_dots):
    dots = '<div class="dot done"></div>' * (total_dots - 1) + '<div class="dot active"></div>'
    return f"""<!-- REPORT -->
<div class="slide" id="lesson-report-slide" style="grid-template-columns:64px 1fr; display:none;">
  <div class="sidebar dark">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5 21 L5 13 M12 21 L12 8 M19 21 L19 16 M23 21 L23 11" stroke="rgba(255,255,255,0.9)" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
      <div class="sb-label">your report</div>
    </div>
    <div class="sb-prog">{dots}</div>
  </div>
  <div class="content">
    <div class="sec-label">Lesson Report · 学习报告</div>
    <h2>你的学习报告 <span class="py-inline">Nǐ de xuéxí bàogào.</span></h2>
    <div id="report-score" class="report-score"></div>
    <div id="report-groups" class="report-groups"></div>
    <div id="report-missed"></div>
  </div>
</div>"""


def review_slide(phrases, cap_small="choose your drink, size, and temperature"):
    grid = '\n'.join([f'<div class="ex" style="margin:0;"><div class="ex-zh">{zh}</div><div class="ex-py">{py}</div></div>' for zh, py in phrases])
    return f"""<!-- REVIEW -->
<div class="slide" style="grid-template-columns:64px 1fr">
  <div class="sidebar dark">
    <div class="sb-icon">
      <svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="14,4 17,11 24,11 18,16 20,23 14,19 8,23 10,16 4,11 11,11" stroke="rgba(255,255,255,0.85)" stroke-width="1.5" fill="none" stroke-linejoin="round"/>
      </svg>
      <div class="sb-label">review</div>
    </div>
    <div class="sb-prog">{ '<div class="dot done"></div>' * 14 }</div>
  </div>
  <div class="content">
    <div class="sec-label">Review · 复习</div>
    <h2>Useful phrases <span class="py-inline">chángyòng yǔjù</span></h2>
    <div class="photo-wide">
      <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=900&q=72" alt="coffee beans" onerror="this.style.display='none'"/>
      <div class="photo-cap">咖啡 kāfēi<small>{cap_small}</small></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;">
{grid}
    </div>
  </div>
</div>"""


def closing(level_tag):
    return f"""<!-- CLOSING -->
<div class="slide slide-close">
  <div class="close-inner">
    <div class="close-zh">谢谢</div>
    <div class="close-detail">
      <div class="py">Xièxie</div>
      <div class="en">Enjoy your coffee with Xinhan Chinese</div>
      <div class="sub">{level_tag} · Ordering Coffee</div>
    </div>
  </div>
</div>"""


LEVELS = {
    "hsk-1": {
        "tag": "HSK 1",
        "words": "8",
        "body_id": "hsk-1/luckin-coffee",
        "warm": {
            "h2": "你喝咖啡吗？ <span class=\"py-inline\">Nǐ hē kāfēi ma?</span>",
            "scene_text": "我喝 ______（咖啡 / 茶 / 水）。",
            "scene_py": "Wǒ hē ___ (kāfēi / chá / shuǐ).",
            "chips1": [("咖啡", "coffee"), ("茶", "tea"), ("水", "water"), ("牛奶", "milk")],
            "chips2": [("热", "hot"), ("冰", "iced")],
            "tip": "Say what you drink — 我喝咖啡 (Wǒ hē kāfēi).",
        },
        "vocab": [
            ("咖啡", "kāfēi", "coffee", "drink"), ("茶", "chá", "tea", "drink"),
            ("水", "shuǐ", "water", "drink"), ("牛奶", "niúnǎi", "milk", "drink"),
            ("热", "rè", "hot", "temp"), ("冰", "bīng", "iced", "temp"),
            ("大", "dà", "big", "size"), ("小", "xiǎo", "small", "size"),
        ],
        "g1": {"strip": [("我要", "wǒ yào", ""), ("咖啡", "kāfēi", "")], "en": "I want coffee.",
               "ex": [("<span class=\"key\">我要</span>咖啡。", "Wǒ yào kāfēi.", "I want coffee."),
                      ("<span class=\"key\">我要</span>茶。", "Wǒ yào chá.", "I want tea."),
                      ("<span class=\"key\">我要</span>水。", "Wǒ yào shuǐ.", "I want water.")]},
        "g2": {"strip": [("热", "rè", "rust"), ("还是", "háishi", ""), ("冰？", "bīng?", "")], "en": "Hot or iced?",
               "ex": [("你要<span class=\"key-r\">热的</span>还是<span class=\"key-r\">冰的</span>？", "Nǐ yào rè de háishi bīng de?", "Do you want hot or iced?", "rust"),
                      ("我要<span class=\"key-r\">热的</span>。", "Wǒ yào rè de.", "I want hot.", "rust"),
                      ("我要<span class=\"key-r\">冰的</span>。", "Wǒ yào bīng de.", "I want iced.", "rust")]},
        "g3": {"strip": [("大杯", "dà bēi", "sky"), ("还是", "háishi", ""), ("小杯？", "xiǎo bēi?", "")], "en": "Big cup or small cup?",
               "ex": [("你要<span class=\"key-s\">大杯</span>还是<span class=\"key-s\">小杯</span>？", "Nǐ yào dà bēi háishi xiǎo bēi?", "Big cup or small cup?", "sky"),
                      ("我要<span class=\"key-s\">大杯</span>。", "Wǒ yào dà bēi.", "I want a big cup.", "sky"),
                      ("我要<span class=\"key-s\">小杯</span>。", "Wǒ yào xiǎo bēi.", "I want a small cup.", "sky")]},
        "dialogue": {"h2": "在咖啡店 <span class=\"py-inline\">zài kāfēi diàn</span>",
                     "bubbles": [
                         ("a", "Staff · 店员", "你好！你要什么？", "Nǐ hǎo! Nǐ yào shénme?", "Hello! What do you want?"),
                         ("b", "Me · 我", "我要咖啡。", "Wǒ yào kāfēi.", "I want coffee."),
                         ("a", "Staff · 店员", "大杯还是小杯？", "Dà bēi háishi xiǎo bēi?", "Big cup or small cup?"),
                         ("b", "Me · 我", "大杯。热的。", "Dà bēi. Rè de.", "Big cup. Hot.")]},
        "learns": [
            ("打开 APP", "Dǎkāi APP.", "first you open the app, then you log in.", [("shot-login.jpg", "login", "登录", "dēnglù · log in")]),
            ("选咖啡", "Xuǎn kāfēi.", "you choose the drink, then you choose hot or iced, big or small.", [("shot-customize.jpg", "customize", "选大小 / 冷热", "size / temperature"), ("shot-sugar-milk.jpg", "sugar", "糖 / 奶", "sugar / milk")]),
            ("付钱、取餐", "Fùqián, qǔcān.", "you pay on the phone, then you get a number.", [("shot-confirm.jpg", "confirm", "确认订单", "quèrèn dìngdān · confirm"), ("shot-done.jpg", "done", "取餐号", "qǔcānhào · pickup number")]),
        ],
        "tests": [
            ("这个画面做什么？", "Zhège huàmiàn zuò shénme?", "group-1", 3, [
                ("shot-login.jpg", "login quiz", "top:57%;left:10%;width:78%;height:5%;", "哪个按钮可以登录？", "Nǎge ànniǔ kěyǐ dēnglù?", "手机号安全登录|shouji hao anquan denglu|log in|login", "手机号安全登录 <span class=\"py\">shǒujīhào ānquán dēnglù · log in</span>"),
                ("shot-menu.jpg", "menu quiz", "top:19.5%;left:64%;width:31%;height:4%;", "常点的咖啡在哪里？", "Chángdiǎn de kāfēi zài nǎlǐ?", "我的常点|wo de chang dian|frequent orders", "我的常点 <span class=\"py\">wǒ de chángdiǎn · frequent orders</span>"),
                ("shot-home-services.jpg", "services quiz", "top:33%;left:6%;width:28%;height:8%;", "自己去店里拿，点哪个？", "Zìjǐ qù diàn lǐ ná, diǎn nǎge?", "到店取|dao dian qu|pickup|pick up", "到店取 <span class=\"py\">dàodiàn qǔ · pick up in store</span>"),
            ]),
            ("选大小和冷热", "Xuǎn dàxiǎo hé lěngrè.", "group-2", 3, [
                ("shot-customize.jpg", "size quiz", "top:40%;left:33%;width:48%;height:6%;", "更大的杯是哪个？", "Gèng dà de bēi shì nǎge?", "特大杯|te da bei|big cup|large", "特大杯 <span class=\"py\">tè dà bēi · extra-large cup</span>"),
                ("shot-sugar-milk.jpg", "sugar quiz", "top:12%;left:28%;width:38%;height:5%;", "不想加糖，点哪个？", "Bù xiǎng jiā táng, diǎn nǎge?", "不另外加糖|bu lingwai jia tang|no sugar", "不另外加糖 <span class=\"py\">bù lìngwài jiā táng · no extra sugar</span>"),
                ("shot-customize.jpg", "temp quiz", "top:55%;left:10%;width:80%;height:6%;", "想要热的，点哪个？", "Xiǎng yào rè de, diǎn nǎge?", "热|rè|hot", "热 <span class=\"py\">rè · hot</span>"),
            ]),
            ("最后两步", "Zuìhòu liǎng bù.", "group-3", 3, [
                ("shot-confirm.jpg", "pay quiz", "top:91%;left:60%;width:37%;height:6%;", "不用密码付款，点哪个？", "Bù yòng mìmǎ fùkuǎn, diǎn nǎge?", "免密支付|mianmi zhifu|pay without password", "免密支付 <span class=\"py\">miǎnmì zhīfù · pay without password</span>"),
                ("shot-done.jpg", "again quiz", "top:19%;left:49%;width:43%;height:6%;", "再买一次一样的，点哪个？", "Zài mǎi yī cì yīyàng de, diǎn nǎge?", "再来一单|zai lai yi dan|order again", "再来一单 <span class=\"py\">zài lái yì dān · order again</span>"),
                ("shot-store-map.jpg", "store quiz", "top:9%;left:8%;width:84%;height:6%;", "换一家店，点哪个？", "Huàn yī jiā diàn, diǎn nǎge?", "选择门店|xuanze mendian|choose store", "选择门店 <span class=\"py\">xuǎnzé méndiàn · choose a store</span>"),
            ]),
        ],
        "final": ("综合挑战", "Zōnghé tiǎozhàn.", "final", 3, [
            ("shot-login.jpg", "final login", "", "这个画面做什么？", "Zhège huàmiàn zuò shénme?", "登录|denglu|log in|sign in", "登录 <span class=\"py\">dēnglù · log in</span>"),
            ("shot-customize.jpg", "final customize", "", "这个画面做什么？", "Zhège huàmiàn zuò shénme?", "选规格|xuan guige|customize|choose size", "选规格 <span class=\"py\">xuǎn guīgé · choose specs</span>"),
            ("shot-done.jpg", "final done", "", "这个画面做什么？", "Zhège huàmiàn zuò shénme?", "取餐|qucan|pick up|pickup", "取餐 / 再来一单 <span class=\"py\">qǔcān · pick up</span>"),
        ]),
        "review": [("我要咖啡。", "Wǒ yào kāfēi."), ("热的还是冰的？", "Rè de háishi bīng de?"),
                   ("大杯还是小杯？", "Dà bēi háishi xiǎo bēi?"), ("我要热的。", "Wǒ yào rè de.")],
        "group_names": {
            "group-1": "Log In & Find · 登录寻找",
            "group-2": "Size & Temperature · 大小冷热",
            "group-3": "Pay & Pick Up · 付款取餐",
            "final": "Final Test · 综合挑战",
        },
    },
    "hsk-2": {
        "tag": "HSK 2",
        "words": "12",
        "body_id": "hsk-2/luckin-coffee",
        "warm": {
            "h2": "你喜欢喝什么？ <span class=\"py-inline\">Nǐ xǐhuan hē shénme?</span>",
            "scene_text": "我喜欢喝 ______（热/冰）的 ______。",
            "scene_py": "Wǒ xǐhuan hē ___ (rè/bīng) de ___.",
            "chips1": [("咖啡", "coffee"), ("拿铁", "latte"), ("美式", "americano"), ("茶", "tea")],
            "chips2": [("热", "hot"), ("冰", "iced"), ("常温", "room temp")],
            "tip": "Tell your partner what you like and whether you prefer it hot or iced.",
        },
        "vocab": [
            ("咖啡", "kāfēi", "coffee", "drink"), ("拿铁", "nátiě", "latte", "drink"),
            ("美式", "měishì", "americano", "drink"), ("茶", "chá", "tea", "drink"),
            ("热", "rè", "hot", "temp"), ("冰", "bīng", "iced", "temp"),
            ("常温", "chángwēn", "room temp", "temp"), ("大杯", "dàbēi", "large", "size"),
            ("小杯", "xiǎobēi", "small", "size"), ("糖", "táng", "sugar", "drink"),
            ("还是", "háishi", "or", "action"), ("多少钱", "duōshao qián", "how much", "action"),
        ],
        "g1": {"strip": [("我要", "wǒ yào", ""), ("一杯", "yì bēi", ""), ("拿铁", "nátiě", "")], "en": "I'd like a latte.",
               "ex": [("<span class=\"key\">我要</span>一杯<span class=\"key\">拿铁</span>。", "Wǒ yào yì bēi nátiě.", "I'd like a latte."),
                      ("<span class=\"key\">我要</span>一杯<span class=\"key\">美式</span>。", "Wǒ yào yì bēi měishì.", "I'd like an americano."),
                      ("<span class=\"key\">我要</span>一杯<span class=\"key\">茶</span>。", "Wǒ yào yì bēi chá.", "I'd like a tea.")]},
        "g2": {"strip": [("大杯", "dàbēi", "rust"), ("还是", "háishi", ""), ("小杯？", "xiǎobēi?", "")], "en": "Large or small?",
               "ex": [("你要<span class=\"key-r\">大杯</span>还是<span class=\"key-r\">小杯</span>？", "Nǐ yào dàbēi háishi xiǎobēi?", "Large or small?", "rust"),
                      ("你要<span class=\"key-r\">热的</span>还是<span class=\"key-r\">冰的</span>？", "Nǐ yào rè de háishi bīng de?", "Hot or iced?", "rust"),
                      ("<span class=\"key-r\">大杯</span>，<span class=\"key-r\">冰的</span>。", "Dàbēi, bīng de.", "Large, iced.", "rust")]},
        "g3": {"strip": [("加", "jiā", "sky"), ("不", "bu", ""), ("加糖？", "jiā táng?", "")], "en": "With or without sugar?",
               "ex": [("你<span class=\"key-s\">加不加</span>糖？", "Nǐ jiā bu jiā táng?", "Do you want sugar?", "sky"),
                      ("我要<span class=\"key-s\">牛奶</span>。", "Wǒ yào niúnǎi.", "I want milk.", "sky"),
                      ("<span class=\"key-s\">不另外加糖</span>。", "Bù lìngwài jiā táng.", "No extra sugar.", "sky")]},
        "dialogue": {"h2": "在瑞幸点咖啡 <span class=\"py-inline\">zài Ruìxìng diǎn kāfēi</span>",
                     "bubbles": [
                         ("a", "Staff · 店员", "您好，请问您要喝什么？", "Nín hǎo, qǐngwèn nín yào hē shénme?", "Hello, what would you like to drink?"),
                         ("b", "Me · 我", "我要一杯拿铁。", "Wǒ yào yì bēi nátiě.", "I'd like a latte."),
                         ("a", "Staff · 店员", "大杯还是小杯？热的还是冰的？", "Dàbēi háishi xiǎobēi? Rè de háishi bīng de?", "Large or small? Hot or iced?"),
                         ("b", "Me · 我", "大杯，冰的。不另外加糖。", "Dàbēi, bīng de. Bù lìngwài jiā táng.", "Large, iced. No extra sugar.")]},
        "learns": [
            ("打开 APP，领优惠券", "Dǎkāi APP, lǐng yōuhuìquàn.", "first open the app, then claim your coupon.", [("shot-login.jpg", "login", "登录", "dēnglù · log in"), ("shot-coupon.jpg", "coupon", "优惠券", "yōuhuìquàn · coupon")]),
            ("选咖啡、选规格", "Xuǎn kāfēi, xuǎn guīgé.", "choose the drink, size, temperature, and sugar level.", [("shot-menu.jpg", "menu", "经典菜单", "jīngdiǎn càidān · classic menu"), ("shot-customize.jpg", "customize", "杯型 / 温度", "size / temperature")]),
            ("付钱、取餐", "Fùqián, qǔcān.", "pay on the phone, then wait for your pickup number.", [("shot-confirm.jpg", "confirm", "确认订单", "quèrèn dìngdān · confirm"), ("shot-done.jpg", "done", "取餐号", "qǔcānhào · pickup number")]),
        ],
        "tests": [
            ("登录和优惠", "Dēnglù hé yōuhuì.", "group-1", 3, [
                ("shot-login.jpg", "login quiz", "top:57%;left:10%;width:78%;height:5%;", "哪个按钮可以登录账号？", "Nǎge ànniǔ kěyǐ dēnglù zhànghào?", "手机号安全登录|shouji hao anquan denglu|log in|login", "手机号安全登录 <span class=\"py\">shǒujīhào ānquán dēnglù · log in</span>"),
                ("shot-coupon.jpg", "coupon quiz", "top:14%;left:5%;width:88%;height:10%;", "这是什么？每周可以领一次。", "Zhè shì shénme? Měi zhōu kěyǐ lǐng yí cì.", "专享券|zhuanxiang quan|exclusive coupon|coupon", "专享券 <span class=\"py\">zhuānxiǎngquàn · exclusive coupon</span>"),
                ("shot-home-services.jpg", "services quiz", "top:33%;left:6%;width:28%;height:8%;", "想自己到店拿咖啡，点哪个？", "Xiǎng zìjǐ dàodiàn ná kāfēi, diǎn nǎge?", "到店取|dao dian qu|pick up in store|pickup", "到店取 <span class=\"py\">dàodiàn qǔ · pick up in store</span>"),
            ]),
            ("选规格", "Xuǎn guīgé.", "group-2", 3, [
                ("shot-menu.jpg", "menu quiz", "top:19.5%;left:64%;width:31%;height:4%;", "哪个标签可以看到常点的咖啡？", "Nǎge biāoqiān kěyǐ kàndào chángdiǎn de kāfēi?", "我的常点|wo de chang dian|my frequent orders|frequent orders", "我的常点 <span class=\"py\">wǒ de chángdiǎn · my frequent orders</span>"),
                ("shot-customize.jpg", "size quiz", "top:40%;left:33%;width:48%;height:6%;", "想要更大杯，应该点哪个？", "Xiǎng yào gèng dà bēi, yīnggāi diǎn nǎge?", "特大杯|te da bei|extra-large cup|extra large", "特大杯 <span class=\"py\">tè dà bēi · extra-large cup</span>"),
                ("shot-sugar-milk.jpg", "sugar quiz", "top:12%;left:28%;width:38%;height:5%;", "不想加糖，应该点哪个？", "Bù xiǎng jiā táng, yīnggāi diǎn nǎge?", "不另外加糖|bu lingwai jia tang|no extra sugar|no sugar", "不另外加糖 <span class=\"py\">bù lìngwài jiā táng · no extra sugar</span>"),
            ]),
            ("付款和取餐", "Fùkuǎn hé qǔcān.", "group-3", 3, [
                ("shot-confirm.jpg", "pay quiz", "top:91%;left:60%;width:37%;height:6%;", "想要免密码付款，应该点哪个？", "Xiǎng yào miǎn mìmǎ fùkuǎn, yīnggāi diǎn nǎge?", "免密支付|mianmi zhifu|pay without password", "免密支付 <span class=\"py\">miǎnmì zhīfù · pay without password</span>"),
                ("shot-done.jpg", "again quiz", "top:19%;left:49%;width:43%;height:6%;", "想再买一次一样的，应该点哪个？", "Xiǎng zài mǎi yí cì yíyàng de, yīnggāi diǎn nǎge?", "再来一单|zai lai yi dan|order again", "再来一单 <span class=\"py\">zài lái yì dān · order again</span>"),
                ("shot-store-map.jpg", "store quiz", "top:9%;left:8%;width:84%;height:6%;", "你要换一家店取咖啡，应该点哪个？", "Nǐ yào huàn yī jiā diàn qǔ kāfēi, yīnggāi diǎn nǎge?", "选择门店|xuanze mendian|choose a store|choose store", "选择门店 <span class=\"py\">xuǎnzé méndiàn · choose a store</span>"),
            ]),
        ],
        "final": ("综合挑战", "Zōnghé tiǎozhàn.", "final", 3, [
            ("shot-login.jpg", "final login", "", "这个画面要做什么？", "Zhège huàmiàn yào zuò shénme?", "登录|denglu|log in|sign in", "登录 <span class=\"py\">dēnglù · log in</span>"),
            ("shot-home-services.jpg", "final services", "", "这个画面主要可以做什么？", "Zhège huàmiàn zhǔyào kěyǐ zuò shénme?", "选到店取或送货|choose pickup or delivery|pickup or delivery", "选到店取或送货 <span class=\"py\">xuǎn dàodiàn qǔ huò sònghuò · choose pickup or delivery</span>"),
            ("shot-confirm.jpg", "final confirm", "", "这是哪个步骤？", "Zhè shì nǎge bùzhòu?", "确认订单|queren dingdan|confirm order|confirm and pay", "确认订单并付款 <span class=\"py\">quèrèn dìngdān bìng fùkuǎn · confirm and pay</span>"),
        ]),
        "review": [("我要一杯拿铁。", "Wǒ yào yì bēi nátiě."), ("大杯还是小杯？", "Dàbēi háishi xiǎobēi?"),
                   ("热的还是冰的？", "Rè de háishi bīng de?"), ("加不加糖？", "Jiā bu jiā táng?"),
                   ("我要自提。", "Wǒ yào zìtí."), ("多少钱？", "Duōshao qián?")],
        "group_names": {
            "group-1": "Sign-in & Promos · 登录优惠",
            "group-2": "Customize Order · 客制化",
            "group-3": "Checkout & Pickup · 付款取餐",
            "final": "Final Test · 综合挑战",
        },
    },
}


LEVELS.update({
    "hsk-4": {
        "tag": "HSK 4",
        "words": "18",
        "body_id": "hsk-4/luckin-coffee",
        "warm": {
            "h2": "你平时怎么点咖啡？ <span class=\"py-inline\">Nǐ píngshí zěnme diǎn kāfēi?</span>",
            "scene_text": "我______用手机点，因为______方便又便宜。",
            "scene_py": "Wǒ ___ yòng shǒujī diǎn, yīnwèi ___ fāngbiàn yòu piányi.",
            "chips1": [("手机", "phone"), ("APP", "app"), ("小程序", "mini app"), ("店里", "in store")],
            "chips2": [("方便", "convenient"), ("便宜", "cheap"), ("快", "fast"), ("省事", "hassle-free")],
            "tip": "Discuss how you usually order coffee and why.",
        },
        "vocab": [
            ("生椰拿铁", "shēngyē nátiě", "coconut latte", "drink"), ("标准美式", "biāozhǔn měishì", "standard americano", "drink"),
            ("燕麦奶", "yànmài nǎi", "oat milk", "drink"), ("优惠券", "yōuhuìquàn", "coupon", "action"),
            ("加入购物车", "jiārù gòuwùchē", "add to cart", "action"), ("立即购买", "lìjí gòumǎi", "buy now", "action"),
            ("自提", "zìtí", "self-pickup", "action"), ("配送", "pèisòng", "delivery", "action"),
            ("会员", "huìyuán", "member", "action"), ("积分", "jīfēn", "points", "action"),
            ("打折", "dǎzhé", "discount", "action"), ("订单", "dìngdān", "order", "action"),
            ("不但", "bùdàn", "not only", "action"), ("而且", "érqiě", "but also", "action"),
            ("虽然", "suīrán", "although", "action"), ("但是", "dànshì", "but", "action"),
            ("被", "bèi", "by (passive)", "action"), ("如果", "rúguǒ", "if", "action"),
        ],
        "g1": {"strip": [("不但", "bùdàn", ""), ("方便", "fāngbiàn", ""), ("而且", "érqiě", ""), ("便宜", "piányi", "")], "en": "Not only convenient, but also cheap.",
               "ex": [("手机点单<span class=\"key\">不但</span>方便，<span class=\"key\">而且</span>便宜。", "Shǒujī diǎndān bùdàn fāngbiàn, érqiě piányi.", "Ordering by phone is not only convenient, but also cheap.", ""),
                      ("这杯咖啡<span class=\"key\">不但</span>好喝，<span class=\"key\">而且</span>很大。", "Zhè bēi kāfēi bùdàn hǎo hē, érqiě hěn dà.", "This coffee is not only tasty, but also large.", "")]},
        "g2": {"strip": [("虽然", "suīrán", "rust"), ("贵", "guì", ""), ("但是", "dànshì", ""), ("好喝", "hǎohē", "")], "en": "Although it's expensive, it tastes good.",
               "ex": [("<span class=\"key-r\">虽然</span>这杯咖啡很贵，<span class=\"key-r\">但是</span>很好喝。", "Suīrán zhè bēi kāfēi hěn guì, dànshì hěn hǎo hē.", "Although this coffee is expensive, it tastes good.", "rust"),
                      ("<span class=\"key-r\">虽然</span>店里人多，<span class=\"key-r\">但是</span>很快。", "Suīrán diàn lǐ rén duō, dànshì hěn kuài.", "Although the shop is crowded, it's fast.", "rust")]},
        "g3": {"strip": [("咖啡", "kāfēi", "sky"), ("被", "bèi", ""), ("喝完", "hē wán", "")], "en": "The coffee was finished (by someone).",
               "ex": [("我的咖啡<span class=\"key-s\">被</span>朋友喝完了。", "Wǒ de kāfēi bèi péngyou hē wán le.", "My coffee was finished by my friend.", "sky"),
                      ("订单<span class=\"key-s\">被</span>取消了。", "Dìngdān bèi qǔxiāo le.", "The order was cancelled.", "sky")]},
        "dialogue": {"h2": "在瑞幸点单 <span class=\"py-inline\">zài Ruìxìng diǎndān</span>",
                     "bubbles": [
                         ("a", "Staff · 店员", "您好，想喝点什么？我们今天的生椰拿铁有优惠。", "Nín hǎo, xiǎng hē diǎn shénme? Wǒmen jīntiān de shēngyē nátiě yǒu yōuhuì.", "Hello, what would you like? Our coconut latte is on sale today."),
                         ("b", "Me · 我", "我要一杯生椰拿铁，大杯冰的，换燕麦奶。", "Wǒ yào yì bēi shēngyē nátiě, dàbēi bīng de, huàn yànmài nǎi.", "I'd like a coconut latte, large iced, with oat milk."),
                         ("a", "Staff · 店员", "好的。您有会员卡吗？会员可以打折。", "Hǎo de. Nín yǒu huìyuán kǎ ma? Huìyuán kěyǐ dǎzhé.", "Sure. Do you have a membership? Members get a discount."),
                         ("b", "Me · 我", "有。虽然我喜欢在店里喝，但是今天太忙，所以选自提。", "Yǒu. Suīrán wǒ xǐhuan zài diàn lǐ hē, dànshì jīntiān tài máng, suǒyǐ xuǎn zìtí.", "Yes. Although I like drinking in-store, I'm too busy today, so I'll choose self-pickup.")]},
        "learns": [
            ("登录并领取优惠券", "Dēnglù bìng lǐngqǔ yōuhuìquàn.", "you sign in once and claim weekly coupons before ordering.", [("shot-login.jpg", "login", "手机号登录", "shǒujīhào dēnglù · phone login"), ("shot-coupon.jpg", "coupon", "领券", "lǐng quàn · claim coupon")]),
            ("浏览菜单并加入购物车", "Liúlǎn càidān bìng jiārù gòuwùchē.", "you browse the menu, compare prices, and add drinks to the cart.", [("shot-menu.jpg", "menu", "经典菜单", "jīngdiǎn càidān · classic menu"), ("shot-member-menu.jpg", "member menu", "会员菜单", "huìyuán càidān · member menu")]),
            ("确认订单并付款", "Quèrèn dìngdān bìng fùkuǎn.", "you review the order, apply coupons, and pay with one tap.", [("shot-customize.jpg", "customize", "客制化", "kèzhìhuà · customize"), ("shot-confirm.jpg", "confirm", "确认订单", "quèrèn dìngdān · confirm order")]),
        ],
        "tests": [
            ("登录和优惠券", "Dēnglù hé yōuhuìquàn.", "group-1", 3, [
                ("shot-login.jpg", "login quiz", "top:57%;left:10%;width:78%;height:5%;", "用什么方式登录最方便？", "Yòng shénme fāngshì dēnglù zuì fāngbiàn?", "手机号安全登录|shouji hao anquan denglu|phone number|phone", "手机号安全登录 <span class=\"py\">shǒujīhào ānquán dēnglù · log in with phone number</span>"),
                ("shot-coupon.jpg", "coupon quiz", "top:14%;left:5%;width:88%;height:10%;", "每周可以领一次的券叫什么？", "Měi zhōu kěyǐ lǐng yí cì de quàn jiào shénme?", "专享券|zhuanxiang quan|exclusive coupon|weekly coupon", "专享券 <span class=\"py\">zhuānxiǎngquàn · exclusive coupon</span>"),
                ("shot-home-services.jpg", "services quiz", "top:33%;left:6%;width:28%;height:8%;", "不想等快递，自己去店里拿选哪个？", "Bù xiǎng děng kuàidì, zìjǐ qù diàn lǐ ná xuǎn nǎge?", "到店取|dao dian qu|pick up in store|pickup", "到店取 <span class=\"py\">dàodiàn qǔ · pick up in store</span>"),
            ]),
            ("浏览和客制化", "Liúlǎn hé kèzhìhuà.", "group-2", 3, [
                ("shot-menu.jpg", "menu quiz", "top:19.5%;left:64%;width:31%;height:4%;", "哪个标签能看到你常点的咖啡？", "Nǎge biāoqiān néng kàndào nǐ chángdiǎn de kāfēi?", "我的常点|wo de chang dian|my frequent orders|frequent", "我的常点 <span class=\"py\">wǒ de chángdiǎn · my frequent orders</span>"),
                ("shot-customize.jpg", "size quiz", "top:40%;left:33%;width:48%;height:6%;", "想要最大杯，应该选哪个？", "Xiǎng yào zuì dà bēi, yīnggāi xuǎn nǎge?", "特大杯|te da bei|extra large|extra-large", "特大杯 <span class=\"py\">tè dà bēi · extra-large cup</span>"),
                ("shot-sugar-milk.jpg", "milk quiz", "top:55%;left:10%;width:80%;height:6%;", "不想用普通牛奶，可以换什么奶？", "Bù xiǎng yòng pǔtōng niúnǎi, kěyǐ huàn shénme nǎi?", "燕麦奶|yanmai nai|oat milk", "燕麦奶 <span class=\"py\">yànmài nǎi · oat milk</span>"),
            ]),
            ("下单和付款", "Xiàdān hé fùkuǎn.", "group-3", 3, [
                ("shot-confirm.jpg", "pay quiz", "top:91%;left:60%;width:37%;height:6%;", "不用输密码就能付款的功能叫什么？", "Bù yòng shū mìmǎ jiù néng fùkuǎn de gōngnéng jiào shénme?", "免密支付|mianmi zhifu|pay without password", "免密支付 <span class=\"py\">miǎnmì zhīfù · pay without password</span>"),
                ("shot-done.jpg", "again quiz", "top:19%;left:49%;width:43%;height:6%;", "想快速重复上次的订单，点哪个按钮？", "Xiǎng kuàisù chóngfù shàngcì de dìngdān, diǎn nǎge ànniǔ?", "再来一单|zai lai yi dan|order again", "再来一单 <span class=\"py\">zài lái yì dān · order again</span>"),
                ("shot-member-card.jpg", "member quiz", "top:47%;left:5%;width:60%;height:18%;", "只有会员才能享受的价格叫什么？", "Zhǐyǒu huìyuán cái néng xiǎngshòu de jiàgé jiào shénme?", "会员价|huiyuan jia|members-only price|member price", "会员价 <span class=\"py\">huìyuán jià · members-only price</span>"),
            ]),
        ],
        "final": ("综合挑战", "Zōnghé tiǎozhàn.", "final", 3, [
            ("shot-login.jpg", "final login", "", "这个画面的主要功能是什么？", "Zhège huàmiàn de zhǔyào gōngnéng shì shénme?", "登录|denglu|log in|sign in", "登录 <span class=\"py\">dēnglù · log in</span>"),
            ("shot-customize.jpg", "final customize", "", "这个页面在让你做什么？", "Zhège yèmiàn zài ràng nǐ zuò shénme?", "选规格|xuan guige|customize|choose drink specs", "选规格（杯型/温度/糖/奶）<span class=\"py\">xuǎn guīgé · choose specs</span>"),
            ("shot-confirm.jpg", "final confirm", "", "这个页面是哪个步骤？", "Zhège yèmiàn shì nǎge bùzhòu?", "确认订单|queren dingdan|confirm order|confirm and pay", "确认订单并付款 <span class=\"py\">quèrèn dìngdān bìng fùkuǎn · confirm and pay</span>"),
        ]),
        "review": [("手机点单不但方便，而且便宜。", "Shǒujī diǎndān bùdàn fāngbiàn, érqiě piányi."),
                   ("虽然贵，但是很好喝。", "Suīrán guì, dànshì hěn hǎo hē."),
                   ("我的咖啡被朋友喝完了。", "Wǒ de kāfēi bèi péngyou hē wán le."),
                   ("会员可以打折。", "Huìyuán kěyǐ dǎzhé.")],
        "group_names": {
            "group-1": "Sign-in & Promos · 登录优惠",
            "group-2": "Browse & Customize · 浏览客制化",
            "group-3": "Checkout & Member · 付款会员",
            "final": "Final Test · 综合挑战",
        },
    },
    "hsk-5": {
        "tag": "HSK 5",
        "words": "20",
        "body_id": "hsk-5/luckin-coffee",
        "warm": {
            "h2": "你为什么喜欢用手机点咖啡？ <span class=\"py-inline\">Nǐ wèishénme xǐhuan yòng shǒujī diǎn kāfēi?</span>",
            "scene_text": "之所以用手机点咖啡，是因为______。",
            "scene_py": "Zhīsuǒyǐ yòng shǒujī diǎn kāfēi, shì yīnwèi ___.",
            "chips1": [("节省时间", "save time"), ("优惠多", "more discounts"), ("不用排队", "no queue"), ("随时可点", "order anytime")],
            "chips2": [("方便", "convenient"), ("划算", "cost-effective"), ("个性化", "personalized"), ("效率高", "efficient")],
            "tip": "Give reasons for your coffee-ordering habits.",
        },
        "vocab": [
            ("之所以", "zhīsuǒyǐ", "the reason why", "action"), ("是因为", "shì yīnwèi", "is because", "action"),
            ("随着", "suízhe", "along with", "action"), ("无论", "wúlùn", "no matter", "action"),
            ("都", "dōu", "all", "action"), ("个性化", "gèxìnghuà", "personalized", "action"),
            ("推荐", "tuījiàn", "recommend", "action"), ("偏好", "piānhào", "preference", "action"),
            ("趋势", "qūshì", "trend", "action"), ("竞争", "jìngzhēng", "competition", "action"),
            ("市场份额", "shìchǎng fèn'é", "market share", "action"), ("消费者", "xiāofèizhě", "consumer", "action"),
            ("体验", "tǐyàn", "experience", "action"), ("效率", "xiàolǜ", "efficiency", "action"),
            ("节省", "jiéshěng", "save", "action"), ("排队", "páiduì", "queue", "action"),
            ("习惯", "xíguàn", "habit", "action"), ("影响", "yǐngxiǎng", "influence", "action"),
            ("选择", "xuǎnzé", "choice", "action"), ("享受", "xiǎngshòu", "enjoy", "action"),
        ],
        "g1": {"strip": [("之所以", "zhīsuǒyǐ", ""), ("点外卖", "diǎn wàimài", ""), ("是因为", "shì yīnwèi", ""), ("省时间", "shěng shíjiān", "")], "en": "The reason I order delivery is to save time.",
               "ex": [("<span class=\"key\">之所以</span>用手机点咖啡，<span class=\"key\">是因为</span>可以节省时间。", "Zhīsuǒyǐ yòng shǒujī diǎn kāfēi, shì yīnwèi kěyǐ jiéshěng shíjiān.", "The reason I order coffee on my phone is that it saves time."),
                      ("<span class=\"key\">之所以</span>选瑞幸，<span class=\"key\">是因为</span>它很便宜。", "Zhīsuǒyǐ xuǎn Ruìxìng, shì yīnwèi tā hěn piányi.", "The reason I choose Luckin is that it's cheap.")]},
        "g2": {"strip": [("随着", "suízhe", "rust"), ("手机支付", "shǒujī zhīfù", ""), ("普及", "pǔjí", "")], "en": "As mobile payment becomes widespread...",
               "ex": [("<span class=\"key-r\">随着</span>手机支付的普及，点咖啡越来越方便。", "Suízhe shǒujī zhīfù de pǔjí, diǎn kāfēi yuè lái yuè fāngbiàn.", "As mobile payment becomes widespread, ordering coffee is becoming more convenient.", "rust"),
                      ("<span class=\"key-r\">随着</span>竞争加剧，优惠券越来越多。", "Suízhe jìngzhēng jiājù, yōuhuìquàn yuè lái yuè duō.", "As competition intensifies, coupons are increasing.", "rust")]},
        "g3": {"strip": [("无论", "wúlùn", "sky"), ("选", "xuǎn", ""), ("什么", "shénme", ""), ("都", "dōu", "")], "en": "No matter what you choose...",
               "ex": [("<span class=\"key-s\">无论</span>你选什么，<span class=\"key-s\">都</span>可以用优惠券。", "Wúlùn nǐ xuǎn shénme, dōu kěyǐ yòng yōuhuìquàn.", "No matter what you choose, you can use a coupon.", "sky"),
                      ("<span class=\"key-s\">无论</span>冷热，<span class=\"key-s\">都</span>有大杯。", "Wúlùn lěng rè, dōu yǒu dàbēi.", "Whether hot or iced, large cups are available.", "sky")]},
        "dialogue": {"h2": "讨论点咖啡的习惯 <span class=\"py-inline\">tǎolùn diǎn kāfēi de xíguàn</span>",
                     "bubbles": [
                         ("a", "Friend · 朋友", "你几乎每天喝咖啡，都是在哪儿买的？", "Nǐ jīhū měitiān hē kāfēi, dōu shì zài nǎr mǎi de?", "You drink coffee almost every day. Where do you buy it?"),
                         ("b", "Me · 我", "我大部分时候用瑞幸的 APP 点。之所以用它，是因为推荐很个性化，而且能省钱。", "Wǒ dà bùfen shíhou yòng Ruìxìng de APP diǎn. Zhīsuǒyǐ yòng tā, shì yīnwèi tuījiàn hěn gèxìnghuà, érqiě néng shěng qián.", "I mostly use the Luckin app. The reason I use it is that the recommendations are personalized and it saves money."),
                         ("a", "Friend · 朋友", "随着生活越来越快，这种方式确实很受欢迎。", "Suízhe shēnghuó yuè lái yuè kuài, zhè zhǒng fāngshì quèshí hěn shòu huānyíng.", "As life gets faster, this method is indeed very popular."),
                         ("b", "Me · 我", "是啊。无论你选哪种口味，都能快速下单。", "Shì a. Wúlùn nǐ xuǎn nǎ zhǒng kǒuwèi, dōu néng kuàisù xiàdān.", "Yeah. No matter which flavor you choose, you can order quickly.")]},
        "learns": [
            ("登录与个性化推荐", "Dēnglù yǔ gèxìnghuà tuījiàn.", "after logging in, the app studies your preferences and recommends drinks.", [("shot-login.jpg", "login", "登录", "dēnglù · log in"), ("shot-menu.jpg", "menu", "推荐", "tuījiàn · recommendation")]),
            ("优惠券与会员体系", "Yōuhuìquàn yǔ huìyuán tǐxì.", "coupons and membership prices influence consumer choices.", [("shot-coupon.jpg", "coupon", "优惠券", "yōuhuìquàn · coupon"), ("shot-member-card.jpg", "member", "会员卡", "huìyuán kǎ · member card")]),
            ("下单流程", "Xiàdān liúchéng.", "the full process from selecting specs to confirming payment.", [("shot-customize.jpg", "customize", "选规格", "xuǎn guīgé · choose specs"), ("shot-confirm.jpg", "confirm", "确认订单", "quèrèn dìngdān · confirm")]),
        ],
        "tests": [
            ("登录和推荐", "Dēnglù hé tuījiàn.", "group-1", 3, [
                ("shot-login.jpg", "login quiz", "top:57%;left:10%;width:78%;height:5%;", "登录账号最常用的方式是什么？", "Dēnglù zhànghào zuì chángyòng de fāngshì shì shénme?", "手机号安全登录|shouji hao anquan denglu|phone number login|phone", "手机号安全登录 <span class=\"py\">shǒujīhào ānquán dēnglù · log in with phone number</span>"),
                ("shot-menu.jpg", "menu quiz", "top:19.5%;left:64%;width:31%;height:4%;", "根据你的偏好，APP 会怎么帮你选？", "Gēnjù nǐ de piānhào, APP huì zěnme bāng nǐ xuǎn?", "推荐|tuijian|recommend|recommendation", "推荐 <span class=\"py\">tuījiàn · recommend</span>"),
                ("shot-my-orders.jpg", "history quiz", "top:25%;left:6%;width:30%;height:5%;", "快速重复上次订单的按钮是哪几个字？", "Kuàisù chóngfù shàngcì dìngdān de ànniǔ shì nǎ jǐ gè zì?", "再来一单|zai lai yi dan|order again", "再来一单 <span class=\"py\">zài lái yì dān · order again</span>"),
            ]),
            ("优惠和会员", "Yōuhuì hé huìyuán.", "group-2", 3, [
                ("shot-coupon.jpg", "coupon quiz", "top:14%;left:5%;width:88%;height:10%;", "每周领取一次的专属优惠叫什么？", "Měi zhōu lǐngqǔ yí cì de zhuānshǔ yōuhuì jiào shénme?", "专享券|zhuanxiang quan|exclusive coupon", "专享券 <span class=\"py\">zhuānxiǎngquàn · exclusive coupon</span>"),
                ("shot-member-card.jpg", "member quiz", "top:47%;left:5%;width:60%;height:18%;", "会员才能享受的特别价格叫什么？", "Huìyuán cái néng xiǎngshòu de tèbié jiàgé jiào shénme?", "会员价|huiyuan jia|members-only price|member price", "会员价 <span class=\"py\">huìyuán jià · members-only price</span>"),
                ("shot-store-map.jpg", "store quiz", "top:9%;left:8%;width:84%;height:6%;", "要更换取餐的门店，应该点哪里？", "Yào gēnghuàn qǔcān de méndiàn, yīnggāi diǎn nǎlǐ?", "选择门店|xuanze mendian|choose a store", "选择门店 <span class=\"py\">xuǎnzé méndiàn · choose a store</span>"),
            ]),
            ("下单与付款", "Xiàdān yǔ fùkuǎn.", "group-3", 3, [
                ("shot-customize.jpg", "customize quiz", "top:40%;left:33%;width:48%;height:6%;", "最大杯的选项是什么？", "Zuì dà bēi de xuǎnxiàng shì shénme?", "特大杯|te da bei|extra large|extra-large cup", "特大杯 <span class=\"py\">tè dà bēi · extra-large cup</span>"),
                ("shot-sugar-milk.jpg", "sugar quiz", "top:12%;left:28%;width:38%;height:5%;", "不额外添加糖分的选项怎么写？", "Bù éwài tiānjiā tángfèn de xuǎnxiàng zěnme xiě?", "不另外加糖|bu lingwai jia tang|no extra sugar", "不另外加糖 <span class=\"py\">bù lìngwài jiā táng · no extra sugar</span>"),
                ("shot-confirm.jpg", "pay quiz", "top:91%;left:60%;width:37%;height:6%;", "免输密码付款的功能名称是什么？", "Miǎn shū mìmǎ fùkuǎn de gōngnéng míngchēng shì shénme?", "免密支付|mianmi zhifu|pay without password", "免密支付 <span class=\"py\">miǎnmì zhīfù · pay without password</span>"),
            ]),
        ],
        "final": ("综合挑战", "Zōnghé tiǎozhàn.", "final", 3, [
            ("shot-login.jpg", "final login", "", "这个界面主要用于什么？", "Zhège jièmiàn zhǔyào yòngyú shénme?", "登录|denglu|log in|sign in", "登录 <span class=\"py\">dēnglù · log in</span>"),
            ("shot-member-menu.jpg", "final member", "", "这个菜单和普通菜单有什么不同？", "Zhège càidān hé pǔtōng càidān yǒu shénme bùtóng?", "会员菜单|huiyuan caidan|member menu|members only", "会员菜单 <span class=\"py\">huìyuán càidān · member menu</span>"),
            ("shot-confirm.jpg", "final confirm", "", "在这个页面你需要做什么？", "Zài zhège yèmiàn nǐ xūyào zuò shénme?", "确认订单|queren dingdan|confirm order|pay", "确认订单并付款 <span class=\"py\">quèrèn dìngdān bìng fùkuǎn · confirm and pay</span>"),
        ]),
        "review": [("之所以用手机点，是因为节省时间。", "Zhīsuǒyǐ yòng shǒujī diǎn, shì yīnwèi jiéshěng shíjiān."),
                   ("随着手机支付普及，点咖啡更方便。", "Suízhe shǒujī zhīfù pǔjí, diǎn kāfēi gèng fāngbiàn."),
                   ("无论你选什么，都能用优惠券。", "Wúlùn nǐ xuǎn shénme, dōu néng yòng yōuhuìquàn."),
                   ("会员价影响了消费者的选择。", "Huìyuánjià yǐngxiǎng le xiāofèizhě de xuǎnzé.")],
        "group_names": {
            "group-1": "Login & Recommendations · 登录推荐",
            "group-2": "Coupons & Membership · 优惠券会员",
            "group-3": "Order & Payment · 下单付款",
            "final": "Final Test · 综合挑战",
        },
    },
    "hsk-6": {
        "tag": "HSK 6",
        "words": "22",
        "body_id": "hsk-6/luckin-coffee",
        "warm": {
            "h2": "移动支付如何改变了中国人的咖啡消费习惯？ <span class=\"py-inline\">Yídòng zhīfù rúhé gǎibiàn le Zhōngguó rén de kāfēi xiāofèi xíguàn?</span>",
            "scene_text": "究其原因，______。",
            "scene_py": "Qiū jí qí yuán, ___.",
            "chips1": [("便捷性", "convenience"), ("价格优势", "price advantage"), ("数据驱动", "data-driven"), ("品牌竞争", "brand competition")],
            "chips2": [("异军突起", "rise suddenly"), ("势不可挡", "unstoppable"), ("根深蒂固", "deep-rooted"), ("因地制宜", "adapt to local conditions")],
            "tip": "Discuss the deeper reasons behind the popularity of app-based coffee ordering.",
        },
        "vocab": [
            ("倘若", "tǎngruò", "if/suppose", "action"), ("固然", "gùrán", "admittedly", "action"),
            ("究其原因为", "qiū jí qí yuán wéi", "the root cause is", "action"), ("换言之", "huàn yán zhī", "in other words", "action"),
            ("潜移默化", "qiányímòhuà", "subtly influence", "action"), ("屡见不鲜", "lǚ jiàn bù xiān", "common sight", "action"),
            ("势不可挡", "shìbùkědǎng", "unstoppable", "action"), ("异军突起", "yìjūntūqǐ", "rise suddenly", "action"),
            ("根深蒂固", "gēnshēndìgù", "deep-rooted", "action"), ("因地制宜", "yīndìzhìyí", "adapt locally", "action"),
            ("市场份额", "shìchǎng fèn'é", "market share", "action"), ("价格战", "jiàgézhàn", "price war", "action"),
            ("用户黏性", "yònghù niánxìng", "user stickiness", "action"), ("消费习惯", "xiāofèi xíguàn", "consumption habit", "action"),
            ("数字化", "shùzìhuà", "digitalization", "action"), ("算法", "suànfǎ", "algorithm", "action"),
            ("补贴", "bǔtiē", "subsidy", "action"), ("扩张", "kuòzhāng", "expansion", "action"),
            ("颠覆", "diānfù", "disrupt", "action"), ("渗透", "shèntòu", "penetrate", "action"),
            ("饱和", "bǎohé", "saturated", "action"), ("红利", "hónglì", "dividend/benefit", "action"),
        ],
        "g1": {"strip": [("倘若", "tǎngruò", ""), ("取消补贴", "qǔxiāo bǔtiē", ""), ("还会", "hái huì", ""), ("便宜吗", "piányi ma", "")], "en": "If subsidies were cancelled, would it still be cheap?",
               "ex": [("<span class=\"key\">倘若</span>没有优惠券，消费者还会买单吗？", "Tǎngruò méiyǒu yōuhuìquàn, xiāofèizhě hái huì mǎidān ma?", "If there were no coupons, would consumers still pay?"),
                      ("<span class=\"key\">倘若</span>价格上涨，市场份额必然下降。", "Tǎngruò jiàgé shàngzhǎng, shìchǎng fèn'é bìrán xiàjiàng.", "If prices rise, market share will inevitably fall.")]},
        "g2": {"strip": [("固然", "gùrán", "rust"), ("方便", "fāngbiàn", ""), ("但", "dàn", ""), ("隐忧", "yǐnyōu", "")], "en": "Convenient, to be sure, but not without hidden concerns.",
               "ex": [("手机点单<span class=\"key-r\">固然</span>高效，<span class=\"key-r\">但</span>也让人更依赖算法推荐。", "Shǒujī diǎndān gùrán gāoxiào, dàn yě ràng rén gèng yīlài suànfǎ tuījiàn.", "Ordering by phone is efficient, to be sure, but it also makes people more dependent on algorithmic recommendations.", "rust"),
                      ("低价策略<span class=\"key-r\">固然</span>能吸引用户，<span class=\"key-r\">但</span>难以持久。", "Dījià cèlüè gùrán néng xīyǐn yònghù, dàn nányǐ chíjiǔ.", "Low-price strategies can attract users, to be sure, but they are hard to sustain.", "rust")]},
        "g3": {"strip": [("究其原因", "qiū jí qí yuán", "sky"), ("为", "wéi", ""), ("数字化", "shùzìhuà", "")], "en": "The root cause is digitalization.",
               "ex": [("<span class=\"key-s\">究其原因为</span>移动支付普及与消费习惯改变。", "Qiū jí qí yuán wéi yídòng zhīfù pǔjí yǔ xiāofèi xíguàn gǎibiàn.", "The root cause is the popularization of mobile payment and changes in consumption habits.", "sky"),
                      ("瑞幸之所以能快速扩张，<span class=\"key-s\">究其原因为</span>补贴与数字化运营。", "Ruìxìng zhīsuǒyǐ néng kuàisù kuòzhāng, qiū jí qí yuán wéi bǔtiē yǔ shùzìhuà yùnyíng.", "The reason Luckin could expand rapidly is, at its root, subsidies and digital operations.", "sky")]},
        "dialogue": {"h2": "深度讨论：咖啡市场的变化 <span class=\"py-inline\">shēndù tǎolùn: kāfēi shìchǎng de biànhuà</span>",
                     "bubbles": [
                         ("a", "Analyst · 分析师", "瑞幸能在短短几年内占据如此大的市场份额，究其原因是什么？", "Ruìxìng néng zài duǎnduǎn jǐ nián nèi zhànjù rúcǐ dà de shìchǎng fèn'é, qiū jí qí yuán shì shénme?", "Luckin captured such a large market share in just a few years. What is the root cause?"),
                         ("b", "Expert · 专家", "究其原因为数字化运营与价格战的双重作用。换言之，补贴改变了消费者的习惯。", "Qiū jí qí yuán wéi shùzìhuà yùnyíng yǔ jiàgézhàn de shuāngchóng zuòyòng. Huàn yán zhī, bǔtiē gǎibiàn le xiāofèizhě de xíguàn.", "The root cause is the combined effect of digital operations and price wars. In other words, subsidies changed consumer habits."),
                         ("a", "Analyst · 分析师", "这种模式固然成功，但是否存在隐患？", "Zhè zhǒng móshì gùrán chénggōng, dàn shìfǒu cúnzài yǐnhuàn?", "This model is successful, to be sure, but are there hidden risks?"),
                         ("b", "Me · 专家", "倘若补贴减少，用户黏性可能下降。不过，一旦习惯形成，便根深蒂固了。", "Tǎngruò bǔtiē jiǎnshǎo, yònghù niánxìng kěnéng xiàjiàng. Bùguò, yīdàn xíguàn xíngchéng, biàn gēnshēndìgù le.", "If subsidies decrease, user stickiness may fall. However, once habits form, they become deeply rooted.")]},
        "learns": [
            ("登录与数据积累", "Dēnglù yǔ shùjù jīlěi.", "each login feeds the algorithm, which then shapes user preferences through personalized recommendations.", [("shot-login.jpg", "login", "手机号登录", "shǒujīhào dēnglù · phone login"), ("shot-menu.jpg", "menu", "算法推荐", "suànfǎ tuījiàn · algorithmic recommendation")]),
            ("优惠策略与用户黏性", "Yōuhuì cèlüè yǔ yònghù niánxìng.", "coupons and membership pricing are tools to build loyalty and expand market share.", [("shot-coupon.jpg", "coupon", "优惠券", "yōuhuìquàn · coupon"), ("shot-member-card.jpg", "member", "会员价", "huìyuán jià · member price")]),
            ("全链路数字化", "Quán liàn lù shùzìhuà.", "from customization to payment, every step is designed to minimize friction and maximize conversion.", [("shot-customize.jpg", "customize", "客制化", "kèzhìhuà · customize"), ("shot-confirm.jpg", "confirm", "一键支付", "yījiàn zhīfù · one-tap payment")]),
        ],
        "tests": [
            ("登录与算法", "Dēnglù yǔ suànfǎ.", "group-1", 3, [
                ("shot-login.jpg", "login quiz", "top:57%;left:10%;width:78%;height:5%;", "用户用什么方式登录账号？", "Yònghù yòng shénme fāngshì dēnglù zhànghào?", "手机号安全登录|shouji hao anquan denglu|phone login", "手机号安全登录 <span class=\"py\">shǒujīhào ānquán dēnglù · log in with phone number</span>"),
                ("shot-menu.jpg", "menu quiz", "top:19.5%;left:64%;width:31%;height:4%;", "APP 根据用户偏好进行什么操作？", "APP gēnjù yònghù piānhào jìnxíng shénme cāozuò?", "推荐|tuijian|recommend", "推荐 <span class=\"py\">tuījiàn · recommend</span>"),
                ("shot-my-orders.jpg", "history quiz", "top:25%;left:6%;width:30%;height:5%;", "提高复购率的快捷按钮是哪几个字？", "Tígāo fùgòu lǜ de kuàijié ànniǔ shì nǎ jǐ gè zì?", "再来一单|zai lai yi dan|order again", "再来一单 <span class=\"py\">zài lái yì dān · order again</span>"),
            ]),
            ("优惠与会员", "Yōuhuì yǔ huìyuán.", "group-2", 3, [
                ("shot-coupon.jpg", "coupon quiz", "top:14%;left:5%;width:88%;height:10%;", "限时领取的专属券名称是什么？", "Xiànshí lǐngqǔ de zhuānshǔ quàn míngchēng shì shénme?", "专享券|zhuanxiang quan|exclusive coupon", "专享券 <span class=\"py\">zhuānxiǎngquàn · exclusive coupon</span>"),
                ("shot-member-card.jpg", "member quiz", "top:47%;left:5%;width:60%;height:18%;", "仅向会员开放的特别价格叫什么？", "Jǐn xiàng huìyuán kāifàng de tèbié jiàgé jiào shénme?", "会员价|huiyuan jia|members-only price", "会员价 <span class=\"py\">huìyuán jià · members-only price</span>"),
                ("shot-store-map.jpg", "store quiz", "top:9%;left:8%;width:84%;height:6%;", "切换取餐门店的功能名称是什么？", "Qiēhuàn qǔcān méndiàn de gōngnéng míngchēng shì shénme?", "选择门店|xuanze mendian|choose a store", "选择门店 <span class=\"py\">xuǎnzé méndiàn · choose a store</span>"),
            ]),
            ("下单与支付", "Xiàdān yǔ zhīfù.", "group-3", 3, [
                ("shot-customize.jpg", "customize quiz", "top:40%;left:33%;width:48%;height:6%;", "最大杯型的名称是什么？", "Zuì dà bēixíng de míngchēng shì shénme?", "特大杯|te da bei|extra large", "特大杯 <span class=\"py\">tè dà bēi · extra-large cup</span>"),
                ("shot-sugar-milk.jpg", "sugar quiz", "top:12%;left:28%;width:38%;height:5%;", "不额外添加糖分的选项怎么写？", "Bù éwài tiānjiā tángfèn de xuǎnxiàng zěnme xiě?", "不另外加糖|bu lingwai jia tang|no extra sugar", "不另外加糖 <span class=\"py\">bù lìngwài jiā táng · no extra sugar</span>"),
                ("shot-confirm.jpg", "pay quiz", "top:91%;left:60%;width:37%;height:6%;", "无需密码即可完成支付的功能叫什么？", "Wúxū mìmǎ jí kě wánchéng zhīfù de gōngnéng jiào shénme?", "免密支付|mianmi zhifu|pay without password", "免密支付 <span class=\"py\">miǎnmì zhīfù · pay without password</span>"),
            ]),
        ],
        "final": ("综合挑战", "Zōnghé tiǎozhàn.", "final", 3, [
            ("shot-login.jpg", "final login", "", "这个界面在整个流程中起什么作用？", "Zhège jièmiàn zài zhěnggè liúchéng zhōng qǐ shénme zuòyòng?", "登录|denglu|log in|sign in", "登录 <span class=\"py\">dēnglù · log in / 收集用户数据</span>"),
            ("shot-member-menu.jpg", "final member", "", "这个菜单体现了什么运营策略？", "Zhège càidān tǐxiàn le shénme yùnyíng cèlüè?", "会员菜单|huiyuan caidan|member menu|membership", "会员菜单 <span class=\"py\">huìyuán càidān · member menu / 会员差异化定价</span>"),
            ("shot-confirm.jpg", "final confirm", "", "这个页面的核心动作是什么？", "Zhège yèmiàn de héxīn dòngzuò shì shénme?", "确认订单|queren dingdan|confirm order|payment", "确认订单并付款 <span class=\"py\">quèrèn dìngdān bìng fùkuǎn · confirm and pay</span>"),
        ]),
        "review": [("倘若取消补贴，消费者还会买单吗？", "Tǎngruò qǔxiāo bǔtiē, xiāofèizhě hái huì mǎidān ma?"),
                   ("手机点单固然高效，但也让人依赖算法。", "Shǒujī diǎndān gùrán gāoxiào, dàn yě ràng rén yīlài suànfǎ."),
                   ("究其原因为数字化运营与价格战。", "Qiū jí qí yuán wéi shùzìhuà yùnyíng yǔ jiàgézhàn."),
                   ("一旦习惯形成，便根深蒂固。", "Yīdàn xíguàn xíngchéng, biàn gēnshēndìgù.")],
        "group_names": {
            "group-1": "Login & Algorithms · 登录算法",
            "group-2": "Coupons & Membership · 优惠券会员",
            "group-3": "Order & Payment · 下单支付",
            "final": "Final Test · 综合挑战",
        },
    },
})


def build_level(level):
    d = LEVELS[level]
    total_slides = 13
    parts = []
    # brand + cover
    parts.append(f'<body data-lesson-id="{d["body_id"]}">')
    parts.append('<div class="deck">')
    parts.append(f'<div class="deck-brand"><span class="brand-name">新汉 Xīnhàn</span><span class="brand-sub">{d["tag"]} · Ordering Coffee</span></div>')
    parts.append(cover(d["tag"], d["words"], f'{d["tag"]} · Ordering Coffee'))
    # warm-up
    s = d["warm"]
    chips1 = ''.join([f'<div class="chip"><span class="ch">{z}</span><span class="py">{e}</span></div>' for z, e in s["chips1"]])
    chips2 = ''.join([f'<div class="chip"><span class="ch">{z}</span><span class="py">{e}</span></div>' for z, e in s["chips2"]])
    parts.append(slide(1, total_slides, "warm up") + f'<div class="sec-label">Warm-up · 热身</div><h2>{s["h2"]}</h2><div class="scene"><svg viewBox="0 0 740 148" xmlns="http://www.w3.org/2000/svg"><rect width="740" height="148" fill="#f0ebe1" rx="8"/><circle cx="120" cy="74" r="45" fill="#d8f3dc"/><path d="M95 55 Q120 45 145 55 L140 100 Q120 110 100 100 Z" fill="#6f5b4d"/><path d="M98 58 Q120 50 142 58 L138 95 Q120 103 102 95 Z" fill="#a1887f"/><path d="M145 65 Q160 60 160 75 Q160 90 142 88" stroke="#6f5b4d" stroke-width="4" fill="none" stroke-linecap="round"/><text x="120" y="130" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="11" fill="#2d6a4f" font-weight="700">咖啡 kāfēi</text><line x1="220" y1="74" x2="300" y2="74" stroke="#b7791f" stroke-width="2" stroke-dasharray="5,4"/><polygon points="295,70 305,74 295,78" fill="#b7791f"/><rect x="340" y="44" width="360" height="70" fill="white" rx="8"/><text x="370" y="70" font-family="Noto Serif SC,serif" font-size="13" fill="#1a1a1a">{s["scene_text"]}</text><text x="370" y="95" font-family="Inter,sans-serif" font-size="10" fill="#7a7a7a">{s["scene_py"]}</text></svg></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;"><div style="background:var(--cream);border-radius:8px;padding:0.85rem 1rem;"><div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--coffee);margin-bottom:0.5rem;">Choices 选择</div><div class="chip-row" style="margin:0;gap:0.35rem;">{chips1}</div></div><div style="background:var(--cream);border-radius:8px;padding:0.85rem 1rem;"><div style="font-size:0.58rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--coffee);margin-bottom:0.5rem;">Reasons / Features 理由特点</div><div class="chip-row" style="margin:0;gap:0.35rem;">{chips2}</div></div></div><div class="tip"><strong>Practice:</strong> {s["tip"]}</div>' + end_slide())
    # vocab
    vcards = '\n'.join([vc(z, p, e, c) for z, p, e, c in d["vocab"]])
    parts.append(slide(2, total_slides, "vocab", done=1, active=2) + f'<div class="sec-label">New Words · 新词 — {d["words"]} words</div><div class="vocab-grid">{vcards}</div><div class="tip"><strong>Tip:</strong> Focus on the highlighted grammar words.</div>' + end_slide())
    # grammar 1
    g = d["g1"]
    exs = '\n'.join([ex(zh, py, en, cls) for item in g["ex"] for zh, py, en, *cls in [item]]) if any(len(item) == 4 for item in g["ex"]) else '\n'.join([ex(zh, py, en) for zh, py, en in g["ex"]])
    # handle optional class
    ex_html = '\n'.join([ex(*item) if len(item) == 3 else ex(*item) for item in g["ex"]])
    parts.append(slide(3, total_slides, "G1 · " + d["g1"]["strip"][0][0]) + f'<div class="sec-label">Grammar 1 · 语法一</div>{grammar_strip(g["strip"], g["en"])}<div class="ex-block">{ex_html}</div>' + end_slide())
    # grammar 2
    g = d["g2"]
    ex_html = '\n'.join([ex(*item) if len(item) == 3 else ex(*item) for item in g["ex"]])
    parts.append(slide(4, total_slides, "G2 · " + d["g2"]["strip"][0][0], "rust") + f'<div class="sec-label">Grammar 2 · 语法二</div>{grammar_strip(g["strip"], g["en"])}<div class="ex-block">{ex_html}</div>' + end_slide())
    # grammar 3
    g = d["g3"]
    ex_html = '\n'.join([ex(*item) if len(item) == 3 else ex(*item) for item in g["ex"]])
    parts.append(slide(5, total_slides, "G3 · " + d["g3"]["strip"][0][0], "sky") + f'<div class="sec-label">Grammar 3 · 语法三</div>{grammar_strip(g["strip"], g["en"])}<div class="ex-block">{ex_html}</div>' + end_slide())
    # dialogue
    dia = d["dialogue"]
    bubs = '\n'.join([bubble(*b) for b in dia["bubbles"]])
    parts.append(slide(6, total_slides, "dialogue", "gold") + f'<div class="sec-label">Dialogue · 对话</div><h2>{dia["h2"]}</h2><div class="dialogue-exchange">{bubs}</div>' + end_slide())
    # learn/test
    for i, (title, py, tip, phones) in enumerate(d["learns"], start=1):
        parts.append(learn_slide(6 + i, total_slides, title, py, tip, phones))
        t = d["tests"][i - 1]
        parts.append(test_slide(7 + i, total_slides, t[0], t[1], t[2], t[3], t[4]))
    # final
    f = d["final"]
    parts.append(test_slide(13, total_slides, f[0], f[1], f[2], f[3], f[4]))
    # report
    parts.append(report_slide(14))
    # review
    parts.append(review_slide(d["review"]))
    # closing
    parts.append(closing(d["tag"]))
    # foot
    group_names_json = json.dumps(d["group_names"], ensure_ascii=False)
    foot = FOOT.replace("{GROUP_NAMES_JSON}", group_names_json)
    return HEAD + '\n'.join(parts) + foot


if __name__ == "__main__":
    for level in ["hsk-1", "hsk-2", "hsk-4", "hsk-5", "hsk-6"]:
        path = os.path.join(ROOT, level, "luckin-coffee", "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        html = build_level(level)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote {path} ({len(html)} bytes)")
