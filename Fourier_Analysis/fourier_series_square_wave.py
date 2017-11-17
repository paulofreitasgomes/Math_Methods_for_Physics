import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

#para usar Latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.style.use("ggplot") #estilo de grafico

#############################################
#########Funcoes

def onda_quadrada(x,T,A,y0 = -1):
	''' Esta funcao cria uma funcao f de onda quadrada com:
	periodo = T
	amplitude = A
	y0 e opcional. Se y0 = 0, a funcao sera somente positiva, 0 < f < A
	o default e a funcao ter media zero: -A/2 < f < A/2
	'''
	if y0 == 0:
		C = A/2
	else:
		C = 0
	return C+(A/2)*signal.square((2/T)*math.pi*x)


# coeficientes
def bn(n):
	n = int(n)
	if (n%2 != 0):
		return 4/(np.pi*n)
	else:
		return 0

def serie_fourier(x, n_max, A, y0 = -1):
	'''x = vetor contendo o dominio da funcao
	n_max = numero de termos na expansao de Fourier
	A = amplitude
	y0 e opcional. Se y0 = 0, a funcao sera somente positiva, 0 < f < A
	o default e a funcao ter media zero: -A/2 < f < A/2
	'''
	Nx = len(x)
	g = np.zeros(Nx)
	for i in range(Nx):
		a0 = 0
		partialSums = a0
		for n in range(1,n_max):
			try:
				partialSums = partialSums + bn(n)*np.sin((2*np.pi*n*x[i])/T)
			except:
				print("pass")
				pass
		g[i] = partialSums
	if y0 == 0:
		C = A/2
	else:
		C = 0
	return C+(A/2)*g

#########Fim das funcoes ##################33
########################################################

#Intervalo em x
x = np.linspace(-2*math.pi,2*math.pi,1000)

T = 2*math.pi #periodo
A = 4 #amplitude
y0 = 0 #opcional
#N_harm = 14 #numero de termos na expansao de Fourier

f = onda_quadrada(x, T, A, y0) #expressao analitica da funcao a ser expandida
g2 = serie_fourier(x, 2, A, y0) #expansao considerando 2 termos
g10 = serie_fourier(x, 10, A, y0) #expansao considerando 10 termos


plt.plot(x, f, 'b', lw = 2, label=r'$f(x)$')
plt.plot(x, g2, 'k', lw = 2, label=r'$g_2(x)$')
plt.plot(x, g10, 'r', lw = 2, label=r'$g_{10}(x)$')
plt.title('Onda quadrada.')
plt.legend(loc='lower left',fontsize = 14)
plt.xlabel(r'$x$', fontsize = 16) #k indica cor preta
plt.ylabel(r'$y(x)$', fontsize = 16)
plt.savefig('fourier_series_square_square_wave.png', dpi = 300, bbox_inches='tight')