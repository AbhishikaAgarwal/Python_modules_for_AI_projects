import face_recognition

img = face_recognition.load_image_file(r"C:\Users\Abhishika Agarwal\Desktop\Python_modules_for_AI_projects\Virat Kohli.jpg")

encoding_img = face_recognition.face_encodings(img)[0]

nxt_img = face_recognition.load_image_file(r"C:\Users\Abhishika Agarwal\Desktop\Python_modules_for_AI_projects\tom_and_jerry.jpg")

encoding_nxt_img = face_recognition.face_encodings(nxt_img)[0]

result = face_recognition.compare_faces([encoding_img], encoding_nxt_img)

if result[0]:
    print('This is Virat Kohli')
else:
    print('Not Virat Kohli')    