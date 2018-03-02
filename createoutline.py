'''
 * Python program to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename>
'''
import cv2, sys
from PIL import Image, ImageDraw
import numpy as np

'''
 * Function to perform Canny edge detection and display the
 * result.
'''
def cannyEdge():
	global img, minT, maxT
	height,width = img.shape[:2]
	blank_img = np.zeros((height,width,3), np.uint8)
	blank_img[:] = (255,255,255)
	gray = cv2.bilateralFilter(img, 11, 17, 17)
	edge = cv2.Canny(gray, minT, maxT)
	newimg, cnts, _= cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(blank_img, cnts, -1, (0,0,0), -1)
	cv2.imwrite('static/outlinedselfie.jpg', blank_img)

'''
 * Main program begins here.
'''
# read command-line filename argument
filename = sys.argv[1]

# load original image as grayscale
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# Hard-coded threshold values
minT = 30
maxT = 150
# perform Canny edge detection and save result
cannyEdge()
