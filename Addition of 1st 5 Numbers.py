# Using for loop
# --------------

num = int(input("Enter the number? "))
total = 0

for x in range(1, num + 1):
    total = total + x
print(total)

# Using while loop
# ----------------

initial_amount = 0
amount = 1
days = 10

while amount<=days:
	initial_amount = initial_amount + amount
	amount += 1
print(initial_amount)



