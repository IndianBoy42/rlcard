from rlcard.games.dungeonmayhem.card import (DungeonMayhemCard,
                                             DestroyShield,
                                             RogueStealDiscard)
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


class DungeonMayhemRogue(DungeonMayhemCharacter):
    """docstring for DungeonMayhemRogue."""

    def __init__(self, np_random):
        super(DungeonMayhemRogue, self).__init__(np_random)

    def new_deck(self):
        """Generate a new deck for the game"""
        counter = 0

        def add(*args, **kwargs):
            nonlocal counter
            self.deck.append(DungeonMayhemCard(id=counter, *args, **kwargs))
            counter += 1

        add(damage=3)  # AllTheThrownDaggers(),
        add(damage=3)  # AllTheThrownDaggers(),
        add(damage=3)  # AllTheThrownDaggers(),
        add(damage=2)  # TwoThrownDaggers(),
        add(damage=2)  # TwoThrownDaggers(),
        add(damage=2)  # TwoThrownDaggers(),
        add(damage=2)  # TwoThrownDaggers(),
        add(damage=1, actions=1)  # OneThrownDagger(),
        add(damage=1, actions=1)  # OneThrownDagger(),
        add(damage=1, actions=1)  # OneThrownDagger(),
        add(damage=1, actions=1)  # OneThrownDagger(),
        add(damage=1, actions=1)  # OneThrownDagger(),
        add(actions=2)  # CunningAction(),
        add(actions=2)  # CunningAction(),
        add(actions=1, health=1)  # StolenPotion(),
        add(actions=1, health=1)  # StolenPotion(),
        add(draw=2, health=1)  # EvenMoreDaggers(),
        add(draw=1, shield=1)  # WingedSerpent(),
        add(draw=1, shield=1)  # WingedSerpent(),
        add(shield=2)  # TheGoonSquad(),
        add(shield=2)  # TheGoonSquad(),
        add(shield=3)  # MyLittleFriend(),
        add(immune=1)  # CleverDisguise(),
        add(immune=1)  # CleverDisguise(),
        add(action=1, power=DestroyShield)  # SneakAttack(),
        add(action=1, power=DestroyShield)  # SneakAttack(),
        add(power=RogueStealDiscard)  # PickPocket(),
        add(power=RogueStealDiscard)  # PickPocket(),
