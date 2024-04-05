import requests
from gtts import gTTS
import pygame
import os
import tempfile
import speech_recognition as sr
import uuid

# API key and headers
NEWS_API_KEY = "91bfde8fda5c46eca821afeedbe67574"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Function to fetch latest news headlines
def get_latest_news(country='eg', category='general', apiKey=NEWS_API_KEY, articles_limit=2):
    try:
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}&category={category}",
            headers=HEADERS
        )
        response.raise_for_status()
        news_headlines = [article["title"] for article in response.json()["articles"][:articles_limit]]
        return news_headlines
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []


def text_to_speech(text, lang='ar'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        # Generate a unique filename for each operation
        unique_filename = f"speech_{uuid.uuid4().hex}.mp3"
        temp_file = os.path.join(tempfile.gettempdir(), unique_filename)
        tts.save(temp_file)
        print(f"File saved to {temp_file}")  # Diagnostic print
        
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()  # Ensure the mixer is stopped
        pygame.mixer.quit()  # Ensure pygame releases the file
        if os.path.exists(temp_file):
            os.remove(temp_file)  # Clean up the temporary file
    except Exception as e:
        print(f"Error in text-to-speech process: {e}")

# Function to recognize speech
def get_speech(lang='ar-EG'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening, please say something...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Adjust timeout as needed
            recognized_text = r.recognize_google(audio, language=lang)
            print(f"Recognized: {recognized_text}")
            return recognized_text
        except sr.WaitTimeoutError:
            print("No speech was detected within the timeout period.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            return ""


# Main interaction function
def news_interaction():
    categories = {
        "الأعمال": "business",
        "الترفيه": "entertainment",
        "العامة": "general",
        "الصحة": "health",
        "العلوم": "science",
        "الرياضة": "sports",
        "التكنولوجيا": "technology"
    }

    text_to_speech("ماذا تريد أن تعرف من الأخبار")
    category_names = "، ".join(categories.keys())
    text_to_speech(f"هناك العديد من فئات الأخبار مثل {category_names}. أي فئة من الأخبار تريد أن تسمع؟")

    user_choice = get_speech()
    print(f"User chose: {user_choice}")

    if user_choice in categories:
        news_headlines = get_latest_news(category=categories[user_choice])
        if news_headlines:
            news_text = '... '.join(news_headlines)
            print(news_text)
            text_to_speech(news_text)
        else:
            text_to_speech("عذراً، لا توجد أخبار في هذه الفئة حالياً.")
    else:
        text_to_speech("لم أتمكن من فهم الفئة المختارة.")

if __name__ == "__main__":
    news_interaction()
