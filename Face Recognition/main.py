# Developed by Marcel Maty & Niklas Schmitz
import mysql.connector
from datetime import datetime
import cv2
import dlib
import face_recognition
import numpy as np
import base64
from io import BytesIO
from PIL import Image

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
face_buffer = []  # Buffer to store face names

# Load the pre-saved encodings and corresponding names
known_face_encodings = []
known_face_names = []
known_face_ID = []

# Function to add a new face


def add_new_face(name, image_path):
    # Load and encode the new face
    face_image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(face_image)[0]

    # Append the new face encoding and name to the lists
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)


# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="anwesenheit"
)

# Cursor erstellen
mycursor = mydb.cursor()

# Funktion zum Hinzufügen eines neuen Gesichts aus der Datenbank

# Developed by Marcel Maty & Niklas Schmitz
def add_face_from_db(Schueler_ID, name, base64_image):
    # Decodieren Sie das Base64-Bild und konvertieren Sie es in ein Numpy-Array
    image_bytes = base64.b64decode(base64_image)
    image = Image.open(BytesIO(image_bytes))
    image_array = np.array(image)

    # Codieren und hinzufügen des Gesichts
    face_encoding = face_recognition.face_encodings(image_array)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)
    known_face_ID.append(Schueler_ID)
    print(Schueler_ID, name)


# Abfrage, um Schülerdaten mit Gesichtsbildern aus der Datenbank abzurufen
mycursor.execute("SELECT Schueler_ID, Vorname, Gesicht FROM schueler")
schueler_data = mycursor.fetchall()

# Schleife zum Hinzufügen der Gesichter aus der Datenbank
for Schueler_ID, vorname, gesicht_base64 in schueler_data:
    add_face_from_db(Schueler_ID, vorname, gesicht_base64)
    Schueler_ID = 0

# Capture video from your webcam (you can also use an image or video file)
video_capture = cv2.VideoCapture(0)

check = 1

while check:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Reset the face buffer
    face_buffer = []

    # Loop through each face in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the current face encoding with the known face encodings
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)

        name = "Unknown"
        Schueler_ID = 0  # Setze Schueler_ID auf 0 für jedes neue Gesicht

        # If a match is found, use the name of the known person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            Schueler_ID = known_face_ID[first_match_index]
        # Add the name to the buffer
        face_buffer.append(name)
        face_buffer.append(Schueler_ID)
        # Draw a rectangle and label the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, str(Schueler_ID), (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)
    # Display the resulting image with faces identified
    cv2.imshow('Video', frame)

    # Exit the program by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print(Schueler_ID)
    if Schueler_ID != 0:
        ID = int(Schueler_ID)
        print(ID)
        mycursor.execute(
            "SELECT Anwesenheit_ID, gangzeit FROM anwesenheit WHERE Schueler_ID = %s ORDER BY Anwesenheit_ID DESC LIMIT 1; ", (ID,))
        result = mycursor.fetchone()
        Anwesenheit_ID = result[0]
        gangzeit = result[1]
        if str(gangzeit) != "None":
            print("Neue anwesenheit")
            now = datetime.now()
            Ankunftszeit = now.strftime('%Y-%m-%d %H:%M:%S')
            mycursor.execute(
                "Insert into anwesenheit(Ankunftszeit,Schueler_ID) Values(%s,%s)", (Ankunftszeit, ID,))
            mydb.commit()
            check = 0
        else:
            now = datetime.now()
            print("anwesenheit Update")
            gangzeit = now.strftime('%Y-%m-%d %H:%M:%S')
            mycursor.execute(
                "UPDATE anwesenheit SET Gangzeit = %s WHERE anwesenheit.Anwesenheit_ID = %s", (gangzeit, Anwesenheit_ID))
            mydb.commit()
            check = 0

# Release the webcam and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()

# Developed by Marcel Maty & Niklas Schmitz