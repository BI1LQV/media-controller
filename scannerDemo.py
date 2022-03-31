#!/usr/bin/env python
# coding: utf-8

# # 导入工具包

# In[1]:


# opencv-python
from typing import Sequence
import cv2
# 时间库
import time
# mediapipe人工智能工具包
import mediapipe as mp
# 导入python绘图matplotlib
import matplotlib.pyplot as plt
import time 

print('trainend')
# # 导入模型

# In[2]:
SCAN_TIME=1

# 导入solution
mp_hands = mp.solutions.hands
# 导入模型
hands = mp_hands.Hands(static_image_mode=False,        # 是静态图片还是连续视频帧
                       max_num_hands=2,                # 最多检测几只手
                       min_detection_confidence=0.7,   # 置信度阈值
                       min_tracking_confidence=0.5)    # 追踪阈值
# 导入绘图函数
mpDraw = mp.solutions.drawing_utils


# # 处理单帧的函数

# In[3]:

imgBuffer = []

# 处理帧函数
def process_frame(img):
    # 水平镜像翻转图像，使图中左右手与真实左右手对应
    # 参数 1：水平翻转，0：竖直翻转，-1：水平和竖直都翻转
    img = cv2.flip(img, 1)
    # BGR转RGB
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 将RGB图像输入模型，获取预测结果
    results = hands.process(img_RGB)

    h, w = img.shape[0], img.shape[1]  # 获取图像宽高

    if results.multi_hand_landmarks:  # 如果有检测到手
        # 遍历每一只检测出的手
        for hand_idx in range(len(results.multi_hand_landmarks)):
            hand_21 = results.multi_hand_landmarks[hand_idx]  # 获取该手的所有关键点坐标
            mpDraw.draw_landmarks(
                img, hand_21, mp_hands.HAND_CONNECTIONS)  # 可视化
            # 记录左右手信息
            temp_handness = results.multi_handedness[hand_idx].classification[0].label

            cz0 = hand_21.landmark[0].z  # 获取手腕根部深度坐标
            # print(temp_handness)
            xyz = []
            for i in range(21):  # 遍历该手的21个关键点
                # 获取3D坐标
                cx = int(hand_21.landmark[i].x * w)
                cy = int(hand_21.landmark[i].y * h)
                cz = hand_21.landmark[i].z
                cc = [cx, cy, cz]
                xyz.append(cc)
            # print(xyz)
            print(xyz)
            imgBuffer.append(xyz)

    return img



# time.sleep(3)
# 获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0)
success, image = cap.read()

# 打开cap
cap.open(0)

capTimeSequence=[]

def process():
        # 获取画面
    success, frame = cap.read()
    if not success:
        print('Error')
        return

    # !!!处理帧函数
    frame = process_frame(frame)

    # 展示处理后的三通道图像
    cv2.imshow('my_window', frame)
    capTimeSequence.append(time.time())
    if capTimeSequence[-1]-capTimeSequence[0]>=1:
        imgBuffer 7*21*3*1
        capTimeSequence 7*1
       #复杂逻辑
       rpc([5*21*3:1])
       imgBuffer=[]
       capTimeSequence=[]


# 无限循环，直到break被触发
while cap.isOpened():
    process()


# 关闭摄像头
cap.release()

# 关闭图像窗口
cv2.destroyAllWindows()
