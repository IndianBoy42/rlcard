from copy import deepcopy

import numpy as np

from rlcard.games.dungeonmayhem import Barbarian, Paladin, Rogue, Wizard
from rlcard.games.dungeonmayhem.card import DungeonMayhemCard
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter


class DungeonMayhemGame:
    def __init__(self, allow_step_back=False):
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        self.players: list[DungeonMayhemCharacter] = []
        self.history: list[dict] = []
        self.current_player_idx: int = 0

    def configure(self, game_config):
        """Specifiy some game specific parameters, such as number of players"""

    def init_game(self):
        """Initialize the game"""
        self.wizard = Wizard(self.np_random)
        self.barbarian = Barbarian(self.np_random)
        self.paladin = Paladin(self.np_random)
        self.rogue = Rogue(self.np_random)
        self.players = [self.wizard, self.barbarian, self.paladin, self.rogue]

    def play_card(self, char: DungeonMayhemCharacter, card: DungeonMayhemCard):
        target = max(self.players, key=lambda x: self.target_heuristic(char, x))
        char.actions -= 1
        char.immune += card.immune
        char.actions += card.actions
        char.heal(card.health)
        for _ in range(card.draw):
            char.draw()
        if card.damage:
            target.take_damage(card.damage)
        if card.damage_everyone:
            for player in self.players:
                player.take_damage(card.damage_everyone)
        if card.power:
            card.power(self, char, target)
        if card.shield:
            char.shields += [(0, card)]
        else:
            char.discardpile.append(card)

    def target_heuristic(
        self, char: DungeonMayhemCharacter, target: DungeonMayhemCharacter
    ):
        """
        Heuristic for choosing a target.
        """
        return target.total_health()  # Maximum health player
        # return -target.total_health())  # Minimum health player

    def current_player(self):
        """Return the current player"""
        return self.players[self.current_player_idx]

    def save_state(self, append_history=True):
        """
        Save the state of the game to an object
        """
        state = {}
        state["wizard"] = deepcopy(self.wizard)
        state["barbarian"] = deepcopy(self.barbarian)
        state["paladin"] = deepcopy(self.paladin)
        state["rogue"] = deepcopy(self.rogue)
        state["current_player"] = self.current_player_idx
        if append_history:
            self.history.append(state)
        return state

    def step(self, action):
        """
        Take an action in the game

        Args:
        - action (dict): the action taken by the player
            - card (int): the index of the card to play in the player's hand
        """
        if self.allow_step_back:
            self.save_state(append_history=True)

        char = self.current_player()

        if char.actions <= 0:
            char.start_turn()

        card = char.hand[action["card"]]
        char.hand.remove(card)
        self.play_card(char, card)

        if char.actions > 0:  # Continue turn next
            return (char, self.current_player_idx)
        elif char.actions == 0:  # End of turn
            self.current_player_idx = (
                self.current_player_idx + 1
            ) % self.get_num_players()
            char = self.current_player()
            return (char, self.current_player_idx)

    def step_back(self):
        """Return to the previous state of the game

        Returns:
            Status (bool): check if the step back is success or not
        """
        if len(self.history) > 0:
            state = self.history.pop()
            (self.wizard, self.barbarian, self.paladin, self.rogue) = (
                state["wizard"],
                state["barbarian"],
                state["paladin"],
                state["rogue"],
            )
            self.players = [self.wizard, self.barbarian, self.paladin, self.rogue]
            return True
        return False

    def get_num_players(self):
        """Return the number of players"""
        return len(self.players)
