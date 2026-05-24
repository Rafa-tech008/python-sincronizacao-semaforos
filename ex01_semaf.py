#OP.SEM.1
#Declaração de variáveis

#Início
import time
import multiprocessing

semaf = None

def init(s):
    global semaf
    semaf = s


def carros (direc):
    with semaf:
        print (f"O carro {direc} partiu")
        time.sleep (0.05)
        print (f"O carro {direc} passou")


def main ():
    i: int = 0
    params = []
    semaforo = None

    params.append (("leste",))
    params.append (("oeste",))
    params.append (("norte",))
    params.append (("sul",))

    with multiprocessing.Manager ()as manager:
        semaforo = manager.Semaphore (1)

        with multiprocessing.Pool (processes = 4, initializer = init, initargs = (semaforo, )) as pool:
            pool.starmap (carros, params)

if (__name__ == "__main__"):
    main()

#Fim