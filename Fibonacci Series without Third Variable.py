f = -1
s = 1
n = int(input("Enter the number? "))

while 0<n :
    print(f + s, end=" ")
    s = f +s
    f = s - f
    n-=1