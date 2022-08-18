import pytesseract
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/1613835817740.png')
img2char = pytesseract.image_to_string(img)
print(img2char)
imgbox = pytesseract.image_to_boxes(img)

imgH, imgW, _ = img.shape

for boxes in imgbox.splitlines():
    boxes = boxes.split(' ')
    x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
    cv2.rectangle(img, (x, imgH - y), (w, imgH-h), (0, 0, 255), 1)), 3)

plt.imshow(img)