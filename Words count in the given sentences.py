sent = input("Enter the Sentences: ")

i = 0
length = len(sent)
count = 1

while i < length :
	if sent[i] == ' ' :
		count += 1
	i += 1
print("Count in the sentences are ", count)