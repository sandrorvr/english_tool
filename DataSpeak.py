import json
from random import randint, choice

class DataSpeak:
    def __init__(self):
        try:
            with open('data.json') as file:
                self.data = json.load(file)
        except OSError:
            print("Erro in file DATA.JSON")
        
        self.index_by_books = self.map_books()

    def map_books(self):
        map_books = {}
        for dt in self.data['asks']:
            map_books[dt['where']] = map_books.get(dt['where'],[])
            map_books[dt['where']].append(dt['id'])
        return map_books
    
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
    def get_random_ask_by_book(self, book):
        n_randint = choice(self.index_by_books[book])
        return (
                self.get_ask_by_id(n_randint), 
                self.get_ask_index(n_randint)
                )

if __name__ == '__main__':
    data = DataSpeak()
    print(data.index_by_books)
    print(data.get_random_ask_by_book('book1'))
