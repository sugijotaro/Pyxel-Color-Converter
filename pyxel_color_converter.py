from PIL import Image
import numpy as np
import argparse
import sys

def closest_color(rgb, color_list):
    r, g, b = rgb
    color_diffs = []
    for color in color_list:
        cr, cg, cb = color
        color_diff = abs(r - cr) + abs(g - cg) + abs(b - cb)
        color_diffs.append(color_diff)
    return color_list[color_diffs.index(min(color_diffs))]

def convert_image(image_path, resize):
    colors = [(0, 0, 0), (43, 51, 95), (126, 32, 114), (25, 149, 156), (139, 72, 82), 
              (57, 92, 152), (169, 193, 255), (238, 238, 238), (212, 24, 108),
              (211, 132, 65), (233, 195, 91), (112, 198, 169), (118, 150, 222),
              (163, 163, 163), (255, 151, 152), (237, 199, 176)]

    img = Image.open(image_path)
    img = img.convert("RGB")

    if resize:
        width, height = img.size
        if max(width, height) > 256:
            if width > height:
                new_width = 256
                new_height = int(256 * (height / width))
            else:
                new_height = 256
                new_width = int(256 * (width / height))
            img = img.resize((new_width, new_height))

    data = np.array(img)
    new_data = np.zeros_like(data)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            new_data[i][j] = closest_color(data[i][j], colors)
            if j % 100 == 0:
                print("\rProcessing... {:.2f}%".format(100 * (i * data.shape[1] + j) / (data.shape[0] * data.shape[1])), end="")

    print("\rProcessing... done!    ")

    new_img = Image.fromarray(new_data, "RGB")
    new_img.save("converted_image.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts an image to closest colors in Pyxel palette.")
    parser.add_argument("image_path", type=str, help="Path to the image to be converted.")
    parser.add_argument("--resize", action='store_true', help="Resizes the image to max 256 pixels if either width or height is larger.")

    args = parser.parse_args()
    convert_image(args.image_path, args.resize)
