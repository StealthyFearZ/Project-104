import cv2

img = cv2.imread('/Users/daksh.raghuvanshi.24/Desktop/PRO-104-Project-Image-main/solar-system.jpg')

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Mercury",(120,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Venus",(220,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Earth",(320,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Moon",(320,100),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Mars",(420,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Jupiter",(620,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Saturn",(820,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Neptune",(920,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Uranus",(1100,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))

cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow('output',img)
cv2.waitKey(0)



