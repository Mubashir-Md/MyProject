import cv2
import face_recognition as fr

font = cv2.FONT_HERSHEY_DUPLEX#setting the font

maaz = fr.load_image_file('C:/Users/mdmub/Documents/Python/maaz new.jpg')
Mlocate = fr.face_locations(maaz)[0]
Mencode = fr.face_encodings(maaz)[0]

messi = fr.load_image_file('C:/Users/mdmub/Documents/Python/messi.jpg')
Melocate = fr.face_locations(messi)[0]
Meencode = fr.face_encodings(messi)[0]

asim = fr.load_image_file('C:/Users/mdmub/Documents/Python/asim.jpeg')
Aslocate = fr.face_locations(asim)[0]
Asencode = fr.face_encodings(asim)[0]

ahmed = fr.load_image_file('C:/Users/mdmub/Documents/Python/ahmed.jpeg')
Alocate = fr.face_locations(ahmed)[0]
Aencode = fr.face_encodings(ahmed)[0]


mubashir = fr.load_image_file('C:/Users/mdmub/Documents/Python/mubashir.jpeg')
Mublocate = fr.face_locations(mubashir)[0]
Mubencode = fr.face_encodings(mubashir)[0]

allEncodings = [Mencode,Meencode,Asencode,Aencode,Mubencode]
allPhotos = ['Maaz','Messi','Asim','Ahmed','Mubashir']

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

Newbie = fr.load_image_file('C:/Users/mdmub/Documents/Python/NewPicture.jpg')
NewBGR = cv2.cvtColor(Newbie,cv2.COLOR_RGB2BGR)
NewLocations = fr.face_locations(Newbie)
NewEncodings = fr.face_encodings(Newbie)

for NewLoc,NewEnc in zip(NewLocations,NewEncodings):
    top,right,bottom,left = NewLoc
    cv2.rectangle(NewBGR,(left,top),(right,bottom),(0,255,0),3)
    name = 'Unknown'
    matcher = fr.compare_faces(allEncodings,NewEnc)
    if True in matcher:
        matchIndex = matcher.index(True)
        name = allPhotos[matchIndex]
    cv2.putText(NewBGR,name,(left,top),font,1,(255,0,0),2)
cv2.imshow('Mubashir',NewBGR)
cv2.waitKey(9000)
