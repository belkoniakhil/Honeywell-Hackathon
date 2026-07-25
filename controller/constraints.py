"""
constraints.py

Safety monitoring for the Digital Twin.
"""


class ConstraintMonitor:

    def __init__(self):

        self.min_whp = 220
        self.max_whp = 280

        self.min_flp = 155
        self.max_flp = 195

        self.min_bhp = 2850
        self.max_bhp = 3150

    def check(self, state):

        warnings = []

        if state.whp < self.min_whp:
            warnings.append("Low WHP")

        if state.whp > self.max_whp:
            warnings.append("High WHP")

        if state.flp < self.min_flp:
            warnings.append("Low FLP")

        if state.flp > self.max_flp:
            warnings.append("High FLP")

        if state.bhp < self.min_bhp:
            warnings.append("Low BHP")

        if state.bhp > self.max_bhp:
            warnings.append("High BHP")

        return warnings