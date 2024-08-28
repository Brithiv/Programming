num = int(input("Enter the number? "))
initial =0

while 0<num :
    initial = initial +num%10
    num = num//10
print(initial)