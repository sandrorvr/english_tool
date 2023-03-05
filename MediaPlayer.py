from DataSpeak import DataSpeak
from gtts import gTTS
from playsound import playsound
from os.path import exists
from time import sleep

from abc import ABC, abstractmethod

class MediaPlayer:
    def __init__(self):
        self.data = DataSpeak()
        self.painel()
    
    def painel(self):
        print('+--------------------------------------------------+')
        print('|                                                  |\n')
        print('|        [0]   EXECUTE SCRIPT NOT INTERACTIVE      |\n')
        print('|        [1]   EXECUTE SCRIPT INTERACTIVE          |\n')
        print('|                                                  |\n')
        print('+--------------------------------------------------+')
        print('\n')
        ch = input('I MUST CHOICE AN OPTION: ')
        book = input('DO YOU WISH A SPECIFIC BOOK?: ')
        if ch == '0':
            self.run_not_interactive(book)
        elif ch == '1':
            self.run_interactive(book)
        else:
            raise('INVALID OPTION')
    
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

    def get_ask(self, book=''):
        if book == '':
            return self.data.get_random_ask()
        else:
            return self.data.get_random_ask_by_book(book)

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
            

    def run_interactive(self,book):
        while True:
            data_ask, id_ask = self.get_ask(book)
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
    
    def run_not_interactive(self,book):
        while True:
            data_ask, id_ask = self.get_ask(book)
            self.speak('ask', (data_ask, id_ask))
            sleep(4)
            self.speak('answer', (data_ask, id_ask))
            sleep(3)


if __name__ == "__main__":
    MediaPlayer()