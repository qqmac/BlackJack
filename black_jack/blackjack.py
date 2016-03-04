import random

import itertools

Ranks = '23456789TJKQKA'
Deck = tuple(''.join(card) for card in itertools.product(Ranks))
playerMoney = 1000

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
# if there's one ace and it can be 11
    elif('A' in hand and value <= 11):
        value += 10

    return value



def main():
    global playerMoney
    
    game = True
    initial = True
    
    # before starting the game, ask the user if they want to change the default money
    while(initial):
        YN = raw_input ("\nThe default money value is $1000.\nWould you like to set your own value? (Y/N)\n").lower()
        if YN in ('yes', 'y'):
            while(1):
                new_money = raw_input ("Please enter the money value (a whole number):\n$")
                if (new_money.isdigit()):
                    playerMoney = int(new_money)
                    initial = False
                    break
                else:
                    print "Invalid money value.\n"
        elif YN in ('no', 'n'):
            break
        else:
            print "\nPlease enter either yes or no.\n"

    while(game):
        handPlayer = random.sample(Deck, 2);
        dealerPlayer = random.sample(Deck, 2);
        bust_player = False
        bust_dealer = False
        turnover_player = False
        turnover_dealer = False

        # Player's turn
        print '\nYou have ${0:0.2f}'.format(playerMoney)
        while(1):
            bet = raw_input ('PLAYER: How much money do you want to bet? (a whole number)\n$')
            if (bet.isdigit()):
                if (int(bet) > playerMoney):
                    print "\nYou cannot bet more than $%s.\n" %playerMoney
                else:
                    break
            else:
                print "\nError. Input is not a valid number.\n"



        game = False
    
    
    
    print handPlayer
    print getHand(handPlayer)
    
    print dealerPlayer
    print getHand(dealerPlayer)

if __name__ == '__main__':
    main()