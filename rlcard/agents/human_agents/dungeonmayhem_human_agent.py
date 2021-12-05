class HumanAgent(object):
    """A human agent for the dungeonmayhem"""

    def __init__(self, num_actions):
        self.use_raw = True
        self.num_actions = num_actions

    @staticmethod
    def step(state):
        """Human agent will display the state and make decisions through interfaces

        Args:
            state (dict): A dictionary that represents the current state

        Returns:
            action (int): The action decided by human
        """
        _print_state(state["raw_obs"], state["action_record"], state["legal_actions"])
        action = int(input(">> You choose action (integer): "))
        while action < 0 or action >= len(state["legal_actions"]):
            print("Action illegal...")
            action = int(input(">> Re-choose action (integer): "))
        return state["raw_legal_actions"][action]

    def eval_step(self, state):
        """Predict the action given the curent state for evaluation. The same to step here.

        Args:
            state (numpy.array): an numpy array that represents the current state

        Returns:
            action (int): the action predicted (randomly chosen) by the random agent
        """
        return self.step(state), {}


def _print_state(raw_obs, action_record, legal_actions):
    """Print out the state of a given player"""
    char = raw_obs
    print("raw_obs")
    __import__("pprint").pprint(raw_obs)

    print("legal_actions")
    __import__("pprint").pprint([card for card in char["hand"]])


def _print_action(action):
    """Print out an action in a nice form

    Args:
        action (str): A string a action
    """
