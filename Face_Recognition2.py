import face_recognition

from PIL import Image

img = face_recognition.load_image_file(r"C:\Users\Abhishika Agarwal\Desktop\Python_modules_for_AI_projects\Kohli_and_Dhoni.jpg")

loc = face_recognition.face_locations(img)

for face_location in loc:
    top,right,bottom,left = face_location
    face_img = img[top:bottom,left:right]

    Pil_img = Image.fromarray(face_img)
    # Pil_img.show()
    Pil_img.save(f'{top}.jpg')