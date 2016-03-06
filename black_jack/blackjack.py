import random
import os
import sys
import itertools

# initialize global variables
Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
Deck = list(''.join(card) for card in itertools.product(Ranks))
playerMoney = 1000
gameNum = 0

# bust, a lost
def bust(name):
    print ("\nBust!\n" + name + " loses.\n")

# add a new card to the hand
def hit(hand):
    global Deck
    
    if Deck:# not empty
        new_card = random.sample(Deck, 1)
        hand.append(new_card[0])
    else:# make new deck
        Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
        Deck = list(''.join(card) for card in itertools.product(Ranks))
        new_card = random.sample(Deck, 1)
        hand.append(new_card[0])
    
    print (hand)
    return hand

# return value of hand
def getHand(hand):
    value = 0
    
    # iterate through cards
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

# end result function
def results(blackjack, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name):
    
    # Black jack!
    if (player == 21 and dealer != 21 and blackjack == True):
        print ("\nBlackJack!\n")
        print (name + " wins!\n")
        gameNum += 1
        print ("Number of games won by " + name + ": " + str(gameNum))
        playerMoney += int(bet)
        print ('You have ${0:0.2f} remaining.'.format(playerMoney))
    # Player wins
    elif (player > dealer and bustP == False or bustD == True):
        print ("\n" + name + " wins!")
        gameNum += 1
        print ("Number of games won by " + name + ": " + str(gameNum))
        playerMoney += int(bet)
        print ('You have ${0:0.2f} remaining.'.format(playerMoney))
    # Tie
    elif (player == dealer and bustP == False):
        print ("\nTie!\n")
        print ("Number of games won by " + name + ": " + str(gameNum))
        print ('You have ${0:0.2f} remaining.'.format(playerMoney))
    # Dealer wins
    else:
        print ("\nHouse wins!\n")
        playerMoney -= int(bet)
        print ("Number of games won by " + name + ": " + str(gameNum))
        print ('You have ${0:0.2f} remaining.'.format(playerMoney))
    
    return (playerMoney, gameNum)



