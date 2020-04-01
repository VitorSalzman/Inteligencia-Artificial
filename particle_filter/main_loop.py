import numpy as np
import argparse
import imutils
import time
import cv2
import os

import pf_tools as pf
import image_process as ip

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python


# cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui


# initialize the video stream, pointer to output video file, and
# frame dimensions
vs = cv2.VideoCapture('basket.mp4')
writer = None

# try to determine the total number of frames in the video file
try:
	prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
		else cv2.CAP_PROP_FRAME_COUNT
	total = int(vs.get(prop))
	print("[INFO] {} total frames in video".format(total))

# an error occurred while trying to determine the total
# number of frames in the video file
except:
	print("[INFO] could not determine # of frames in video")
	print("[INFO] no approx. completion time can be provided")
	total = -1

#define constant
TIMELOCKED = 15
TIMELOST = 5

contPerdeSinal = TIMELOCKED
contTempoPerdido = TIMELOST
filter_is_on = False

find = True

# loop over frames from the video file stream
while True:
	(grabbed, frame) = vs.read()

	if not grabbed:
		break
	
	start = time.time()
	center = None

	H,W,_ = frame.copy().shape

	text1 = "count to miss center: {}".format(contPerdeSinal)
	cv2.putText(frame,text1,(W-220,H-40),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0),2)

	if contPerdeSinal < 0:
		find = False
		if contTempoPerdido < 0:
			find = True
			contPerdeSinal = TIMELOCKED
			contTempoPerdido = TIMELOST

		contTempoPerdido = contTempoPerdido -1
	contPerdeSinal = contPerdeSinal -1

	if find is True:
		center = ip.find_centroid(frame)
		text2 = "Target: LOCKED"
		cv2.putText(frame,text2,(W-220,H-20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0),2)
	else:
		center = None
		text2 = "Target: LOST"
		cv2.putText(frame,text2,(W-220,H-20),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255),2)
	
	


	# print("center: {}".format(center))

	if filter_is_on == False:
		if center is None: continue
		particleFilter = pf.ParticleFilter(500,center,10)
		filter_is_on = True

	if particleFilter.filter_steps(center) is False :
		filter_is_on = False
		continue

	frame = particleFilter.drawBox(frame)
	cv2.imshow("Image",frame)



	# cv2.imshow("Image", frame)
	# cv2.waitKey(0)


	end = time.time()

	# check if the video writer is None
	if writer is None:
		# initialize our video writer
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter('basket.avi', fourcc, 30,
			(frame.shape[1], frame.shape[0]), True)

		# some information on processing single frame
		if total > 0:
			elap = (end - start)
			print("[INFO] single frame took {:.4f} seconds".format(elap))
			print("[INFO] estimated total time to finish: {:.4f}".format(
				elap * total))

	
	# write the output frame to disk
	writer.write(frame)

# release the file pointers
print("[INFO] cleaning up...")
writer.release()
vs.release()