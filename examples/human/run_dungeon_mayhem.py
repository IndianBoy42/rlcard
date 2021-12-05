from typing import Any

import rlcard
from rlcard.agents.dungeonmayhem_random_agent import RandomAgent
from rlcard.agents.human_agents.dungeonmayhem_human_agent import (
    HumanAgent, _print_action)
from rlcard.utils import set_seed, tournament

env = rlcard.make("dungeon-mayhem", config={"allow_step_back": False})
human_agent: Any = HumanAgent(env.num_actions)
opponents = [RandomAgent(env.num_actions) for _ in range(3)]
env.set_agents([human_agent] + opponents)

print(">> Dungeon Mayhem : Player vs Random Agents")

while True:
    set_seed(0)

    print("Start a new game")

    trajectories, payoffs = env.run(is_training=False)
    # If the human does not take the final action, we need to
    # print other players action
    final_state = trajectories[0][-1]
    action_record = final_state["action_record"]
    state = final_state["raw_obs"]
    _action_list = []
    for i in range(1, len(action_record) + 1):
        if action_record[-i][0] == state["current_player"]:
            break
        _action_list.insert(0, action_record[-i])
    for pair in _action_list:
        print(">> Player", pair[0], "chooses ", end="")
        _print_action(pair[1])
        print("")

    print("===============     Result     ===============")
    if payoffs[0] > 0:
        print("You win!")
    else:
        print("You lose!")
    print("")
    input("Press any key to continue...")
