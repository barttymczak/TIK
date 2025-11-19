import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

dane = np.loadtxt("dane1.txt", skiprows = 1)
x_dane = dane[:,0]
y_dane = dane[:,1]

def f(x, a, b):
    return a*x+b

parameters, covariance = spo.curve_fit(f, x_dane, y_dane)

print(covariance)
errors = np.sqrt(np.diag(covariance))
print(errors)
print("a = ", parameters[0], "pm ", errors[0])
print("b = ", parameters[1], "pm ", errors[1])

my_x = np.linspace(-6,10,100)

plt.figure()
plt.scatter(x_dane,y_dane, c="green", marker="x", colorizer="pink",
            s=10, lw=0.75, label="dane pomiarowe"
            )
plt.plot(x_dane,f(x_dane, parameters[0], parameters[1]), c="crimson", label="f(x)=ax+b", lw=2)
plt.title("a= "+format(parameters[0], ".3f")+"$\\quad b= $"+format(parameters[1], ".2f"))
plt.xlabel("$x$",loc="right")
plt.ylabel("$y$",loc="top")
plt.xlim(-6,12)
plt.ylim(-16,22)
plt.legend(frameon=False)
plt.savefig("wykres_dane1.pdf")
plt.close()

dane2 = np.loadtxt("dane2.txt", skiprows = 1)
t_dane = dane2[:,0]
x_dane = dane2[:,1]
x_err = dane2[:,2]

def g(t,a,v_0,x_0):
    return 0.5*a*t**2+v_0*t+x_0

parameters2, covariance2 = spo.curve_fit(g, t_dane, x_dane, sigma=x_err, absolute_sigma=True)
my_t = np.linspace(0,10,200)
errors2 = np.sqrt(np.diag(covariance2))

plt.figure()
plt.errorbar(t_dane, x_dane, x_err, fmt="o", markersize = 3, capsize= 3)
plt.plot(my_t,g(my_t , *parameters2),color="pink")
plt.legend(frameon=False)
plt.xlabel("$t$ [s]",loc="right")
plt.ylabel("$x$ [m]",loc="top")
plt.xlim(0,10)
plt.ylim(-10,100)

plt.savefig("wykres_dane2.pdf")
plt.close()

x_fit=g(my_t , *parameters2)

chi2= np.sum((x_dane-x_fit)**2/x_err**2)
dof = len(x_dane) - len(parameters2)
print("chi2/dof = ", chi2/dof)
