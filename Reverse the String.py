num = "Hello"
lenght = len(num) -1
reverse = ""

while lenght >= 0:
    reverse = reverse + num[lenght]
    lenght-=1
print(reverse)