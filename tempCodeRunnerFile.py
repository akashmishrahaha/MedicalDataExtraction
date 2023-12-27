from pdf2image import convert_from_path
import cv2
import os
import glob  # Don't forget to import glob
import pytesseract

images = convert_from_path(
    "sample.pdf", 500, poppler_path="C:\\Program Files\\poppler-23.11.0\\Library\\bin"
)
# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Specify the directory where you want to save the JPEG files
output_directory = "C:\\Users\\mishr\\OneDrive\\Documents\\MedicalDataExtraction"

# Iterate through the converted images and save them as JPEG files
for i, image in enumerate(images):
    output_path = os.path.join(output_directory, f"page{i}.jpg")
    image.save(output_path, "JPEG")

# Use glob to get a list of JPEG files in the specified directory
file_extension = "*.jpg"
file_pattern = os.path.join(output_directory, file_extension)
matching_files = glob.glob(file_pattern)

# Iterate through the matching JPEG files and print their paths
for filepath in matching_files:
    img = cv2.imread("filepath")
    target_height = 600
    ratio = target_height / img.shape[0]
    new_dimensions = (int(img.shape[1] * ratio), target_height)
    resized_img = cv2.resize(img, new_dimensions)
    cv2.imshow("Resized Image", resized_img)
    text = pytesseract.image_to_string(img)
    print(text)
    # Wait for a key event and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
