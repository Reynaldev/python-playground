import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./assets/test-image.jpg")

# Converting BGR color to RGB color format
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(rgb_img)

plt.waitforbuttonpress()
plt.close("all")
