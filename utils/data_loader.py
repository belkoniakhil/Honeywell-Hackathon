"""
data_loader.py

Loads and calibrates the Honeywell dataset.

This module is the ONLY module that reads the CSV.
"""

import csv
from bisect import bisect_left


class DatasetLoader:

    def __init__(self, csv_path):

        self.rows = []

        with open(csv_path, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                self.rows.append(row)

        self.flow_lookup = self._build_lookup(
            "Choke_pct",
            "OilRate_bbl_hr"
        )

        self.whp_lookup = self._build_lookup(
            "Choke_pct",
            "WHP_psi"
        )

        self.flp_lookup = self._build_lookup(
            "Choke_pct",
            "FLP_psi"
        )

        self.bhp_lookup = self._build_lookup(
            "Choke_pct",
            "BHP_psi"
        )

    # ----------------------------------------------------

    def _build_lookup(self, x_column, y_column):

        groups = {}

        for row in self.rows:

            x = float(row[x_column])
            y = float(row[y_column])

            groups.setdefault(x, []).append(y)

        table = []

        for x in sorted(groups):

            avg = sum(groups[x]) / len(groups[x])

            table.append((x, avg))

        return table

    # ----------------------------------------------------

    def interpolate(self, table, x):

        xs = [p[0] for p in table]
        ys = [p[1] for p in table]

        if x <= xs[0]:
            return ys[0]

        if x >= xs[-1]:
            return ys[-1]

        idx = bisect_left(xs, x)

        x1, y1 = xs[idx - 1], ys[idx - 1]
        x2, y2 = xs[idx], ys[idx]

        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

    # ----------------------------------------------------

    def flow(self, choke):

        return self.interpolate(self.flow_lookup, choke)

    def whp(self, choke):

        return self.interpolate(self.whp_lookup, choke)

    def flp(self, choke):

        return self.interpolate(self.flp_lookup, choke)

    def bhp(self, choke):

        return self.interpolate(self.bhp_lookup, choke)