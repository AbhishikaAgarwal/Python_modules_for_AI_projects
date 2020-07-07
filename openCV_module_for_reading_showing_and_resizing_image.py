import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Abhishika Agarwal\Desktop\Images\Virat Kohli.jpg",1)

img = cv2.resize(img,(300,300))
print(img.shape)

cv2.imshow("Master",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
