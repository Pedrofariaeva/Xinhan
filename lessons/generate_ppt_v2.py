from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from lxml import etree

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

img_dir = '/Users/pedro/Documents/GitHub/Xinhan/lessons/images/'

# Colors
C_HEADER = RGBColor(232, 67, 147)   # pink/coral
C_TEXT = RGBColor(45, 52, 54)       # dark grey
C_WHITE = RGBColor(255, 255, 255)
C_LIGHT = RGBColor(250, 250, 250)
C_ACCENT = RGBColor(9, 132, 227)    # blue

def add_textbox(slide, left, top, width, height, text, font_size, bold=False, italic=False, color=C_TEXT, align=PP_ALIGN.LEFT, name='Microsoft YaHei'):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = align
    font = p.font
    font.size = Pt(font_size)
    font.bold = bold
    font.italic = italic
    font.name = name
    font.color.rgb = color
    return txBox

def add_bullets(slide, left, top, width, height, items, font_size, color=C_TEXT, line_space=1.4):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = "• " + item
        p.level = 0
        p.space_after = Pt(10)
        font = p.font
        font.size = Pt(font_size)
        font.name = 'Microsoft YaHei'
        font.color.rgb = color
    return txBox

def add_rounded_card(slide, left, top, width, height, fill_color=C_WHITE, line_color=None, transparency=0.0):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if transparency > 0:
        # Set alpha via XML
        fill = shape.fill._xPr
        solidFill = fill.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
        if solidFill is not None:
            srgbClr = solidFill.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
            if srgbClr is not None:
                alpha = etree.SubElement(srgbClr, '{http://schemas.openxmlformats.org/drawingml/2006/main}alpha')
                alpha.set('val', str(int((1 - transparency) * 100000)))
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    # Adjust corner rounding
    shape.adjustments[0] = 0.1
    return shape

def add_header_bar(slide, color):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    bar.fill.solid()
    bar.fill.fore_color.rgb = color
    bar.line.fill.background()
    return bar

def add_image(slide, img_file, left, top, width, height, rounded=False):
    img_path = img_dir + img_file
    try:
        if rounded:
            # Add picture inside rounded rect is complex; just add picture for now
            pic = slide.shapes.add_picture(img_path, Inches(left), Inches(top), Inches(width), Inches(height))
        else:
            pic = slide.shapes.add_picture(img_path, Inches(left), Inches(top), Inches(width), Inches(height))
        return pic
    except Exception as e:
        print(f"Error adding image {img_file}: {e}")
        return None

# Slide 1: Title with full background image
def make_title_slide():
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Full background image
    img = add_image(slide, 'friends_playing.jpg', 0, 0, 13.333, 7.5)
    if img:
        spTree = slide.shapes._spTree
        sp = img._element
        spTree.remove(sp)
        spTree.insert(2, sp)
    # Dark overlay gradient from left
    overlay = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(8), Inches(7.5))
    overlay.fill.solid()
    overlay.fill.fore_color.rgb = RGBColor(30, 30, 60)
    fill_el = overlay.fill._xPr
    solidFill = fill_el.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
    if solidFill is not None:
        srgbClr = solidFill.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
        if srgbClr is not None:
            alpha = etree.SubElement(srgbClr, '{http://schemas.openxmlformats.org/drawingml/2006/main}alpha')
            alpha.set('val', '75000')
    overlay.line.fill.background()
    spTree = slide.shapes._spTree
    sp = overlay._element
    spTree.remove(sp)
    spTree.insert(3, sp)
    
    add_textbox(slide, 0.8, 2.4, 6.5, 1.2, "💖 Friendship", 72, bold=True, color=C_WHITE)
    add_textbox(slide, 0.8, 3.6, 6.5, 0.8, "The Best Gift in Life", 32, color=RGBColor(251, 194, 235))
    add_textbox(slide, 0.8, 4.5, 6.5, 0.6, "A 2-Hour Journey to Better Speaking & Writing", 20, color=RGBColor(200, 200, 220))
    add_textbox(slide, 0.8, 5.2, 6.5, 0.5, "Grade 7 • Spoken English • Test Prep", 16, color=RGBColor(180, 180, 210))
    add_textbox(slide, 11.5, 6.9, 1.5, 0.3, "1 / 20", 14, color=C_WHITE, align=PP_ALIGN.RIGHT)

