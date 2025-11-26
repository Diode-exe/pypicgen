import numpy as np
from PIL import Image
from matplotlib import colors as cl
import datetime
import os

output_dir = "img"
os.makedirs(output_dir, exist_ok=True)

grid_width = 512
grid_height = 512
num_pixels = grid_width * grid_height

# Prepare color map as a proper uint8 NumPy array
css_colors = list(cl.CSS4_COLORS.keys())
rgb_map = np.array(
    [tuple(int(cl.CSS4_COLORS[name][i:i+2], 16) for i in (1, 3, 5))
     for name in css_colors],
    dtype=np.uint8
)

def getTimeAndDate():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def generator():
    while True:
        # Generate indices for all pixels
        indices = np.random.randint(0, len(css_colors), size=num_pixels)

        # Map indices to RGB
        img_array = rgb_map[indices]

        # Ensure it's the right shape
        img_array = img_array.reshape((grid_height, grid_width, 3))

        # Convert to image
        img = Image.fromarray(img_array, "RGB")
        img.save(f"{output_dir}/{getTimeAndDate()}.png")
        print("Image saved!")

generator()
