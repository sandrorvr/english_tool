import json
from random import randint

class DataSpeak:
    def __init__(self):
        try:
            with open('data.json') as file:
                self.data = json.load(file)
        except OSError:
            print("Erro in file DATA.JSON")

    def data_asks_lenght(self):
        return len(self.data['asks'])-1
    
    def get_ask_by_id(self, id):
        return self.data['asks'][id]
    
    def get_ask_index(self, id):
        return self.data['asks'][id]['id']
    
    def get_random_ask(self):
        n_randint = randint(0, self.data_asks_lenght())
        return (
                self.get_ask_by_id(n_randint), 
                self.get_ask_index(n_randint)
                )
    
    