# Generic content slide with optional image
def make_content_slide(number, title, image_file=None, content_fn=None, header_color=C_HEADER):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = RGBColor(245, 247, 250)
    bg.line.fill.background()
    spTree = slide.shapes._spTree
    sp = bg._element
    spTree.remove(sp)
    spTree.insert(2, sp)
    
    # Header bar
    add_header_bar(slide, header_color)
    add_textbox(slide, 0.6, 0.25, 12, 0.7, title, 36, bold=True, color=C_WHITE)
    
    # Content area width depends on image
    content_w = 7.8 if image_file else 12.0
    content_left = 0.6
    
    # White content card
    card_h = 5.8
    add_rounded_card(slide, content_left - 0.15, 1.4, content_w + 0.3, card_h, fill_color=C_WHITE)
    
    if content_fn:
        content_fn(slide, content_left, 1.65, content_w, 5.4)
    
    if image_file:
        # Image card on right
        add_rounded_card(slide, 9.0, 1.4, 3.8, 5.8, fill_color=C_WHITE)
        img = add_image(slide, image_file, 9.15, 1.55, 3.5, 5.5)
        if img:
            spTree = slide.shapes._spTree
            sp = img._element
            spTree.remove(sp)
            # Insert after the white card
            spTree.insert(6, sp)
    
    add_textbox(slide, 11.5, 6.9, 1.5, 0.3, f"{number} / 20", 14, color=RGBColor(150, 150, 150), align=PP_ALIGN.RIGHT)
    return slide

make_title_slide()

# Slide 2
make_content_slide(2, "🤔 Warm-Up Discussion", image_file='students_classroom.jpg',
    content_fn=lambda s, l, t, w, h: add_bullets(s, l, t + 0.5, w, h - 1, [
        "How many good friends do you have?",
        "What do you and your friends like to do together?",
        "Can you describe your best friend in 3 words?",
        "What makes a true friend?"
    ], 26), header_color=RGBColor(161, 140, 209))

# Slide 3
make_content_slide(3, "👥 Types of Friends", image_file='school_activity.jpg',
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.6, "Learn these words to describe different friends:", 20, color=RGBColor(100,100,100)),
        add_bullets(s, l, t + 0.8, w, h - 1, [
            "best friend — 最好的朋友",
            "close friend — 亲密的朋友",
            "classmate — 同学",
            "online friend — 网友",
            "childhood friend — 发小",
            "teammate — 队友",
            "pen pal — 笔友",
            "neighbor — 邻居"
        ], 22)
    )[1], header_color=RGBColor(132, 250, 176))

# Slide 4
make_content_slide(4, "✨ Personality Adjectives (1)", image_file='chatting.jpg',
    content_fn=lambda s, l, t, w, h: add_bullets(s, l, t + 0.3, w, h - 0.5, [
        "kind 善良的", "helpful 乐于助人的", "funny 有趣的",
        "outgoing 外向的", "honest 诚实的", "loyal 忠诚的",
        "hard-working 勤奋的", "clever 聪明的"
    ], 24), header_color=RGBColor(252, 203, 144))

# Slide 5
make_content_slide(5, "🌈 Personality Adjectives (2)", image_file='chatting.jpg',
    content_fn=lambda s, l, t, w, h: add_bullets(s, l, t + 0.3, w, h - 0.5, [
        "patient 有耐心的", "caring 关心他人的", "brave 勇敢的",
        "creative 有创造力的", "shy / quiet 害羞的/安静的",
        "generous 大方的", "understanding 善解人意的", "sporty 爱运动的"
    ], 24), header_color=RGBColor(224, 195, 252))

# Slide 6
make_content_slide(6, "💬 Key Phrases About Friendship",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.6, "Use these phrases when you talk or write about friends:", 20, color=RGBColor(100,100,100)),
        add_bullets(s, l, t + 0.8, w, h - 1, [
            "get along well with — 与…相处融洽",
            "have something in common — 有共同之处",
            "be good at — 擅长",
            "care about — 关心",
            "help ... with ... — 帮助…做…",
            "share ... with ... — 与…分享",
            "trust each other — 互相信任",
            "keep secrets — 保守秘密"
        ], 22)
    )[1], header_color=RGBColor(255, 154, 158))

# Slide 7
make_content_slide(7, "📐 Grammar: Describing People",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "Present Simple: He / She + is / has + ...", 22, bold=True, color=C_ACCENT),
        add_bullets(s, l, t + 0.7, w, h - 1, [
            "She is tall and thin.",
            "He has short black hair.",
            "She wears glasses.",
            "He is very funny and outgoing.",
            "She is good at English."
        ], 26)
    )[1], header_color=RGBColor(161, 196, 253))

# Slide 8
make_content_slide(8, "🔄 Present Simple vs. Continuous",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "Remember the difference:", 20, color=RGBColor(100,100,100)),
        add_bullets(s, l, t + 0.6, w, 2.0, [
            "Simple (habits): She always helps me.",
            "Continuous (now): She is helping me now."
        ], 24),
        add_textbox(s, l, t + 3.0, w, 0.8, "Use always / usually / often with Present Simple!", 22, bold=True, color=C_HEADER, align=PP_ALIGN.CENTER)
    )[1], header_color=RGBColor(212, 252, 121))

