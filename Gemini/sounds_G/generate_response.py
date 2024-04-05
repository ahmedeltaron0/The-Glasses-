from gtts import gTTS
from datetime import datetime

def text_to_speech(text, lang='ar'):
    tts = gTTS(text=text, lang=lang, slow=False)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    tts.save(filename)
    return filename
