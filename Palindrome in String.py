num = "1221"
lenght = len(num) -1
reverse = ""

while lenght >= 0:	
    reverse = reverse + num[lenght]
    lenght-=1
print(reverse)
if num == reverse:
    print("It is a Palindrome")
else:
    print("Not a Plaindrome")

#         (OR)

name1 = input("Enter name? ")
name2 = name1[::-1]
print(name2)

if name1 == name2 :
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
