import cv2

img = cv2.imread("./sign_board.png")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

offset = 50

first_half = grey_img[offset:-offset, offset:grey_img.shape[1]//2]
second_half = grey_img[offset:-offset, grey_img.shape[1]//2:-offset]

_, thresh_half1 = cv2.threshold(first_half, 200, 255, cv2.THRESH_BINARY_INV)
_, thresh_half2 = cv2.threshold(second_half, 200, 255, cv2.THRESH_BINARY_INV)

"""

Now, the first image corresponds to the places with their names
So, we will extract the characters from that image by applying some operations related to contours

"""

_, contours, _ = cv2.findContours(thresh_half1.copy(), mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

#### Sorting the contours on the basis of their areas
sorted_contours1 = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

### Finding the index of the contour from where non-english character contours start showing up
for i in range (len(sorted_contours1)):
    if (cv2.contourArea(sorted_contours1[i+1])<800 and (cv2.contourArea(sorted_contours1[i])-cv2.contourArea(sorted_contours1[i+1]) >= 300)):
        break

### Iterating throughout the sorted contours from the second contour to the i-th contour
### Ignored 1st contour - Because it corresponds to the whole window or bounding box of the image
### Ignored every contour after i-th index - Because it all the contours after that index correspond to non-english symbols

for c in sorted_contours1[1:i+1]:
    print(cv2.contourArea(c))
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(first_half, (x, y), (x + w, y + h), color=0, thickness=2)


