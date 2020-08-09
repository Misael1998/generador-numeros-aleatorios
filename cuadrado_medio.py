import collections
class AleatorioMedio:
    def __init__(self):
        self.semilla = 12345678
        self.dgt_significativo = 4
        self.cola = []
    
    def __init__(self, semilla, dgt_significativo):
        self.semilla = semilla 
        self.dgt_significativo = dgt_significativo
        self.cola = []

    def generar_numero_aleatorio(self):
        cuadrado = self.semilla ** 2
        sem = str(cuadrado)
        if self.dgt_significativo >= len(sem):
            self.semilla = int(sem)
            alt = int(sem) / (10**self.dgt_significativo)
            self.cola.append(self.semilla)
            return alt 
        else: 
            i = 0
            while len(sem) != self.dgt_significativo:
                if i%2 == 0:
                    sem = sem[:-1]
                else:
                    sem = sem[1:]
                i += 1

            self.semilla = int(sem)
            alt = int(sem) / (10**self.dgt_significativo)
            self.cola.append(self.semilla)
            return alt
    
    def obtener_cola(self):
        cola_local = self.cola
        seen = set(cola_local)
        uniq = []
        for item in cola_local:
            if item not in cola_local:
                uniq.append(item)
        print(cola_local)