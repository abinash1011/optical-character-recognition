import easyocr
import numpy as np
import cv2
from matplotlib import pyplot as plt

img_path = '/content/surf.jpeg'

reader = easyocr.Reader(['en'], gpu = False)
result = reader.readtext(img_path)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(img_path)
img = cv2.rectangle(img,top_left,bottom_right,(0,0,255),3)
img = cv2.putText(img,text,top_left, font, 0.5,(255,255,255),2,cv2.LINE_AA)
plt.imshow(img)
plt.show()