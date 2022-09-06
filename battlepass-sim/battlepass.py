class BattlePass:

    def __init__(self, level: int = 0) -> None:

        self.points = 0
        self.level = level

        # TODO: Put in mapping between levels and rewards.
        self.rewards_map = {
            0: {"wagering_tokens": 1000, "portals": 10},
            10: {"treasure_i": 1},
        }

    def _process_rewards(self, points: int) -> None:

        self.points += points

        levels_gained = divmod(self.points, 100)[0]

        if levels_gained > 1:
            self._process_level_up(levels_gained)

        self.points = divmod(self.points, 100)[1]

    def _process_level_up(self, levels_gained: int) -> None:

        self.level += levels_gained
