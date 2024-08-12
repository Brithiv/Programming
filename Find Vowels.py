name = input("Enter your name: ")

i = 0
length = len(name)

while i < length :
	if name[i] in ['a', 'e', 'i', 'o', 'u'] :
		print(name[i], end=' ')
	i += 1