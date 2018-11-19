# -*- coding: utf-8 -*-
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)

g = np.array([0,0])
 
while(1):
 
    # フレームを取得
    ret, frame = cap.read()
 
    # フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # 取得する色の範囲を指定する
    lower_yellow = np.array([40, 80, 70])
    upper_yellow = np.array([90, 255, 140])
 
    # 指定した色に基づいたマスク画像の生成
    img_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
 
    # フレーム画像とマスク画像の共通の領域を抽出する。
    img_color = cv2.bitwise_and(frame, frame, mask=img_mask)
 

    if np.count_nonzero(img_mask) > 0:      #マスクが存在するとき
        label = cv2.connectedComponentsWithStats(img_mask) #ラベリング

        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)  


        max_index = np.argmax(data[:,4])
  
        g =  center[max_index]      #一番面積が大きいマスクの重心

    print (g)

    frame = cv2.circle(frame, (int(g[0]),int(g[1])), 40, (0, 255, 0), 5, 8)
    cv2.imshow("SHOW COLOR IMAGE", frame)
 
    # qを押したら終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()