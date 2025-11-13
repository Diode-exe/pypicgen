from PIL import Image
from matplotlib import colors as cl
from random import randint

output = "array.txt"

def number_gen():
    with open (output, "w") as f:
        for each in range(1, 262144):
            rn = str(randint(1, 148))
            f.write(" ")
            f.write(rn)
        f.write(" ")

number_gen()

source = "array.txt"
lines = []
colors = []

try:
    with open(source, "r") as f:
        for line in f:
            lines.append(line.strip())
except FileNotFoundError:
    print(f"[ERROR] {source} not found!")
    exit()

css_colors = cl.CSS4_COLORS  # dict: name -> hex string

# Create a numeric color map
color_map = {i: name for i, name in enumerate(css_colors.keys())}

# Convert hex to RGB
rgb_map = {
    name: tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    for name, hex_color in css_colors.items()
}

# Convert lines to colors properly
for line in lines:
    for num_str in line.split():  # split by whitespace
        if num_str.isdigit():
            num = int(num_str)
            if num in color_map:
                colors.append(color_map[num])

# Create 512x512 image
grid_width = 512
grid_height = 512
img = Image.new("RGB", (grid_width, grid_height))

for i, color_name in enumerate(colors):
    if i >= grid_width * grid_height:
        break
    x = i % grid_width
    y = i // grid_width
    img.putpixel((x, y), rgb_map.get(color_name, (0, 0, 0)))

img.save("pixel_grid.png")
print("Image saved!")


