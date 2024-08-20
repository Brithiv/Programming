num = 11
div = 2

while div < num :
    if num % div == 0 :
        print("Not a Prime Number")
        break			# give a non-prime number then only you will know why you are using 'break' here.
    div += 1
else:
    print("It is a Prime Number")