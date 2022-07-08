
from classes.deck import Deck
from classes.player import Player
from classes.card import Card

# bicycle = Deck()
# bicycle.show_cards()

class War:
    def __init__(self, player1, player2, score=0):
        self.player1 = player1
        self.player2 = player2
        self.score = score

    def deal_cards(self):
        deck = Deck()
        deck.shuffle()
        for i in range(0, len(deck.cards), 1):
            if i % 2 == 0:
                self.player1.cards.append(deck.cards[i])
            else:
                self.player2.cards.append(deck.cards[i])
        # print("*" * 100)
        # print(self.player2.cards)

    def play_round(self):
        for i in range(0, 1):
            self.player1.score += self.player1.cards[i].point_val
            self.player1.cards[i].append
            print(self.player1.score)            
            self.player2.score += self.player2.cards[i].point_val

            print(self.player2.score)
            # print(self.player1.cards[i].card_info())
            # print(self.player1.cards[i].point_val + self.player2.cards[i].point_val)

    def play_game(self):
        for i in range(0, len(self.player1.cards, +2))

p1 = Player()
p2 = Player()
game1 = War(p1, p2)
game1.deal_cards()
game1.play_round()



