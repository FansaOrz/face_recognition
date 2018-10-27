#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dlib
import cv2
import time
from face_train_use_keras import Model

def read_capture(detector):
    # 加载模型
    model = Model()
    model.load_model(file_path='./model/face.model.h5')

    num = 100
    video = cv2.VideoCapture(0)
    if video.isOpened():
        success, frame = video.read()
        while success:
            im = frame.copy()

            # dlib的人脸检测器只能检测80x80和更大的人脸，如果需要检测比它小的人脸，需要对图像上采样，一次上采样图像尺寸放大一倍
            # rects = detector(img,1) #1次上采样
            rects = detector(im, 0)
            print rects
            for rect in rects:  # rect.left(),rect.top(),rect.right(),rect.bottom()
                img2recog = im[rect.top() - 10: rect.bottom() + 10, rect.left() - 10: rect.right() + 10]
                faceID = model.face_predict(img2recog)
                if faceID == 0:
                    print "======================================================", faceID
                    cv2.rectangle(im, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)

                    # 文字提示是谁
                    cv2.putText(im, 'jiashi',
                                (rect.left() + 30, rect.top() - 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
                elif faceID == 1:
                    print "======================================================", faceID
                    cv2.rectangle(im, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)

                    # 文字提示是谁
                    cv2.putText(im, 'renzhongxing',
                                (rect.left() + 30, rect.top() - 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
                elif faceID == 2:
                    print "======================================================", faceID
                    cv2.rectangle(im, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)

                    # 文字提示是谁
                    cv2.putText(im, 'jingzhibo',
                                (rect.left() + 30, rect.top() - 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
                elif faceID == 3:
                    print "======================================================", faceID
                    cv2.rectangle(im, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)

                    # 文字提示是谁
                    cv2.putText(im, 'zhanghaiyang',
                                (rect.left() + 30, rect.top() - 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
            cv2.imshow('capture face detection', im)
            if cv2.waitKey(1) >= 0:
                break
            success, frame = video.read()
        cv2.destroyAllWindows()
        video.release()



if __name__ == '__main__':
    detector = dlib.get_frontal_face_detector()
    read_capture(detector)