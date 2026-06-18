from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
H = Path(__file__).parent
W, HT = 640, 320
img = Image.new("RGB", (W, HT))
d = ImageDraw.Draw(img)
top, bot = (28, 18, 45), (60, 36, 110)
for y in range(HT):
    t = y / (HT - 1)
    d.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
# barres egaliseur
spec = [40, 120, 180, 90, 150, 70]
bw, gap = 26, 16
total = len(spec) * bw + (len(spec) - 1) * gap
x = W // 2 - total // 2
base = 250
for h in spec:
    d.rounded_rectangle([x, base - h, x + bw, base], radius=12, fill=(196, 142, 244))
    x += bw + gap
try:
    f = ImageFont.truetype("segoeuib.ttf", 40)
except Exception:
    f = ImageFont.load_default()
d.text((W / 2, 285), "Stem Extractor", fill=(236, 228, 247), font=f, anchor="mm")
img.save(H / "preview.png")
print("preview OK")