def main():
    os.system('clear')
    
    global playerMoney
    global gameNum
    global Deck
    
    game = True
    initial = True
    number = True
    
    print ("Welcome to Black Jack.\n")
    
    # ask for player's name
    name = input ("Please enter your name:\n")
    
    # before starting the game, ask the user if they want to change the default money
    while(initial):
        YN = input ("\nThe default money value is $1000.\nWould you like to set your own value? (Y/N)\n").lower()
        if YN in ('yes', 'y'):
            while(1):
                new_money = input ("Please enter the money value (a whole number):\n$")
                if (new_money.isdigit()):
                    playerMoney = int(new_money)
                    initial = False
                    break
                else:
                    print ("Invalid money value.\n")
        elif YN in ('no', 'n'):
            break
        else:
            print ("\nPlease enter either yes or no.\n")

    # if player wants to toggle card values
    while(1):
        Toggle = input ("\nWould you like to see the card values? (Y/N)\n").lower()
        if Toggle in ('yes', 'y'):
            break
        elif Toggle in ('no', 'n'):
            number = False
            break
        else:
            print ("\nPlease enter either yes or no.\n")

    os.system('clear')
    
    # Start game
    while(game):
        # initialize variables
        bust_player = False
        bust_dealer = False
        turnover_player = False
        turnover_dealer = False
        dealer_value = 0
        player_value = 0
        blackjack = False
        
        # shuffle through deck
        Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
        Deck = list(''.join(card) for card in itertools.product(Ranks))
        
        # grab two cards from deck
        handPlayer = random.sample(Deck, 2)
        
        # remove cards from deck
        for i in handPlayer:
            if Deck:# not empty
                Deck.remove(i)
            else:# make new deck
                Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
                Deck = list(''.join(card) for card in itertools.product(Ranks))
                Deck.remove(i)
    
        handDealer = random.sample(Deck, 2);
        
        for i in handDealer:
            if Deck:# not empty
                Deck.remove(i)
            else:# make new deck
                Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
                Deck = list(''.join(card) for card in itertools.product(Ranks))
                Deck.remove(i)


        # Player's turn

        print ('\nYou have ${0:0.2f}'.format(playerMoney))
        while(1):
            bet = input ('How much money do you want to bet? (a whole number)\n$')
            if (bet.isdigit()):
                if (int(bet) > playerMoney):
                    print ("\nYou cannot bet more than $%s.\n" %playerMoney)
                else:
                    break
            else:
                print ("\nError. Input is not a valid number.\n")
            
        # print the first two cards of player
        print ('PLAYER')
        print (handPlayer)
        player_value = getHand(handPlayer)
        if (number):
            print (player_value)
        
        # print one card for dealer
        print ('\nDEALER')
        print ("['" + str(handDealer[0]) + "']")
        dealer_value = getHand(handDealer[0])
        if (number):
            print (dealer_value)

        # automatic black jack
        if player_value == 21:
            turnover_player = True
            turnover_dealer = True
            blackjack = True

        # get player's input
        count1 = 1
        while (turnover_player == False):
            action = input ('\nWould you like to hit or stand? (Type "hit", "stand", or "help")\n').lower()
            if (action == 'help'):
                print ("\nNumbers from 2 to 9 count as face value\n"+
                       "10, Jack, Queen, and King count as 10\n" +
                       "Ace counts as either 1 or 10\n")
            elif (action == 'hit'):
                hit(handPlayer)
                count1 += 1
                if Deck:# not empty
                    Deck.remove(handPlayer[count1])
                else:# make new deck
                    Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
                    Deck = list(''.join(card) for card in itertools.product(Ranks))
                    Deck.remove(handPlayer[count1])
                
                player_value = getHand(handPlayer)
                if (number):
                    print (player_value)
            
                # bust
                if (player_value > 21):
                    bust_player = True
                    bust(name)
                    break
                # automatic stand if 21
                elif (player_value == 21):
                    turnover_player = True

            elif (action == 'stand'):
                turnover_player = True
            else:
                print ("\nError. Input is not valid.\n")
        
        # Dealer's turn
        print ("\nDealer's hand:")
        print (handDealer)
        dealer_value = getHand(handDealer)
        if (number):
            print (dealer_value)
        
        count = 1
        while (turnover_dealer == False and bust_player == False):
            
            dealer_value = getHand(handDealer)
            # dealer must hit
            while (dealer_value < 17):
                hit(handDealer)
                count += 1
                if Deck:# not empty
                    Deck.remove(handDealer[count])
                else:# make new deck
                    Ranks = '22223333444455556666777788889999TTTTJJJJQQQQKKKKAAAA'
                    Deck = list(''.join(card) for card in itertools.product(Ranks))
                    Deck.remove(handDealer[count])
                
                
                dealer_value = getHand(handDealer)
                if (number):
                    print (dealer_value)
                
                # bust
                if (dealer_value > 21):
                    bust_dealer = True
                    bust('Dealer')
                    break
                # end turn
                elif (dealer_value >= 17 and dealer_value <= 21):
                    turnover_dealer = True
            turnover_dealer = True
    
        # grab final card values
        player_value = getHand(handPlayer)
        dealer_value = getHand(handDealer)
        
        # get results
        (playerMoney, gameNum) = results(blackjack, player_value, dealer_value, bust_player, bust_dealer, playerMoney, gameNum, bet, name)
        
        # continue playing?
        if (playerMoney <= 0):
            print ('You are out of money!')
            game = False
        else:
            cont_game = input('\nWould you like to keep playing? (Y/N)\n').lower()
            if cont_game  in ('no', 'n'):
                game = False
            else:
                os.system('clear')

if __name__ == '__main__':
    main()