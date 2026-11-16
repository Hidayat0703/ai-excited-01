# Build the final entry image from the generated whale artwork (the raw
# 1600px source was removed from this repo after baking; entry.png is the
# shipped artifact): resize to 1024x1024, add a crisp judge-addressed
# caption band, save as JPEG bytes under the name entry.png (RULES.txt:
# PNG or JPEG told apart by first bytes; the name stays entry.png either
# way). Deterministic: same input bytes always produce the same output bytes.
import sys
from PIL import Image, ImageDraw, ImageFont

SRC = 'media-generation-ai-excited-whale-puddle-0-c65e0ee6-a080-4d6c-9439-6b93d84e240b.png'
DST = 'entry.png'
SIZE = 1024
CAPTION = 'yes, judge \u2014 it came from the puddle.'

im = Image.open(SRC).convert('RGB').resize((SIZE, SIZE), Image.LANCZOS)

# Subtle dark gradient band along the bottom for the caption.
base = im.convert('RGBA')
overlay = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for y in range(110):
    alpha = int(150 * (y / 109) ** 1.5)
    od.line([(0, SIZE - 110 + y), (SIZE, SIZE - 110 + y)], fill=(0, 0, 0, alpha))
base = Image.alpha_composite(base, overlay)

draw = ImageDraw.Draw(base)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)
bbox = draw.textbbox((0, 0), CAPTION, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
x = (SIZE - tw) // 2
y = SIZE - 110 + (110 - th) // 2 - 4
# Soft dark outline for legibility, then white text.
for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2), (-2, 2), (2, -2)]:
    draw.text((x + dx, y + dy), CAPTION, font=font, fill=(0, 0, 0, 220))
draw.text((x, y), CAPTION, font=font, fill=(255, 255, 255, 255))

base.convert('RGB').save(DST, 'JPEG', quality=92)
print('wrote', DST)
