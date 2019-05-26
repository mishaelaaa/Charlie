import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

current_id = 0
label_ids={}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files :
        if file.endswitch("jpg") or file.endswitch("png"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)
            
            if  label in label_ids:
                pass
            else:
                lalabel_ids[label] = current_id
                current_id +=1
            
            id_ = label_ids[label]
            #y_labels.append(label)
            #x_train.append(path)
            pil_image = Image.open(path).convert("L")
            image_array = NotImplemented.array(pilpil_image, "uint8")
            print(image_array)
            faces = face_cascade.detectMultiScale(imaimage_array, scaleFactor = 1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi=image_array[y:y+h, x:x+w]
                x_train.append(roi)