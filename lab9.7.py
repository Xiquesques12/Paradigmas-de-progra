from mpi4py import MPI
import numpy
comm = MPI.COMM_WOLRD
rank = comm.Get_rank()

#============================================
#se indica el tipo de datos explicitamente
#============================================

#============================================
#ejemplo 1 usando enteros
#============================================
if rank == 0:
    #============================================
    #arreglo de entero del 0 al 9
    #============================================
    data = numpy.arange(10,dtype = 'i')
    #============================================
    #envio bloqueante especificando el tipo de dato
    #============================================
    comm.Send([data,MPI.INT], dest=1 , tag=77)
elif rank==1:
    data = numpy.empty(10, dtype ='i')
    comm.Recv([data,MPI.INT], source=0, tag=77)
    print(data)
#============================================
#Ejemplo 2 usando flotantes
#============================================
if rank == 0:
    data = numpy.arange(10,dtype=numpy.float64)
    comm.Send(data,dest=1,tag=13)
elif rank ==1:
    data = numpy.empty(10,dtype=numpy.float64)
    comm.Recv(data, source=0,tag=13)
    print(data)