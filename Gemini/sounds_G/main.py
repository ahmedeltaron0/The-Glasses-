from capture_voice import get_audio
import cv2
from gemini_api import gemini_response, gemini_vision_response
from playing_audio import speech_answer
from snapshot import snapshot

while  True:
    query = get_audio()
    
    
    
    response = gemini_vision_response(snapshot(),query)
    
    print(response)
    
    