#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:14:43 2024
@author: bernard
"""
import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

video_path = "/Users/bernard/airsea/bernard/code/UCONN/wave_flume/demo/data/*.mov"
#video_path = "/Users/bernard/airsea/bernard/code/UCONN/wave_flume/demo/data/*test2.mov"


video_files = sorted(glob.glob(video_path))


wave_id = 4#2#1 #0
video_file = video_files[wave_id]
print(video_file)

#===================================== SELECT CALIBARTION FRAME==================================
cap = cv2.VideoCapture(video_files[wave_id])
calibration_frame = 10 #117

if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    cap.set(cv2.CAP_PROP_POS_FRAMES, calibration_frame)
    frame_number = calibration_frame  
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    paused = False 

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:  
                cap.set(cv2.CAP_PROP_POS_FRAMES, calibration_frame)
                frame_number = calibration_frame
                continue
            frame_number += 1 
        
        text = f"Frame: {frame_number:03d}"  
        font_scale = 1.5
        font_thickness = 4
        font = cv2.FONT_HERSHEY_SIMPLEX

       
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
        box_coords = ((10, 10), (10 + text_width + 10, 10 + text_height + 10))
        cv2.rectangle(frame, box_coords[0], box_coords[1], (0, 0, 0), cv2.FILLED)
        cv2.putText(frame, text, (15, 10 + text_height), font, font_scale, (255, 255, 255), font_thickness)
        cv2.imshow("UCONN AirSea Lab", frame)
        key = cv2.waitKey(30) & 0xFF
        if key == ord(' '):  
            paused = not paused
        elif key == ord('q'):  # 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()


#===================================CALIBATE=======================================

cap = cv2.VideoCapture(video_file)
#calibration_frame = 2
cap.set(cv2.CAP_PROP_POS_FRAMES, calibration_frame)
ret, img = cap.read()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize = (26,5))
plt.tight_layout()
plt.imshow(img, cmap = 'RdBu', vmin = 0, vmax = 255)
plt.title("Calibration Horizontally", fontsize = 30)
plt.xlabel("Visit us @UCONN.AirSea-Lab RM142", fontsize = 18, labelpad= 9)
points_hor = plt.ginput(2)  
plt.close()

points_hor = np.array(points_hor)
gap_pixel_x = abs(points_hor[0][0] - points_hor[1][0])

known_hor_mm = float(input("Enter the known length between selected points on the ruler (in mm): "))
fac_x = known_hor_mm / gap_pixel_x
print(f"Pixel-to-mm conversion factor: {fac_x:.2f} mm/pixel")


##calb vert

plt.figure(figsize = (26,5))
plt.tight_layout()
plt.imshow(img, cmap = 'RdBu', vmin = 0, vmax = 255)
plt.title("Calibration Vertically", fontsize = 30)
plt.xlabel("Visit us @UCONN.AirSea-Lab RM142", fontsize = 18, labelpad= 9)
points_vert = plt.ginput(2)  
plt.close()


points_vert = np.array(points_vert)
gap_pixel_y = abs(points_vert[0][1] - points_vert[1][1])


# points = np.array(points)
# pixel_distance = np.linalg.norm(points[1] - points[0])

known_vert_mm = float(input("Enter the known vertical dots on the white tape (in mm): "))
#known_vert_mm = 150
fac_y = known_vert_mm / gap_pixel_y
print(f"Pixel-to-mm conversion factor: {fac_y:.2f} mm/pixel")




#==================================measure wave_lenght===================================
frame = img.copy()
#frame[0:100, :] = 0
#frame[220:, :] = 0


plt.figure(figsize = (26,5))
plt.tight_layout()
#plt.imshow(frame, cmap = 'gray', vmin = 0, vmax = 255)
plt.imshow(frame, vmin = 0, vmax = 255)

plt.title("Measure Wave lenght", fontsize = 35)
points_wavelength = plt.ginput(2)  
plt.close()



wavelenght = fac_x * (points_wavelength[1][0]- points_wavelength[0][0])
print(f'The wavelength is = {wavelenght} mm')



#============================= measure wave_height ==========================================
plt.figure(figsize = (26,5))
plt.tight_layout()
plt.imshow(frame, cmap = 'gray', vmin = 0, vmax = 255)
plt.title("Measure Wave Height", fontsize = 35)
points_waveheight = plt.ginput(2)  
plt.close()

waveheight = fac_y * abs(points_waveheight[1][1] - points_waveheight[0][1])
print(f'The wave Height is = {waveheight} mm')




#============================ WAVE PERIOD ================================================

cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0
    paused = False  

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:  
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0) #loop video 
                frame_number = 0
                continue
            frame_number += 1 


        text = f"Frame: {frame_number:03d}" 
        font_scale = 1.5
        font_thickness = 4
        font = cv2.FONT_HERSHEY_SIMPLEX

        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
        box_coords = ((10, 10), (10 + text_width + 10, 10 + text_height + 10))
        cv2.rectangle(frame, box_coords[0], box_coords[1], (0, 0, 0), cv2.FILLED)
        cv2.putText(frame, text, (15, 10 + text_height), font, font_scale, (255, 255, 255), font_thickness)
        cv2.imshow("Measure Wave Period", frame)
        
        slow_speed_delay = 500  # Set delay to 100 ms for slower playback
        key = cv2.waitKey(slow_speed_delay) & 0xFF
        if key == ord(' '): 
            paused = not paused
        elif key == ord('q'):  # 'q' to quit
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
#====================calculate the period

start_frame= 21#19#6 #27 #6 #11 #29 #12 #58
stop_frame = 30#28#17 #42 #20 #25 #3 #25 #66
fps = 30

period = (stop_frame - start_frame)/fps
print(f'The period is = {period} seconds')
print(f'The frequency is = {1/period} Hz')




# ##Calibration checks
# Ih, Iw = np.shape(img)
# Iw*fac
