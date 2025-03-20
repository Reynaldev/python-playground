import cv2

# img = cv2.imread("./assets/test-image.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("./assets/test-image.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Behold!", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
