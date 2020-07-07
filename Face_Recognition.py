import face_recognition

img = face_recognition.load_image_file(r"C:\Users\Abhishika Agarwal\Desktop\Python_modules_for_AI_projects\Virat Kohli.jpg")

loc = face_recognition.face_locations(img)

# print(loc)

print(f'There are {len(loc)} people in this image')
