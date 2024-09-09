# Using while loop:
# ----------------
num = 11
div = 2

while div < num :
    if num % div == 0 :
        print("Not a Prime Number")
        break			
    div += 1
else:
    print("It is a Prime Number")


# Using for loop:
# --------------
num=int(input("Enter the number:"))

if num==2:
    print("It is Prime Number")
else:
    for i in range(2,num):
        if num%i == 0:
            print("It is not a prime")
            break
    else:
        print("It is Prime")
        
