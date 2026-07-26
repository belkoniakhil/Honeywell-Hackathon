"""
target_tracking.py

Changing production targets.
"""

from config import SimulationConfig
from simulator.simulator import OilWellSimulator
from controller.controller import AutonomousController


class TargetTrackingScenario:

    def run(self):

        simulator = OilWellSimulator(
            SimulationConfig.default()
        )

        controller = AutonomousController(simulator)
        simulator.controller = controller
        state = simulator.reset()

        targets = [
            (140, 20),
            (120, 20),
            (150, 20),
        ]

        print("\n" + "=" * 70)
        print("Scenario : Dynamic Target Tracking")
        print("=" * 70)

        for target, steps in targets:

            print(f"\nNew Target Flow = {target}\n")

            for _ in range(steps):

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