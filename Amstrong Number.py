num= int(input("Enter the Number? "))
num1 = num
amstrong = 0

while 0<num :
    rem = num%10
    amstrong =amstrong + (rem*rem*rem)
    num = num//10
if num1 == amstrong :
    print("It is a Amstrong Number")
else:
    print("It is not a Amstrong Number")