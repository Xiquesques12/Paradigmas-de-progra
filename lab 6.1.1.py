from Curva import curva
import matplotlib.pyplot as plt
import math

np: int = 5
a = []
for j in range(0,np):
    a.append((1.0)*math.cos(float(j*2*math.pi/np)))
for j in range(0,np):
    a.append((1.0)*math.sin(float(j*2*math.pi/np)))
curva = Curva(a,2)
n = 1000
dx = 1.0/float(n)
for i in range(0,n):
    r = float(i)*dx
    try:
        [x,y] = curva.interpolacion(2,r)
        plt.scatter(x,y,marker = '0', color = 'blue')
        [x,y] = curva.interpolacion(1,r)
        plt.scatter(x,y,marker='o', color= 'black')
        [x,y] = curva.interpolacion(0,r)
        plt.scatter(x,y,marker = 'o', color = 'red')
    except Exception as es:
        print(e)
        break