import speech_recognition as sr

''' open microphone then capture,
    and recognize voice using speech recognition Library,
    then return text that recognized 
'''
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
    
get_audio()