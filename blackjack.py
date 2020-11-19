# class Card トランプ(suit=柄,number=数字)
# class Deck デッキ(deal=カードを配る,shuffle)
# class Hand 手札
# class Game ゲーム


class Card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} {self.number}'


trump = Card('♥', 10)
print(trump)


class Deck():
    suits = ['♠', '♥', '♣', '♦']
    number = [1, 2, 3]
