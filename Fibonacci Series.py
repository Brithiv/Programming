# Using while loop:
# ----------------
f,s = -1,1
n = 10		

while 0<n :
    t = f+s
    print(t, end =" ")
    f=s
    s=t
    n-=1

# Using for loop:
# --------------
f=-1
s=1
num = int(input("Enter the number? "))

for i in range(num+1):
    t=f+s
    print(t, end=" ")
    f=s
    s=t
    
