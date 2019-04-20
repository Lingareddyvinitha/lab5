import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,200)
y=np.sin(2*np.pi*20.0/400.0*n)
x=np.random.rand(y.shape[0])
l=len(n)
h=[]
s=l-1
for i in range(l):
	p=x[s-i]
	h.append(p)
print "time reversal x is:\n"

z=len(n)+len(n)-1
r=len(n)
u=[]
for n in range(z):
	q=0
	for k in range(l):
		if n-k<r and n-k>=0:
			q +=x[k]*(h[n-k])
	u.append(q)
print "auto correlation of x is:\n"
	
print u
plt.subplot(211)
plt.plot(x)
plt.subplot(212)
plt.plot(u)
plt.show()