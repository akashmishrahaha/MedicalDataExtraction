import pytesseract
import cv2

# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image using OpenCV
img = cv2.imread("page0.jpg")


# Display the resized image
cv2.imshow("Resized Image", img)
text = pytesseract.image_to_string(img)
print(text)
# Wait for a key event and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
