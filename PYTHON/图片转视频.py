import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from subprocess import call


img_root = '/Users/fanc/Downloads/image/'
out_root = '/Users/fanc/Downloads/image/PeppaPig.avi'
# Edit each frame's appearing time!
fps = 20
fourcc = VideoWriter_fourcc(*"MJPG")  #支持jpg
videoWriter = cv2.VideoWriter(out_root, fourcc, fps, (640, 480))
im_names = os.listdir(img_root)
print(len(im_names))
for im_name in range(len(im_names) - 2):
    string = img_root + 'frame' + str(im_name) + '.jpg'
    print(string)
    frame = cv2.imread(string)
    frame = cv2.resize(frame, (640, 480))
    videoWriter.write(frame)

videoWriter.release()

dir = out_root.strip(".avi")
command = "ffmpeg -i %s.avi %s.mp4" % (dir, dir)
call(command.split())