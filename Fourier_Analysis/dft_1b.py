import numpy as np
import matplotlib.pyplot as plt
import cmath #modulo para lidar com numeros complexos

#Funcao que calcula a transformada
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)
    return c

#Acertar a fonte para usar latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#Importando o arquivo com o sinal de audio
y = np.loadtxt("pitch.txt",float)
c = dft(y) #Calculando a transformada

#Preparacao do graficos
fig, ax1 = plt.subplots()
plt.title('Transformada Discreta de Fourier',fontsize=20)
#Eixo da esquerda
ax1.plot(abs(c), '-b', lw = 2)
ax1.set_xlabel('$k$', fontsize = 20)
ax1.set_ylabel(r'$\vert c_k \vert$', color='b', fontsize = 20)
ax1.tick_params('y', colors='b')

#Eixo da direita
ax2 = ax1.twinx()
ax2.plot(y, '-r', lw = 2)
ax2.set_xlim(0,500)
ax2.set_ylabel('$y_k$', color='r', fontsize = 20)
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.savefig('DFT_1b_grafico.pdf',dpi=200)