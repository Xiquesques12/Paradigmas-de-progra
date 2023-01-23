#============================================
#mpirun -n 4 python tareas_mpi.py
#============================================
from mpi4py import MPI
#============================================
#objeto de comunicadores
#============================================
comm = MPI.COMM_WOLRD
#============================================
#cuantos somos en total
#============================================
size = comm.Get_size()  
#============================================
#quien soy
#============================================
rank = comm.Get_rank()
#============================================
#so yo soy el cero hago esto
#============================================
if rank==0:
    print("yo soy el proceso 0")
#============================================
#si yo soy el uno hago esto otro
#============================================
elif rank == 1:
    print("yo soy el proceso 1")
#============================================
#si yo no soy ni el uno ni el dos hago esto
#============================================
else:
    print("yo no soy ninguno de los dos primeros procesos")
print("reportandome, yo soy el proceso", str(rank), "de", str(size))