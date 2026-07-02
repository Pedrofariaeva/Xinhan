from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE, MSO_SHAPE_TYPE
from pptx.dml.color import RGBColor
from lxml import etree

img_dir = '/Users/pedro/Documents/GitHub/Xinhan/lessons/images/'

def add_framed_image(slide, img_file, left, top, width, height):
    img_path = img_dir + img_file
    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left - 0.08), Inches(top - 0.08), Inches(width + 0.16), Inches(height + 0.16))
    frame.fill.solid()
    frame.fill.fore_color.rgb = RGBColor(255, 255, 255)
    frame.line.fill.background()
    frame.adjustments[0] = 0.08
    pic = slide.shapes.add_picture(img_path, Inches(left), Inches(top), Inches(width), Inches(height))
    spTree = slide.shapes._spTree
    spTree.remove(frame._element)
    spTree.remove(pic._element)
    spTree.insert(3, frame._element)
    spTree.insert(4, pic._element)

def find_shape_by_pos(slide, shape_type, left_in, top_in, width_in, height_in, tol=0.1):
    for shape in slide.shapes:
        if shape.shape_type == shape_type:
            if (abs(shape.left.inches - left_in) < tol and
                abs(shape.top.inches - top_in) < tol and
                abs(shape.width.inches - width_in) < tol and
                abs(shape.height.inches - height_in) < tol):
                return shape
    return None

# Open user's updated file
prs = Presentation('/Users/pedro/Documents/GitHub/Xinhan/lessons/English speaking  friendship middle school(3).pptx')

# Slide 1: Bottom center image
slide = prs.slides[0]
add_framed_image(slide, 'friends_hanging.jpg', 4.2, 5.0, 4.8, 2.2)

# Slide 3: Bottom center image (content ends around y=5.2)
slide = prs.slides[2]
add_framed_image(slide, 'school_kids.jpg', 4.5, 5.3, 4.0, 1.6)

# Slide 9: Shrink main rectangle & text, add image on right
slide = prs.slides[8]
rect = find_shape_by_pos(slide, MSO_SHAPE.RECTANGLE, 1.50, 2.00, 10.33, 3.50)
if rect:
    rect.width = Inches(7.2)
txt = find_shape_by_pos(slide, MSO_SHAPE_TYPE.TEXT_BOX, 2.00, 2.30, 9.33, 3.00)
if txt:
    txt.width = Inches(6.2)
add_framed_image(slide, 'girls_chatting.jpg', 9.1, 2.0, 3.5, 3.5)

# Slide 16: Shrink dialogue rectangle & text, add image on right
slide = prs.slides[15]
rect = find_shape_by_pos(slide, MSO_SHAPE.RECTANGLE, 2.50, 1.70, 8.33, 4.20)
if rect:
    rect.width = Inches(5.8)
# Shrink long dialogue lines (x=3.50, w=7.00 -> w=4.8)
for shape in slide.shapes:
    if shape.shape_type == MSO_SHAPE_TYPE.TEXT_BOX:
        if abs(shape.left.inches - 3.50) < 0.1 and abs(shape.width.inches - 7.00) < 0.1:
            shape.width = Inches(4.5)
add_framed_image(slide, 'friends_hanging.jpg', 8.8, 2.0, 3.8, 3.8)

# Slide 18: Shrink story rectangle & text, add image on right
slide = prs.slides[17]
rect = find_shape_by_pos(slide, MSO_SHAPE.RECTANGLE, 1.50, 1.70, 10.33, 3.50)
if rect:
    rect.width = Inches(7.2)
txt = find_shape_by_pos(slide, MSO_SHAPE_TYPE.TEXT_BOX, 1.80, 2.50, 9.70, 2.50)
if txt:
    txt.width = Inches(6.0)
add_framed_image(slide, 'birthday_party.jpg', 9.1, 1.9, 3.5, 3.5)

# Slide 20: Shrink homework rectangle & text, add image on right
slide = prs.slides[19]
rect = find_shape_by_pos(slide, MSO_SHAPE.RECTANGLE, 2.00, 1.70, 9.33, 3.50)
if rect:
    rect.width = Inches(6.3)
txt = find_shape_by_pos(slide, MSO_SHAPE_TYPE.TEXT_BOX, 2.30, 2.00, 8.33, 3.20)
if txt:
    txt.width = Inches(5.3)
add_framed_image(slide, 'books_friends.jpg', 8.7, 1.9, 3.8, 3.5)

# Save with the exact name the user wants
prs.save('/Users/pedro/Documents/GitHub/Xinhan/lessons/English speaking  friendship middle school(3).pptx')
print("Done: images added to your updated file while preserving your text changes.")
