from replit import clear
from art import logo
print(logo)

def highest_bidder(database):
  highest_bid = 0
  winner = " "
  for i in database:
    if database[i] > highest_bid:
      winner = i
      bid_amount = database[i]
  print(f"the winner is {winner} with a bid of ${bid_amount}")
    
database = {}
is_continue = True
while is_continue:
  name = input("What is your name? \n ")
  bidding = int(input("What is your bid? $ \n"))
  database[name] = bidding
  other_bidders = input("Are there any other bidders \n")
  if other_bidders =="no":
    is_continue = False
    highest_bidder(database)
  elif other_bidders == "yes":
    clear()
