import numpy as np

class Proceso:
    #IdProc = 0
    def __init__(self, i, tiempo, estado):
        #Proceso.IdProc += 1
        #self.IdProc = Proceso.IdProc
        self.IdProc = i
        self.tiempo = tiempo

    def getIdProc(self):
        return self.IdProc

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getTiempo(self):
        return self.tiempo

    def ejecutar(self, q):
        temp = self.tiempo
        self.tiempo -= q
        if self.tiempo < 0:
            self.tiempo = 0
            return temp
        else:
            return q

class RoundRobin:
    def __init__(self, quantum, numProc):
        self.quantum = quantum
        self.numProc = numProc
        self.tiempoTotal = 0

    def crearProceso(self, i):
        p = Proceso(i, np.random.randint(1,100), True)
        print "Proceso %d --> Tiempo = %d"%(p.getIdProc(), p.getTiempo())
        return p

    def crearCola(self):
        self.cola = Cola()
        for i in range(self.numProc):
            self.cola.agregar(self.crearProceso(i+1))

    def procesar(self):
        self.crearCola()
        print "\nProceso \t T. restante \t Total"
        turnos = 0
        while self.cola.estaVacia() == False:
            turnos += 1
            q = self.cola.getFirst().ejecutar(self.quantum)
            self.tiempoTotal += q
            print "%d \t\t %d \t\t %d"%(self.cola.getFirst().getIdProc(), self.cola.getFirst().getTiempo(), self.tiempoTotal)

            if self.cola.getFirst().tiempo > 0:
                self.cola.agregar(self.cola.getFirst())

            self.cola.avanzar();

        return turnos

class Cola:
    count = -1
    def __init__(self):
        self.items = []

    def getFirst(self):
        return self.items[0]


    def getItems(self):
        return self.items

    def getItem(self, ix):
        return self.items[ix]

    def estaVacia(self):
        if Cola.count < 0:
            return True
        else:
            return False

    def agregar(self, item):
        Cola.count += 1
        self.items.append(item)

    def avanzar(self):
        Cola.count -= 1
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)


n = 3
q = 15

turnos = RoundRobin(q, n).procesar()
print "Se completo en un total de %d turnos"%(turnos)
