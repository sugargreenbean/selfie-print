import face_recognition
from PIL import Image, ImageDraw

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load an image
img = face_recognition.load_image_file("static/selfie.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(img)
face_encodings = face_recognition.face_encodings(img, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pil_image = Image.fromarray(img)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    PIL_box=[left-50, top-150, right+50, bottom+50]
    crop_img = pil_image.crop(PIL_box)

# You can also save a copy of the new image to disk if you want by uncommenting this line
crop_img.save("static/cropselfie.jpg")
