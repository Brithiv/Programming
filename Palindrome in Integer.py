num = int(input("Enter the number? "))
num1 =num		# Take a copy of num = num1 (in next comment you will be knowing the answer)
initial = 0

while 0<num:		# 'while' will run until num>0 after that it will become num=0, inthose case you can't compare 'num' with 'initial'
    initial = initial * 10 + num%10
    num=num//10
print(initial)
if num1 == initial :
    print("It is a Palindrome")
else:
    print("Not a Palindrome")