f,s = -1,1
n = 10		# they are ordering 1st 10 multiplies

while 0<n :
    t = f+s
    print(t, end =" ")
    f=s
    s=t
    n-=1