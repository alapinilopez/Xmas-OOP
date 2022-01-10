class Book:
    def __init__(self, title, author, price, stock, objectid):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._objectid = objectid
        pass

    def get_info(self):
        return f""" \n Título: {self._title}\n Autor: {self._author}\n Precio: {self._price}\n Stock: {self._stock}\n Id: {self._objectid} """

    def get_title(self):
        return self._title
    def set_title(self, new_title):
        self._title = new_title

    def get_author(self):
        return self._author
    def set_author(self, new_author):
        self._author = new_author

    def get_price(self):
        return self._price
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Asigne un precio mayor a 0")

    def get_stock(self):
        return self._stock
    def set_stock(self, new_stock):
        self._stock = new_stock

    def get_objectid(self):
        return self._objectid
    def set_objectid(self, new_objectid):
        self._objectid = new_objectid
 
    
book1 = Book("1984", "George Orwell", 17.99, 20, 1)
book2 = Book("Metro 2033", "Dimitry Noseke", 15.99, 50, 2)

print(book1.get_info())
# print(book2.get_title())