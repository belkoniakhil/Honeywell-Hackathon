"""
optimizer.py

Optimizer for autonomous choke control.

Strategy
--------
1. Evaluate feasible choke positions.
2. Predict future well state.
3. Reject unsafe operating points.
4. Compute multi-objective cost.
5. Select the safest candidate with minimum cost.

Objectives
----------
- Track target production
- Maintain safe operating pressures
- Reduce unnecessary choke movement

This is a simplified MPC-style optimizer using
one-step prediction.
"""

from controller.predictor import Predictor


class Optimizer:

    def __init__(self, predictor: Predictor):

        self.predictor = predictor

        # -------------------------------------------------
        # Cost Weights
        # -------------------------------------------------

        self.w_tracking = 1.0
        self.w_pressure = 0.05
        self.w_movement = 0.10

        # -------------------------------------------------
        # Safety Limits
        # -------------------------------------------------

        self.MIN_WHP = 200
        self.MAX_WHP = 300

        self.MIN_FLP = 150
        self.MAX_FLP = 200

        self.MIN_BHP = 2800
        self.MAX_BHP = 3200

        # Warning thresholds
        self.WHP_WARNING_LOW = 220
        self.WHP_WARNING_HIGH = 280

        self.FLP_WARNING_LOW = 160
        self.FLP_WARNING_HIGH = 195

        self.BHP_WARNING_LOW = 2850
        self.BHP_WARNING_HIGH = 3180

        # Stores last optimization result
        self.last_decision = None
        # Stores every evaluated candidate
        self.search_history = []

    def optimize(self, state, target_flow):

        current_choke = state.choke
        # Clear previous optimization history
        self.search_history.clear()
        self.last_candidates = []
        best_cost = float("inf")
        best_choke = current_choke
        best_decision = None

        # ---------------------------------------------
        # Local search around current operating point
        # ---------------------------------------------

        start = max(0, int(current_choke - 20))
        end = min(100, int(current_choke + 20))

        candidate_found = False

        for choke in range(start, end + 1, 5):

            prediction = self.predictor.predict(
                state,
                choke,
            )

            # -----------------------------------------
            # Hard Safety Constraints
            # -----------------------------------------

            if (
                prediction["whp"] < self.MIN_WHP
                or prediction["whp"] > self.MAX_WHP
                or prediction["flp"] < self.MIN_FLP
                or prediction["flp"] > self.MAX_FLP
                or prediction["bhp"] < self.MIN_BHP
                or prediction["bhp"] > self.MAX_BHP
            ):
                self.search_history.append({
                    "choke": choke,
                    "predicted_flow": prediction["flow"],
                    "tracking_cost": None,
                    "pressure_cost": None,
                    "movement_cost": None,
                    "total_cost": None,
                    "safe": False,
                    "selected": False,
                })

                continue
               

            candidate_found = True

            predicted_flow = prediction["flow"]

            tracking_cost = abs(
                target_flow - predicted_flow
            )
       

            # -----------------------------------------
            # Soft Pressure Penalty
            # -----------------------------------------

            pressure_cost = 0.0

            whp = prediction["whp"]
            flp = prediction["flp"]
            bhp = prediction["bhp"]

            if whp < self.WHP_WARNING_LOW:
                pressure_cost += self.WHP_WARNING_LOW - whp

            elif whp > self.WHP_WARNING_HIGH:
                pressure_cost += whp - self.WHP_WARNING_HIGH

            if flp < self.FLP_WARNING_LOW:
                pressure_cost += self.FLP_WARNING_LOW - flp

            elif flp > self.FLP_WARNING_HIGH:
                pressure_cost += flp - self.FLP_WARNING_HIGH

            if bhp < self.BHP_WARNING_LOW:
                pressure_cost += self.BHP_WARNING_LOW - bhp

            elif bhp > self.BHP_WARNING_HIGH:
                pressure_cost += bhp - self.BHP_WARNING_HIGH

            # -----------------------------------------
            # Choke Movement Cost
            # -----------------------------------------

            movement_cost = abs(
                choke - current_choke
            )

            # -----------------------------------------
            # Total Cost
            # -----------------------------------------

            total_cost = (
                self.w_tracking * tracking_cost
                + self.w_pressure * pressure_cost
                + self.w_movement * movement_cost
            )
            self.search_history.append({
                "choke": choke,
                "predicted_flow": predicted_flow,
                "tracking_cost": tracking_cost,
                "pressure_cost": pressure_cost,
                "movement_cost": movement_cost,
                "total_cost": total_cost,
                "safe": True,
                "selected": False,
            })
            self.last_candidates.append(
                        {
                            "choke": choke,
                            "predicted_flow": predicted_flow,
                            "predicted_whp": whp,
                            "tracking_cost": tracking_cost,
                            "pressure_cost": pressure_cost,
                            "movement_cost": movement_cost,
                            "total_cost": total_cost,
                        }
                    )          

            if total_cost < best_cost:

                best_cost = total_cost
                best_choke = choke

                best_decision = {
                    "target_flow": target_flow,
                    "chosen_choke": choke,
                    "predicted_flow": predicted_flow,
                    "predicted_whp": whp,
                    "predicted_flp": flp,
                    "predicted_bhp": bhp,
                    "tracking_cost": tracking_cost,
                    "pressure_cost": pressure_cost,
                    "movement_cost": movement_cost,
                    "total_cost": total_cost,
                }

        # ---------------------------------------------
        # Fallback
        # ---------------------------------------------

        if not candidate_found:

            best_choke = current_choke

            best_decision = {
                "target_flow": target_flow,
                "chosen_choke": current_choke,
                "predicted_flow": state.flow,
                "predicted_whp": state.whp,
                "predicted_flp": state.flp,
                "predicted_bhp": state.bhp,
                "tracking_cost": abs(target_flow - state.flow),
                "pressure_cost": float("inf"),
                "movement_cost": 0,
                "total_cost": float("inf"),
                "warning": "No safe operating point found.",
            }
        for candidate in self.search_history:

            if candidate["choke"] == best_choke:

                candidate["selected"] = True   
        self.last_decision = best_decision

        return best_choke