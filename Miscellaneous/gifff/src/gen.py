from PIL import Image

flag = input("Enter the flag: ").encode("utf-8").hex()

colors = [flag[i:i+6].rjust(6, '0') for i in range(0, len(flag), 6)]

def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_image(hex_color):
    image = Image.new("RGB", (20, 20), hex_to_rgb(hex_color))
    return image

images = []
for color in colors:
    image = create_image(color)
    images.append(image)

container = Image.new("RGB", (20, 20), (0, 0, 0))
container.save("chall.gif", save_all=True, append_images=images, duration=1, loop=0)