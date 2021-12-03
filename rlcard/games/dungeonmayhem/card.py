from dataclasses import dataclass
from typing import Callable, Optional

from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter
from rlcard.games.dungeonmayhem.game import DungeonMayhemGame
from rlcard.games.dungeonmayhem.paladin import DungeonMayhemPaladin
from rlcard.games.dungeonmayhem.rogue import DungeonMayhemRogue


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
    power: Optional[
        Callable[
            [DungeonMayhemGame, DungeonMayhemCharacter, DungeonMayhemCharacter], None
        ]
    ] = None


# RogueImmune -- card.immune

# DestroyShield -- TODO: heuristic
def DestroyShield(
    game: DungeonMayhemGame, rogue: DungeonMayhemRogue, target: DungeonMayhemCharacter
):
    index = max(range(0, len(target.shields)), key=lambda i: target.shields[i][0])
    target.destroy_shield(index)


# PaladinDestroyShields
def PaladinDestroyShields(game: DungeonMayhemGame):
    for p in game.players:
        for _ in range(len(p.shields)):
            p.destroy_shield()


# RogueStealDiscard
def RogueStealDiscard(
    game: DungeonMayhemGame, rogue: DungeonMayhemRogue, target: DungeonMayhemCharacter
):
    card = target.discardpile.pop()
    game.play_card(rogue, card)


# PaladinGetDiscard
def PaladinGetDiscard(
    game: DungeonMayhemGame,
    paladin: DungeonMayhemPaladin,
    target: DungeonMayhemCharacter,
):
    # TODO: heuristic or card value table?
    pass


# BarbarianDiscardHand
def BarbarianDiscardHand(game: DungeonMayhemGame):
    for p in game.players:
        p.discard_hand()
        for _ in range(3):
            p.draw()


# BarbarianDestroyShield -- TODO: heuristic

# BarbarianHeal
def BarbarianHeal(
    game: DungeonMayhemGame,
    barbarian: DungeonMayhemCharacter,
):
    barbarian.heal(3)
    for p in game.players:
        if p != barbarian:
            p.take_damage(1)


# WizardFireball -- card.damage_everyone

# WizardStealShield
def WizardStealShield(
    game: DungeonMayhemGame,
    wizard: DungeonMayhemCharacter,
    target: DungeonMayhemCharacter,
):
    shield = target.shields.pop()
    wizard.shields.append(shield)


# WizardSwapHP
def WizardSwapHP(
    game: DungeonMayhemGame,
    wizard: DungeonMayhemCharacter,
    target: DungeonMayhemCharacter,
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
