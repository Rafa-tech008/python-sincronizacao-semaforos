#OP.SEM.4
#Declaração de variáveis

#Início

import time
import random 
import multiprocessing

lock = None
pista = None
vetor = [0]*7


def init (p, v, l):
    global pista
    global vetor
    global lock
    pista = p
    vetor = v
    lock = l

def treino (equipe, indent):
    global pista
    global vetor
    global lock

    voltas = 3
    volta: int = 0
    temp: float = 0.0

    times = ["Ferrari", "Mercedes", "Racing club", "Audi", "Williams", "McLaren", "Alpine"]
    idx = times.index (equipe)
    while True:
        with lock:
            if vetor[idx] == 0:
                vetor[idx] = 1
                break
        time.sleep(0.5)

    with pista:
        print (f"A vez da {equipe} do carro {indent} inicia")
        acum = 0
        volta = 0   
        for i in range (voltas):
            temp = random.randint (7, 15)
            acum += temp
            time.sleep (0.05)
            volta += 1
            print (f"A {equipe} do carro {indent} percorre a volta {volta} em {acum}s")
            vetor [idx]= 0        
        print (f"A {equipe} do carro {indent} finalizou a volta {voltas} em {acum}s")
        
              
            
def main ():
    params = []
    vet_pos = [0]*7

    vet_valor = multiprocessing.Array ("i", vet_pos)

    params.append (("Ferrari", 1))
    params.append (("Ferrari", 2))
    params.append (("Mercedes", 1)) 
    params.append (("Mercedes", 2)) 
    params.append (("Racing club", 1))
    params.append (("Racing club", 2))
    params.append (("Audi", 1))
    params.append (("Audi",2))
    params.append (("Williams", 1)) 
    params.append (("Williams", 2)) 
    params.append (("McLaren", 1))
    params.append (("McLaren", 2)) 
    params.append (("Alpine", 1)) 
    params.append (("Alpine", 2))

    with multiprocessing.Manager () as manager:
        pista = manager.Semaphore (5)
        lock = manager.Lock ()
        vet_valor = manager.list([0]*7) 
        
        with multiprocessing.Pool (processes=14, initializer=init, initargs= (pista, vet_valor, lock)) as pool:
            pool.starmap (treino, params)

if (__name__=="__main__"):
    main ()

#Fim