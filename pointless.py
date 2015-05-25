# Models the number of new teams on each show of the BBC gameshow "Pointless"
# There are 4 teams on each episode.  
# Teams get two chances to win the gameshow
# If a team wins the show they are replaced by a new team next episode
# If a team loses two episodes they are replaced by a new team next episode
# This program models that process assuming random winners

from random import randint

# Game object to handle progression of teams
class Game(object):

	def __init__(self):
		self.players = [1,1,1,1]

	def episode(self):
		self.who_wins()
		self.next_state()

	# Randomly assigns one team as winner
	def who_wins(self):
		winning_team = randint(0,3)
		self.players[winning_team] = "W"
		return self.players

	# Moves onto the next show, bringing on new teams if they
	# have been on twice or won
	def next_state(self):
		new_players = []
		for team in self.players:
			if team == 1:
				new_players.append(2)
			else:
				new_players.append(1)
		self.players = new_players
		return new_players

	def get_players(self):
		return self.players

series1 = Game()

number_of_episodes = 10000000

# Run through the episodes and record the number of occurences 
# of each possible number of new players 
results_summary = []

for i in range(number_of_episodes):
	series1.episode()
	players = series1.get_players()
	new_players = players.count(1)
	results_summary.append(new_players)

#count and print number of occurences of each number of new players
for i in range(4):
	occurences =  results_summary.count(i+1)
	percentage = float(occurences)/number_of_episodes
	print ("Number " + str(i+1) + "- Occurences: " + str(occurences) + " Percentage: " + str(percentage))