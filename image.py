#myenv/Scripts/activate 
import math
import cv2
import cvzone
from ultralytics import YOLOgit remote add origin https://github.com/shalinimimrot/Object-Detection-.git


model = YOLO("ppe.pt") 


classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 
              'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']


img = cv2.imread("ppe4.jpg")  


results = model(img, stream=True)
for r in results:
    boxes = r.boxes
    for box in boxes:
  
        x1, y1, x2, y2 = box.xyxy[0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1

       
        conf = math.ceil((box.conf[0] * 100)) / 100
      
        cls = int(box.cls[0])
        currentClass = classNames[cls]
        
      
        print(currentClass)
        
        if conf > 0.5:
            if currentClass in ['NO-Hardhat', 'NO-Safety Vest', 'NO-Mask']:
                myColor = (0, 0, 255) 
            elif currentClass in ['Hardhat', 'Safety Vest', 'Mask']:
                myColor = (0, 255, 0)  
            else:
                myColor = (255, 0, 0) 

            
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                               (max(0, x1), max(35, y1)), scale=1, thickness=1, colorB=myColor,
                               colorT=(255, 255, 255), colorR=myColor, offset=5)
            
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()