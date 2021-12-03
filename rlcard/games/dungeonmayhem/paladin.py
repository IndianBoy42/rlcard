from rlcard.games.dungeonmayhem.card import (DungeonMayhemCard,
                                             PaladinDestroyShields,
                                             PaladinGetDiscard)
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


class DungeonMayhemPaladin(DungeonMayhemCharacter):
    """docstring for DungeonMayhemPaladin."""

    def __init__(self, np_random):
        super(DungeonMayhemPaladin, self).__init__(np_random)

    def new_deck(self):
        """Generate a new deck for the game"""
        counter = 0

        def add(*args, **kwargs):
            nonlocal counter
            self.deck.append(DungeonMayhemCard(id=counter, *args, **kwargs))
            counter += 1

        add(damage=3)  # ForTheMostJustice(),
        add(damage=3)  # ForTheMostJustice(),
        add(damage=2)  ## ForEvenMoreJustice(),
        add(damage=2)  ## ForEvenMoreJustice(),
        add(damage=2)  ## ForEvenMoreJustice(),
        add(damage=2)  ## ForEvenMoreJustice(),
        add(damage=1, actions=1)  ## ForJustice(),
        add(damage=1, actions=1)  ## ForJustice(),
        add(damage=1, actions=1)  ## ForJustice(),
        add(actions=2)  # FingerwagOfJudgment(),
        add(actions=2)  # FingerwagOfJudgment(),
        add(damage=3, health=1)  # DivineSmite(),
        add(damage=3, health=1)  # DivineSmite(),
        add(damage=3, health=1)  # DivineSmite(),
        add(damage=2, health=1)  # FightingWords(),
        add(damage=2, health=1)  # FightingWords(),
        add(damage=2, health=1)  # FightingWords(),
        add(actions=2)  # HighCharisma(),
        add(actions=2)  # HighCharisma(),
        add(draw=2, health=1)  # CureWounds(),
        add(shield=1, draw=1)  # SpinningParry(),
        add(shield=1, draw=1)  # SpinningParry(),
        add(shield=3)  # DivineShield(),
        add(shield=3)  # DivineShield(),
        add(shield=2)  # Fluffly(),
        add(actions=1, power=PaladinDestroyShields)  # BanishingSmite(),
        add(heal=2, power=PaladinGetDiscard)  # DivineInspiration(),
        add(heal=2, power=PaladinGetDiscard)  # DivineInspiration(),
