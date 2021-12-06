from rlcard.games.dungeonmayhem.card import DungeonMayhemCard as Card


class DungeonMayhemCharacter:
    ID = -1

    def __init__(self, np_random):
        self.np_random = np_random
        self.hand: list[Card] = []
        self.discardpile: list[Card] = []
        self.deck: list[Card] = []
        self.health = 10
        self.shields: list[tuple[int, Card]] = []
        self.immune = 0
        self.actions = 1
        self.idx_to_card: dict[int, Card] = {}
        self.card_to_idx: dict[Card, int] = {}

    def _new_deck(self, add):
        raise NotImplementedError

    @staticmethod
    def new_deck(_new_deck):
        deck = []
        counter = 0

        def add(*args, **kwargs):
            nonlocal counter
            deck.append(Card(id=counter, *args, **kwargs))
            counter += 1

        _new_deck(add)

        card_to_idx = {card: i for i, card in enumerate(deck)}
        idx_to_card = {i: card for i, card in enumerate(deck)}
        total_number_of_cards = counter

        return (deck, card_to_idx, idx_to_card, total_number_of_cards)

    def start_turn(self):
        self.actions = 1
        self.immune = 0
        self.draw()

    def total_health(self):
        return self.health + self.total_shields()

    def total_shields(self):
        return sum(shield[0] for shield in self.shields)

    def draw_n(self, n):
        for _ in range(n):
            self.draw()

    def draw(self):
        if len(self.deck) == 0:
            self.deck = self.discardpile
            self.discardpile = []
            self.np_random.shuffle(self.deck)
        card = self.deck.pop()
        self.hand.append(card)
        return card

    def destroy_shield(self, index=0):
        (_, card) = self.shields.pop(index)
        self.discardpile.append(card)

    def heal(self, amt):
        self.health += amt
        if self.health > 10:
            self.health = 10

    def discard_hand(self):
        for card in self.hand:
            self.discardpile.append(card)
            self.hand.remove(card)

    def take_damage(self, amt):
        for (i, (remaining, card)) in enumerate(self.shields):
            left = remaining - amt
            if left > 0:
                self.shields[i] = (left, card)
                return
            else:
                amt -= remaining
                self.shields[i] = (0, card)

        destroyed = [shield for shield in self.shields if shield[0] == 0]
        self.discardpile.extend(shield[1] for shield in destroyed)
        self.shields = [shield for shield in self.shields if shield[0] > 0]

        self.health -= amt
        if self.health <= 0:
            self.health = 0
            return True
        return False
