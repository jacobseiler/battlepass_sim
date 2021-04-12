class Guild:

    def __init__(self, level: int = 1) -> None:

        self._level = 1
        self._rewards_map = {}

        self._update_for_level()
