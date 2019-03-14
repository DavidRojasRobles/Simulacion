
#Este programa simula la espera de pacientes en una sala de urgencias, categorizados 
#partiendo de tres prioridades. En la sala puede haber entre tres y 5 doctores y se 
#asegura que se atiendan entre 10 y 30 pacientes, cuyas prioridades son asignadas
#aleatoriamente. El programa muestra el tiempo de espera promedio de los pacientes por prioridad
#para dos escenarios, donde varían el número de pacientes y de médicos presentes en la sala.

import numpy as np
import heapq

def atender(doc, pac):

    tiempos = []
    pacientes = []
    heapq.heapify(pacientes)

    # for n in range(np.random.randint(10,30)): #numero de pacientes
    for n in range(pac): #numero de pacientes

        heapq.heappush(pacientes, [np.random.randint(3), np.random.randint(1,100)]) #[prioridad, tiempo]

    prioridades = [pacientes[i][0] for i in range(len(pacientes))]

    doctores = []
    #for n in range(np.random.randint(3,5)): #numero de doctores
    for i in range(doc): #numero de doctores
        doctores.append(pacientes[0] if pacientes[0] else None)
        pacientes.pop(0)
        tiempos.append(0)

    cont = 0
    while len(pacientes) > 0:
        for i in range(len(doctores)):
            if doctores[i][1] > 0:
                doctores[i][1] -= 1
            else:
                if len(pacientes) > 0:
                    doctores[i] = pacientes[0]
                    pacientes.pop(0)
                    tiempos.append(cont)
        cont += 1

    x = 0
    for i in range(3):
        scores[i].append(np.mean(tiempos[x:x+prioridades.count(i)]))
        x += prioridades.count(i)

# p = int(raw_input('Cuantos pacientes?\t'))
# d = int(raw_input('Cuantos medicos?\t'))
# p = 20
# d = 5

for i in range(2):
    scores = {0:[], 1:[], 2:[]}
    d = np.random.randint(3,5)
    p = np.random.randint(10,20)
    for i in range(10):
        atender(d,p)
    print('\n\nPara %d doctores y %d pacientes se tiene que:'%(d,p))
    for i in range(len(scores)):
        print('Tiempo de espera promedio para prioridad %d: %f min'%(i,np.mean(scores[i])))
