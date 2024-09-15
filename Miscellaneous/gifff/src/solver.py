from PIL import Image, ImageSequence

chall = Image.open("../dist/chall.gif")

frames = [frame.copy() for frame in ImageSequence.Iterator(chall)]

def rgb_to_hex(rgb_color):
    return "".join(f"{c:02x}" for c in rgb_color)

hexstring = ""
for f in frames[1:]:
    color = rgb_to_hex( f.getpixel((0, 0)))
    hexstring += color

flag = bytes.fromhex(hexstring).decode("utf-8")
print(flag)

