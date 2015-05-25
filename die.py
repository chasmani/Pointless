# A simple die modelled as a Markov process.  
# Using random number generator to roll the die
# Results over a series of rolls are collected and compared to expected values
# As number of rolls increase, percentage result tends towards expected value. 

from random import randint

# Die object to handle rolls
class Die(object):

	def __init__(self):
		self.state = self.roll()

	def roll(self):
		self.state = randint(1,6)
		return self.state

#Collect the results procedulary
die1 = Die()

results = []

rolls = 1000

#roll the dice "rolls" times
#store in results array
for i in range(rolls):

	rolled_number = die1.roll()
	results.append(rolled_number)

# Calculate expected results based on probabilities
print ("Expected- Occurences: " + str(rolls/6) + " Percentage: " + str(float(1)/6)) 

#count number of occurences of each side
for i in range(6):
	occurences =  results.count(i+1)
	percentage = float(occurences)/rolls
	print ("Number " + str(i+1) + "- Occurences: " + str(occurences) + " Percentage: " + str(percentage))