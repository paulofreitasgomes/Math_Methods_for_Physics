import numpy as np
import matplotlib.pyplot as plt
#from scipy import fft #modulo que calcula transformada rapida de Fourier

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

Fs = 150                         # sampling rate
Ts = 1.0/Fs                      # intervalo de tempo de gravacao
t = np.arange(0,1,Ts)            # cria um vetor de 1 a 1 com step de Ts
ff = 5                           # frequency of the signal
y = np.sin(2 * np.pi * ff * t)

plt.subplot(2,1,1)
plt.plot(t,y,'-b', lw = 2)
plt.xlabel(r'Tempo $t$')
plt.ylabel(r'Amplitude $y(t)$')

plt.subplot(2,1,2)
n = len(y)                       # numero de componentes em y
k = np.arange(n) #cria um vetor de 0 a n-1 com n componentes
T = n/Fs
frq = k/T # two sides frequency range
freq = frq[range(int(n/2))]           # remove o lado negativo

Y = np.fft.fft(y)/n              # fft computing and normalization
Y = Y[range(int(n/2))]

plt.plot(freq, abs(Y), '-r', lw = 2)
plt.xlabel(r'Frequencia $f$ (Hz)')
plt.ylabel(r'$\vert \Gamma (f) \vert $')
plt.savefig('grafico_FFT_sine.pdf',dpi = 300, bbox_inches='tight')

