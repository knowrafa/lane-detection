import cv2
import numpy as np

s = 10

def new_value(image, row, col):
	new_intensity = 0
	intensity = image[row,col]

	for i in range(1, s+1, 1):
		#print(row, col, col-3*i,col+3*i, i)
		#print(str(image[row][col]) + " -- " + str(temp))
		#print (str(image[row,col-(3*i if (col-3*i >= 0) else 0)]) + " // " + str(image[row,col+(3*i if (col+3*i < width) else 0)]))
		#print("MIN " + str(min(max(image[row,col]- (image[row,col-(3*i if (col-3*i >= 0) else 0)]), 0), max(image[row,col]- (image[row,col+(3*i if (col+3*i < width) else 0)]), 0))))
		#print("FIRST CALC: " + str(image[row,col]- (image[row,col-(3*i if (col-3*i >= 0) else 0)])))
		#print("SECOND CALC: " + str(image[row,col]- (image[row,col+(3*i if (col+3*i < width) else 0)])))

		l3i = image[row,col-(3*i if (col-3*i >= 0) else 0)]
		r3i = image[row,col+(3*i if (col+3*i < width) else 0)]
		
		#if(intensity < l3i):
		#	l3i = 0

		#if(intensity < r3i):
		#	r3i = 0

		new_intensity = new_intensity + min(max(int(intensity)- int(l3i) , 0), max(int(intensity)- int(r3i), 0))

	return new_intensity


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

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))

closing = cv2.morphologyEx(otsu_image, cv2.MORPH_CLOSE, kernel)

#print(otsu_image)
cv2.imwrite("new_otsu.png", closing)
cv2.imshow("OTSU", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()