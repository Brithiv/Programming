start = 1
end = int(input("Enter your Numb: "))

while end >= 1 :		# put 1 or else while multiple if you put 0 answer also will be 0.
	start = start * end
	end -= 1
print(start)