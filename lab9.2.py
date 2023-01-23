from mpi4py import MPI
#============================================
#objeto mensaje
#============================================
class Mensaje:
    def __init__(self, rank):
        #iterador
        self.x = range(rank*10)
        #string
        self.p = "vengo del proceso" + str(rank)
#============================================
#programa principal
#============================================
if _name_ == "_main_":
    comm = MPI.COMM_WOLRD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    #print(s.x)
    #============================================
    #Que te mande el anterior y si es cero que sea el ultimo
    #============================================
    fuente = rank-1 if rank != 0 else size-1

    #============================================
    #mandalo al siguiente y si eres el ultimo mandalo al primero
    #============================================
    destino = rank+1 if rank != size-1 else 0
    #============================================
    #send y recv son operaciones bloqueadas y generan que el
    #codigo se atore esperando que alguien reciba un mensaje
    #esto se resuelve enviando con los pares y recibiendo con
    #los impares
    #============================================
    # si soy par
    if rank%2==0:
        #============================================
        #enviar mensaje s al dest
        #============================================
        comm.send(s, dest=destino)
        #============================================
        #recibir de source y lo pone en m
        #============================================
        m = comm.recv(source=fuente)
    #si no soy par
    else:
        #============================================
        #recibir primero y mandar mensaje despues
        #============================================
        m = comm.recv(source = fuente)
        comm.send(s,dest = destino)
    print("soy el proceso", rank, ", el resultado es", len(m.x),",",m.p)
    