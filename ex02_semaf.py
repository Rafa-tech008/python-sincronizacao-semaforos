#OP.SEM.2
#Declaração de variáveis

semaf = None
corredor: int = 0

import time
import random
import multiprocessing

def init (c, s):
    global semaf
    global corredor
    semaf = s
    corredor = c


def processo (indent, vel):
    global semaf
    global corredor

    t: int = 0
    temp = random.randint (1000, 2000)

    t= 200 / vel
    print (f"A pessoa {indent} leva {t: .2f}s")
    time.sleep (t)

    with semaf:
        print (f"A pessoa {indent} termina os {corredor.value}m")
        temp = temp / 1000
        time.sleep (temp)


def main ():
    id: int = 0
    params = [0]*4
    speed: int = 0

    global semaf
    global corredor

    corredor = multiprocessing.Value ("i", 200)

    semaf = None
    for id in range (4):
        speed = random.randint (4, 6)
        params [id] = ((id + 1, speed,))

    with multiprocessing.Manager () as manager:
        semaf = manager.Semaphore (1)

        with multiprocessing.Pool (processes=4, initializer=init, initargs=(corredor, semaf)) as pool:
            pool.starmap (processo, params)


if (__name__ == "__main__"):
    main ()

    #Fim