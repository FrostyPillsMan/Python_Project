from PIL import Image, ImageFilter


(left, upper, right, lower) = (400, 550, 700, 900)
# 4-tuple that defines the left(x1), upper(y1), right(x2), and bottom(y2) edges of the region that you wish to crop.
# option 2 change argument into box(x1, y1, x2, y2)


def image_mode(image):
    original_image = image.getbands()
    return original_image


def cmyk_mode(cmyk_image):
    new_image = cmyk_image.getbands()
    return new_image


def gray_mode(gray_image):
    new_image = gray_image.getbands()
    return new_image


def erode(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image


if __name__ == "__main__":
    # Read the image from the file
    # with Image.open("./Practise Python/Pillow/img/Switzerland House.jpg") as img:
    with Image.open("./Practise Python/Pillow/img/Tom Hanks.png") as img:
        img.load()

        # Change image resolution
        # cropped_img = img.crop((left, upper, right, lower))
        # print(cropped_img.size)
        # cropped_img.show()

        # Resize the image dimensions
        # low_res_img = cropped_img.resize(
        # (cropped_img.width // 4, cropped_img.height // 4)
        # )
        # cropped_img.show()

        # Reduce size of image resolution
        # low_res_img = cropped_img.reduce(1)
        # low_res_img.show()
        # print(low_res_img.size)

        # Rotate or flip image based on options.
        # converted_img = img.transpose(Image.ROTATE_270)
        # converted_img.show()

        cmyk_img = img.convert("CMYK")  # Looks similar to original image
        gray_img = img.convert("L")  # Grayscale

        # cmyk_img.show()
        # gray_img.show()

        # Returns value of each band from the image in a tuple
        # attract_img_mode = gray_mode(gray_img)
        # print(attract_img_mode)

        # Edit Color mode of the image
        # red, green, blue, _ = img.split()
        # print(green)
        # print(green.mode)

        # zeroed_band = red.point(lambda _: 0)
        # Mix with other colours using point()

        # first argument in merge() determines the mode of the image that you want to create.
        # second argument contains the individual bands that you want to merge into a single image.

        # red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
        # green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
        # blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

        # red_merge.show()
        # green_merge.show()
        # blue_merge.show()

        img_Tom_Hanks = img.convert("L")
        # img_Tom_Hanks.show(title="Greyscale Tom Hanks")
        threshold = 125  # Input data where allows change pixels of an image
        img_Tom_Hanks_threshold = img_Tom_Hanks.point(
            lambda x: 255 if x > threshold else 0
        )
        # Convert image through Binary mode(0/1).
        img_Tom_Hanks_threshold = img_Tom_Hanks.convert("1")
        # img_Tom_Hanks_threshold.show(title="New Hanks")

        # Remove white pixels representing on the background image.
        step_1 = erode(12, img_Tom_Hanks_threshold)
        # step_1.show()

        # Find gap and filter out from the image.
        step_2 = dilate(58, step_1)
        # step_2.show()

        # Adjust mask of the image
        Tom_hanks_Mask = erode(45, step_2)
        Tom_hanks_Mask = Tom_hanks_Mask.convert("L")
        Tom_hanks_Mask = Tom_hanks_Mask.filter(ImageFilter.BoxBlur(20))
        # Tom_hanks_Mask.show()

        Wallpaper_blank = img_Tom_Hanks.point(lambda _: 0)
        tom_hank_segmented = Image.composite(
            img_Tom_Hanks, Wallpaper_blank, Tom_hanks_Mask
        )
        # tom_hank_segmented.show()


    with Image.open("./Practise Python/Pillow/img/Pewdiepie Dope.jpg") as img_Pewdiepie:
        img_Pewdiepie.load()

        img_Pewdiepie.paste(
            img_Tom_Hanks.resize((img_Tom_Hanks.width // 5, img_Tom_Hanks.height // 5)),
            (750, 900),
            Tom_hanks_Mask.resize(
                (Tom_hanks_Mask.width // 5, Tom_hanks_Mask.height // 5)
            ),
        )

        img_Pewdiepie.show()

    with Image.open("./Practise Python/Pillow/img/Dota.jpg") as Dota_img:
        Dota_img.load()

        img_dota = img.convert("L")
        threshold = 125
        img_dota = img_dota.point(lambda x: 255 if x > threshold else 0)
        img_dota = img_dota.resize((img_dota.width // 2, img_dota.height // 2))
        img_dota = img_dota.filter(ImageFilter.CONTOUR)
        # img_dota.save("./Practise Python/Pillow/save_new_img/Tom Hanks Edited.jpeg", format="JPEG")
        img_dota = img_dota.point(lambda x: 0 if x == 255 else 255)

        img_Pewdiepie.paste(img_dota, (380, 460), img_dota)
        img_Pewdiepie.show()

        # Original Image
        # img.show(title="Tom Hanks")
