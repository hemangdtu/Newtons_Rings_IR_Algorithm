import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelmin
import sys

#read input image, resize it if needed, and apply a basic gaussian blur to remove
#high-frequency noise

img = cv2.imread("test_1.jpg",0)
img = cv2.resize(img,(0,0), fx=1,fy=1)
img = cv2.medianBlur(img,5)

#rescale color space from rbg to bw
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
bwimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#apply the hough transform to obtain detected circles in the image
#circles should be an array with each element of the form [xpos, ypos, radius]

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,5,50,param1=110,param2=80,minRadius=40,maxRadius=0)
circles = np.uint16(np.around(circles))

#obtain the center of the image for size calculations
center = np.array(np.shape(img)) / 2.0

# iterate through all circles found, and draw those within a certain radius of the center of the image
# to filter out the stuff we don't want
# also choose one of these circles to be the one we use, and save it's center point -- This is a bit of a bodge, as it simply
# pulls a random circle - in theory, this is the only one that should be found, but this isn't always certain depending on noise

trueCenter = None
for i in circles[0]:
    if((np.abs(i[1] - center[0]) ** 2 + np.abs(i[0] - center[1]) ** 2) ** 0.5 < 35 ):
        trueCenter = i
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#transform to polar and draw image - do this twice, once for the image to display,
#and once for the one to do the math on (which should not have debug graphics - eg the center of the circle drawn)
size = int(np.shape(img)[0]/2)
dst	= cv2.warpPolar(cimg,(size,size), (trueCenter[0],trueCenter[1]), maxRadius= size, flags = cv2.WARP_POLAR_LINEAR)
dst2 = cv2.warpPolar(bwimg,(size,size), (trueCenter[0],trueCenter[1]), maxRadius= size, flags = cv2.WARP_POLAR_LINEAR)

#plot intensities and figures
fig = plt.figure()

plt.subplot(2, 2, 1)
plt.imshow(cimg)

plt.subplot(2, 2, 2)
#plot pixel intensities from center to the side of the image (bad way)
plt.plot(range(0,len(bwimg[trueCenter[1]]))[trueCenter[0]:],[i[1] for i in bwimg[trueCenter[1]]][trueCenter[0]:])


plt.subplot(2, 2, 3)
plt.imshow(dst)

plt.subplot(2, 2, 4)
#Find the average value of each column in the transformed image, and plot that value instead (better way)
plt.xlabel("Pixel Distance")
plt.ylabel("Average Intensity")

average_val = [sum([dst2[j][i][1] for j in range(0,len(dst[i]))]) / len(dst[i]) for i in range(0, len(dst))]
plt.plot(range(0,len(dst)), average_val)

#find local minima, and plot those on the graph. also print them (pixel distances)
mins = argrelmin(np.array(average_val), order=1)
plt.plot(mins[0][1:],[average_val[i] for i in mins[0][1:]], 'gx')

file1 = open(r"output.txt","w")
# [print(i) for i in mins[0][1:12]]
for i in mins[0][1:12]:
    file1.write(str(i)+"\n")
file1.close()


plt.show()
