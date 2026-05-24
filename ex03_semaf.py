#OP.SEM.3
#Declaração de variáveis

#Início

import time
import random
import multiprocessing

semaf = None
posit: int = 0
distance: int = 0

def init (s, p, d):
    global semaf
    global posit
    global distance
    semaf = s
    posit = p
    distance = d

def corrida_sapos (indent):
    global semaf
    global posit
    global distance
    
    pulo: int = 0
    acumulador = 0

    while (acumulador < distance.value):
        pulo = random.randint (1,5)
        acumulador += pulo
        print (f"O sapo {indent} pulou {pulo}cm e percorreu {acumulador}cm")
        time.sleep (0.5)
        
    with semaf:
        posit.value += 1
        print (f"O sapo {indent} foi o {posit.value}º")

def main ():
    global semaf
    global posit
    global distance

    id: int = 0
    params = []*5
    salto: int = 0

    distance = multiprocessing.Value ("i", 30)
    posit = multiprocessing.Value ("i", 0)

    for id in range (5):
            params.append (id + 1)

    with multiprocessing.Manager () as manager:
        semaf = manager.Semaphore (1)

        with multiprocessing.Pool (processes=5, initializer= init, initargs= (semaf, posit, distance)) as pool:
            pool.map (corrida_sapos, params)

if (__name__ == "__main__"):
    main ()

#Fim