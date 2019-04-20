x=input("take x values") #ex:[1,2,3]
h=input("take y values") 
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
		
	
print u
