
# import pytesseract
#
# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'c://program_files/teseract-ocr/tesseract'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))

import numpy as np

import cv2
from PIL import Image
from pytesseract import pytesseract

# # Defining paths to tesseract.exe
# # and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image_path = r"sample_images\service_provider.png"
#
# # Opening the image & storing it in an image object
# img = Image.open(image_path)
#
# # Providing the tesseract executable
# # location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract
#
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img)
#
# # Displaying the extracted text
# print(text)
# # print(text[:-1])


# def apply_threshold(image_, argument):
#     switcher = {
#         1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
#         2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
#         3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
#         18: cv2.adaptiveThreshold(cv2.medianBlur(img, 7), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
#         19: cv2.adaptiveThreshold(cv2.medianBlur(img, 5), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
#         20: cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
#     }
#     return switcher.get(argument, "Invalid method")

# Scaling
# def set_image_dpi(file_path):
#     im = Image.open(file_path)
#     length_x, width_y = im.size
#     factor = min(1, float(1024.0 / length_x))
#     size = int(factor * length_x), int(factor * width_y)
#     im_resized = im.resize(size, Image.ANTIALIAS)
#     temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
#     temp_filename = temp_file.name
#     im_resized.save(temp_filename, dpi=(300, 300))
#     return temp_filename
# Noise Reduction
# def remove_noise_and_smooth(file_name):
#     img = cv2.imread(file_name, 0)
#     filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
#     kernel = np.ones((1, 1), np.uint8)
#     opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
#     closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
#     img = image_smoothening(img)
#     or_image = cv2.bitwise_or(img, closing)
#     return or_image


# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

images = ['service_provider.png', 'down.png', 'up.png', 'ping.png', 'rand.png']

for image in images:
    # print(f"sample_images\\{image}")
    # Load using PIL
    # img = Image.open(f"sample_images\\{image}")

    # Load using OpenCV
    img = cv2.imread(f"sample_images\\{image}")

    ''' pre process image for better results '''

    # Rescale
    # img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    # convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply a blur
    # img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(img)

    print(f"\n{image.split('.')[0]}: {text}")
