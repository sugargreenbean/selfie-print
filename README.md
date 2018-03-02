# selfie-print
3D Print the outline contours from a selfie
TODO: Clean up code, take in command line arguments instead of hard code, full requirements listed, test on 3D printer

# Requirements

Install OpenCV

Install DLIB

Install face_recognition

# Step 1: Take a Selfie
![](/static/selfie.jpg "Input Selfie, Format JPG")

# Step 2: Recognize face, create bounding box, and crop
![](/static/cropselfie.jpg "Cropped Selfie")

# Step 3: Find edges, find and draw contours
![](/static/outlinedselfie.jpg "Outlined Selfie")

# Step 4: JPG => PNG => PNM => SVG Selfie
![](/static/vectorselfie.svg "SVG Selfie")

# Step 5: SVG => STL
![](/static/stl.jpg "STL in Autodesk Fusion 360")

![](/static/stlrotate.jpg "Rotate STL in Autodesk Fusion 360")
