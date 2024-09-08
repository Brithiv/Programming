# Using while loop:
# -----------------
sent = input("Enter the Sentences: ")

i = 0
length = len(sent)
count = 1

while i < length :
	if sent[i] == ' ' :
		count += 1
	i += 1
print("Count in the sentences are ", count)

# Using for loop:
# ---------------
sent = "Welcome to python"       
wordsCount = 1

for x in sent :
    if x==" " :
        wordsCount+=1
print(wordsCount)
