from dataclasses import dataclass
from typing import Any, Callable, Optional

# from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter
# from rlcard.games.dungeonmayhem.game import DungeonMayhemGame
# from rlcard.games.dungeonmayhem.paladin import DungeonMayhemPaladin
# from rlcard.games.dungeonmayhem.rogue import DungeonMayhemRogue


@dataclass(frozen=True)
class DungeonMayhemCard:
    """
    The class for a card.
    """

    id: int
    immune: int = 0
    shield: int = 0
    damage: int = 0
    health: int = 0
    actions: int = 0
    draw: int = 0
    damage_everyone: int = 0
    power: Optional[Callable[[Any, Any, Any], None]] = None


# RogueImmune -- card.immune

# RogeuDestroyShield
# BarbarianDestroyShield
# DestroyShield
def DestroyShield(game: Any, player: Any, target: Any):
    # Destroy the shield with most remaining value
    index = max(range(0, len(target.shields)), key=lambda i: target.shields[i][0])
    target.destroy_shield(index)


# PaladinDestroyShields
def PaladinDestroyShields(game: Any, player: Any, target: Any):
    for p in game.players:
        for _ in range(len(p.shields)):
            p.destroy_shield()


# RogueStealDiscard
def RogueStealDiscard(game: Any, player: Any, target: Any):
    card = target.discardpile.pop()
    game.play_card(rogue, card)


# PaladinGetDiscard
def PaladinGetDiscard(game: Any, player: Any, target: Any):
    # TODO: heuristic or card value table?
    pass


# BarbarianDiscardHand
def BarbarianDiscardHand(game: Any, player: Any, target: Any):
    for p in game.players:
        p.discard_hand()
        for _ in range(3):
            p.draw()


# BarbarianHeal
def BarbarianHeal(game: Any, barbarian: Any, target: Any):
    barbarian.heal(3)
    for p in game.players:
        if p != barbarian:
            p.take_damage(1)


# WizardFireball -- card.damage_everyone

# WizardStealShield
def WizardStealShield(
    game: Any,
    wizard: Any,
    target: Any,
):
    shield = target.shields.pop()
    wizard.shields.append(shield)


# WizardSwapHP
def WizardSwapHP(
    game: Any,
    wizard: Any,
    target: Any,
):
    wizard.health, target.health = target.health, wizard.health


MightPowers = {
    "PaladinDestroyShields": PaladinDestroyShields,
    "RogueStealDiscard": RogueStealDiscard,
    "BarbarianDiscardHand": BarbarianDiscardHand,
    "BarbarianHeal": BarbarianHeal,
    "WizardStealShield": WizardStealShield,
    "WizardSwapHP": WizardSwapHP,
}
