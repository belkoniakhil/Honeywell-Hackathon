"""
metrics.py

Controller performance evaluation.
"""

from simulator.history import SimulationHistory


class ControllerMetrics:

    def __init__(self, history: SimulationHistory):

        self.history = history

    def rmse(self, target):

        flows = self.history.get_flows()

        error = 0

        for flow in flows:

            error += (flow - target) ** 2

        return (error / len(flows)) ** 0.5

    def max_error(self, target):

        return max(
            abs(flow - target)
            for flow in self.history.get_flows()
        )

    def steady_state_error(self, target):

        return abs(
            self.history.get_flows()[-1]
            - target
        )

    def overshoot(self, target):

        return max(
            self.history.get_flows()
        ) - target