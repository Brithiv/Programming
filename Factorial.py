# Using While loop:
# ----------------
start = 1
end = int(input("Enter your Numb: "))

while end >= 1 :		
	start = start * end
	end -= 1
print(start)


# Using For loop:
# ---------------
num = int(input("Enter the number? "))
total = 1

for x in range(1, num + 1):
    total = total * x
print(total)
