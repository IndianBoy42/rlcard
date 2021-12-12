from rlcard.games.dungeonmayhem.card import (BarbarianDiscardHand,
                                             BarbarianHeal, DestroyShield)
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


def _new_deck(add):
    """Generate a new deck for the game"""
    add(damage=2)  #  BrutalPunch(),
    add(damage=2)  #  BrutalPunch(),
    add(actions=2)  #  TwoAxes(),
    add(actions=2)  #  TwoAxes(),
    add(damage=1, actions=1)  #  HeadButt(),
    add(damage=1, actions=1)  #  HeadButt(),
    add(damage=3)  #  BigAxe(),
    add(damage=3)  #  BigAxe(),
    add(damage=3)  #  BigAxe(),
    add(damage=3)  #  BigAxe(),
    add(damage=3)  #  BigAxe(),
    add(damage=4)  #  Rage(),
    add(damage=4)  #  Rage(),
    add(shield=3)  #  Raff(),
    add(shield=3)  #  Raff(),
    add(shield=2)  #  SpikedShield(),
    add(shield=1, draw=1)  #  BagOfRats(),
    add(draw=2, health=1)  #  SnackTime(),
    add(draw=2)  #  OpenTheArmory(),
    add(draw=2)  #  OpenTheArmory(),
    add(draw=1, health=1)  #  Flex(),
    add(draw=1, health=1)  #  Flex(),
    add(actions=1, power=BarbarianDiscardHand)  #  BattleRoar(),
    add(actions=1, power=BarbarianDiscardHand)  #  BattleRoar(),
    add(draw=1, power=DestroyShield)  #  MightyToss(),
    add(draw=1, power=DestroyShield)  #  MightyToss(),
    add(power=BarbarianHeal)  #  WhirlingAxes(),
    add(power=BarbarianHeal)  #  WhirlingAxes(),


class DungeonMayhemBarbarian(DungeonMayhemCharacter):
    """docstring for DungeonMayhemBarbarian."""

    def __init__(self, np_random):
        super(DungeonMayhemBarbarian, self).__init__(np_random, DungeonMayhemBarbarian)

    base_deck = DungeonMayhemCharacter.new_deck(_new_deck)
    idx_to_card = base_deck[1]
    total_number_of_cards = base_deck[2]
