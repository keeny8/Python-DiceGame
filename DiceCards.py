import random

#Game from when we were kids
#	We have 6 dice and we bet if we will match the card or not
	
class Dice:
	@staticmethod
	def roll():
		return (random.randint(0,5)+1)
		
class Card:
	@staticmethod
	def getCard():
		card = [0,0,0,0,0,0]
		i = 0
		while i < len(card):
			card[i] = Dice.roll()
			i+=1
		return card

class DiceHolder:
	def __init__(self, diceCount=9):
		self.diceCount = diceCount
		self.shakeDice()
		
	def __str__(self):
		retStr = "";
		for x in self.diceValues:
			retStr = retStr+str(x)+", "
		retStr = retStr+"\n"
		return retStr
		
	def setDiceCount(self, amount):
		self.diceCount = amount
	
	def getDice(self):
		return self.diceValues
	
	def shakeDice(self):
		self.diceValues = []
		i = 0
		while i < self.diceCount:
			self.diceValues.append(Dice.roll())
			i += 1
	
class DiceCards:
	@staticmethod
	def playARound():
		card = Card.getCard()
		card.sort()		
		matches = card.copy()
		print("Card: ")
		print(card)

		i = 0
		won = False
		diceholder = DiceHolder()
		while i < 3:
			diceholder.shakeDice()	
			diceholder.getDice().sort()
			print("Dice Roll: ")
			print(diceholder.getDice())
			#matches
			for dice in diceholder.getDice():
				cardIndex = 0
				while cardIndex < len(matches):
					if matches[cardIndex] == dice:
						#dice matches set matches to 0
						matches[cardIndex] = 0
						diceholder.setDiceCount(diceholder.diceCount-1)	
						break
					cardIndex += 1
			print("Matches: ")
			print(matches)
			if sum(matches) == 0:
				won = True
				break
			i += 1			
		if won:
			print("Game Won!")
			return 1
		else:
			print("Round Lost")
			return 0	
			
while True:
	win = DiceCards.playARound()
	print("Play again? y/n")
	input1 = input()
	if(input1!='y' != input1!='yes'):
		break