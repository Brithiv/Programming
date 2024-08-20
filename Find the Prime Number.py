num = 11
div = 2

while div < num :
    if num % div == 0 :
        print("Not a Prime Number")
        break			
    div += 1
else:
    print("It is a Prime Number")
