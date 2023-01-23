from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD
rank= comm.Get_rank(   )
#tamaño del arreglo
n=10
if rank ==0:
    #arreglo de enteros del 0 al n-1
    data = numpy.arange(n,dtype='i')
else:
    #arreglo vacio de enteros del tamaño n
    data = numpy.empty(n,dtype='i')

#============================================
#broadcast pro qie imdica el tipo de dato
#optimizado para comunicacion rapida
#============================================
comm.Bcast([data,MPI.INT], root=0)
#============================================
#asegurarse que todo salio bien
#============================================
for i in range(n):
    assert data[i]==1
print(data)
