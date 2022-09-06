from typing import Tuple, Dict

import numpy as np

class Cavern:

    def __init__(self) -> None:

        self.rooms_completed = 0
        self.consumables = {
            "arrows": 0,
            "flares": 0,
            "wands": 0,
        }

        # TODO: Account for the fact that there is two caverns.
        self.remaining_rewards = {
            "small_points": 48,
            "large_points": 9,
            "arrows": 10,
            "flares": 10,
            "wands": 10,
            "style_fragment": 9,
            "unlock_key": 3,
        }

        self._points_map = {"small_points": 250, "large_points": 2000}

    def _process_win(self, details: Dict[str, str]) -> int:
        probability_func = details["distribution"]
        probability_params = details["params"]

        probability_complete_room = probability_func(*probability_params)

        if probability_complete_room > np.random.uniform():
            # TODO: Account for double/triple rooms completed in one win.
            rooms_completed = 1

            rewards = [self._determine_reward() for _ in range(rooms_completed)]
            points_earned = sum([reward[1] for reward in rewards if reward[0] == "points"])
        else:
            points_earned = 0

        # TODO: Account for the fact that you can get arrows?

        return points_earned

    def _determine_reward(self) -> Tuple[str, int]:

        # Assume rewards are uniformly distributed across all rooms.
        remaining_rewards = sum(self.remaining_rewards.values())
        probability_rewards = {
            reward: number_remaining / remaining_rewards
            for reward, number_remaining in self.remaining_rewards.items()
        }

        reward = np.random.choice(list(probability_rewards.keys()), p=list(probability_rewards.values()))

        try:
            reward_value = self._points_map[reward]
            reward_name = "points"
        except KeyError:
            reward_value = 1
            reward_name = reward

        return reward_name, reward_value
