import requests
from generate_response import  text_to_speech
from playing_audio import  play_audio
from dotenv import dotenv_values

GEMINI_KEY = dotenv_values('.env').get('gemini_api')
WEATHER_KEY = dotenv_values('.env').get('weather_api')

city = "Cairo"

def get_weather():
    api_key = WEATHER_KEY

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['current']["temp_c"]
        
        # Example usage:
        if weather:
            tex = f"درجة الحرارة الان هي {weather} سيليزياس"
                
        return tex
    else:
        print("Error fetching weather data:", response.status_code)
        return None

print(get_weather())