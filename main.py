import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image9.jpg', 0)
inverted = 255 - img
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
sketch = cv2.divide(img, 255 - blurred, scale=256)
plt.imshow(sketch, cmap='gray')
plt.axis('off') 
plt.show()