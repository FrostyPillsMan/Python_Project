"""
Drawing text✅
Applying filters✅
Using masks✅
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps


def add_text(image, text, topright, size, colour):
    font = ImageFont.truetype(
        "./Practise Python/Pillow/fonts/PlayfulTime-BLBB8.ttf", size
    )
    draw = ImageDraw.Draw(image)
    draw.multiline_text(topright, text, font=font, fill=colour)
    return image


filters = {
    "Blur": ImageFilter.BLUR,
    "Box Blur": ImageFilter.BoxBlur(10),
    "Gaussian Blur": ImageFilter.GaussianBlur(25),
    "Sharpen": ImageFilter.SHARPEN,
    "Smooth": ImageFilter.SMOOTH,
    "Smooth More": ImageFilter.SMOOTH_MORE,
    "Find_Edges": ImageFilter.FIND_EDGES,  # Option 1
    "Edge Enhance": ImageFilter.EDGE_ENHANCE,
    "Edge Enhance_More": ImageFilter.EDGE_ENHANCE_MORE,
    "Emboss": ImageFilter.EMBOSS,
    "Details": ImageFilter.DETAIL,
}


def create_circular(image):
    # offset = (image.width - image.height) // 2
    # image = image.crop((offset, 0, image.height + offset, image.height))
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    outer = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    outer.putalpha(mask)
    return outer


if __name__ == "__main__":
    # for key, value in filters.items():
    # with Image.open("./Practise Python/Pillow/img/Switzerland House.jpg") as img:

    with Image.open("./Practise Python/Pillow/img/Darth Malgus.jpg") as img:
        img.load()
        # img = add_text(img, "Hello Switzerland!\nIt's good to see you.", (200, 300), 250, (0, 0, 255))
        # img.save("./Practise Python/Pillow/save_new_img/Switzerland-House.png", format="PNG")

        # image = img.filter(value)
        # image.save(f"./Practise Python/Pillow/filter_image/Switzerland-House{key}.jpeg", format="JPEG")


        # Option 2
        # img_gray = img.convert("L")
        # edges = img_gray.filter(ImageFilter.FIND_EDGES)
        # edges.show()
        # break

        image = img.convert("RGBA")
        circular_img = create_circular(image)
        circular_img.show()

