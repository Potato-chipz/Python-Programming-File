from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase):
    def setUp(self):
        '''
            create 4 card objects for testing
        '''
        self.c1 = Card(2,'hearts')
        self.c2 = Card(6,'spades')
        self.c3 = Card(3,'hearts')
        self.c4 = Card(3,'chocolate') #for testing a ValueError in Card class
        self.c5 = Card(23,'peach') #for testing a ValueError in Card class 

    def test_init(self):
        '''
        assert c1 card has a value of 2
        assert c1 card has a suit of hearts 
        '''
        self.assertEqual(self.c1.value,2) #evaluated to True
        self.assertEqual(self.c1.suit,'hearts') #evaluated to True

    def test_repr(self):
        '''
        a = string representaion of c1
        b = repr function output in class Card
        assert if a equal b 
        '''
        a = 'Card(2 of hearts)'
        b = f'Card({self.c1.value} of {self.c1.suit})'
        self.assertEqual(b,a) #evaluated to True

    def test_lt(self):
        '''
        if two created objects c4,c5 are not cards 
                raise ValueError 
            elif two created cards c1 and c3 don't have the same suit 
                return a boolean: c1 has a smaller suit than c2
                
            else (two created cards c1 and c2 have the same suit)
                return a boolean: the c1 card has a smaller card value than the c3 card value 
        '''
        if not isinstance(self.c4,Card) and not isinstance(self.c5,Card):
            raise ValueError("This is an invalid Card")
        elif (self.c1.suit != self.c2.suit):
            assert(self.c1.suit < self.c2.suit) #evaluated to True
        else:
            assert(self.c1.value < self.c3.value) #evaluated to True


class TestDeck(unittest.TestCase):
    def setUp(self): 
        '''
        instance variable: ideal_deck = default deck that has 52 cards of all values(1-13) and all 4 suits
        instance variable: test_deck = A manually made deck for later testing
        instance variable: empty_deck = empty deck
        '''
        self.ideal_deck = Deck()
        self.test_deck = Deck([3,4],["diamonds","hearts"])
        self.empty_deck = Deck([],[])
    
    def test_init(self):
        '''
        assert test_deck has 2 values [3,4]
        assert test_deck has 2 suits["diamonds","hearts"]
        '''
        self.assertEqual(self.test_deck.value,[3,4]) #evaluated to True
        self.assertEqual(self.test_deck.suits,["diamonds","hearts"]) #evaluated to True
    
    def test_len(self):
        '''
        assert ideal_deck has a length of 52 cards
        '''
        self.assertEqual(len(self.ideal_deck),52) #evaluated to True
    
    def test_sort(self):
        '''
        sort the test_deck
        assert the sorted test_deck will have values and suits in order
        '''
        self.test_deck.sort()
        self.assertEqual(str(self.test_deck),'Deck: [Card(3 of diamonds), Card(4 of diamonds), Card(3 of hearts), Card(4 of hearts)]') #evaluated to True
    
    def test_shuffle(self):
        '''
        shuffle the test_deck
        assert the shuffled test_deck will have a different order compared to the orginal,sorted test_deck
        '''
        self.test_deck.shuffle()
        self.assertNotEqual(str(self.test_deck),'Deck: [Card(3 of diamonds), Card(3 of hearts), Card(4 of diamonds), Card(4 of hearts)]') #evaluated to True

    def test_repr(self):
        '''
        assert the repr function in class Deck returns a correct string representation of the cards in test_deck
        '''
        self.assertEqual(repr(self.test_deck),'Deck: [Card(3 of diamonds), Card(3 of hearts), Card(4 of diamonds), Card(4 of hearts)]') #evaluated to True
    
    def test_draw_top(self):
        '''
        if it's an empty deck
            raise a RuntimeError
        else
            card_remove_exp = 'Card(4 of hearts)' --> expected card to be removed from the test_deck
            card_remove_td = card removed uisng draw_top()function in class Deck
            assert(exp == td)
        '''
        if self.assertEqual(len(self.empty_deck),0): #evaluated to True
            raise RuntimeError("Cannot draw from empty deck") 
        else:
            card_remove_exp = 'Card(4 of hearts)'
            card_remove_td = self.test_deck.draw_top()
            self.assertEqual(str(card_remove_td),card_remove_exp) #evaluated to True

class TestHand(unittest.TestCase):
    def setUp(self):
        '''
        test_d: Set up a hand of cards for later testing
        '''
        self.test_d = Hand([Card(value,'spades') for value in range(1,3,1)])
    
    def test_repr(self):
        '''
        assert the repr funtion in class Hand returns a correct string representation of each card in test_d Hand 
        '''
        self.assertEqual(repr(self.test_d),'Hand: [Card(1 of spades), Card(2 of spades)]') #evaluated to True
    
    def test_play_card(self):
        '''
        assert play function in class Hand returns Card(1,'spades') when find in test_d 
        assert play function in class Hand returns Card(2,'spades') when find in test_d 
        '''
        self.assertEqual(str(self.test_d.play(Card(1,'spades'))),'Card(1 of spades)')#evaluated to True
        self.assertEqual(str(self.test_d.play(Card(2,'spades'))),'Card(2 of spades)')#evaluated to True

unittest.main() # Runs all tests above