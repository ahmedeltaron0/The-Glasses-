import os
import speech_recognition as sr
from gtts import gTTS
import pygame
from datetime import datetime
import uuid
import hijri_converter

def speak(text, lang='ar'):
    filename = f'temp_voice_{uuid.uuid4()}.mp3'
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(filename)

def listen_for_speech(prompt=None):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    if prompt:
        speak(prompt, 'ar')
    with microphone as source:
        # Reduced duration for faster response but consider ambient noise level
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Timeout waiting for speech.", 'ar')
            return None
    try:
        command = recognizer.recognize_google(audio, language='ar')
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        speak("لم أتمكن من فهم الكلام، يرجى المحاولة مرة أخرى.", 'ar')
    except sr.RequestError:
        speak("حدث خطأ في الاتصال بخدمة التعرف على الكلام.", 'ar')
    return None

def get_gregorian_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_hijri_date():
    today = datetime.now()
    hijri_date = hijri_converter.Gregorian(today.year, today.month, today.day).to_hijri()
    return f"{hijri_date.day} {hijri_date.get_month_name()} {hijri_date.year}"

def main():
    command = listen_for_speech("أنا جاهز، قل تاريخ لمعرفة التاريخ، وقل وقت لمعرفة الوقت.")
    if command:
        if "وقت" in command:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"الوقت الآن هو {current_time}", 'ar')
        elif "تاريخ" in command:
            date_type_command = listen_for_speech("قل هجري للتاريخ الهجري، أو ميلادي للتاريخ الميلادي.")
            if "هجري" in date_type_command:
                hijri_date = get_hijri_date()
                speak(f"التاريخ الهجري اليوم هو {hijri_date}", 'ar')
            elif "ميلادي" in date_type_command:
                gregorian_date = get_gregorian_date()
                speak(f"التاريخ الميلادي اليوم هو {gregorian_date}", 'ar')
            else:
                speak("لم أتمكن من فهم اختيارك.", 'ar')
        else:
            speak("لم أتمكن من فهم الأمر.", 'ar')

if __name__ == "__main__":
    main()
