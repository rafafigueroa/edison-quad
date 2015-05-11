import base64
import numpy as np
import cv2
import cv
from PIL import Image
import StringIO
from goprohero import GoProHero
import time

camera = GoProHero(password='rafadrone')
#camera.command('fov','170')
#camera.command('mode','still')
#camera.command('picres','5MP wide')
camera.command('record','off')

#imgstr = open("testimage.txt","rb").read()

while True:
	imgstr = camera.image()[21:]	
#	open("test.txt","w").write(imgstr).close()
	imgraw = base64.decodestring(imgstr)
	pilImage = Image.open(StringIO.StringIO(imgraw));
	frame = np.array(pilImage)
	#bwframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#edges = cv2.Canny(bwframe, 100, 100)


	cv2.imshow('frame', frame)
	#cv2.imshow('edges', edges)

	#matImage = cv.fromarray(npImage)
	cv2.waitKey(1)
	
	#time.sleep(1)
