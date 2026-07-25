"""
csv_export.py

Exports simulation history to CSV.
"""

import csv
import os


class CSVExporter:

    def export(
        self,
        history,
        output_folder="results",
    ):

        os.makedirs(output_folder, exist_ok=True)

        path = os.path.join(
            output_folder,
            "simulation.csv",
        )

        with open(path, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Time",
                "Flow",
                "WHP",
                "FLP",
                "BHP",
                "Choke",
            ])

            for state in history.states:

                writer.writerow([
                    state.time,
                    state.flow,
                    state.whp,
                    state.flp,
                    state.bhp,
                    state.choke,
                ])

        return path