import cv2;
image=cv2.imread("poster.jpg")
#cv2.imshow("Display Image",image)
rocket=image[120:360,400:500]
#cv2.imshow("Rocket",rocket)

image[0:240,500:600]=rocket
texttoshow="Rocket is here"
cv2.putText(image,texttoshow,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(100,150,250))
cv2.imshow("Edited Image",image)
cv2.waitKey(0)