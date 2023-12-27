from pdf2image import convert_from_path
import cv2

images = convert_from_path(
    "sample.pdf", 500, poppler_path="C:\\Program Files\\poppler-23.11.0\\Library\\bin"
)

for i in range(len(images)):
    # Read the image using OpenCV
    cv2.imread(images[i].save("page" + str(i) + ".jpg", "JPEG"))
