name = input("Enter your name: ")

i = 0
length = len(name)

while i < length :
	if name[i] in ['a', 'e', 'i', 'o', 'u'] :
		print(name[i], end=' ')
	i += 1

	(OR)

name = input("Enter your name: ")

i = 0
length = len(name)

while i < length :
	if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u' :
		print(name[i])
	i += 1
