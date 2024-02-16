import numpy as np

# Python library on dealing with numeric arrays
from PIL import Image


# Creating Square
square = np.zeros((600, 600))  
# Create an array size of dimensional 2d image
square[200:400, 200:400] = 255 
# Represents row and column of the image
square_img = Image.fromarray(square) 
# Convert the NumPy array into an object of type Image


print(square_img)
square_img.show()
