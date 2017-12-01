"""
Codigo adaptado de:
http://firsttimeprogrammer.blogspot.com.br/2015/03/taylor-series-with-python-and-sympy.html
"""

import sympy as sy
import numpy as np
import sympy.functions as syfun #erf(x) no Sympy
import matplotlib.pyplot as plt
import scipy.special as scysp #erf(x) no Scipy
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.style.use("ggplot") #estilo do grafico

# Funcao fatorial
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

#Expansao de Taylor em x0 da funcao function
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    return p

# Definicao da funcao f a ser expandida
x = sy.Symbol('x') #define x como sendo uma variavel analitica
f = syfun.erf(x) #definicao da funcao a ser expandida

#Grafico da serie de Taylor de f
x_lims = [-5,5]
x1 = np.linspace(x_lims[0],x_lims[1],800)
y1 = []
cores = ['g', 'b', 'r', 'y'] #cores
i2 = 0

for j in range(1,32,10):
    func = taylor(f,0,j)
    #print('Taylor expansion at n='+str(j),func)
    for k in x1:
        y1.append(func.subs(x,k))
    plt.plot(x1,y1,cores[i2],label=r'$q=$ '+str(j))
    i2 += 1
    y1 = []

Nx1 = len(x1)
func = np.empty(Nx1)
for i in range(Nx1): #calculando a funcao 
    func[i] = scysp.erf(x1[i])

#Grafico da funcao f
plt.plot(x1,func, '--k', label = r'erf$(x)$')
plt.xlim(x_lims)
plt.ylim([-5,5])
plt.xlabel(r'$x$',fontsize = 16)
plt.ylabel(r'$y(x)$',fontsize = 16)
plt.legend(loc='lower right',fontsize = 14)
plt.grid(True)
plt.title(r'Serie de Taylor $g_q(x)$')

plt.savefig('serie_taylor_erf.pdf',dpi = 300, bbox_inches='tight')
