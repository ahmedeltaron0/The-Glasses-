import cv2
import time
from gtts import gTTS
import os
import pygame

def speak_message(message, language='ar'):
    tts = gTTS(text=message, lang=language)
    filename = "temp_message.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()  # Ensure to stop the music
    pygame.mixer.quit()  # Quit the mixer to release the file
    os.remove(filename)  # Now attempt to remove the file

def check_light_condition():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera")
        return

    # Announce the start of light checking
    speak_message("جاري معرفة حالة الإضاءة")

    time.sleep(5)  # Allow camera to adjust
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        cap.release()
        return
    
    # Compute mean brightness
    mean = cv2.meanStdDev(frame)
    print("Mean brightness:", mean[0][0])  # Add this line to help debug
    if mean[0][0] < 50:  # This threshold may need to be adjusted based on your environment
        feedback_text = "عذرا، لا يوجد إضاءة كافية"
        print("Dark")
    else:
        feedback_text = "الإضاءة كافية"
        print("LIGHT")
    
    # Text-to-Speech feedback for the result
    speak_message(feedback_text)

    cap.release()
    cv2.destroyAllWindows()

# Example usage
check_light_condition()
