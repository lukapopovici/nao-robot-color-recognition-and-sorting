import cv2
import numpy as np
import os


def preprocess_image(image):
    # 30% Zoom pentru eliminarea marginilor inutile din background
    height, width = image.shape[:2]
    center_x, center_y = width // 2, height // 2
    zoom_factor = 0.3  
    
    # Operatiune de resize pentru a ...
    # Putea sa aleg chestii precum conturui dupa valori pe care ma pot baza ca au o limita
    crop_x = int(center_x * zoom_factor)
    crop_y = int(center_y * zoom_factor)
    cropped = image[center_y - crop_y:center_y + crop_y, center_x - crop_x:center_x + crop_x]
    resized = cv2.resize(cropped, (500, 500))


    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)

    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
   
    edges = cv2.Canny(cleaned, 50, 150)
    
    return resized, edges