
# Cavern compliance should be a decaying distribution for casuals or agnostic grinders.  That is, as they complete
# cavern rooms, the probability they complete a room decreases.
personas = {
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
