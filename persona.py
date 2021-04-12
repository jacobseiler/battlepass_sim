from typing import Optional

import numpy as np

# Cavern compliance should be a decaying distribution for casuals or agnostic grinders.  That is, as they complete
# cavern rooms, the probability they complete a room decreases.

settings_dict = {
    "agnostic_grinder": {
        "games_per_day": {
            "distribution": np.random.normal,
            "params": [5, 2],
            "frequency_roll": "daily",
        },
        "win_rate": {
            "distribution": np.random.normal,
            "params": [0.53, 0.02],
            "frequency_roll": "per_game",
        },
        "cavern_compliance": {
            "distribution": np.random.binomial,
            "params": [1, 0.5],
            "frequency_roll": "per_game",
        },
        "contract_compliance": {
            "distribution": np.random.binomial,
            "params": [1, 0.5],
            "frequency_roll": "per_game",
        },
        "wagering_strategy": {
            "strategy": "all",
        },
        "tip_trading_strategy": {
            "strategy": None,
        },
        "starting_level": 150,
    },
}

class Persona:

    def __init__(self, persona_type: Optional[str] = None) -> None:

        self._possible_personas = [
            "agnostic_grinder",
            "targeted_grinder",
            "agnostic_intermediate",
            "targeted_intermediate",
            "agnostic_casual",
            "targeted_casual",
        ]

        # FIXME: This should be handled by a setter.
        if persona_type not in self._possible_personas:
            raise ValueError(
                f"Persona {persona_type} not allowed. Possible personas are {self._possible_personas}."
            )

        self.details = settings_dict[persona_type]
