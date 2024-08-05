# Multiples of 2 and 3:
# --------------------

start = 1
end = 20

start = 6
while start<=20:
    print(start, end= " ")
    start+=6

# Other Method:
# ------------

while start <= end :
    if start % 2 == 0 and start % 3 == 0:
        print(start, end =" ")
    start += 1
