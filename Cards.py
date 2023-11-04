import random

class Card: 

    def __init__(self,value,suit):
        '''
        paramter with two instance variables value and suit 
        ----------------------------------------------------
            self.value = user input value 
            self.suit = user input suit
        '''
        self.value = value
        self.suit = suit

    def __repr__(self):
        '''
        parameter
        ---------
            return string in formate Card(value, suit)
        '''
        return f'Card({self.value} of {self.suit})'
    
    def __lt__(self,other):
        '''
        parameter
        ---------
            if two created objects are not cards 
                raise ValueError 
            elif two cards don't have the same suit 
                return a boolean: the former card has a smaller suit than the latter card
                
            else (two cards have the same suit)
                return a boolean: the former card has a smaller card value than the latter card value      
        '''
        if not isinstance(self,Card) and not isinstance(other,Card):
            raise ValueError("This is an invalid Card!")
        elif self.suit != other.suit: 
            return self.suit < other.suit 
        else:
            return self.value < other.value

class Deck:

    def __init__(self,value = range(1,14), suits = ['clubs', 'diamonds', 'hearts', 'spades']):
        '''
        parameter(self,range(1-4),suits[])
        ----------------------------------
        sorted the value of the card object 
        sorted the suits of the card object
        empty card_list 
        outer for loop for each value
            inner for loop for each suit 
                append card object(value,suit) to the card_list 
        '''
        self.value = sorted(value)
        self.suits = sorted(suits)
        self.card_list = []
        for v in self.value: #for each value 
            for s in self.suits: #for each suit
                self.card_list.append(Card(v,s)) #add cards of each combination provided the values and suits

    def __len__(self):
        '''
        parameter
        ---------
            return the length of the card_list
        '''
        return len(self.card_list)
    
    def sort(self):
        '''
        parameter
        ---------
            sort the card objects in card_list
        '''
        self.card_list.sort()
    
    def shuffle(self):
        '''
        parameter
        ---------
            shuffle card objects in card_list 
        '''
        random.shuffle(self.card_list)

    def __repr__(self):
        '''
        parameter
        ---------
            return a string of a deck of card objects  
        '''
        return f'Deck: {self.card_list}' 
    
    def draw_top(self):
        '''
        parameter
        ---------
            if card_list is empty 
                raise Runtime Error 
            else 
                remove the last card object(top) in the card_list 
                return the last card in deck  
        '''
        if len(self.card_list) == 0: 
            raise RuntimeError("Cannot draw from empty deck")
        else: 
            top = self.card_list[-1] #last card in card_list
            self.card_list.remove(top)
            return top
 
class Hand(Deck):
    
    def __init__(self,card_list):
        '''
        parameter(self,card_list)
        -------------------------
            inherit the card_list from Deck class
        '''
        self.card_list = card_list
    
    def __repr__(self):
        '''
        parameter
        ---------
            return a string for a hand of cards
        '''
        return f'Hand: {self.card_list}'

    def play(self,card):
        '''
        parameter
        ---------
            get wanted card value
            get wanted card suit 

            boolean variable: as if the card on the hand is not found 
            i = 0 start to look for the first card in hand

            for each card in hand 
                if the wanted card's value and suit maches a card's value and suit in hand 
                    set found to be True
                    return and remove tha wated card 
                
                i = 1 + i on to search for the next card in hand 
            
            if the card is not found 
                raise a RunTime error --> the wanted card is not in hand

                    
        '''
        input_card_value = card.value
        input_card_suit = card.suit

        found = False #set to default if the wanted card is not found in Hand
        i = 0 #index of each card in card_list, starts @ 0

        for c in self.card_list:
            if input_card_value == c.value and input_card_suit == c.suit:
                found = True #found the wanted card in Hand
                return self.card_list.pop(i)
            
            i = 1 + i #incremnet the card index by 1 
        
        if found == False: #if the wanted hard is not in Hand
            raise RuntimeError(f'Attempt to play {card} that is not in Hand: {self.card_list}')
