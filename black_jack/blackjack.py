import random
import os
import itertools

Ranks = '23456789TJKQKA'
Deck = tuple(''.join(card) for card in itertools.product(Ranks))
playerMoney = 1000

#functions
def bust(name):
    print "\nBust!\n" + name + " loses."

# add a new card to the hand
def hit(hand):
    new_card = random.sample(Deck, 1)
    hand.append(new_card[0])
    print hand

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
    os.system('clear')
    global playerMoney
    
    game = True
    initial = True
    number = True
    gameNum = 0
    
    print ("Welcome to Black Jack.\n")
    
    # ask for player's name
    name = raw_input ("Please enter your name:\n")
    
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

    # if player wants to toggle card values
    while(1):
        Toggle = raw_input ("Would you like to see the card values? (Y/N)\n").lower()
        if Toggle in ('yes', 'y'):
            break
        elif Toggle in ('no', 'n'):
            number = False
            break
        else:
            print "\nPlease enter either yes or no.\n"

    os.system('clear')
    while(game):
        handPlayer = random.sample(Deck, 2);
        handDealer = random.sample(Deck, 2);
        bust_player = False
        bust_dealer = False
        turnover_player = False
        turnover_dealer = False
        bet_value = 0
        dealer_value = 0
        player_value = 0

        # Player's turn
        print 'PLAYER'
        print handPlayer
        player_value = getHand(handPlayer)
        if (number):
            print player_value
        
        print '\nDEALER'
        print handDealer
        dealer_value = getHand(handDealer)
        if (number):
            print dealer_value

        print '\nYou have ${0:0.2f}'.format(playerMoney)
        while(1):
            bet = raw_input ('How much money do you want to bet? (a whole number)\n$')
            if (bet.isdigit()):
                if (int(bet) > playerMoney):
                    print "\nYou cannot bet more than $%s.\n" %playerMoney
                else:
                    break
            else:
                print "\nError. Input is not a valid number.\n"



        while (turnover_player == False):
            action = raw_input ('Would you like to hit or stand? (Type "hit", "stand", or "help")\n').lower()
            if (action == 'help'):
                print ("\nNumbers from 2 to 9 count as face value\n"+
                       "10, Jack, Queen, and King count as 10\n" +
                       "Ace counts as either 1 or 10\n")
            elif (action == 'hit'):
                hit(handPlayer)
                player_value = getHand(handPlayer)
                if (number):
                    print player_value
                
                # bust
                if (player_value > 21):
                    bust_player = True
                    bust(name)
                    break
            elif (action == 'stand'):
                turnover_player = True
            else:
                print "\nError. Input is not valid.\n"

        # Dealer's turn
        while (turnover_dealer == False and bust_dealer == False):
            dealer_value = getHand(handPlayer)
            # dealer must hit
            if (dealer_value < 17):
                hit(handDealer)
                dealer_value = getHand(handDealer)
                if (dealer_value > 21):
                    bust_dealer = True
                    bust('Dealer')
                    break
                else:
                    turnover_dealer = True
            else:
                turnover_dealer = True
                    
#        player_value = getHand(handPlayer)
#        dealer_value = getHand(handDealer)

        if (player_value > dealer_value and bust_player == False):
            print name + " wins!"
            gameNum += 1
            print "Number of games won by " + name + ": " + str(gameNum)
            bet_value += bet
        game = False
    
    
    
           #print handPlayer
           #print getHand(handPlayer)
    
           #print dealerPlayer
           #print getHand(dealerPlayer)

if __name__ == '__main__':
    main()