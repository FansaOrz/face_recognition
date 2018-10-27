#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dlib
import cv2
import time


def read_capture(detector):
    num = 100
    cap = cv2.VideoCapture(0)
    success, frame = cap.read()

    while success:
        img_np = frame.copy()
        '''
        msg = VideoDev.getImageRemote(rgb_top)
        w = msg[0]
        h = msg[1]
        c = msg[2]
        data = msg[6]
        ba = str(bytearray(data))
        nparr = np.fromstring(ba, np.uint8)
        img_np = nparr.reshape((h, w, c))
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        '''
        # dlib的人脸检测器只能检测80x80和更大的人脸，如果需要检测比它小的人脸，需要对图像上采样，一次上采样图像尺寸放大一倍
        # rects = detector(img,1) #1次上采样
        rects = detector(img_np, 0)
        print rects
        if len(rects) != 0:
            img_name = '%s%d.jpg'%('/home/jiashi/Pictures/keras_dataset/zhangjiashi/', num)
            num += 1

        for rect in rects:  # rect.left(),rect.top(),rect.right(),rect.bottom()
            if len(rects) != 0:
                img2save = img_np[rect.top() - 10: rect.bottom() + 10, rect.left() - 10: rect.right() + 10]
                cv2.imwrite(img_name, img2save)
                print "=================="
                print rect.left()
                print rect.right()
                print rect.top()
                print rect.bottom()
            cv2.rectangle(img_np, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)
        cv2.imshow('capture face detection', img_np)
        if cv2.waitKey(1) >= 0:
            break
        success, frame = cap.read()
    cv2.destroyAllWindows()
    cap.release()



if __name__ == '__main__':
    detector = dlib.get_frontal_face_detector()
    read_capture(detector)
