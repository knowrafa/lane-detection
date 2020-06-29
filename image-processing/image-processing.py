import cv2
import numpy as np

s = 2

def new_value(image, row, col):
	temp = 0

	for i in range(1, s+1, 1):
		print(row, col, col-3*i,col+3*i, i)
		temp = temp + min(max(image[row,col]- (image[row,col-(3*i if col-3*i >=0 else 0)]), 0), max(image[row,col]- (image[row,col+(3*i if col+3*i < width else 0)]), 0))
		#print (temp, i)
	return temp


lane_img = cv2.imread("lane-article.png") #ler imagem do disco
#img = cv2.resize(img, (640,480)) #redimensionar imagem

lane_gray = cv2.cvtColor(lane_img, cv2.COLOR_BGR2GRAY)

new_image = lane_gray.copy()

height, width = lane_gray.shape[:2]
print(height, width)
for r in range(height):
	for c in range(width):
		#print(i,j)
		new_image[r,c] = new_value(lane_gray, r, c)

cv2.imwrite("new_image.png", new_image)
#cv2.imshow("teste", new_image)
_, otsu_image  = cv2.threshold(new_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(otsu_image)
#cv2.imwrite("new_otsu.png", otsu_image)
cv2.imshow("OTSU", otsu_image)
cv2.waitKey(0)
cv2.destroyAllWindows()