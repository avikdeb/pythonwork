print ("Find sum of numbers divisible by 3 and 5")
sum = 0
for i in range(1,50):
	if i%3==0 and i%5 == 0:
		print ("The number is %s" %i)
		sum = sum + i
		
print ("The sum of numbers is %s" %sum)