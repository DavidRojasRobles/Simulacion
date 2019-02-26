#For this program we assume tanks are 2 dimensional and rectangular,
#all tanks start empty,
#first tank is the one to get external flow
#all tanks are filled by only one flow
#all tanks fill up from the top,
#the fluid filling them has a density of one,
#the flow starts as soon as the fluid reaches it,
#flows have an offset read left to right or down-up,
#there can't be more than one flow with the same offset per tank
#No flows can be positioned at the corners of the tank
#and the next tank stars filling as soon as the fluid reaches the flow
import numpy as np


class tank:

    def __init__(self, id, height, width):

        self.id = id

        self.height = height

        self.width = width

        self.capacity = height * width

        self.content = 0


    def setId(self, id):

        self.id = id


    def getId(self):

        return self.id


    def getHeight(self):

        return self.height


    def getWidth(self):

        return self.width


    def getCapacity(self):

        return self.capacity


    def setContent(self, content):

        self.content = content


    def getContent(self):

        return self.content


    # def fillTank(self, fillsIt, holes):


    # self.content += flow

    # return ('Tank %s is full!!')%(self.id)


    def isFull(self):

        if self.content < self.capacity:

            return False

        else:

            return True



class flow:

    def __init__(self, id, size, offset):

        self.id = id

        self.size = size

        self.offset = offset


    def setId(self, id):

        self.id = id


    def getId(self):

        return self.id


    def setSize(self, size):

        self.size = size


    def getSize(self):

        return self.size


    def setOffset(self, offset):

        self.offset = offset


    def getOffset(self):

        return self.offset


class run:


    def __init__(self, tankNum, flowNum):

        self.tankNum = tankNum
        self.flowNum = flowNum
        self.tanks = []
        self.flows = []
        self.count = 0
        self.relations = {}

        self.createTanks()
        self.createFlows()
        self.printRels()
        self.fillEmUp()


    def printRels(self):

      for key, relTuple in self.relations.iteritems():

        print self.relations[key][0].getId() if key != 0 else self.relations[key][0], self.relations[key][1].getId(), self.relations[key][2].getId()


    def setExternalFlow(self):

        # efsize = int(raw_input('Size of external flow? \t'))

        efsize = 25

        ef = flow(-1, efsize, 'null')

        self.flows.append(ef)

        return ef


    def AddRelation(self, origin, flow, destination):

        self.relations[self.count] = origin, flow, destination

        self.count += 1


    def getFiller(self, tank):

        for key, relTuple in self.relations.iteritems():

            #print('tank %d in key %d and %d == %d')%(tank.getId(), key, relTuple[2].getId(), tank.getId())

            if (tank in relTuple) and (relTuple[2] == tank):

                return self.relations[key][1] #return flow id

        print('no flow fills tank %d'%(tank.getId()))


    def getHoles(self, tank):

        f = []

        for key, relTuple in self.relations.iteritems():

            if (tank in relTuple) and (relTuple[0] == tank):

                f.append(self.relations[key][1])

        return f


    def createTanks(self):

      #print 'Empiece con el primer tanque (cominenza a llenarse de primero)'

      for i in range(self.tankNum):

        #print('\nPara el tanque %d:')%(i)

        height, width = 30, 30

        #height = int(raw_input('Altura del tanque:\t'))

        #width = int(raw_input('Ancho del tanque:\t'))

        self.tanks.append(tank(i, height, width))

        if len(self.tanks) == 1:

          ef = self.setExternalFlow()

          self.AddRelation('null', ef , self.tanks[i])


    def createFlows(self):

        a = [10 , 10, 30]
        b = [5, 10, 15]
        o = [0, 0, 2]
        d = [1, 2, 3]

        for i in range(self.flowNum):

          #print('\nPara el flujo %d:')%(i)

          #origin = int(raw_input('Tanque de origen:\t'))

          #destination = int(raw_input('Tanque destino:\t'))

          #size = int(raw_input('Tamano del flujo:\t'))

          #offset = int(raw_input('Altura del flujo (0 si esta en el fondo):\t'))

          origin = o[i]
          destination = d[i]
          size = a[i]
          offset = b[i]

          self.flows.append(flow(i, size, offset))

          self.AddRelation(self.tanks[origin], self.flows[i+1], self.tanks[destination])



    def findNextHole(self, holes):
        nextHole = 'null'
        minHoleKey = 'null'

        # get first hole
        if len(holes) > 0:
            holeHeights = {}
            for i in range(len(holes)):
              holeHeights[i] = holes[i].getOffset()

            minHoleKey = min(holeHeights, key=holeHeights.get)

            nextHole = holes[minHoleKey] #This is actually a flow object

        return nextHole, minHoleKey
    
    def fillEmUp(self):

        self.fillTank(self.tanks[0])


    def fillTank(self, tank):

        #print '\n------------------------for tank', tank.getId()


        filler = self.getFiller(tank) #filler (object)

        holes = self.getHoles(tank) #list of flows originated from tank (object)
        nextHole, minHoleKey = self.findNextHole(holes)
        while(tank.isFull() == False):

            currentHeight = tank.getContent()/tank.getWidth()
            
            if (type(nextHole) != str) and (currentHeight >= nextHole.getOffset()):
                
                for key, relTuple in self.relations.iteritems():

                    if (relTuple[1] == nextHole):

                        nextTank = relTuple[2]
                        ntid = nextTank.getId()
                        #print 'nextTank =', nextTank.getId()

                        self.fillTank(nextTank) #this tank has to be the one at the destination of the lowest hole in the current tank
                        #print '\ncontinuing on tank', tank.getId()
                        if len(holes) > 0:
                          #print 'popping hole', holes[minHoleKey].getId()
                          holes.pop(minHoleKey) #Removes flow with min height after filling everything down from it
                          nextHole, minHoleKey = self.findNextHole(holes)

            toAdd = tank.getContent() + filler.getSize()
            tank.setContent(toAdd) #adds filler size with current tank content

        print('EL tanque %d esta lleno!!'%(tank.getId()))

#t = int(raw_input('Numero de tanques: '))
#f = int(raw_input('Numero de flujos: '))

t, f = 4, 3

run(t, f)
