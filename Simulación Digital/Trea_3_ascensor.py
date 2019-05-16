import numpy as np
from collections import OrderedDict as dict

class Ascensor:

    def __init__(self, pisos):
        self.pasajeros = 0
        self.piso = 0
        self.maxPiso = pisos
        self.limite = 10

    def setPasajeros(self, pasajeros):
        self.pasajeros = pasajeros

    def getPasajeros(self):
        return self.pasajeros

    def setLimite(self, limite):
        self.limite = limite

    def getLimite(self):
        return self.limite

    # def setPiso(self, piso):
    #     self.piso = piso

    def getPiso(self):
        return self.piso

    def ingresan(self, ingresan):
        self.pasajeros += ingresan

    def salen(self, salen):
        self.pasajeros -= salen

    def subir(self):
        if self.piso < self.maxPiso:
            self.piso +=1

    def bajar(self):
        if self.piso > 0:
            self.piso -=1

pisos = int(raw_input('¿Cuantos pisos?'))
viajes = int(raw_input('¿Cuantos viajes?'))

# pisos = 4
# viajes = 3
ascensor = Ascensor(pisos)
registro = {}
for i in range(pisos*2*viajes):
    salen = np.random.randint(0,ascensor.getPasajeros()) if ascensor.getPasajeros() > 0 else 0
    ascensor.salen(salen)
    ingresan = np.random.randint(0,(ascensor.getLimite()-ascensor.getPasajeros())) if ascensor.getPasajeros() < ascensor.getLimite() else 0
    ascensor.ingresan(ingresan)
    registro[ascensor.getPiso()] = salen, ingresan, ascensor.getPasajeros()

    ascensor.subir() if i < pisos-1 else ascensor.bajar()
    if i != 0 and (i+1)%pisos == 0:
        # if (i+1)%pisos*2 == 0:
        #     print i+1, dict(sorted(registro.items(), reverse = True))
        print i+1, registro
