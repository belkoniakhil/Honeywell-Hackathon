"""
step_response.py

Open-loop step response experiment.

No controller is used.
The choke is manually changed from
30% to 60%.
"""

from config import SimulationConfig
from simulator.simulator import OilWellSimulator


class StepResponseScenario:

    def run(self):

        simulator = OilWellSimulator(
            SimulationConfig.default()
        )

        state = simulator.reset()

        print("\n" + "=" * 70)
        print("Open Loop Step Response")
        print("=" * 70)

        for _ in range(20):

            state = simulator.step(30)

            print(
                f"t={state.time:4.0f}s | "
                f"Flow={state.flow:7.2f} | "
                f"Choke={state.choke:5.1f}"
            )

        print("\n----- STEP CHANGE -----\n")

        for _ in range(40):

            state = simulator.step(60)

            print(
                f"t={state.time:4.0f}s | "
                f"Flow={state.flow:7.2f} | "
                f"Choke={state.choke:5.1f}"
            )

        return simulator