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

    #         self.content += flow
    #     return ('Tank %s is full!!')%(self.id)

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
        # print 'tanks: '
        # print self.tanks
        # print'flows: '
        # print self.flows
        # print self.relations
        self.printRels()
        self.fillEmUp()

    def printRels(self):
        print self.relations[0][0], self.relations[0][1].getId(), self.relations[0][2].getId()
        print self.relations[1][0].getId(), self.relations[1][1].getId(), self.relations[1][2].getId()
        print self.relations[2][0].getId(), self.relations[2][1].getId(), self.relations[2][2].getId()


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

        # if len(f) != 0:
        #     return f
        # else:
        #     print('no flow comes out of tank %d, bud'%(tank.getId()))

    def createTanks(self):
        #print 'Please start with the first tank (will start filling first)'
        for i in range(self.tankNum):
            #print('for tank %d: \n')%(i)
            height, width = 25, 15
            # height = int(raw_input('Tank height?\t'))
            # width = int(raw_input('Tank width?\t'))
            self.tanks.append(tank(i, height, width))
            if len(self.tanks) == 1:
                ef = self.setExternalFlow()
                self.AddRelation('null', ef , self.tanks[i])
                #print 'added rel {%d: , %s, %d, %d}'%(self.count, 'null', ef.getId(), self.tanks[i].getId())

    def createFlows(self):
        a = [5 , 5]
        b = [5, 10]
        o = [0, 0]
        d = [1, 2]
        for i in range(self.flowNum):
            #print('\nFor flow %d:')%(i)
            # origin = int(raw_input('What tank does it come from? \t'))
            # destination = int(raw_input('What tank does it go to? \t'))
            # size = int(raw_input('Flow size? \t'))
            # offset = int(raw_input('Flow offset? (if in bottom: 0) \t'))

            origin = o[i]
            destination = d[i]
            size = a[i]
            offset = b[i]


            self.flows.append(flow(i, size, offset))
            self.AddRelation(self.tanks[origin], self.flows[i+1], self.tanks[destination])
            #print 'added rel {%d: %d, %d, %d}'%(self.count, self.tanks[origin].getId(), self.flows[i+1].getId(), self.tanks[destination].getId())


    def fillEmUp(self):
        self.fillTank(self.tanks[0])

    def fillTank(self, tank):
        print '\nfor tank', tank.getId()

        filler = self.getFiller(tank) #filler (object)
        print 'filler', filler.getId()
        holes = self.getHoles(tank) #list of flows originated from tank (object)
        print 'len(holes) = ', len(holes)

        nextHole = 'null'

        # get first hole
        #currently works forn only one level of flows
        if len(holes) > 0:
            holeHeights = {}
            for i in range(len(holes)):
                holeHeights[i] = holes[i].getOffset()

            minHoleKey = min(holeHeights, key=holeHeights.get)
            nextHole = holes[minHoleKey] #This is actually a flow object
            print 'len(holes) > 0: nextHole (flow)= ', nextHole.getId()
        else:
            if nextHole == 'null':
                print 'nextHole (flow)= ', nextHole
            else:
                print 'nextHole (flow)= ', nextHole.getId()

        while(tank.isFull() == False):
            print 'inside while tank isn\'t full: nextHole (flow)=', nextHole
            currentHeight = tank.getContent()/tank.getWidth()
            if (type(nextHole) != str) and (currentHeight >= nextHole.getOffset()):
                print 'inside if: nextHole (flow)= ', nextHole.getId()
                for key, relTuple in self.relations.iteritems():
                    if (relTuple[1] == nextHole):
                        nextTank = self.relations[key][2]
                        print 'nextTank =', nextTank.getId()
                        self.fillTank(nextTank) #this tank has to be the one at the destination of the lowest hole in the current tank
                if len(holes) > 0:
                    holes.pop(minHoleKey) #Removes flow with min height after filling everything down from it
            toAdd = tank.getContent() + filler.getSize()
            tank.setContent(toAdd) #adds filler size with current tank content



        # while(tank.isFull() == False):
        #     toAdd = tank.getContent() + filler.getSize()
        #     tank.setContent(toAdd) #adds filler size with current tank content
        # print('Tank %d is full!'%(tank.getId()))


# def ff(a, tank):
#     for key, relTuple in a.iteritems():
#         if (tank in relTuple) and (relTuple[2] == tank):
#             return a[key][1] #return flow id
#     print('no flow fills tank %d'%(tank))
#
# def hh(a, tank):
#     f = []
#     for key, relTuple in a.iteritems():
#         if (tank in relTuple) and (relTuple[0] == tank):
#             print('tank %d in reltuple %s and %d == %d')%(tank, relTuple, relTuple[0], tank)
#             f.append(a[key][1])
#
#     if len(f) != 0:
#         return f
#     print('no flow comes out of tank %d, bud'%(tank))
#
# a = {
#     0: ('null', -1, 0),
#     1: (0,0,1),
#     2: (0,1,2)
# }
#
# tank = 2
#
# result = hh(a, tank)
#
# print result


# t = int(raw_input('how many tanks?\t'))
# f = int(raw_input('how many flows? (source flow not included)\t'))

t, f = 3, 2
run(t, f)
