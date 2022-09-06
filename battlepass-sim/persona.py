from typing import Optional

import numpy as np

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
        """
        if persona_type not in self._possible_personas:
            raise ValueError(
                f"Persona {persona_type} not allowed. Possible personas are {self._possible_personas}."
            )

        self.details = settings_dict[persona_type]
        """
