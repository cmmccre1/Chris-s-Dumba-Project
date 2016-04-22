import random

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

twos=Stack();
threes=Stack();
fours=Stack();
fives=Stack();
sixes=Stack();
sevens=Stack();
eights=Stack();
nines=Stack();
tens=Stack();
elevens=Stack();
decksize = 52;

for x in range(0,4):
	twos.push(2);
	
for x in range(0,4):
	threes.push(3);
	
for x in range(0,4):
	fours.push(4);
	
for x in range(0,4):
	fives.push(5);
	
for x in range(0,4):
	sixes.push(6);
	
for x in range(0,4):
	sevens.push(7);
	
for x in range(0,4):
	eights.push(8);
	
for x in range(0,4):
	nines.push(9);
	
for x in range(0,16):
	tens.push(10);
	
for x in range(0,4):
	elevens.push(11);


class Player:
	def __init__(self):
		self.handValue = 0;
		self.money = 200;
		random.seed();
		
		
	def winMoney(self, winnings):
		self.money += winnings
		
	def addCard(self, newCard):
		self.handValue += newCard
		
	def setHand(self, newHand):
		self.handValue = newHand
		
	def loseMoney(self, losings):
		self.money -= losings
		
	def clearHand(self):
		self.handValue = 0
		
	def hand(self):
		return self.handValue
		
	def draw(self):
		drawInt = random.randint(2,11)
		card_drawn = False;
		while(not (card_drawn) and (decksize > 0)):
			if(drawInt == 2):
				if(twos.size() > 0):
					self.addCard(twos.pop());
					card_drawn = True;
				else:
					continue;	
			elif(drawInt == 3):
				if(threes.size() > 0):
					self.addCard(threes.pop());
					card_drawn = True;
				else:
					continue;
			elif(drawInt == 4):
				if(fours.size() > 0):
					self.addCard(fours.pop());
					card_drawn = True;
				else:
					continue;
			elif(drawInt == 5):
				if(fives.size() > 0):
					self.addCard(fives.pop());
					card_drawn = True;
				else:
					continue;
			elif(drawInt == 6):
				if(sixes.size() > 0):
					self.addCard(sixes.pop());
					card_drawn = True;
				else:
					continue;	
			elif(drawInt == 7):
				if(sevens.size() > 0):
					self.addCard(sevens.pop());
					card_drawn = True;
				else:
					continue;
			elif(drawInt == 8):
				if(eights.size() > 0):
					self.addCard(eights.pop());
					card_drawn = True;
				else:
					continue;	
			elif(drawInt == 9):
				if(nines.size() > 0):
					self.addCard(nines.pop())
					card_drawn = True;
				else:
					continue;
			elif(drawInt == 10):
				if(tens.size() > 0):
					self.addCard(tens.pop())
					card_drawn = True;
				else:
					continue;	
			elif(drawInt == 11):
				if(elevens.size() > 0):
					self.addCard(elevens.pop())
					card_drawn = True;
				else:
					continue;

player = Player();
dealer = Player();
play = True;
bust = False;
currentBet = 10;

while(decksize > 0):
	print();

	play = True
	while(play == True):
		if(player.hand() == 0):
			player.draw()
			player.draw()
			dealer.draw()
		print("You have a total of : " + str(player.hand()))
		print("The dealer is showing a " + str(dealer.hand()))
		
		msg = input("Hit, Stay, or Split?")
		if(msg.lower() == "hit"):
			temp = player.hand();
			player.draw();
			if(player.hand() > 21):
				print("Your total is " + str(player.hand()));
				print("You drew a " + str(player.hand() - temp) + " and busted");
				bust = True;
				play = False;
				player.clearHand();
				dealer.clearHand();
		if(msg.lower() == "stay"):
			dealer.draw();
			print("dealer now has a total of " + str(dealer.hand()));
			while(dealer.hand() <17):
				dealer.draw();
				print("Dealer hand: " + str(dealer.hand()));
			if(dealer.hand() > 21):
				print("Dealer hand: " + str(dealer.hand()));
				print("Dealer drew a " + str(dealer.hand() - 21));
				print("dealer busts you win!");
				player.clearHand();
				dealer.clearHand();
				play = False;
			else:
				if(dealer.hand() > player.hand()):
					print("Dealer wins!");
					player.clearHand();
					play = False;
					dealer.clearHand();
				else:
					print("You win!");
					player.clearHand();
					play = False;
					dealer.clearHand();