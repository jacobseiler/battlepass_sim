from typing import Dict, List, Union, Optional
from datetime import datetime
from collections import defaultdict

import numpy as np

from battlepass import BattlePass
from cavern import Cavern
from persona import Persona
from wagering import Wagering
from guild import Guild

class Player:

    def __init__(self, persona: Optional[str] = None) -> None:

        self._persona_type = persona
        self.persona = Persona(persona)

        self.battlepass = BattlePass(self.persona.details["starting_level"])
        self.cavern = Cavern()
        self.guild = Guild()
        self.wagering = Wagering(self.battlepass)

        self._date_started = None

        self._games: Dict[datetime, List[bool]] = defaultdict(list)

    def __repr__(self) -> str:

        return f"Player has persona {self._persona_type} with level {self.battlepass.level}"

    def play_games_for_day(self, date: datetime) -> str:

        # Reset counters for day.
        # For example, reset number of contracts completed.

        # Check to see if we are in a new week.  If so, then reset counters for the week (wagering + labyrinth).

        games_played_func = self.persona.details["games_per_day"]["distribution"]
        games_played_params = self.persona.details["games_per_day"]["params"]

        number_games_played = games_played_func(*games_played_params)

        for game_num in range(int(number_games_played)):
            self._play_game(date, self.persona.details["win_rate"])

    def _play_game(self, date: datetime, win_rate_details: Dict[str, Union[str, List[float]]]) -> None:

        win_probability_func = win_rate_details["distribution"]
        win_probability_params = win_rate_details["params"]

        probability_win = win_probability_func(*win_probability_params)

        if probability_win > np.random.uniform():
            win = True
        else:
            win = False

        self._games[date].append(win)

        if win:
            self._process_win()

    def _process_win(self) -> None:

        points_earned = self.cavern._process_win(self.persona.details["cavern_compliance"])
        self.battlepass._process_rewards(points_earned)
