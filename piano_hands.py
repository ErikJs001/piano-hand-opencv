# Erik Josías González Lucas | 25 - Dic - 2021

# Libraries for Images from Phone
import requests
import numpy as np
import imutils

# OpenCV library
import cv2

# Hank tracking with mediapipe
import hand_tracking as ht

# Libraries for sounds
import pygame
from pydub import AudioSegment
from pydub.playback import play

# We draw the reference points of the piano
def draw_lines(frame):
    # Flats Notes [Db, Eb, Gb, Ab, Bb]
    # Db
    cv2.line(frame, (50, 0), (50, 150), (0, 0, 0), 5)
    cv2.line(frame, (100, 0), (100, 150), (0, 0, 0), 5)
    cv2.line(frame, (50, 150), (100, 150), (0, 0, 0), 5)

    # Eb
    cv2.line(frame, (150, 0), (150, 150), (0, 0, 0), 5)
    cv2.line(frame, (200, 0), (200, 150), (0, 0, 0), 5)
    cv2.line(frame, (150, 150), (200, 150), (0, 0, 0), 5)

    # Gb
    cv2.line(frame, (300, 0), (300, 150), (0, 0, 0), 5)
    cv2.line(frame, (350, 0), (350, 150), (0, 0, 0), 5)
    cv2.line(frame, (300, 150), (350, 150), (0, 0, 0), 5)

    # Ab
    cv2.line(frame, (400, 0), (400, 150), (0, 0, 0), 5)
    cv2.line(frame, (450, 0), (450, 150), (0, 0, 0), 5)
    cv2.line(frame, (400, 150), (450, 150), (0, 0, 0), 5)

    # Bb
    cv2.line(frame, (500, 0), (500, 150), (0, 0, 0), 5)
    cv2.line(frame, (550, 0), (550, 150), (0, 0, 0), 5)
    cv2.line(frame, (500, 150), (550, 150), (0, 0, 0), 5)

    # Natural Notes [C, D, E, F, G, A, B]
    # C
    cv2.line(frame, (1, 0), (1, 250), (255, 255, 255), 5)
    cv2.line(frame, (75, 150), (75, 250), (255, 255, 255), 5)
    cv2.line(frame, (1, 250), (75, 250), (255, 255, 255), 5)

    # D
    cv2.line(frame, (75, 250), (125, 250), (255, 255, 255), 5)
    cv2.line(frame, (175, 150), (175, 250), (255, 255, 255), 5)
    cv2.line(frame, (125, 250), (175, 250), (255, 255, 255), 5)

    # E
    cv2.line(frame, (250, 0), (250, 250), (255, 255, 255), 5)
    cv2.line(frame, (175, 250), (250, 250), (255, 255, 255), 5)

    # F
    cv2.line(frame, (325, 150), (325, 250), (255, 255, 255), 5)
    cv2.line(frame, (175, 250), (325, 250), (255, 255, 255), 5)

    # G
    cv2.line(frame, (425, 150), (425, 250), (255, 255, 255), 5)
    cv2.line(frame, (325, 250), (425, 250), (255, 255, 255), 5)

    # A
    cv2.line(frame, (525, 150), (525, 250), (255, 255, 255), 5)
    cv2.line(frame, (425, 250), (525, 250), (255, 255, 255), 5)

    # B
    cv2.line(frame, (625, 0), (625, 250), (255, 255, 255), 5)
    cv2.line(frame, (525, 250), (625, 250), (255, 255, 255), 5)

    return frame

# Get the sound paths
def path_sound(note):
    path = "Sounds/" + note +"4.wav"

    return path

# Define the screen dimensions
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = ht.handDetector(detectionCon = 0.7)

# Index fingers
# Thumb - index - middle - ring - little finger
index_fingers = [4, 8, 12, 15, 20]

# Index of sounds
keys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


# Substitute the IP Camera address of your application
#url = "http://192.168.100.26:8080/shot.jpg"

# Start pygame for sounds
pygame.init()
pygame.mixer.init()

# We assign an empty sound to begin to gather the others.
sound_empty = AudioSegment.from_file("Sounds/empty.wav")
sound2 = AudioSegment.from_file("Sounds/empty.wav")
combined = sound_empty.overlay(sound2)
print(type(combined))

while True:
    # IMAGE - PHONE
    # Obtain the image from the phone
    """ 
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = imutils.resize(frame, width=1000, height=1800)

    frame = cv2.imdecode(img_arr, -1)

    frame = cv2.flip(frame, 1)
    """

    # IMAGE - WEBCAM
    ret, frame = cap.read()

    # Detect hands 
    frame = detector.findHands(frame)

    # Draw the lines of an octave
    frame = draw_lines(frame)

    # Obtain the positions of the fingers
    lmList = detector.findPositions(frame, draw=False)
    if len(lmList) != 0:

        # Iterate through all the fingers to know their positions and if they are touching any key.
        for i in index_fingers:
            x, y = lmList[i][1], lmList[i][2]

            # Natural Notes [C - D - E - F - G - A - B]
            # C
            if x > 1 and x < 75 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[0]))

            # D
            elif x > 75 and x < 175 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[2]))
                
            # E
            elif x > 175 and x < 250 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[4]))
                
            # F
            elif x > 250 and x < 325 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[5]))
            
            # G
            elif x > 325 and x < 425 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[7]))
                
            # A
            elif x > 425 and x < 525 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[9]))
                
            # B
            elif x > 525 and x < 625 and y > 150 and y < 250:
                sound2 = AudioSegment.from_file(path_sound(keys[11]))
                
            # Flats Notes [Db, Eb, Gb, Ab, Bb]
            # Db
            elif x > 50 and x < 100 and y > 0 and y < 150:
                sound2 = AudioSegment.from_file(path_sound(keys[1]))
            
            # Eb
            elif x > 150 and x < 200 and y > 0 and y < 150:
                sound2 = AudioSegment.from_file(path_sound(keys[3]))
                
            # Gb
            elif x > 300 and x < 350 and y > 0 and y < 150:
                sound2 = AudioSegment.from_file(path_sound(keys[6]))
                
            # Ab
            elif x > 400 and x < 450 and y > 0 and y < 150:
                sound2 = AudioSegment.from_file(path_sound(keys[8]))
                
            # Bb
            elif x > 500 and x < 550 and y > 0 and y < 150:
                sound2 = AudioSegment.from_file(path_sound(keys[10]))
            
            combined = combined.overlay(sound2)
            combined.export("Sounds/combined.wav", format='wav')
        
        # We sound the set of keys played.
        mix = pygame.mixer.Sound("Sounds/combined.wav")
        mix.play()

        # We restart combined so that the sounds are not overwritten.
        combined = sound_empty
        combined.export("Sounds/combined.wav", format='wav')

                
    # We show the frame
    cv2.imshow("Frame", frame)

	# Press 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
