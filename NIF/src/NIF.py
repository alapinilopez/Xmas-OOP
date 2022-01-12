
class NIF:
    def __init__(self):
        self.valid_chars = ['T', 'R', 'W', 'A', 'G', 'M', 'Y',
        'F', 'P', 'D', 'X', 'B', 'N', 'J',
        'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        pass
    # importar el num del DNI
    def get_info(self):
        return f"""\n Número: {self.dni_num}\n NIF: {self.NIF}"""
     
    def get_char(self, position):
        try:
            return self.valid_chars[position]
        except:
            return 'Fuera de rango'

    
    def set_NIF(self, DNI):
        table_position = int(DNI) % 23
        return self.get_char(table_position)
    
    def get_NIF(self):
        return self.NIF
        
    

    #dividir el num del dni entre 23 y asignarle el nif segun el valor del resto
# dni1 = NIF(45371654Z)

