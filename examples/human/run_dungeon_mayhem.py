import cProfile
import os
import pstats
from typing import Any

import rlcard
from rlcard.agents.dungeonmayhem_random_agent import RandomAgent
from rlcard.agents.human_agents.dungeonmayhem_human_agent import (
    HumanAgent, _print_action)
# from rlcard.agents.random_agent import RandomAgent
from rlcard.utils import set_seed, tournament

env = rlcard.make("dungeon-mayhem", config={"allow_step_back": False})

if False:
    human_agent: Any = HumanAgent(env.num_actions)
    opponents = [RandomAgent(env.num_actions) for _ in range(3)]
    env.set_agents([human_agent] + opponents)
else:
    opponents = [RandomAgent(env.num_actions) for _ in range(4)]
    env.set_agents(opponents)

print(">> Dungeon Mayhem : Player vs Random Agents")


def run_game():
    return env.run(is_training=False)


# cProfile.run("env.run(is_training=False)", "dm.stats")
# os.system("python -m flameprof dm.stats -o dm.svg")
# # Use python -m flameprof something.stats -o something.svg
# # Open svg in chrome and view
# os.system("google-chrome dm.svg")

print(tournament(env, 1000))

raise ValueError("")


while True:
    set_seed(0)

    print("Start a new game")

    trajectories, payoffs = run_game()
    # If the human does not take the final action, we need to
    # print other players action
    final_state = trajectories[0][-1]
    action_record = final_state["action_record"]
    state = final_state["raw_obs"]
    _action_list = []
    for i in range(1, len(action_record) + 1):
        if action_record[-i][0] == state["current_player_idx"]:
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
