import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)
time.sleep(2)
bg=0

for i in range(60):
    ret,bg=cap.read()

bg=np.flip(bg,axis=1)

while(cap.isOpen()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.filp(img,axis=1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    u_black=np.array([104,153,70])
    l_black=np.array([30,30,70])
    mask=cv2.inRange(hsv,u_black,l_black)

    res=cv2.bitWise_and(img,img,mask=mask)

    final_output=cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)
    cv2.imshow("magic",final_output)
    cv2.weightKey(1)
    

cap.release()
out.release()
cv2.destroyAllWidows()