import random
#<Tell us about your Agent here>
# import any external 


class Agent:

	def __init__(self):
		'''
		Place any initialisation code for your agent here (if any)
		'''
		pass

	def next_move(self, game_state, player_state):
		'''
		This method is called each time your Agent is required to choose an action
		If you're just starting out or are new to Python, you can place all your 
		code within the ### CODE HERE ### tags. If you're more familiar with Python
		and how classes and modules work, then go nuts. 
		(Although we recommend that you use the Scrims to check your Agent is working)
		'''

		###### CODE HERE ######

		# a list of all the actions your Agent can choose from
		actions = ['','u','d','l','r','p']

		# randomly choosing an action
		action = random.choice(actions)

		###### END CODE ######

		return action
