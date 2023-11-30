import sys
import cv2
import datetime
from random import randint

tracker_types = ['KCF', 'CSRT']
tracker_type = tracker_types[1]

if tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()

print(tracker)

video = cv2.VideoCapture('C:\\Users\\André\\Desktop\\opencv\\FREE STOCK FOOTAGE - Heavy traffic.mp4')

if not video.isOpened():
    print('[ERROR] video file not loaded')
    sys.exit()

ok, frame = video.read()

if not ok:
    print('[ERROR] no frame captured')
    sys.exit()

print('[INFO] video loaded and frame capture started')

bbox = cv2.selectROI(frame)

print('[INFO] select ROI and press ENTER or SPACE')
print('[INFO] cancel selection by pressing C')
print(bbox)

ok = tracker.init(frame, bbox)

if not ok:
    print('[ERROR] tracker not initialized')
    sys.exit()

print('[INFO] tracker was initialized on ROI')

colours = (randint(0, 255), randint(0, 255), randint(0, 255))

while True:
    ok, frame = video.read()

    if not ok:
        print('[INFO] end of video file reached')
        break

    ok, bbox = tracker.update(frame)

    print(ok, bbox)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), colours, 3)
        cv2.putText(frame, str(tracker_type), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    else:
        cv2.putText(frame, 'No Track', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

    cv2.imshow('Single Track', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
video_codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
prefix = 'recording/' + datetime.datetime.now().strftime("%y%m%d_%H%M%S")
basename = "object_track.mp4"
video_output = cv2.VideoWriter("_".join([prefix, basename]), video_codec, fps, (frame_width, frame_height))
video_output.write(frame)

video.release()
cv2.destroyAllWindows()
