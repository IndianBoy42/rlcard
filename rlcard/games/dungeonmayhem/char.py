from rlcard.games.dungeonmayhem.card import DungeonMayhemCard as Card


class DungeonMayhemCharacter:
    def __init__(self, np_random):
        self.np_random = np_random
        self.hand: list[Card] = []
        self.discardpile: list[Card] = []
        self.deck: list[Card] = []
        self.health = 10
        self.shields: list[tuple[int, Card]] = []
        self.immune = 0
        self.actions = 0

    def start_turn(self):
        self.actions = 1
        self.immune = 0
        self.draw()

    def total_health(self):
        return self.health + sum([shield[0] for shield in self.shields])

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
        while True:
            if self.shields[0][0] == 0:
                self.shields.pop(0)
                self.discardpile.append(self.shields[0][1])
            else:
                break

        self.health -= amt
        if self.health <= 0:
            self.health = 0
            return True
        return False
