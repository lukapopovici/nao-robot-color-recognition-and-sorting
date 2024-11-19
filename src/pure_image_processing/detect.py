import cv2
import numpy as np
import random
import os
from random import shuffle
from preprocess import preprocess_image


#Script helper pentru vizualizarea efectului preprocesarii asupra gasirii contururilor
def display_contours(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image {image_path} not found!")
        return
    
    useless,edges = preprocess_image(image)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_canvas = np.zeros_like(image)
    
    for contour in contours:
        color = [random.randint(0, 255) for _ in range(3)]  # Generam o culoare aleatorie sa vizualizam contururile
        cv2.drawContours(contour_canvas, [contour], -1, color, thickness=2) # si le desenam :))
    
    cv2.imshow(f"CONTUR - {os.path.basename(image_path)}", contour_canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show():
    folder_path = "samples"  
    image_files = ["1.jpg", "2.jpg", "3.jpg","4.png"] 
    shuffle(image_files) 

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"Processing: {image_file}")
        display_contours(image_path)


show()
cv2.destroyAllWindows()
