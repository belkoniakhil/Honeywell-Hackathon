"""
controller.py

High-level autonomous choke controller.

Responsibilities
----------------
1. Receive the current well state.
2. Ask the optimizer for the best choke position.
3. Apply choke rate limiting.
4. Return the final choke position.
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

        # Maximum choke movement per controller decision
        self.MAX_CHOKE_STEP = 5

    def decide(self, state, target_flow):
        """
        Compute the next choke position while limiting
        choke movement to ±5%.
        """

        # Optimizer returns only the target choke
        target_choke = self.optimizer.optimize(
            state,
            target_flow,
        )

        current_choke = state.choke

        # Apply movement limiter
        delta = target_choke - current_choke

        if delta > self.MAX_CHOKE_STEP:
            target_choke = current_choke + self.MAX_CHOKE_STEP

        elif delta < -self.MAX_CHOKE_STEP:
            target_choke = current_choke - self.MAX_CHOKE_STEP

        return target_choke