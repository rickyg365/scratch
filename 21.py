import os
import random


"""
.----.
| cc |
|    |
'____'
"""


# values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#
# suites = {
#     "Spade": u'\u2660',
#     "Club": u'\u2663',
#     "Heart": u'\u2665',
#     "Diamond": u'\u2666'
# }


# for i in range(7):
#     """
#     Was stuck on this for a while.
#
#     Note that encoding works from Unicode to bytes,
#     and decoding works from bytes to Unicode. - wovano
#
#     Resource: https: //stackoverflow.com/questions/60692756/python3-convert-unicode-literals-string-to-unicode-string
#     """
#     base_uni = fr'\u266{i}'
#
#     print((base_uni.encode('utf-8').decode('unicode-escape')))

# for name, symbol in suites.items():
#     print(f"{name}:\t{symbol}")
#
# deck = [(s, v) for s in suites for v in values]
#
# new_deck = {}
#
# for raw_card in deck:
#     suite = raw_card[0]
#     val = raw_card[1]
#
#     new_deck[f"{suite}_{val}"] = val
#     new_card = Card(suite, val)
#
# print(new_deck)


class Card:
    def __init__(self, card_suite, card_value, card_symbol=""):
        self.suite = card_suite
        self.value = card_value

        self.symbol = card_symbol

    def __str__(self):
        # text = f"\n.--."
        # text += f"\n|{self.symbol}{self.value}|"
        # text += f"\n'__'"
        text = f"|{self.symbol}{self.value}|"
        return text

    def add_symbol(self, new_symbol):
        self.symbol = new_symbol


class Deck:
    """
    The default draw card is random but I can use a queue to drop the top card in the deck
    """
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    SUITES = {
        "Spade": u'\u2660',
        "Club": u'\u2663',
        "Heart": u'\u2665',
        "Diamond": u'\u2666'
    }

    def __init__(self):
        """
        self.deck for quick reference
        self.cards for display and symbols hehe
        """
        self.deck = []
        self.cards = []

        self.current_deck = []
        self.removed_deck = []

        deck_list = [(s, v) for s in self.SUITES for v in self.VALUES]

        for raw_card in deck_list:
            suite = raw_card[0]
            val = raw_card[1]

            # Method 1
            self.deck.append(f"{suite}_{val}")
            # Method 2
            sym = self.SUITES[suite]
            self.add_card(suite, val, sym)

        self.current_deck = list(self.deck)
        self.size_of_current = len(self.current_deck)

    def __str__(self):
        text = ""
        for card in self.cards:
            text += f"\n{card}"
        return text

    def __len__(self):
        return len(self.current_deck)

    def add_card(self, card_suite, card_value, card_symbol=""):
        new_obj = Card(card_suite, card_value, card_symbol)

        self.cards.append(new_obj)

    def use_card(self, card_info):
        # card_info = suite_value
        # print(card_info)
        self.current_deck.remove(card_info)
        self.removed_deck.append(card_info)

    def reset_deck(self):
        self.current_deck = list(self.deck)
        self.removed_deck = []

    def draw_card(self):
        self.size_of_current = len(self.current_deck)
        if self.size_of_current < 1:
            print("Out of Cards: RESET")
            return None
        r = random.randint(0, self.size_of_current - 1)

        chosen_card = self.current_deck[r]
        # print(chosen_card)
        self.use_card(chosen_card)

        return self.cards[r]


class Blackjack:
    def __init__(self, player_name="Player"):
        self.player_name = player_name
        self.score = 0
        self.dealer_score = 0

        self.deck = Deck()

        self.player_hand = []
        self.dealer_hand = []

    def __str__(self):
        text = f"{self.player_name}[{self.score}]:\n{self.player_hand}"
        return text

    @staticmethod
    def add_score(card_value):
        # self.score +=
        if card_value in 'jJqQkK':
            return 10

        elif card_value in 'aA':
            return 1

        else:
            return int(card_value)

    @staticmethod
    def is_full(list_obj):
        current_amount = len(list_obj)
        if current_amount >= 5:
            print("Hand is full!")
            return False
        return True

    def check_deck(self):
        if len(self.deck) < 1:
            return False
        return True

    def card_to_hand(self, dealer=False):
        deck_status = self.check_deck()
        if not deck_status:
            return False

        if dealer:
            hand_status = self.is_full(self.dealer_hand)

            if hand_status:
                dealers_card = self.deck.draw_card()

                self.dealer_hand.append(dealers_card)
                self.dealer_score += self.add_score(dealers_card.value)
                return True

            return False

        hand_status = self.is_full(self.player_hand)

        if hand_status:
            players_card = self.deck.draw_card()

            self.player_hand.append(players_card)
            self.score += self.add_score(players_card.value)
            return True

        return False

    def play_round(self):

        # Check if players hand is full
        dealer_status = self.card_to_hand(True)

        player_status = self.card_to_hand()

        if (dealer_status is False) and (player_status is False):
            return False

        # self.dealer_hand.append(dealers_card)
        # self.player_hand.append(players_card)

        text = f"Dealer[{self.dealer_score}]: "
        for card in self.dealer_hand:
            text += f"{card} "
        text += f"\n{self.player_name}[{self.score}]: "
        for c in self.player_hand:
            text += f"{c} "
        # print(*self.player_hand)
        print(text)
        return True

    def play(self):
        game_status = True
        while game_status:
            game_status = self.play_round()
            input("Hit?(y/n): ")


if __name__ == "__main__":
    new_deck = Deck()

    # while new_deck.current_deck:
    #     new_card = new_deck.draw_card()
    #     print(new_card)
    #     # print(new_deck.removed_deck)
    #
    # print(new_deck.current_deck)
    # new_deck.reset_deck()
    # print(new_deck.current_deck)

    # print(new_deck)
    # card1 = new_deck.draw_card()
    # card2 = new_deck.draw_card()
    # card3 = new_deck.draw_card()
    #
    # print(card1)
    # print(card2)
    # print(card3)

    new_game = Blackjack()
    new_game.play()
