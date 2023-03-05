from DataSpeak import DataSpeak
from Speak import Speak
from os.path import exists

data = DataSpeak()

key = 's'
while True:
    data_ask, id_ask = data.get_random_ask()
    print(data_ask['ask'])
    if not exists(f'./file_mp3/ask_{id_ask}.mp3'):
        Speak.saveMP3(f'ask_{id_ask}', data_ask['ask'])
        Speak.saveMP3(f'answer_{id_ask}', data_ask['answer'])
        Speak.playerMP3(f'ask_{id_ask}')
    else:
        Speak.playerMP3(f'ask_{id_ask}')

    key = input('Do you to want do?\n')
    Speak.playerMP3(f'answer_{id_ask}')
    if key == 'quit':
        print('BY\n')
        break

