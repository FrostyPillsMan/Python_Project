from PIL import Image, ImageColor, ImageOps

with Image.open("./Practise Python/Pillow/img/Tom Hanks.png") as img:
    img.load()

    # max_thumbnail_size = (200, 200)
    # img.thumbnail(max_thumbnail_size)

    img = img.convert("RGB")

    datas = img.getdata()

    new_data_img = []

    for item in datas:
        if item[0] in list(range(200, 256)):
            new_data_img.append((255, 224, 100))
        else:
            new_data_img.append(item)

    # update image data
    img.putdata(new_data_img)

    color = "green"

    border = (20, 10, 20, 10)

    new_img = ImageOps.expand(img, border=border, fill=color)

    new_img.save("test_background.jpg")

