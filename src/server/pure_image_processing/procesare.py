import cv2
import numpy as np
import os
from preprocess import preprocess_image
folder_path = "samples" 

#declarare manuala a imaginilor de test
image_files = ["1.jpg", "2.jpg", "3.jpg","4.png","5.png","6.png","7.png"]


def find_longest_contour(image, edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    max_length = 0
    longest_contour = None
    
    for contour in contours:
        length = cv2.arcLength(contour, closed=False)
        if length > max_length:
            max_length = length
            longest_contour = contour
    
    output_image = image.copy()
    if longest_contour is not None:
        cv2.drawContours(output_image, [longest_contour], -1, (0, 255, 0), 2)
    
    return longest_contour, output_image



def get_average_color(image, contour):
    #media aritmetica a culorilor dintr-un contur
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    mean_color = cv2.mean(masked_image, mask=mask)[:3]  
    return tuple(map(int, mean_color))  


#dupa valorile rgb ale culorilor, am clasificat culorile in N categorii...
def classify_color(rgb_color):
    r, g, b = rgb_color
    
    if r > 200 and g < 100 and b < 100:
        return "Red"
    elif r > 200 and g > 150 and b < 100:
        return "Orange"
    elif r > 200 and g > 200 and b < 100:
        return "Yellow"
    elif r < 150 and g > 200 and b < 150:
        return "Green"
    elif r < 100 and g > 200 and b > 200:
        return "Cyan"
    elif r < 100 and g < 150 and b > 200:
        return "Blue"
    elif r > 150 and g < 100 and b > 150:
        return "Purple"
    elif r > 100 and g < 100 and b < 100:
        return "Dark Red"
    elif r < 100 and g < 100 and b < 100:
        return "Black"
    elif r > 200 and g > 200 and b > 200:
        return "White"
    elif r > 150 and g > 150 and b > 150:
        return "Light Gray"
    elif r > 100 and g > 100 and b > 100:
        return "Gray"
    elif r > 100 and g > 50 and b < 50:
        return "Brown"
    elif r > 150 and g < 50 and b > 50:
        return "Magenta"
    elif r < 50 and g > 50 and b > 150:
        return "Indigo"
    else:
        return "Unknown"



def process_images(folder_path, image_files):
    for file_name in image_files:
        file_path = os.path.join(folder_path, file_name)
        
        img = cv2.imread(file_path)
        
        if img is None:
            print(f"Failed to read {file_name}. Skipping.")
            continue

        resized_img, edges = preprocess_image(img)
        closest_contour, output_img = find_longest_contour(resized_img, edges)
        
        if closest_contour is not None:
            avg_color = get_average_color(resized_img, closest_contour)
            # Dintr-un motiv sau altul totul e BGR , il convertim in RGB :((
            avg_color = avg_color[::-1]
            print(f"Average color (RGB) of the object in {file_name}: {avg_color}")
            color_name = classify_color(avg_color)
            print(f"The object is likely: {color_name}")
            cv2.drawContours(output_img, [closest_contour], -1, (0, 255, 0), 2)
            cv2.imshow(f"Processed {file_name}", output_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()  

        else:
            print(f"No valid contour found in {file_name}. Check the input folder or images.")
            continue


#functia care va fi importata si folosita in server


def PROCESARE(img):
    if img is None:
        return "Error: Unable to load image"
    
    resized_img, edges = preprocess_image(img)
    closest_contour, output_img = find_longest_contour(resized_img, edges)
    
    if closest_contour is not None:
        avg_color = get_average_color(resized_img, closest_contour)
        avg_color = avg_color[::-1]
        #print(f"Average color (RGB): {avg_color}")
        color_name = classify_color(avg_color)
        return color_name
    else:
        return "INVALID! NO CONTOUR FOUND!"

process_images(folder_path, image_files)
cv2.destroyAllWindows()
