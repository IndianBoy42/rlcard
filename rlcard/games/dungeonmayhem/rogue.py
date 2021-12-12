from rlcard.games.dungeonmayhem.card import DestroyShield, RogueStealDiscard
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


def _new_deck(add):
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
    add(actions=1, power=DestroyShield)  # SneakAttack(),
    add(actions=1, power=DestroyShield)  # SneakAttack(),
    add(power=RogueStealDiscard)  # PickPocket(),
    add(power=RogueStealDiscard)  # PickPocket()


class DungeonMayhemRogue(DungeonMayhemCharacter):
    """docstring for DungeonMayhemRogue."""

    def __init__(self, np_random):
        super(DungeonMayhemRogue, self).__init__(np_random, DungeonMayhemRogue)

    base_deck = DungeonMayhemCharacter.new_deck(_new_deck)
    idx_to_card = base_deck[1]
    total_number_of_cards = base_deck[2]