# Slide 9
make_content_slide(9, "🎤 Speaking Model", image_file='chatting.jpg',
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "My Best Friend", 22, bold=True, color=C_ACCENT),
        add_textbox(s, l, t + 0.6, w, 4.0, "Lin Mei is my best friend. We have been classmates since Grade 5. She is kind and hard-working. She has long hair and always wears a smile. She is good at English and often helps me with my homework. We both love playing badminton after school. Last week, she shared her umbrella with me when it rained. I think a good friend is someone who truly cares about you. Lin Mei is such a friend.", 20, color=C_TEXT)
    )[1], header_color=RGBColor(251, 194, 235))

# Slide 10
make_content_slide(10, "📝 Speaking Framework", image_file='books_reading.jpg',
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "How to Describe Your Best Friend (1 minute)", 20, bold=True, color=RGBColor(100,100,100)),
        add_bullets(s, l, t + 0.6, w, h - 1, [
            "1. Basic info: name, age, how you met",
            "2. Appearance: height, hair, glasses",
            "3. Personality: kind, funny, helpful...",
            "4. Hobbies: good at, likes to...",
            "5. A story: what you did together",
            "6. Why you like him/her"
        ], 23)
    )[1], header_color=RGBColor(253, 203, 241))

# Slide 11
make_content_slide(11, "🗣️ Speaking Practice: Pair Work",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w / 2 - 0.2, 0.5, "Student A", 24, bold=True, color=C_ACCENT),
        add_textbox(s, l, t + 0.6, w / 2 - 0.2, 2.5, "Describe your best friend. Use at least 5 new words from today's lesson.", 20, color=C_TEXT),
        add_textbox(s, l + w / 2 + 0.2, t, w / 2 - 0.2, 0.5, "Student B", 24, bold=True, color=C_HEADER),
        add_textbox(s, l + w / 2 + 0.2, t + 0.6, w / 2 - 0.2, 3.0, "Listen and ask one question:\n\n• How long have you known each other?\n• What do you usually do together?\n• What makes him/her special?", 19, color=C_TEXT)
    ), header_color=RGBColor(137, 247, 254))

# Slide 12
make_content_slide(12, "✍️ Writing Structure",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "A Good Paragraph About a Friend", 22, bold=True, color=C_ACCENT),
        add_bullets(s, l, t + 0.7, w, h - 1, [
            "Topic sentence: Who is this person?",
            "Detail 1: Appearance (looks)",
            "Detail 2: Personality & hobbies",
            "Detail 3: A story or memory",
            "Closing: Why is this friendship important?"
        ], 24),
        add_textbox(s, l, t + 4.5, w, 0.6, "Target length: 60–80 words", 18, bold=True, color=C_HEADER, align=PP_ALIGN.CENTER)
    )[1], header_color=RGBColor(253, 219, 146))

# Slide 13
make_content_slide(13, "✏️ Guided Writing Practice",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "Fill in the blanks, then rewrite as a paragraph:", 18, color=RGBColor(100,100,100)),
        add_textbox(s, l, t + 0.6, w, 4.0, "My best friend is __________. We met __________. He/She is __________ and __________. He/She has __________. We both like __________. Last week, __________. I feel __________ because __________.", 22, color=C_TEXT)
    )[1], header_color=RGBColor(168, 237, 234))

# Slide 14
make_content_slide(14, "🎯 Test Prep: My Best Friend",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "Common Writing Prompt (60–80 words)", 20, bold=True, color=C_ACCENT),
        add_bullets(s, l, t + 0.7, w, h - 1.5, [
            "Write about your best friend.",
            "Include: introduction, appearance, personality, hobbies",
            "Explain why you are good friends."
        ], 24),
        add_textbox(s, l, t + 4.0, w, 0.8, "Tip: Use and, but, because, so, when, if", 20, bold=True, color=C_HEADER, align=PP_ALIGN.CENTER)
    )[1], header_color=RGBColor(255, 154, 158))

# Slide 15
make_content_slide(15, "📝 Test Prep: Narrative Writing",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.5, "\"An Unforgettable Day with My Friend\"", 22, bold=True, color=C_ACCENT),
        add_bullets(s, l, t + 0.7, w, h - 1, [
            "When & Where — set the scene",
            "What happened — the event",
            "How you helped each other",
            "What you learned about friendship"
        ], 24),
        add_textbox(s, l, t + 4.2, w, 0.6, "Use past tense: was, were, did, went, helped, shared...", 20, bold=True, color=C_HEADER, align=PP_ALIGN.CENTER)
    )[1], header_color=RGBColor(102, 126, 234))

