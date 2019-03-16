
#Este programa simula la espera de pacientes en una sala de urgencias, categorizados
#en tres prioridades. En la sala puede haber entre tres y 5 doctores y se asegura
#que se atiendan entre 10 y 30 pacientes, cuyas prioridades son asignadas aleatoriamente.
#El programa muestra el tiempo de espera promedio (en minutos) de los pacientes por prioridad
#para dos escenarios, donde varian el numero de pacientes y de medicos presentes en la sala.

import numpy as np
import heapq

def atender(doc, pac): #Simula la atencion de los pacientes

    tiempos = [] #Guaradra el tiempo de espera de cada paciente
    pacientes = [] #Guaradra la prioridad y el tiempo de atencion del paciente en sala de espera
    heapq.heapify(pacientes) #Permite usar HeapQueue con la lista pacientes

    for n in range(pac): #numero de pacientes

        heapq.heappush(pacientes, [np.random.randint(3), np.random.randint(1,40)]) #[prioridad, tiempo]
        #Crea la llena la lista pacientes y la ordena de 0 a 2
        #heapq permite organizar la lista pacientes por prioridad (de menor a mayor: 0 a 2 en este caso)
    prioridades = [pacientes[i][0] for i in range(len(pacientes))] #Guarda las prioridades de
    #todos los pacientes atendidos

    doctores = [] #Guardara el paciente actual que atiende el doctor
    for i in range(doc): #numero de doctores
        doctores.append(pacientes[0] if pacientes[0] else None) #Anade el primer paciente
        pacientes.pop(0) #Remueve el primer paciente (ya en doctores)
        tiempos.append(0) #Anade tiempo 0 al paciente que esta siendo atendido, pues no tuvo que esperar

    cont = 0 #Cuenta los minutos
    while len(pacientes) > 0: #Mientras aun haya pacientes esperando
        for i in range(len(doctores)):
            if doctores[i][1] > 0: #Si el tiempo de atencion del paciente > 0
                doctores[i][1] -= 1 #Se resta un minuto del t de atencion
            else:
                if len(pacientes) > 0: #Si aun hay pacientes
                    doctores[i] = pacientes[0] #Asigne el siguiente paciente al consultorio
                    pacientes.pop(0) #Se elimina el paciente de la sala de espera
                    tiempos.append(cont) #Se anade el tiempo de espera del paciente siendo atendido
        cont += 1

    x = 0
    for i in range(3):
        scores[i].append(np.mean(tiempos[x:x+prioridades.count(i)])) #Asigna el promedio de tiempo
        #de los paciente por prioridad a la lista scores
        x += prioridades.count(i)

for i in range(2): #Numero de casos
    scores = {0:[], 1:[], 2:[]}
    d = np.random.randint(3,5) #Numero de doctores
    p = np.random.randint(10,20) #Numero de pacientes
    for i in range(100): #Iteraciones en que se acumula informacion
        atender(d,p)
    print('\n\nPara %d doctores y %d pacientes se tiene que:'%(d,p))
    for i in range(len(scores)):
        print('Tiempo de espera promedio para prioridad %d: %f min'%(i,np.mean(scores[i])))
        #Se imprime el promedio de tiempo de espera de los pacientes por prioridad
