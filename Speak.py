from gtts import gTTS
from playsound import playsound

class Speak:
    def __init__(self):
        pass
    
    @staticmethod
    def saveMP3(name_file, text, language='en', slow=False):
        gTTS(text=text, lang=language, slow=slow).save(f'./file_mp3/{name_file}.mp3')
    
    def playerMP3(name_file):
        playsound(f'./file_mp3/{name_file}.mp3')