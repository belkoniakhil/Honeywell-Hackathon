"""
report.py

Creates a text report describing controller performance.
"""

import os


class ReportGenerator:

    def generate(
        self,
        metrics,
        target,
        output_folder="results",
    ):

        os.makedirs(output_folder, exist_ok=True)

        path = os.path.join(
            output_folder,
            "controller_report.txt",
        )

        with open(path, "w") as file:

            file.write("Honeywell Autonomous Production Optimizer\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Target Flow : {target:.2f} bbl/hr\n\n")

            file.write(
                f"RMSE                : {metrics.rmse(target):.3f}\n"
            )

            file.write(
                f"Maximum Error       : {metrics.max_error(target):.3f}\n"
            )

            file.write(
                f"Steady State Error  : {metrics.steady_state_error(target):.3f}\n"
            )

            file.write(
                f"Overshoot           : {metrics.overshoot(target):.3f}\n"
            )

        return path