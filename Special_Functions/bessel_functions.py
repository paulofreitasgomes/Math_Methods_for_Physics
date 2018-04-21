
"""Link da pagina das definicoes das funcoes de Bessel
do modulo Scipy
https://docs.scipy.org/doc/scipy/reference/special.html
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scsp
import cmath

#para usar Latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.style.use("seaborn-dark") 

Q = 80
eixox = np.linspace(0,10,Q)
Jn1, Jn0 = np.empty(Q), np.empty(Q)
Yn1, Yn0 = np.empty(Q), np.empty(Q) 
jn0_sph, jn1_sph = np.empty(Q), np.empty(Q) 
yn0_sph, yn1_sph = np.empty(Q), np.empty(Q) 

for i in range(Q):
	Jn0[i] = scsp.jn(0,eixox[i])
	Jn1[i] = scsp.jn(1,eixox[i])
	Yn0[i] = scsp.yn(0,eixox[i])
	Yn1[i] = scsp.yn(1,eixox[i])
	jn0_sph[i] = scsp.spherical_jn(0,eixox[i],derivative = False)
	jn1_sph[i] = scsp.spherical_jn(1,eixox[i],derivative = False)
	yn0_sph[i] = scsp.spherical_yn(0,eixox[i],derivative = False)
	yn1_sph[i] = scsp.spherical_yn(1,eixox[i],derivative = False)


plt.plot(eixox, Jn0, '-b', lw = 2, label=r'$J_0(x)$')
plt.plot(eixox, Jn1, '-r', lw = 2, label=r'$J_1(x)$')
plt.plot(eixox, Yn0, '-k', lw = 2, label=r'$Y_0(x)$')
plt.plot(eixox, Yn1, '-g', lw = 2, label=r'$Y_1(x)$')
plt.title('Funcoes de Bessel.', fontsize = 20)
plt.legend(loc='lower right', fontsize = 16)
plt.grid(True)
axes = plt.gca()
axes.set_xlim([0,10])
axes.set_ylim([-1.1,1.04])
plt.xlabel(r'$x$', fontsize = 20) #k indica cor preta
#plt.ylabel(r'Funcoes de Bessel', fontsize = 20)
plt.savefig('bessel_functions.pdf', dpi = 300, bbox_inches='tight')
plt.close()

plt.plot(eixox, jn0_sph, '-b', lw = 2, label=r'$j_0(x)$')
plt.plot(eixox, jn1_sph, '-r', lw = 2, label=r'$j_1(x)$')
plt.plot(eixox, yn0_sph, '-k', lw = 2, label=r'$y_0(x)$')
plt.plot(eixox, yn1_sph, '-g', lw = 2, label=r'$y_1(x)$')
plt.title('Funcoes de Bessel esfericas.', fontsize = 20)
plt.legend(loc='lower right', fontsize = 16)
plt.grid(True)
axes = plt.gca()
axes.set_xlim([0,10])
axes.set_ylim([-1.1,1.04])
plt.xlabel(r'$x$', fontsize = 20) #k indica cor preta
#plt.ylabel(r'Funcoes de Bessel', fontsize = 20)
plt.savefig('spherical_bessel_functions.pdf', dpi = 300, bbox_inches='tight')
plt.close()