# Slide 16
make_content_slide(16, "🎭 Dialogue: Making Friends", image_file='friends_playing.jpg',
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.4, "Practice with a partner!", 18, italic=True, color=RGBColor(100,100,100)),
        add_textbox(s, l, t + 0.6, w, 0.45, "A: Hi! I'm Lily. What's your name?", 21, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 1.05, w, 0.45, "B: I'm Mei. Nice to meet you!", 21, color=C_HEADER),
        add_textbox(s, l, t + 1.55, w, 0.45, "A: Nice to meet you too! Do you like playing basketball?", 21, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 2.0, w, 0.45, "B: Yes, I love it! I play every weekend.", 21, color=C_HEADER),
        add_textbox(s, l, t + 2.55, w, 0.45, "A: Great! We can play together after school.", 21, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 3.0, w, 0.45, "B: That's wonderful! Let's be friends.", 21, color=C_HEADER)
    )[1], header_color=RGBColor(240, 147, 251))

# Slide 17
make_content_slide(17, "🎭 Dialogue: Helping a Friend",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.4, "Key phrases in bold", 18, italic=True, color=RGBColor(100,100,100)),
        add_textbox(s, l, t + 0.6, w, 0.45, "A: You look sad. What's wrong?", 21, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 1.05, w, 0.45, "B: I failed my English test. I feel terrible.", 21, color=C_HEADER),
        add_textbox(s, l, t + 1.55, w, 0.45, "A: Don't worry. I can help you with vocabulary.", 21, bold=True, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 2.0, w, 0.45, "B: Really? That's so kind of you!", 21, bold=True, color=C_HEADER),
        add_textbox(s, l, t + 2.55, w, 0.45, "A: We can study together every Saturday.", 21, color=C_ACCENT),
        add_textbox(s, l + 0.3, t + 3.0, w, 0.45, "B: Thank you! You are a true friend.", 21, color=C_HEADER)
    )[1], header_color=RGBColor(79, 172, 254))

# Slide 18
make_content_slide(18, "📖 A Story About Friendship", image_file='birthday.jpg',
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w, 0.45, "Sharing an Umbrella ☂️", 22, bold=True, color=C_ACCENT),
        add_textbox(s, l, t + 0.6, w, 3.8, "Last Friday, it rained heavily after school. I forgot my umbrella. My friend Li Hua saw me standing at the school gate. She walked over and said, \"Let's share my umbrella!\" Her umbrella was small, but we walked home together. We both got a little wet, but we laughed all the way. That day, I learned: a true friend is someone who gets wet with you.", 19, color=C_TEXT),
        add_textbox(s, l, t + 4.5, w, 0.6, "Discuss: What did Li Hua do? Why was it kind? Have you ever helped a friend?", 17, bold=True, color=C_HEADER)
    )[1], header_color=RGBColor(67, 233, 123))

# Slide 19
make_content_slide(19, "🔑 Review & Key Takeaways",
    content_fn=lambda s, l, t, w, h: (
        add_textbox(s, l, t, w / 2 - 0.2, 0.5, "Key Words", 22, bold=True, color=C_ACCENT),
        add_bullets(s, l, t + 0.6, w / 2 - 0.2, 4.0, [
            "loyal, honest, kind",
            "helpful, funny, caring",
            "get along well with",
            "have something in common",
            "care about, trust",
            "share ... with ..."
        ], 19),
        add_textbox(s, l + w / 2 + 0.2, t, w / 2 - 0.2, 0.5, "Key Structures", 22, bold=True, color=C_ACCENT),
        add_bullets(s, l + w / 2 + 0.2, t + 0.6, w / 2 - 0.2, 4.0, [
            "He/She is + adj.",
            "He/She has + noun",
            "We like to + verb",
            "We are good at + v-ing",
            "A true friend is someone who..."
        ], 19)
    ), header_color=RGBColor(250, 112, 154))

# Slide 20
make_content_slide(20, "📝 Homework & Next Steps",
    content_fn=lambda s, l, t, w, h: (
        add_bullets(s, l, t + 0.3, w, 3.5, [
            "Write a paragraph (80 words) about your best friend.",
            "Prepare a 1-minute oral introduction of your friend.",
            "Memorize 10 new adjectives from today's lesson.",
            "Think of a short story about you and a friend to share next class."
        ], 24),
        add_textbox(s, l, t + 4.2, w, 0.7, "\"A friend in need is a friend indeed.\"", 26, italic=True, color=C_HEADER, align=PP_ALIGN.CENTER),
        add_textbox(s, l, t + 5.0, w, 0.5, "See you next time! 👋", 20, color=RGBColor(100,100,100), align=PP_ALIGN.CENTER)
    )[1], header_color=RGBColor(48, 207, 208))

prs.save('/Users/pedro/Documents/GitHub/Xinhan/lessons/friendship_presentation.pptx')
print("Beautiful PPT v2 created successfully!")
