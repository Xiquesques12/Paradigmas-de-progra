#============================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun -n 4 python3 hola_mpi.py
#============================================
#para correr en 4 procesos
#============================================
from mpi4py import MPI
#============================================
#crear un objeto comunicador
#============================================
comunicadores = MPI.COMM_WOLRD
#============================================
#numero total de procesos
#============================================
n_procesos = comunicadores.Get_size()
#============================================
#Numero identificador de este proceso
#============================================
quien_soy = comunicadores.Get_rank()
print("saludos desde el proceso", str(quien_soy),"de", str(n_procesos))
