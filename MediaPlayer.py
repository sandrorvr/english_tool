from DataSpeak import DataSpeak
from gtts import gTTS
from playsound import playsound
from os.path import exists
from time import sleep

from abc import ABC, abstractmethod

class MediaPlayer:
    def __init__(self):
        self.data = DataSpeak()
        self.run()
    
    def saveMP3(self, name_file, text, language='en', slow=False):
        gTTS(text=text, lang=language, slow=slow).save(f'./file_mp3/{name_file}.mp3')
    
    def playerMP3(self, name_file):
        playsound(f'./file_mp3/{name_file}.mp3')
    
    def loadSpeak(self, id_ask, data_ask):
        self.saveMP3(f'ask_{id_ask}', data_ask['ask'])
        self.saveMP3(f'answer_{id_ask}', data_ask['answer'])
    
    def speak(self, tp, data):
        data_ask, id_ask = data
        print(data_ask[tp])
        if not exists(f'./file_mp3/ask_{id_ask}.mp3'):
            self.loadSpeak(id_ask, data_ask)
        
        self.playerMP3(f'{tp}_{id_ask}')


    def control(self, state, data):
        data_ask, id_ask = data
        if state == 'next':
            self.speak('ask', (data_ask, id_ask))
        elif state == 'repeat':
            while state == 'repeat':
                self.speak('ask', (data_ask, id_ask))
                state = input('Do you to want do?\n')
        else:
            state = 'exit'
        return state
            

    def run(self):
        while True:
            data_ask, id_ask = self.data.get_random_ask()
            state = self.control('repeat', (data_ask, id_ask))
            if state == 'answer':
                self.speak('answer', (data_ask, id_ask))
                sleep(3)
            elif state == 'exit':
                print('BY\n')
                break
            else:
                self.speak('answer', (data_ask, id_ask))
                sleep(3)


if __name__ == "__main__":
    MediaPlayer()