import os
import pygame
from gtts import gTTS
from datetime import datetime
import wikipedia
import speech_recognition as sr
import time

def text_to_speech(text, lang='ar'):
    tts = gTTS(text=text, lang=lang, slow=False)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    tts.save(filename)
    return filename

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

def get_audio(lang='ar'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=lang)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def search_wikipedia_and_respond():
    wikipedia.set_lang("ar")
    initial_prompt = "عايزْ تعملْ سيرشْ عنْ إيهْ"
    prompt_audio_file = text_to_speech(initial_prompt)
    play_audio(prompt_audio_file)
    
    search_query = get_audio()
    if search_query:
        try:
            summary = wikipedia.summary(search_query, sentences=3)
            print(summary)
            summary_audio_file = text_to_speech(summary)
            play_audio(summary_audio_file)
        except wikipedia.exceptions.PageError:
            error_message = "لم أتمكن من إيجاد نتائج"
            error_audio_file = text_to_speech(error_message)
            play_audio(error_audio_file)
        except Exception as e:
            print(f"An error occurred: {e}")

search_wikipedia_and_respond()
