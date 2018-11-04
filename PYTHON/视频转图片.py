import cv2
videoFile = '/Users/fanc/Downloads/PeppaPig.mp4'
outputFile = '/Users/fanc/Downloads/image/frame'
vc = cv2.VideoCapture(videoFile)
c = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    print('openerror!')
    rval = False

timeF = 10  #视频帧计数间隔次数
while rval:
    #print(c)
    rval, frame = vc.read()
    if c % timeF == 0:
        print('write')
        cv2.imwrite(outputFile + str(int(c / timeF) - 1) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
vc.release()
