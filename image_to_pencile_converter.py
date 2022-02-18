import cv2
import sys

image = cv2.imread(sys.argv[1])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch Image", pencil_sketch)


result=cv2.imwrite('Pencil Sketch Image.jpg',pencil_sketch)

if result==True:
  print("File saved successfully")
else:
  print("Error in saving file")

cv2.waitKey(6000)
cv2.destroyWindow("Pencil Sketch Image using OpenCV")
