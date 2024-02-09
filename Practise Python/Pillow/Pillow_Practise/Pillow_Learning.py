from PIL import Image


(left, upper, right, lower) = (400, 550, 700, 900)
# 4-tuple that defines the left(x1), upper(y1), right(x2), and bottom(y2) edges of the region that you wish to crop.


def image_mode(image):
    original_image = image.getbands()
    return original_image
    
def cmyk_mode(cmyk_image):
    new_image = cmyk_image.getbands()
    return new_image

def gray_mode(gray_image):
    new_image = gray_image.getbands()
    return new_image
    
        
if __name__ == "__main__":
    # Read the image from the file
    with Image.open("./Practise Python/Pillow/img/Switzerland House.jpg") as img:
        img.load()

        # cropped_img = img.crop((left, upper, right, lower))
        # print(cropped_img.size)
        # cropped_img.show()

        # low_res_img = cropped_img.resize(
        #  (cropped_img.width // 4, cropped_img.height // 4)
        # )
        # cropped_img.show()

        # Reduce size of image resolution
        # low_res_img = cropped_img.reduce(1)
        # low_res_img.show()
        # print(low_res_img.size)

        # Rotate or flip image based on options.
        # converted_img = img.transpose(Image.ROTATE_270)
        # converted_img.show()

        cmyk_img = img.convert("CMYK") # Looks similar to original image
        gray_img = img.convert("L")  # Grayscale

        # cmyk_img.show()
        # gray_img.show()

        # attract_img_mode = gray_mode(gray_img)
        # print(attract_img_mode)
        
        (red, green, blue) = img.split()
        print(green)
        print(green.mode)

        # img.show(title="House Of Switzerland")

