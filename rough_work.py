import cv2
import numpy as np

cap = cv2.VideoCapture('MerryGoRound_high_res.mp4') #Open Video File, from current directory
#Choose output format and name
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output_harris_merry.avi",fourcc,10.0,(1920,1080)) #make sure the dimensions are the same size as input data 

n=0

while(cap.isOpened()):
        

    ret, img = cap.read()

    if ret==False:
        break
    
    out.write(img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        break 

cap.release()
out.release()
cv2.destroyAllWindows()
print("o.O.o")