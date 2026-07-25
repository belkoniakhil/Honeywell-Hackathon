"""
predictor.py

Predict future well response for a candidate choke.
"""

from simulator.state import WellState


class Predictor:

    def __init__(self, flow_model, pressure_model):

        self.flow_model = flow_model
        self.pressure_model = pressure_model

    def predict(self, state: WellState, choke: float):

        predicted_flow = self.flow_model.next_flow(
            state,
            choke,
        )

        predicted_whp, predicted_flp, predicted_bhp = (
            self.pressure_model.next_pressures(
                state,
                choke,
            )
        )

        return {
            "flow": predicted_flow,
            "whp": predicted_whp,
            "flp": predicted_flp,
            "bhp": predicted_bhp,
        }