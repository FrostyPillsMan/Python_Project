from PIL import Image


(left, upper, right, lower) = (200, 350, 500, 700)
# 4-tuple that defines the left(x1), upper(y1), right(x2), and bottom(y2) edges of the region that you wish to crop.


if __name__ == "__main__":
    # Read the image from the file
    with Image.open("./Practise Python/Pillow/img/Switzerland House.jpg") as img:
        img.load()
        
        cropped_img = img.crop((left, upper, right, lower))
        # print(cropped_img.size)
        # cropped_img.show()
        
        # low_res_img = cropped_img.resize(
           #  (cropped_img.width // 4, cropped_img.height // 4)
        # )
        # cropped_img.show()
        
        low_res_img = cropped_img.reduce(4)
        low_res_img.show()


