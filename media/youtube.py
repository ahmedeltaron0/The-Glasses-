from gtts import gTTS
import pygame
from datetime import datetime
import speech_recognition as sr
import pywhatkit
from pynput.keyboard import Key, Controller
import time
import os
import tempfile

temp_files = []  # List to keep track of temporary file names

def text_to_speech(text, lang='ar'):
    global temp_files
    tts = gTTS(text=text, lang=lang, slow=False)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)
    temp_file.close()
    
    temp_files.append(temp_file.name)  # Add the file name to the list for later cleanup
    
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

# No attempt to delete the file immediately after playback

def cleanup_temp_files():
    for filename in temp_files:
        try:
            os.remove(filename)
            print(f"Successfully deleted {filename}")
        except PermissionError as e:
            print(f"Failed to delete {filename}: {e}")

def get_audio(lang='ar'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=lang)
        return text
    except Exception as e:
        print("Error recognizing speech:", e)
        return ""

def youtube_interaction():
    # Ask what the user wants to listen to
    text_to_speech("عايزْ تسمع إيهْ")
    
    # Capture the user's response
    media_request = get_audio()
    print(media_request)
    
    # Acknowledge the request and play it on YouTube
    if media_request:
        talk = f'جاري تشغيل {media_request}'
        text_to_speech(talk)
        pywhatkit.playonyt(media_request)
    
        # Pause to allow the browser and YouTube to load
        time.sleep(8)
        
        # Initial play/pause to ensure video is playing
        keyboard = Controller()
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        
        # Voice control loop for media control
        while True:
            media_control = get_audio()
            
            if "اسكت" in media_control or "وقف" in media_control:
                # Pause the video
                keyboard.press(Key.space)
                keyboard.release(Key.space)
            
            elif "شغل" in media_control or "كمل" in media_control:
                # Play the video
                keyboard.press(Key.space)
                keyboard.release(Key.space)
            
            elif "اخرج" in media_control or "اقفل" in media_control:
                # Close the browser tab
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release('w')
                keyboard.release(Key.ctrl)
                text_to_speech("تم إيقاف برنامج اليوتيوب")
                break
if __name__ == "__main__":
    try:
        youtube_interaction()
    finally:
        cleanup_temp_files()  # Attempt to clean up all temp files at the end