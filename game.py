import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False

score = [0,0]

while True:
    imgbg = cv2.imread("Resources/BG.png")
    success,img = cap.read()

    imgscale = cv2.resize(img,(0,0),None,0.875,0.875)
    imgscale = imgscale[:,80:480]


    hands,img = detector.findHands(imgscale)

    if startGame:
        if stateResult is False:
            timer = time.time()-initialTime
            cv2.putText(imgbg,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    if fingers == [0,0,0,0,0]:
                        playerMove = 1
                    if fingers == [1,1,1,1,1]:
                        playerMove = 2
                    if fingers == [0,1,1,0,0]:
                        playerMove = 3

                    randomNumber = random.randint(1,3)
                    imgAi = cv2.imread(f"Resources/{randomNumber}.png",cv2.IMREAD_UNCHANGED)
                    imgbg = cvzone.overlayPNG(imgbg,imgAi)


                    if (playerMove==1 and randomNumber==3) or (playerMove==2 and randomNumber==1) or (playerMove==3 and randomNumber==2):
                        score[1]+=1

                    if (playerMove ==3 and randomNumber==1)or (playerMove==1 and randomNumber==2)or(playerMove==2 and randomNumber ==3):
                        score[0]+=1
    
    imgbg[234:654,795:1195]=imgscale
    if stateResult:
        imgbg = cvzone.overlayPNG(imgbg,imgAi,[149,310])
    cv2.putText(imgbg,str(score[0]),(410,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6)
    cv2.putText(imgbg,str(score[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6)
    cv2.imshow("BG",imgbg)
    key = cv2.waitKey(1)
    if key==ord("s"):
        startGame = True
        initialTime = time.time()
        stateResult = False

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if score[0]>score[1]:
    print("AI wins")
elif score[1]>score[0]:
    print("Player wins")
else:
    print("Tie")