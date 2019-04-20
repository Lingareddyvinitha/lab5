x=input("take x values") #ex:[1,2,3]
l=len(x)
h=[]
s=l-1
for i in range(l):
	p=x[s-i]
	h.append(p)
print "time reversal x is:\n"
print h
z=len(x)+len(h)-1
r=len(h)
u=[]
for n in range(z):
	q=0
	for k in range(l):
		if n-k<r and n-k>=0:
			q +=x[k]*(h[n-k])
	u.append(q)
print "auto correlation of x is:\n"	
print u
