# Step 1: Import required libraries
import cv2
import matplotlib.pyplot as plt

# Step 2: Load Haar Cascade classifier (comes with OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 3: Define function for face detection on an image
def detect_faces_in_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert BGR to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Show the result
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title(f"Detected {len(faces)} Face(s)")
    plt.show()

# Step 4: Run detection on a test image
detect_faces_in_image('test.jpg')  # Replace with your image filename
# Step 5: Real-time webcam face detection
def detect_faces_webcam():
    cap = cv2.VideoCapture(0)  # 0 is the default webcam

    if not cap.isOpened():
        print("Cannot access webcam")
        return

    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Real-Time Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Uncomment to run real-time detection
# detect_faces_webcam()
