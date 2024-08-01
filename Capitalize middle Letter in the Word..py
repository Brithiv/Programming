# In the name, the middle letter must be capital and
# the remaining name should be small

name = input("Enter your Name: ")
i=0
mid = len(name) // 2
print(name[:mid] + name[mid].upper() + name[mid + 1:])