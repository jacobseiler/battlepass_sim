from battlepass import BattlePass

class Wagering:

    def __init__(self, battlepass: BattlePass) -> None:

        # Dependant on BP level
        number_tokens = 0
        for reward_level, reward in battlepass.rewards_map.items():

            if battlepass.level < reward_level:
                break
            try:
                number_tokens += reward["wagering_tokens"]
            except KeyError:
                pass

        self._maximum_tokens = number_tokens
        self._number_tokens = number_tokens
