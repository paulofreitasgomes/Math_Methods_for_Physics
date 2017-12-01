import math
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
def calc_pi(Nlados, raio):
	pontos = int(Nlados)+1 #n de lados
	nx, ny = [], [] #coordenadas dos vertices
	for theta in np.linspace(0,2*np.pi,pontos):
		nx.append(raio*np.cos(theta))
		ny.append(raio*np.sin(theta))    
	N = len(nx)
	area_p = 0.0
	for i in range(N-1):
	    area_p += nx[i]*ny[i+1] - nx[i+1]*ny[i]
	area_p = 0.5*abs(area_p) #area do poligono
	pi_est = area_p / raio **2
	return pi_est

def grafico(Nlados, raio):
	pontos = int(Nlados)+1 #n de lados
	nx, ny = [], [] #coordenadas dos vertices
	for theta in np.linspace(0,2*np.pi,pontos):
		nx.append(raio*np.cos(theta))
		ny.append(raio*np.sin(theta))
	circulo = plt.Circle((0,0), raio, lw = 3, edgecolor = 'r', facecolor = 'none')
	fig = plt.gcf()
	ax = fig.gca()
	ax.add_artist(circulo)
	plt.plot(nx,ny,c='b', lw=1)
	plt.fill_between(nx,ny) #cor do poligono
	plt.title('$N=$ '+str(Nlados)+', $r=$ '+str(raio)+'.', fontsize = 16)
	plt.axis('equal')
	plt.xticks([])
	plt.yticks([])
	axes = plt.gca()
	axes.set_ylim([-1.2,1.2])
	axes.set_xlim([-1.2,1.2])
	plt.savefig("figura.pdf", dpi = 300)
	plt.close()

def grafico2(raio, L):
	lados = np.arange(3,L,1)
	ele = len(lados)
	pi_est = np.zeros(ele)
	ind = 0
	func_pi = math.pi*np.ones(ele)
	for nl in lados:
		pi_est[ind] = calc_pi(nl,raio)
		ind += 1
	erro = (math.pi - pi_est[ele-1])*(100/math.pi)
	axes = plt.gca()
	plt.plot(lados,pi_est,'-b', lw = 2, label = '$\pi_e (N)$')
	plt.plot(lados,func_pi,'--r', lw = 2, label = r'$\pi=$ 3.1415...')
	plt.legend(loc='lower right',fontsize = 16)
	plt.xlabel(r'Lados $N$ ', fontsize = 16) #k indica cor preta
	plt.ylabel(r'Valores de $\pi$', fontsize = 16)
	axes.set_ylim([1.0,3.5])
	plt.text(70,1.7,r'$\Delta =$ '+str(round(erro,2))+'%',fontsize = 16, color = 'k')
	plt.savefig("figura2.pdf", dpi = 300)
	plt.close()

L, raio = 100, 1.0
grafico(6, raio)
grafico2(raio, L)
