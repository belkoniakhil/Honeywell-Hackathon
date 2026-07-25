"""
controller.py

High-level autonomous choke controller.

Responsibilities
----------------
1. Receive the current well state.
2. Ask the optimizer for the best choke position.
3. Return the selected choke.
"""

from controller.predictor import Predictor
from controller.optimizer import Optimizer


class AutonomousController:

    def __init__(self, simulator):

        self.predictor = Predictor(
            simulator.flow_model,
            simulator.pressure_model,
        )

        self.optimizer = Optimizer(
            self.predictor,
        )

    def decide(self, state, target_flow):
        """
        Compute the next choke position.
        """

        return self.optimizer.optimize(
            state,
            target_flow,
        )