from NIF import NIF

class DNI:
    def __init__(self, DNI):
        self.DNI = DNI
        self.tabla = NIF()

    def get_info(self):
        return f"""\n DNI: {self.dni_num}\n NIF"""

    def check_length(self):
        return len(self.DNI) == 9

    def check_number(self):
        return self.DNI[:-1].isdigit()

    def DNI_healthy(self):
        if self.check_length() and self.check_number:
            return True
        else: 
            return False

    def get_letter(self):
        return self.DNI[-1]

    def DNI_nums(self):
        return self.DNI[:-1]

    def DNI_check(self):
        if self.DNISano:
            if self.tabla.calcularLetra(self.DNINumbers()) == self.getLetter():
                return True
            else: 
                return False
