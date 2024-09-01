num = int(input("Enter the number? "))
num1 =num		
initial = 0

while 0<num:		
    initial = initial * 10 + num%10
    num=num//10
print(initial)
if num1 == initial :
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
