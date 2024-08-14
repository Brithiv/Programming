name = input("Enter your name: ")

i = 0
length = len(name)

while i < length :
	if name[i] not in ['a', 'e', 'i', 'o', 'u'] :
		print(name[i])
	i += 1