"""
LOAD-And-Save
Rotating-And-Scaling Images
Drawing Shapes
"""

from PIL import Image, ImageDraw
# import os


class InvalidFactor(Exception):
    pass


# Checking if the image size is valid, otherwise raise Error.
def scaled_im(image, size):
    if size < 0:
        raise InvalidFactor("The scale must be greater than zero.")
    return image.resize((round(image.width * size), round(image.height * size)))


def image_atrribute(image):
    """
    format - shows the type of image
    size - shows width and height in pixels
    mode - shows color of the image
    """
    image = img.format, img.size, img.mode
    return image


def add_cross(image, colour):
    draw = ImageDraw.Draw(image)
    draw.line((0, 0) + image.size, fill=colour, width=10)
    draw.line((0, image.size[1], image.size[0], 0), fill=colour, width=10)
    return image


def add_rectangle(image, topleft, bottomright, colour):
    draw = ImageDraw.Draw(image)
    draw.rectangle((topleft, bottomright), fill=colour)
    return image


def add_square(image, topleft, size, colour):
    draw = ImageDraw.Draw(image)
    draw.rectangle((topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return image


def add_ellipse(image, topleft, bottomright, colour):
    draw = ImageDraw.Draw(image)
    draw.ellipse((topleft, bottomright), fill=colour)
    return image


def add_circle(image, topleft, size, colour):
    draw = ImageDraw.Draw(image)
    draw.ellipse((topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return image


if __name__ == "__main__":
    # Read the image from the file
    with Image.open("./Practise Python/Pillow/img/Yamimash.jpg") as img:
        # Read the image into memory so that the file can now be closed
        img.load()
        # print(type(img))
        # print(isinstance(img, Image.Image))

        # rotated_im = img.rotate(45, expand=True)
        # scaled_im = img.resize((600, 1000))

        # scaled_image = scaled_im(img, 2)
        # print(scaled_image.size)

        # Saves the image as a temporary file and displays it using default image viewer of the operating system.
        # scaled_image.show(title="Yamimash")

        # img.save("./Practise Python/Pillow/save_new_img/Yamimash.jpeg")

        # image_shown = image_atrribute(img)
        # print(image_shown)

        # image_cross = add_cross(img, (255, 0, 0))
        # image_cross.show()

        # image_rectangle = add_rectangle(img, (100, 100), (700, 350), (0, 255, 0))
        # image_rectangle.show()

        # image_square = add_square(img, (675, 890), 240, (0, 0, 255))
        # image_square.show()

        # image_ellipse = add_ellipse(img, (985, 1025), (620, 400), (255, 0, 0))
        # image_ellipse.show()

        # image_circle = add_circle(img, (2145, 1425), 300, (0, 0, 225))
        # image_circle.show()


    # Show list of "jpg" files
    # open_image = [image for image in os.listdir("./Practise Python/Pillow/img") if image.endswith(".jpg")]
    # print(open_image)


