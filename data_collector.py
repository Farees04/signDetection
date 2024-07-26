
import cv2
import os

directory= 'data/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')


for i in range(65,91):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')


cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()

    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    # cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(128,128))
    interrupt = cv2.waitKey(10)
    if 65 <= interrupt <= 90:
        letter = chr(interrupt)
        file_path = os.path.join(directory, letter +"/"+ str(len(os.listdir(directory+"/"+letter)))+".jpg")
        cv2.imwrite(file_path,frame)
    if interrupt == 96 :
        cv2.imwrite(os.path.join(directory+'blank/' + str(len(os.listdir(directory+"/blank"))))+ '.jpg',frame)
