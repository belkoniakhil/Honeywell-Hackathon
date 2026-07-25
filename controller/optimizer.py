"""
optimizer.py

Optimizer for autonomous choke control.

Strategy
--------
1. Evaluate every feasible choke position (0-100%).
2. Predict the resulting flow.
3. Compute a weighted cost.
4. Select the choke with the minimum cost.

This is a simplified Model Predictive Control (MPC)-style optimizer.
"""

from controller.predictor import Predictor


class Optimizer:

    def __init__(self, predictor: Predictor):

        self.predictor = predictor

        # Cost Weights
        self.w_tracking = 1.0
        self.w_pressure = 0.05
        self.w_movement = 0.10

    def optimize(self, state, target_flow):

        current_choke = state.choke

        best_cost = float("inf")
        best_choke = current_choke

        # IMPORTANT:
        # Search the full choke range.
        # This prevents the optimizer from getting trapped
        # in a local minimum.
        for choke in range(0, 101, 5):

            prediction = self.predictor.predict(
                state,
                choke,
            )

            predicted_flow = prediction["flow"]

            tracking_error = abs(
                target_flow - predicted_flow
            )

            predicted_whp = prediction["whp"]

            pressure_penalty = 0.0

            # Soft safety penalties
            if predicted_whp < 220:
                pressure_penalty += (220 - predicted_whp)

            elif predicted_whp > 280:
                pressure_penalty += (predicted_whp - 280)

            movement_penalty = abs(
                choke - current_choke
            )

            total_cost = (
                self.w_tracking * tracking_error
                + self.w_pressure * pressure_penalty
                + self.w_movement * movement_penalty
            )

            if total_cost < best_cost:

                best_cost = total_cost
                best_choke = choke

        return best_choke