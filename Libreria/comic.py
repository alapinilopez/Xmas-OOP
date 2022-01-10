from book import *

class Comic(Book):
    def __init__(self, title, author, price, stock, illustrators, vol, objectid ):
        super().__init__(title, author, price, stock, objectid)
        self._illustrators = illustrators
        self._vol = vol

    def get_info(self):
        info = super().get_info()
        str_illustrators = ", ".join(self._illustrators)
        return info + f"""\n Ilustradores: {str_illustrators}\n Volumen: {self._vol}  """
        

comic1 = Comic("Batman: The Killing Joke", "Paco Pepe", 30.0, 10,["Marko", "Heredia"], 1)
comic2 = Comic("Dragon Ball Z", "Akira Toriyama", 20, 40, ["Akira Toriyama"], 2)
