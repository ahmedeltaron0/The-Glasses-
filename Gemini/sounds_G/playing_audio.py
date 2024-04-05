import pygame
import time
import os
from generate_response import  text_to_speech

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Wait a bit for playback to finish properly

    # Attempt to delete the file with some delay to ensure it's not in use
    time.sleep(0.5)  # Wait a bit more before trying to delete the file
    try:
        os.remove(filename)
    except PermissionError as e:
        print(f"Could not delete the audio file immediately: {e}")
        # Optionally, try again after a longer delay or log this for later cleanup.
        
def speech_answer(text):
    ret = text_to_speech(text)
    play_audio (ret)