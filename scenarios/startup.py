"""
startup.py

Startup scenario.
"""

from config import SimulationConfig
from simulator.simulator import OilWellSimulator
from controller.controller import AutonomousController


class StartupScenario:

    def run(self):

        simulator = OilWellSimulator(
            SimulationConfig.default()
        )

        controller = AutonomousController(simulator)
        simulator.controller = controller
        state = simulator.reset()

        target = 140

        print("\n" + "=" * 70)
        print("Scenario : Startup")
        print("=" * 70)

        for _ in range(60):
            choke = controller.decide(
            state,
            target,
            )

            state = simulator.step(choke)        

            print(
                f"t={state.time:4.0f}s | "
                f"Flow={state.flow:7.2f} | "
                f"Target={target:7.2f} | "
                f"Choke={state.choke:5.1f}"
            )

        return simulator