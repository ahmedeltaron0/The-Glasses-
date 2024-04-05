import os
import pygame
from gtts import gTTS
import speech_recognition as sr

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

def play_tts_message(message, filename="temp.mp3", lang="ar"):
    tts = gTTS(text=message, lang=lang, slow=False)
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()  # Ensure to stop the music
    pygame.mixer.quit()  # Quit the mixer to release the file
    os.remove(filename)  # Now attempt to remove the file

def interact_with_quran(surah_dict):
    play_tts_message("تم تشغيل برنامج القرأن")
    play_tts_message("عايز تسمع انهي سوره")

    surah_input = get_audio()

    surah_key = next((key for key, value in surah_dict.items() if surah_input in [key, value]), None)
    if surah_key:
        surah_name = surah_dict[surah_key]
        play_tts_message(f"جاري تشغيل سورة {surah_name}")

        filename = f"E:\\DR BAHAA\\The Glasses\\Qur'an\\Qur'an\\{surah_key}.mp3"
        if os.path.exists(filename):
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while True:
                command = get_audio()
                if 'وقف' in command:
                    pygame.mixer.music.pause()
                elif 'شغل' in command:
                    pygame.mixer.music.unpause()
                elif 'اقفل' in command:
                    pygame.mixer.music.stop()
                    play_tts_message("تم إيقاف برنامج القرءان")
                    pygame.mixer.quit()  # Quit the mixer to ensure it releases any files.
                    break
        else:
            print(f"Audio file for {surah_name} not found.")
    else:
        print("Surah not recognized.")

# Example surah_dict mapping
surah_dict = {
    '001': 'الفاتحة',
    '002': 'البقرة',
    '003': 'آل عمران',
    '004': 'النساء',
    '005': 'المائدة',
    '006': 'الأنعام',
    '007': 'الأعراف',
    '008': 'الأنفال',
    '009': 'التوبة',
    '010': 'يونس',
    '011': 'هود',
    '012': 'يوسف',
    '013': 'الرعد',
    '014': 'إبراهيم',
    '015': 'الحجر',
    '016': 'النحل',
    '017': 'الإسراء',
    '018': 'الكهف',
    '019': 'مريم',
    '020': 'طه',
    '021': 'الأنبياء',
    '022': 'الحج',
    '023': 'المؤمنون',
    '024': 'النور',
    '025': 'الفرقان',
    '026': 'الشعراء',
    '027': 'النمل',
    '028': 'القصص',
    '029': 'العنكبوت',
    '030': 'الروم',
    '031': 'لقمان',
    '032': 'السجدة',
    '033': 'الأحزاب',
    '034': 'سبأ',
    '035': 'فاطر',
    '036': 'يس',
    '037': 'الصافات',
    '038': 'ص',
    '039': 'الزمر',
    '040': 'غافر',
    '041': 'فصلت',
    '042': 'الشورى',
    '043': 'الزخرف',
    '044': 'الدخان',
    '045': 'الجاثية',
    '046': 'الأحقاف',
    '047': 'محمد',
    '048': 'الفتح',
    '049': 'الحجرات',
    '050': 'ق',
    '051': 'الذاريات',
    '052': 'الطور',
    '053': 'النجم',
    '054': 'القمر',
    '055': 'الرحمن',
    '056': 'الواقعة',
    '057': 'الحديد',
    '058': 'المجادلة',
    '059': 'الحشر',
    '060': 'الممتحنة',
    '061': 'الصف',
    '062': 'الجمعة',
    '063': 'المنافقون',
    '064': 'التغابن',
    '065': 'الطلاق',
    '066': 'التحريم',
    '067': 'الملك',
    '068': 'القلم',
    '069': 'الحاقة',
    '070': 'المعارج',
    '071': 'نوح',
    '072': 'الجن',
    '073': 'المزمل',
    '074': 'المدثر',
    '075': 'القيامة',
    '076': 'الإنسان',
    '077': 'المرسلات',
    '078': 'النبأ',
    '079': 'النازعات',
    '080': 'عبس',
    '081': 'التكوير',
    '082': 'الإنفطار',
    '083': 'المطففين',
    '084': 'الإنشقاق',
    '085': 'البروج',
    '086': 'الطارق',
    '087': 'الأعلى',
    '088': 'الغاشية',
    '089': 'الفجر',
    '090': 'البلد',
    '091': 'الشمس',
    '092': 'الليل',
    '093': 'الضحى',
    '094': 'الشرح',
    '095': 'التين',
    '096': 'العلق',
    '097': 'القدر',
    '098': 'البينة',
    '099': 'الزلزلة',
    '100': 'العاديات',
    '101': 'القارعة',
    '102': 'التكاثر',
    '103': 'العصر',
    '104': 'الهمزة',
    '105': 'الفيل',
    '106': 'قريش',
    '107': 'الماعون',
    '108': 'الكوثر',
    '109': 'الكافرون',
    '110': 'النصر',
    '111': 'المسد',
    '112': 'الإخلاص',
    '113': 'الفلق',
    '114': 'الناس',
        # Add the rest of the mappings
}

if __name__ == "__main__":
    interact_with_quran(surah_dict)
