"""
model_validation.py

Validates the Digital Twin against the
Honeywell calibration dataset.
"""

import os
import csv

from config import SimulationConfig
from simulator.simulator import OilWellSimulator


class ModelValidator:

    def __init__(self):

        self.simulator = OilWellSimulator(
            SimulationConfig.default()
        )

    def validate(self):

        dataset = self.simulator.dataset.data

        results = []

        for row in dataset:

            choke = row["choke"]

            expected_flow = row["flow"]

            state = self.simulator.reset()

            state = self.simulator.step(choke)

            predicted_flow = state.flow

            error = predicted_flow - expected_flow

            percent_error = abs(error) / expected_flow * 100

            results.append({
                "choke": choke,
                "expected": expected_flow,
                "predicted": predicted_flow,
                "error": error,
                "percent": percent_error,
            })

        return results

    def export_csv(self, results):

        os.makedirs(
            "results/validation",
            exist_ok=True,
        )

        path = "results/validation/validation.csv"

        with open(path, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Choke",
                "Dataset Flow",
                "Predicted Flow",
                "Error",
                "Percent Error",
            ])

            for r in results:

                writer.writerow([
                    r["choke"],
                    round(r["expected"], 3),
                    round(r["predicted"], 3),
                    round(r["error"], 3),
                    round(r["percent"], 3),
                ])

        return path