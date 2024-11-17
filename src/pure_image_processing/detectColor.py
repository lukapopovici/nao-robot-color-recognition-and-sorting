import cv2
import numpy as np
import os

folder_path = "samples" 

image_files = ["1.jpg", "2.jpg", "3.jpg"]

def preprocess_image(image):
    resized = cv2.resize(image, (500, 500))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    #Aplicam GaussianBlur pentru a reduce zgomotul din imagine si a face detectia mai usoara
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    #Aplicam Canny Edge Detector pentru a detecta marginile
    edges = cv2.Canny(cleaned, 50, 150)

    return resized, edges

###gasire contur bazat pe punctul de centru al ... conturului   
def find_closest_contour(image, edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    img_center = np.array([image.shape[1] // 2, image.shape[0] // 2])
    min_distance = float('inf')
    closest_contour = None
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 500: 
            continue
        
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            centroid = np.array([cx, cy])
            
            distance = np.linalg.norm(centroid - img_center)
            if distance < min_distance:
                min_distance = distance
                closest_contour = contour
    
    output_image = image.copy()
    if closest_contour is not None:
        cv2.drawContours(output_image, [closest_contour], -1, (0, 255, 0), 2)
    
    return closest_contour, output_image

def get_average_color(image, contour):
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    avg_color = cv2.mean(masked_image, mask=mask)[:3]  
    return avg_color

#Clasificam culorule bazat pe hue
#functie bazta pe thresholding 
#practic vorbind e un placeholder
def classify_color(bgr_color):
    hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]
    hue = hsv_color[0]

    if hue >= 0 and hue <= 10:
        return "Red"
    elif hue > 10 and hue <= 50:
        return "Orange"
    elif hue > 50 and hue <= 90:
        return "Yellow"
    elif hue > 90 and hue <= 170:
        return "Green"
    elif hue > 170 and hue <= 260:
        return "Blue"
    elif hue > 260 and hue <= 320:
        return "Purple"
    else:
        return "Red"  

for file_name in image_files:
    file_path = os.path.join(folder_path, file_name)
    img = cv2.imread(file_path)
    
    resized_img, edges = preprocess_image(img)
    closest_contour, output_img = find_closest_contour(resized_img, edges)
        
    if closest_contour is not None:
        cv2.imshow(f"Processed {file_name}", output_img)
        print(f"Showing: {file_name}")
            
        avg_color = get_average_color(resized_img, closest_contour)
        print(f"Average color (BGR) of the object in {file_name}: {avg_color}")
            
        color_name = classify_color(avg_color)
        print(f"The object is likely: {color_name}")
        
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
    else:
        print(f"NU RULEZI SCRIPTUL IN FOLDERFUL CORECT")
