from mpi4py import MPI
import math
import os
import time

def calc():
    for i in range (0,4000000):
        math.sqrt(i)
threads = []
cpus  = os.cpu_count()
print("nucleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" %i)
    threads.append(Thread(target=calc))
start = time.time()
for thread in threads:
    thread.start()
for tread in threads:
    thread.join()
end = time.time()
print("se tardo: ",end-start)