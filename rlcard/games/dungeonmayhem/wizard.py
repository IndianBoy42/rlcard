from rlcard.games.dungeonmayhem.card import (DungeonMayhemCard,
                                             WizardStealShield, WizardSwapHP)
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


class DungeonMayhemWizard(DungeonMayhemCharacter):
    """docstring for DungeonMayhemWizard."""

    def __init__(self, np_random):
        super(DungeonMayhemWizard, self).__init__(np_random)

    def new_deck(self):
        """Generate a new deck for the game"""
        counter = 0

        def add(*args, **kwargs):
            nonlocal counter
            self.deck.append(DungeonMayhemCard(id=counter, *args, **kwargs))
            counter += 1

        add(damage=3)  # LightningBolt(),
        add(damage=3)  # LightningBolt(),
        add(damage=3)  # LightningBolt(),
        add(damage=3)  # LightningBolt(),
        add(damage=2)  # BurningHands(),
        add(damage=2)  # BurningHands(),
        add(damage=2)  # BurningHands(),
        add(damage=1, actions=1)  # MagicMissile(),
        add(damage=1, actions=1)  # MagicMissile(),
        add(damage=1, actions=1)  # MagicMissile(),
        add(actions=2)  # SpeedOfThought(),
        add(actions=2)  # SpeedOfThought(),
        add(actions=2)  # SpeedOfThought(),
        add(health=1, actions=1)  # EvilSneer(),
        add(health=1, actions=1)  # EvilSneer(),
        add(draw=3)  # KnowledgeIsPower(),
        add(draw=3)  # KnowledgeIsPower(),
        add(draw=3)  # KnowledgeIsPower(),
        add(shield=1, draw=1)  # Shield(),
        add(shield=1, draw=1)  # Shield(),
        add(shield=2)  # Stoneskin(),
        add(shield=3)  # MirrorImage(),
        add(damage_everyone=3)  # Fireball(),
        add(damage_everyone=3)  # Fireball(),
        add(power=WizardStealShield)  # Charm(),
        add(power=WizardStealShield)  # Charm(),
        add(power=WizardSwapHP)  # VampiricTouch(),
        add(power=WizardSwapHP)  # VampiricTouch(),
