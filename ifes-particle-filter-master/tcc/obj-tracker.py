from models import *
from utils import *
from sort import *

import os, sys, time, datetime, random
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch.autograd import Variable

from PIL import Image
import cv2


videopath = 'test.mp4'
config_path='config/yolov3.cfg' # yolov3.cfg contains the architecture definition of model
weights_path='config/yolov3.weights' # yolov3.weights contains the weights from a pre-trained model that uses the architecture defined in yolov3.cfg
class_path='config/coco.names' # class namaes of coco image dataset on wich the model was trained
img_size=416 # image size
conf_thres=0.8 # confidence threshold
nms_thres=0.4 #  non-maximum suppression threshold

# Load model and weights
model = Darknet(config_path, img_size=img_size) # from models
model.load_weights(weights_path)
#model.cuda() # parse the model to be computed on GPU
model.eval() # evaluation mode == don`t track the gradient
classes = utils.load_classes(class_path) # list with the name of classes from coco dataset

def pilimage(frame):
    # Creates an image memory from an object exporting the array interface
    return Image.fromarray(frame)

def preprocess(img):
    """
    Requires a Pillow image as input.
    """
    # transformation steps that will be applyed in the image
    ratio = min(img_size/img.size[0], img_size/img.size[1])
    imw = round(img.size[0] * ratio)
    imh = round(img.size[1] * ratio)
    img_transforms=transforms.Compose([transforms.Resize((imh,imw)),
                                       transforms.Pad((max(int((imh-imw)/2),0),
                                       max(int((imw-imh)/2),0), max(int((imh-imw)/2),0),
                                       max(int((imw-imh)/2),0)), (128,128,128)),
                                       transforms.ToTensor()])

    image_tensor = img_transforms(img) # apply transformation
    input_img = image_tensor.unsqueeze_(0)
    return input_img

def detect_image(input_img):
    """
    This is the function that will return detections for a specified image.
    """
    # run inference on the model and get detections
    with torch.no_grad():
        detections = model(input_img)
        detections = utils.non_max_suppression(detections, 80, conf_thres, nms_thres)

    return detections[0]


# Boundin box colors
colors=[(255,0,0),(0,255,0),(0,0,255),(255,0,255),(128,0,0),(0,128,0),(0,0,128),(128,0,128),(128,128,0),(0,128,128)]

# Creating a object tracker
mot_tracker = Sort()

# openning the video
vid = cv2.VideoCapture(videopath)


frames = 0
starttime = time.time()
while(True):
    ret, frame = vid.read() # Reading the video
    if not ret:
        break
    frames += 1
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pilimg = pilimage(frame)
    input_img = preprocess(pilimg)
    detections = detect_image(input_img) # get object detections from the actual frame
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Getting frame size references
    img = np.array(pilimg)
    pad_x = max(img.shape[0] - img.shape[1], 0) * (img_size / max(img.shape))
    pad_y = max(img.shape[1] - img.shape[0], 0) * (img_size / max(img.shape))
    unpad_h = img_size - pad_y
    unpad_w = img_size - pad_x

    if detections is not None:
        print(detections)
        tracked_objects = mot_tracker.update(detections.cpu())
        unique_labels = detections[:, -1].cpu().unique()
        n_cls_preds = len(unique_labels)
        #for x1, y1, x2, y2, obj_id, cls_pred in tracked_objects:
        for x1, y1, x2, y2, obj_id in tracked_objects:
            box_h = int(((y2 - y1) / unpad_h) * img.shape[0])
            box_w = int(((x2 - x1) / unpad_w) * img.shape[1])
            y1 = int(((y1 - pad_y // 2) / unpad_h) * img.shape[0])
            x1 = int(((x1 - pad_x // 2) / unpad_w) * img.shape[1])
            color = colors[int(obj_id) % len(colors)]
            #cls = classes[int(cls_pred)]
            cv2.rectangle(frame, (x1, y1), (x1+box_w, y1+box_h), color, 4)
            #cv2.rectangle(frame, (x1, y1-35), (x1+len(cls)*19+80, y1), color, -1)
            cv2.rectangle(frame, (x1, y1-35), (x1+1*19+80, y1), color, -1)
            #cv2.putText(frame, cls + "-" + str(int(obj_id)), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)
            cv2.putText(frame, "classe" + "-" + str(int(obj_id)), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)
    cv2.imshow('Stream',frame)
    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break

totaltime = time.time() - starttime
print(frames, "frames", totaltime/frames, "s/frame")
cv2.destroyAllWindows()
vid.release()
