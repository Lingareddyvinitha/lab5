x=input("take x values") #ex:[1,2,3]
y=input("take y values")
l=len(y)
h=[]
s=l-1
for i in range(l):
	p=y[s-i]
	h.append(p)
print "time reversal y is:\n"
print h
z=len(x)+len(h)-1
w=len(x)
r=len(h)
u=[]
for n in range(z):
	q=0
	for k in range(w):
		if n-k<r and n-k>=0:
			q +=x[k]*(h[n-k])
	u.append(q)
print "cross_correlation of x and y is:\n"
	
print u
