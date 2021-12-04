from collections import Counter, OrderedDict
from itertools import count

import numpy as np

from rlcard.envs import Env
from rlcard.games.dungeonmayhem import (DungeonMayhemClasses,
                                        DungeonMayhemIDBarbarian,
                                        DungeonMayhemIDPaladin,
                                        DungeonMayhemIDRogue,
                                        DungeonMayhemIDWizard, Game)
from rlcard.games.dungeonmayhem.char import DungeonMayhemCharacter
from rlcard.games.dungeonmayhem.game import DungeonMayhemGame

counter = count()
state_health_idx = next(counter)
state_immune_idx = next(counter)
state_actions_idx = next(counter)
NUM_PLAYERS = DungeonMayhemGame.NUM_PLAYERS
state_other_health_idx = [next(counter) for _ in range(NUM_PLAYERS - 1)]
state_other_immune_idx = [next(counter) for _ in range(NUM_PLAYERS - 1)]
state_other_immune_idx = [next(counter) for _ in range(NUM_PLAYERS - 1)]
state_other_class_idx = [next(counter) for _ in range(NUM_PLAYERS - 1)]
state_total_indices = next(counter)

counter = count()
state_in_hand_idx = next(counter)
state_in_discard_idx = next(counter)
state_in_deck_idx = next(counter)
state_in_shields_idx = next(counter)


class DungeonMayhemEnv(Env):
    """
    The environment for Dungeom Mayhem
    """

    def __init__(self, config):
        self.name = "dungeonmayhem"
        self.game = Game()
        super(DungeonMayhemEnv, self).__init__(config)
        self.state_shape = [
            (state_total_indices + char_class.total_number_of_cards,)
            for char_class in DungeonMayhemClasses
        ]
        action_shape = [None for _ in DungeonMayhemClasses]

    def _extract_state(self, state):
        """Encode state
        Args:
            state (dict): dict of original state
        """
        extracted_state = {}
        """
            extracted_state is a Python dictionary. It consists of 
            observation state['obs'], 
            legal actions state['legal_actions'], 
            raw observation state['raw_obs'],
            raw legal actions state['raw_legal_actions'].
            each of these are np arrays
        """
        obs = np.zeros(self.state_shape[state_health_idx], dtype=int)
        obs[state_health_idx] = state["health"]
        obs[state_immune_idx] = state["immune"]
        obs[state_actions_idx] = state["actions"]
        for card in state["hand"]:
            obs[card.id] = state_in_hand_idx
        for card in state["discard"]:
            obs[card.id] = state_in_discard_idx
        # for card in state["deck"]:
        #     obs[card.id] = state_in_deck_idx
        for card in state["shields"]:
            obs[card.id] = state_in_shields_idx
        for j in range(DungeonMayhemGame.NUM_PLAYERS - 1):
            i = state["other_classes"][j]
            obs[state_other_health_idx[i]] = state["other_health"][i]
            obs[state_other_immune_idx[i]] = state["other_immune"][i]
            obs[state_other_class_idx[i]] = state["other_class"][i]
            # TODO: encode other players discard pile and shields

        ## TODO: shouldn't this be extracted from state parameter not from self.game? idk
        extracted_state["legal_actions"] = self._get_legal_actions()

        extracted_state["raw_obs"] = state
        extracted_state["raw_legal_actions"] = [a for a in state["legal_actions"]]
        extracted_state["action_record"] = self.action_recorder

    def _decode_action(self, action_id):
        """Action id -> the action in the game. Must be implemented in the child class.
        Args:
            action_id (int): the id of the action
        Returns:
            action (string): the action that will be passed to the game engine.
        """
        return action_id

    def get_payoffs(self):
        """Get the payoffs of players. Must be implemented in the child class.
        Returns:
            payoffs (list): a list of payoffs for each player
        """
        # If there is a winner he gets +1, everyone else gets -1
        winner = self.game.winner()
        return [1 if winner == player else -1 for player in self.game.players]

    def _get_legal_actions(self):
        """Get all legal actions for current state
        Returns:
            legal_actions (list): a list of legal actions' id
        """
        # Get the IDs of the cards in the current player's hand
        char = self.game.current_player()
        return [card.id for card in char.hand]

    # def get_perfect_information(self):
    #     """Get the perfect information of the current state
    #     Returns:
    #         (dict): A dictionary of all the perfect information of the current state
    #     """
