import numpy as np
import math
import matplotlib.pyplot as plt

lista=[1,4,7,9]
tab1 =np.array(lista)
print(2*tab1)
print(np.sin(tab1))
tab2 = np.array([[1,4,7,9],[2,5,8,3]])
print(tab2)
print(len(tab1), len(tab2))
print(np.shape(tab1), np.shape(tab2))
print(tab2[:,2])
print(np.reshape(tab1,(2,2)))

tab8 = np.arange(0,10,1)
tab8 = 2**tab8
print(tab8)

x=np.linspace(-3*np.pi, 3*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
xmax = np.arange(-2*np.pi+np.pi/2, 3*np.pi, 2*np.pi)
ymax = np.ones(3)

ticks = np.arange(-3*np.pi, 10, np.pi)
print(ticks)

plt.figure(figsize=(8,5),facecolor="grey")
plt.plot(x,y1,color="navy", ls="dashed", lw=0.75)
plt.plot(x,y2,color="crimson", ls="dotted", lw=0.75)
plt.scatter(xmax, ymax, size=3, color="teal")

plt.grid(lw=0.5)
plt.xlabel("$\\alpha$")
plt.ylabel("$f(\\alpha)$")
plt.xlim(-3*np.pi, 3*np.pi,)
plt.ylim(-1.5 , 1.5)
plt.xticks(ticks,["$-3*\\pi$","$-2*\\pi$","$-\\pi$","$0$","$\\pi$","$2*\\pi$","$3*\\pi$"])
plt.legend(frameon=False, loc=2, fontsize=12)
plt.title("wykres")

plt.savefig('plot.pdf')
plt.close()
