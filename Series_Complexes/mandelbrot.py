import numpy as np
import matplotlib.pyplot as plt
def limite(c,L,Ni):
	z = 0
	for i in range(Ni):
		z = z*z + c
	if abs(z) <= L: 
		res = 1
	else:
		res = 0		
	return res
Ni, L, steps = 100,2.0,1000
x,y = np.linspace(-2,0.5,steps),np.linspace(-1,1,steps)
Ne = len(x)
fm = np.zeros((Ne,Ne))
for ix in range(Ne):
	for iy in range(Ne):
		fm[ix,iy] = limite(complex(x[ix],y[iy]),L,Ni)
plt.imshow(fm,cmap = 'Reds', interpolation = 'bicubic', extent = (x.min(), x.max(), y.min(), y.max()))
plt.title('Fractal Mandelbrot',fontsize=16, color = 'blue')
plt.xlabel(r'Re$(c)$', fontsize = 16) #k indica cor preta
plt.ylabel(r'Im$(c)$', fontsize = 16)
plt.axis('scaled')
axes = plt.gca()
axes.set_xlim([x.min(),x.max()])
axes.set_ylim([y.min(),y.max()])
plt.savefig('fractal_mandelbrot.pdf', dpi = 300)
#plt.show()
