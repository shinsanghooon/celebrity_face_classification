import os
import cv2

face_cascade = cv2.CascadeClassifier('/Users/sinsanghun/anaconda/pkgs/opencv-2.4.11-py27_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('/Users/sinsanghun/anaconda/pkgs/opencv-2.4.11-py27_1/share/OpenCV/haarcascades/haarcascade_eye.xml')

lst = ["김혜수", "엄지원", "라미란", "심은하", "김민희"]

for name in lst:
    for i in range(500):
        os.chdir(pwd)
        os.chdir(pic_location + name)
        try:
            filename = name + str(i+1) + ".jpg"
            img = cv2.imread(filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3,5)
            print(faces)
            if len(faces)!=0:
                for (x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
                    cropped = img[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]
                    eyes = eye_casecade.detectMultiScale(roi_gray)
                    #for (ex, ey, ew, eh) in eyes:
                    #   cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

                    #cv2.imshow('Image view', roi_gray)
                    cv2.imwrite(filename, roi_gray)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
        except:
            print("not picture")
            pass
