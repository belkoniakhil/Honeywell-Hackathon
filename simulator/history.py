"""
history.py

Stores every simulator state.

This allows us to:

- Plot graphs
- Export CSV
- Compare controllers
- Calculate metrics
- Replay simulations
"""

from simulator.state import WellState


class SimulationHistory:

    def __init__(self):

        self.states = []

    # -----------------------------------------------------

    def add(self, state: WellState):
        """
        Store a copy of the current state.
        """

        self.states.append(state)

    # -----------------------------------------------------

    def clear(self):
        """
        Remove all recorded states.
        """

        self.states.clear()

    # -----------------------------------------------------

    def last(self):

        if not self.states:
            return None

        return self.states[-1]

    # -----------------------------------------------------

    def __len__(self):

        return len(self.states)

    # -----------------------------------------------------

    def get_times(self):

        return [state.time for state in self.states]

    def get_flows(self):

        return [state.flow for state in self.states]

    def get_whp(self):

        return [state.whp for state in self.states]

    def get_flp(self):

        return [state.flp for state in self.states]

    def get_bhp(self):

        return [state.bhp for state in self.states]

    def get_chokes(self):

        return [state.choke for state in self.states]