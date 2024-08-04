# Using for loop:
# Even Numbers from 2-20:

for i in range(2,21,2):
    print(i, end=" ")

# Other Method:
# -------------

count = 2
while count<=20 :
    print(count, end=" ")
    count+=2

# Using while loop:
# -----------------
start = 2
end =20
while start <= end :
    if start % 2 == 0 :
        print(start, end =" ")
    start += 1