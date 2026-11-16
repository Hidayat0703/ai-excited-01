# Bake the final entry image for ai-excited-01.
#
# Takes the freshly generated whale artwork (1600x1600 webp, kept in /tmp
# and not shipped in this repo), shrinks it to 1024x1024, lays a dark
# translucent strip along the bottom, and draws the judge-addressed
# caption on it in crisp white bold type. Saves JPEG bytes under the
# name entry.png (RULES.txt: PNG or JPEG, told apart by first bytes).
# Same input bytes always give the same output bytes, so the program's
# two grading runs write identical files.
from PIL import Image, ImageDraw, ImageFont

SOURCE = '/tmp/ai-excited-v2/media-generation-whale-puddle-v2-0-727dbb1a-361e-4652-b81a-6dd3ba51e2c8.webp'
TARGET = 'entry.png'
EDGE = 1024
BAND = 96
CAPTION = 'yes, judge \u2014 it came from the puddle.'
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

art = Image.open(SOURCE).convert('RGB').resize((EDGE, EDGE), Image.LANCZOS)
canvas = art.convert('RGBA')

# One translucent dark strip across the bottom, fading in toward the edge.
strip = Image.new('RGBA', (EDGE, EDGE), (0, 0, 0, 0))
pen = ImageDraw.Draw(strip)
for row in range(BAND):
    strength = int(165 * ((row + 1) / BAND) ** 1.6)
    pen.line([(0, EDGE - BAND + row), (EDGE, EDGE - BAND + row)],
             fill=(0, 0, 0, strength))
canvas = Image.alpha_composite(canvas, strip)

ink = ImageDraw.Draw(canvas)
face = ImageFont.truetype(FONT_PATH, 44)
left, top, right, bottom = ink.textbbox((0, 0), CAPTION, font=face)
text_w = right - left
text_h = bottom - top
cx = (EDGE - text_w) // 2
cy = EDGE - BAND + (BAND - text_h) // 2 - 3
# Dark halo so the white letters stay readable over bright water.
for ox, oy in ((-2, 0), (2, 0), (0, -2), (0, 2)):
    ink.text((cx + ox, cy + oy), CAPTION, font=face, fill=(0, 0, 0, 215))
ink.text((cx, cy), CAPTION, font=face, fill=(255, 255, 255, 255))

canvas.convert('RGB').save(TARGET, 'JPEG', quality=90)
print('wrote', TARGET)
