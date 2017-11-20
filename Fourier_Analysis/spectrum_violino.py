import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as scfft #, ifft, fftshift
import math, os
from scipy.io.wavfile import write, read

tol = 1e-14 

##########################################################33
#########Definicao de funcoes

def isPower2(num):
	"""
	Check if num is power of two
	"""
	return ((num & (num - 1)) == 0) and num > 0

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

def wavread(filename):
	"""
	Read a sound file and convert it to a normalized floating point array
	filename: name of file to read
	returns fs: sampling rate of file, x: floating point array
	"""

	if (os.path.isfile(filename) == False):                  # raise error if wrong input file
		raise ValueError("Input file is wrong")

	fs, x = read(filename)

	if (len(x.shape) !=1):                                   # raise error if more than one channel
		raise ValueError("Audio file should be mono")

	if (fs !=44100):                                         # raise error if more than one channel
		raise ValueError("Sampling rate of input sound should be 44100")

	#scale down and convert audio into floating point number in range of -1 to 1
	x = np.float32(x)/norm_fact[x.dtype.name]
	return fs, x

def dftAnal(x, w, N):
	"""
	Analysis of a signal using the discrete Fourier transform
	x: input signal, w: analysis window, N: FFT size 
	returns mX, pX: magnitude and phase spectrum
	"""

	#if not(UF.isPower2(N)):                                 # raise error if N not a power of two
	if not(isPower2(N)):                                 # raise error if N not a power of two
		raise ValueError("FFT size (N) is not a power of 2")

	if (w.size > N):                                        # raise error if window size bigger than fft size
		raise ValueError("Window size (M) is bigger than FFT size")

	hN = (N/2)+1                                            # size of positive spectrum, it includes sample 0
	hM1 = int(math.floor((w.size+1)/2))                     # half analysis window size by rounding
	hM2 = int(math.floor(w.size/2))                         # half analysis window size by floor
	fftbuffer = np.zeros(N)                                 # initialize buffer for FFT
	w = w / sum(w)                                          # normalize analysis window
	xw = x*w                                                # window the input sound
	fftbuffer[:hM1] = xw[hM2:]                              # zero-phase window in fftbuffer
	fftbuffer[-hM2:] = xw[:hM2]        
	X = scfft.fft(fftbuffer)                                      # compute FFT
	absX = abs(X[:int(hN)])                                      # compute ansolute value of positive side
	absX[absX<np.finfo(float).eps] = np.finfo(float).eps    # if zeros add epsilon to handle log
	mX = 20 * np.log10(absX)                                # magnitude spectrum of positive frequencies in dB
	X[:int(hN)].real[np.abs(X[:int(hN)].real) < tol] = 0.0            # for phase calculation set to 0 the small values
	X[:int(hN)].imag[np.abs(X[:int(hN)].imag) < tol] = 0.0            # for phase calculation set to 0 the small values         
	pX = np.unwrap(np.angle(X[:int(hN)]))                        # unwrapped phase spectrum of positive frequencies
	return mX, pX

#################################################

(fs, x) = wavread('violin-B3.wav')
w = np.hamming(1024)
N = 1024
pin = 5000
hM1 = int(math.floor((w.size+1)/2)) 
hM2 = int(math.floor(w.size/2))  
x1 = x[pin-hM1:pin+hM2]
mX, pX = dftAnal(x1, w, N)

plt.figure(1, figsize=(9.5, 7))
plt.subplot(311)
plt.plot(np.arange(-hM1, hM2), x1, lw=1.5)
plt.axis([-hM1, hM2, min(x1), max(x1)])
plt.ylabel('amplitude')
plt.title('x (violin-B3.wav)')

plt.subplot(3,1,2)
plt.plot(np.arange(mX.size), mX, 'r', lw=1.5)
plt.axis([0, mX.size, -90, max(mX)])
plt.title ('magnitude spectrum: mX = 20*log10(abs(X))')
plt.ylabel('amplitude (dB)')

plt.subplot(3,1,3)
plt.plot(np.arange(mX.size), pX, 'c', lw=1.5)
plt.axis([0, mX.size, min(pX), max(pX)])
plt.title ('phase spectrum: pX=unwrap(angle(X))')
plt.ylabel('phase (radians)')

plt.tight_layout()
plt.savefig('spectrum_violino.pdf', dpi = 300, bbox_inches='tight')
#plt.show()
