import collections
class AleatorioCongruencial:
    def __init__(self):
        self.semilla = 15
        self.multiplicador = 8
        self.constante_aditiva = 16
        self.modulo = 100
        self.cola = []

    def __init__(self, semilla, multiplicador, constante_aditiva, modulo):
        self.semilla = semilla
        self.multiplicador = multiplicador
        self.constante_aditiva = constante_aditiva
        self.modulo = modulo
        self.cola = []

    def generar_aleatorio(self):
       cola_local = self.cola
       if len(cola_local) == 0:
           xn = (self.multiplicador*self.semilla + self.constante_aditiva) % self.modulo 
           self.cola.append(xn)
           return xn
       else:
            sem = cola_local[ len(cola_local) - 1 ]
            xn = (self.multiplicador*sem + self.constante_aditiva) % self.modulo
            self.cola.append(xn)
            return(xn)

    def obtener_cola_periodo(self):
        cola_local = self.cola
        if len(cola_local) == 0:
            return 0, 0
        else:
            repedios = [x for x, y in collections.Counter(cola_local).items() if y > 1]
            cola_set = set(cola_local)
            col = len(cola_set) - len(repedios)
            periodo = len(cola_set)
            return col, periodo


