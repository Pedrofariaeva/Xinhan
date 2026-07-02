from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

prs = Presentation('/Users/pedro/Documents/GitHub/Xinhan/lessons/friendship_presentation.pptx')
img_dir = '/Users/pedro/Documents/GitHub/Xinhan/lessons/images/'

def add_framed_image(slide, img_file, left, top, width, height, frame_color=RGBColor(255,255,255)):
    """Add image with rounded white frame"""
    img_path = img_dir + img_file
    
    # White rounded frame
    frame = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left - 0.08), Inches(top - 0.08),
        Inches(width + 0.16), Inches(height + 0.16)
    )
    frame.fill.solid()
    frame.fill.fore_color.rgb = frame_color
    frame.line.fill.background()
    frame.adjustments[0] = 0.08
    
    # Image
    pic = slide.shapes.add_picture(img_path, Inches(left), Inches(top), Inches(width), Inches(height))
    
    # Send frame and pic to back (above background)
    spTree = slide.shapes._spTree
    for shape in [frame, pic]:
        sp = shape._element
        spTree.remove(sp)
        spTree.insert(3, sp)
    return pic

# Add images at bottom center of selected slides, framed, preserving original layout
placements = [
    (0, 'friends_hanging.jpg',   4.4, 4.6, 4.5, 2.4),  # Slide 1: Title
    (2, 'school_kids.jpg',       4.8, 5.1, 3.8, 2.0),  # Slide 3: Types of Friends
    (8, 'girls_chatting.jpg',    4.9, 5.1, 3.6, 2.1),  # Slide 9: Speaking Model
    (15, 'friends_hanging.jpg',  4.8, 5.1, 3.8, 2.0),  # Slide 16: Dialogue Making Friends
    (17, 'birthday_party.jpg',   4.9, 5.1, 3.6, 2.1),  # Slide 18: Story
    (19, 'books_friends.jpg',    4.8, 5.2, 3.8, 1.8),  # Slide 20: Homework
]

for slide_idx, img_file, left, top, width, height in placements:
    slide = prs.slides[slide_idx]
    add_framed_image(slide, img_file, left, top, width, height)

prs.save('/Users/pedro/Documents/GitHub/Xinhan/lessons/friendship_presentation.pptx')
print("Images added cleanly to original layout!")
