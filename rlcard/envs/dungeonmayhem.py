from collections import Counter, OrderedDict

import numpy as np

from rlcard.envs import Env
from rlcard.games.dungeonmayhem import (DungeonMayhemIDBarbarian,
                                        DungeonMayhemIDPaladin,
                                        DungeonMayhemIDRogue,
                                        DungeonMayhemIDWizard, Game)


class DungeonMayhemEnv(Env):
    """
    The environment for Dungeom Mayhem
    """

    def __init__(self, config):
        self.name = "dungeonmayhem"
        self.game = Game()
        super(DungeonMayhemEnv, self).__init__(config)

    def _extract_state(self, state):
        """Encode state
        Args:
            state (dict): dict of original state
        """
        if state["self"] == DungeonMayhemIDWizard:
            pass
        elif state["self"] == DungeonMayhemIDPaladin:
            pass
        elif state["self"] == DungeonMayhemIDRogue:
            pass
        elif state["self"] == DungeonMayhemIDBarbarian:
            pass

        """
            State is a Python dictionary. It consists of 
            observation state['obs'], 
            legal actions state['legal_actions'], 
            raw observation state['raw_obs'],
            raw legal actions state['raw_legal_actions'].
        """

    def get_payoffs(self):
        """Get the payoffs of players. Must be implemented in the child class.
        Returns:
            payoffs (list): a list of payoffs for each player
        """

    def _decode_action(self, action_id):
        """Action id -> the action in the game. Must be implemented in the child class.
        Args:
            action_id (int): the id of the action
        Returns:
            action (string): the action that will be passed to the game engine.
        """

    def _get_legal_actions(self):
        """Get all legal actions for current state
        Returns:
            legal_actions (list): a list of legal actions' id
        """

    # def get_perfect_information(self):
    #     """Get the perfect information of the current state
    #     Returns:
    #         (dict): A dictionary of all the perfect information of the current state
    #     """

    def get_action_feature(self, action):
        """For some environments such as DouDizhu, we can have action features
        Returns:
            (numpy.array): The action features
        """
