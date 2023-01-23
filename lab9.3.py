from mpi4py import MPI
#============================================
#Objeto mensaje
#============================================
class Mensaje:
    def __init__(self,rank):
        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso" +str(rank) 
#============================================
# programa principal
#============================================  
if __name__ =="_main_" :
    comm =MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    s = Mensaje(rank)
    src= rank-1 if rank != 0 else size-1
    dst = rank+1 if rank!= size-1 else 0

    #============================================
    #envio no bloquenate
    #============================================
    comm.isend(s,dest=dst)
    #============================================
    #recibir no bloqueante con espera
    #req: request (peticion)
    #============================================
    req = comm.irecv(source = src)
    a = req.wait()
    print("soy el proceso",rank,",el resultado es",len(a.x),a.p)
    