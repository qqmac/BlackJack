import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import blackjack

class BlackJackTestCase(TestCase):
    """Tests for 'blackjack.py'."""
    
    def test_bust(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            blackjack.bust("player")
            self.assertEqual(fake_out.getvalue(), "\nBust!\nplayer loses.\n\n")
        
    def test_hit(self):
        hand = ['2','3']
        newhand = blackjack.hit(hand)
        self.assertEqual(len(newhand), 3)

    def test_getHand(self):
        hand = ['6']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 6)

    def test_getHand1(self):
        hand = ['2','3']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 5)

    def test_getHand2(self):
        hand = ['T','J']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 20)

    def test_getHand3(self):
        hand = ['A','A']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 12)

    def test_getHand4(self):
        hand = ['9','A']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 20)

    def test_getHand5(self):
        hand = ['K','A']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 21)

    def test_getHand6(self):
        hand = ['K','J','A']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 21)

    def test_getHand7(self):
        hand = ['Q','7', 'A']
        val = blackjack.getHand(hand)
        self.assertEqual(val, 18)

    def test_resultBlackJack(self):
        blackj = True
        player = 21
        dealer = 20
        bustP = False
        bustD = False
        playerMoney = 1000
        gameNum = 0
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nBlackJack!\n\n" + name + " wins!\n\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")

    def test_resultBlackJackTie(self):
        blackj = True
        player = 21
        dealer = 21
        bustP = False
        bustD = False
        playerMoney = 100
        gameNum = 1
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nTie!\n\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")

    def test_resultTie(self):
        blackj = False
        player = 19
        dealer = 19
        bustP = False
        bustD = False
        playerMoney = 100
        gameNum = 1
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nTie!\n\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")

    def test_resultWin(self):
        blackj = False
        player = 21
        dealer = 19
        bustP = False
        bustD = False
        playerMoney = 100
        gameNum = 1
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nPlayer wins!\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")

    def test_resultWin2(self):
        blackj = False
        player = 20
        dealer = 18
        bustP = False
        bustD = False
        playerMoney = 100
        gameNum = 1
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nPlayer wins!\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")

    def test_bustTrue(self):
        blackj = False
        player = 20
        dealer = 21
        bustP = False
        bustD = True
        playerMoney = 100
        gameNum = 1
        bet = "10"
        name = "Player"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            (money, game) = blackjack.results(blackj, player, dealer, bustP, bustD, playerMoney, gameNum, bet, name)
            self.assertEqual(fake_out.getvalue(), "\nPlayer wins!\nNumber of games won by "
                             + name + ": " + str(game)+ "\nYou have $" + str(money) +".00 remaining.\n")



if __name__ == '__main__':
    unittest.main()