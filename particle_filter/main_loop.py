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

flag = 0

# loop over frames from the video file stream
while True:
	# read the next frame from the file
	(grabbed, frame) = vs.read()

	# if the frame was not grabbed, then we have reached the end
	# of the stream
	if not grabbed:
		break

	start = time.time()

	center = ip.find_centroid(frame)
	if center == None: continue

	# print("center",center)

	if flag ==0:
		vet_particles = pf.start(center)
		flag = 1
	
	(vet_particles,frame_drawed) = pf.filter_steps(vet_particles,center,frame) #remover esse frame quando estiver funcionando

	frame = frame_drawed
	# frame = pf.drawBox(vet_particles.copy())
	
	# pf.print_vet_particles(vet_particles.copy())

	cv2.imshow("Image", frame)
	cv2.waitKey(0)


	end = time.time()

	# check if the video writer is None
	# if writer is None:
	# 	# initialize our video writer
	# 	fourcc = cv2.VideoWriter_fourcc(*"MJPG")
	# 	writer = cv2.VideoWriter('basket.avi', fourcc, 30,
	# 		(frame.shape[1], frame.shape[0]), True)

	# 	# some information on processing single frame
	# 	if total > 0:
	# 		elap = (end - start)
	# 		print("[INFO] single frame took {:.4f} seconds".format(elap))
	# 		print("[INFO] estimated total time to finish: {:.4f}".format(
	# 			elap * total))

	
	# write the output frame to disk
	# writer.write(frame)

# release the file pointers
print("[INFO] cleaning up...")
writer.release()
vs.release()