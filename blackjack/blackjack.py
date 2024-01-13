############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Imports the logo provided
#from art import logo
import random
#Make a list that holds the values for all the cards, no names needed
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def draw(deck):
  deck.append(cards[random.randint(0,12)])

def calculate(deck):
  sum = 0;
  for card in deck:
    sum = sum + card
  return sum



def final(player, computer):
  print(f"Your final hand: {player}, final score: {calculate(player)}")
  print(f"Computer's final hand: {computer}, final score: {calculate(computer)}")
  if calculate(player) > 21:
    print("You lost!!")
  elif calculate(player) == calculate(computer):
    print("Its a tie!")
  elif calculate(player) == 21:
    print("You won!")
  elif calculate(computer) == 21:
    print("You lost!!!")
  elif calculate(computer) > 21:
    print("You won!")
  elif calculate(player) < 21 and calculate(computer) < 21:
    if calculate(player) < calculate(computer):
      print("You lost!!!")
    else:
      print("You won!")
  
def decision():
  decision = input("Would you like to draw another card?(y/n)")
  if (decision == "y"):
    return True
  else:
    return False

def blackjack():
  print(logo)
  playerHand = []
  computerHand = []
  draw(playerHand)
  draw(playerHand)
  draw(computerHand)
  print(f"Your cards: {playerHand}, current score: {calculate(playerHand)}")
  print(f"Computer's first card: {computerHand[0]}")
  cont = decision()
  while cont:
    draw(playerHand)
    print(f"Your cards: {playerHand}, current score: {calculate(playerHand)}")
    if calculate(playerHand) > 21:
      cont = False
    else:
      cont = decision()
  while calculate(computerHand) < 17:
    draw(computerHand)
  final(playerHand, computerHand)
  a = input("Would you like to play again?(y/n)")
  if a == "y":
    blackjack()

