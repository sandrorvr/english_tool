from gtts import gTTS
from playsound import playsound

class Speak:
    
    @staticmethod
    def saveMP3(name_file, text, language='en', slow=False):
        gTTS(text=text, lang=language, slow=slow).save(f'./file_mp3/{name_file}.mp3')
        
    @staticmethod
    def playerMP3(name_file):
        playsound(f'./file_mp3/{name_file}.mp3')
