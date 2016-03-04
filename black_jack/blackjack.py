import random

import itertools

Ranks = '23456789TJKQKA'
Deck = tuple(''.join(card) for card in itertools.product(Ranks))
defaultMoney = 1000

#functions
def deal():
    pass

def hit():
    pass

def bust():
    pass

def stand():
    pass

# return value of hand
def getHand(hand):
    value = 0
    
    for x in hand:
        if(x == 'A'):
            value += 1
        elif(x.isalpha()):
            value += 10
        else:
             value += int(x)

# if the hand has two aces
    if(value == 2):
        value = 12
# if there's one ace
    elif('A' in hand and value <= 11):
        value += 10

    return value



def main():
    handPlayer = random.sample(Deck, 2);
    dealerPlayer = random.sample(Deck, 2);
    
    print handPlayer
    print getHand(handPlayer)
    
    print dealerPlayer
    print getHand(dealerPlayer)

if __name__ == '__main__':
    main()