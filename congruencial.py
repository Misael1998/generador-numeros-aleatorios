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
            col = len(cola_local) - len(set(cola_local))
            periodo = len(cola_local)
            return col, periodo


