name = input("Enter your name: ")

i = 0
length = len(name)
count = 0

while i < length :
	if name[i] in ['a', 'e', 'i', 'o', 'u'] :
		count += 1
	i += 1
print("Vowel count is ", count)