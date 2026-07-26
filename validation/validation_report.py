"""
validation_report.py

Creates a validation report for the Digital Twin.
"""

import math
import os


class ValidationReport:

    def generate(self, results):

        os.makedirs(
            "results/validation",
            exist_ok=True,
        )

        rmse = math.sqrt(
            sum(r["error"] ** 2 for r in results)
            / len(results)
        )

        mae = (
            sum(abs(r["error"]) for r in results)
            / len(results)
        )

        max_error = max(
            abs(r["error"])
            for r in results
        )

        avg_percent = (
            sum(r["percent"] for r in results)
            / len(results)
        )

        path = "results/validation/report.txt"

        with open(path, "w") as file:

            file.write("Digital Twin Validation Report\n")
            file.write("=" * 40 + "\n\n")

            file.write(f"RMSE               : {rmse:.3f}\n")
            file.write(f"Mean Absolute Error: {mae:.3f}\n")
            file.write(f"Maximum Error      : {max_error:.3f}\n")
            file.write(f"Average % Error    : {avg_percent:.3f}\n")

        return path