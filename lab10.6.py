from mpi4py import MPI
import math
import os
import time

def calc():
    for i in range(0,400000):
        math.sqrt(i)
procesos = []
cpus = os.cpu_count()
print ("Nucelos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el proceso %d" %i)
    procesos.append(Process(target=calc))
start = time.time()
for proceso in procesos:
    proceso.start()
for proceso in procesos:
    proceso.join()
end = time.time()
print("se tardo: ",end-start)
