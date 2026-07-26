"""
plots.py

Generates professional plots for the Honeywell
Autonomous Production Optimizer.
"""

import os
import matplotlib.pyplot as plt


class PlotGenerator:

    def generate(
        self,
        history,
        target_flow,
        output_folder="results",
    ):

        os.makedirs(output_folder, exist_ok=True)

        times = history.get_times()
        flows = history.get_flows()
        chokes = history.get_chokes()
        whp = history.get_whp()
        flp = history.get_flp()
        bhp = history.get_bhp()

        # ===================================================
        # Flow Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(times, flows, linewidth=2, label="Flow")

        plt.axhline(
            target_flow,
            color="red",
            linestyle="--",
            label="Target"
        )

        plt.title("Flow vs Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Flow (bbl/hr)")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "flow_vs_time.png",
            ),
            dpi=300
        )

        plt.close()

        # ===================================================
        # Choke Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(
            times,
            chokes,
            linewidth=2,
        )

        plt.title("Choke Position")
        plt.xlabel("Time (s)")
        plt.ylabel("Choke (%)")
        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "choke_vs_time.png",
            ),
            dpi=300
        )

        plt.close()

        # ===================================================
        # Pressure Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(times, whp, label="WHP")
        plt.plot(times, flp, label="FLP")
        plt.plot(times, bhp, label="BHP")

        plt.title("Pressure Trends")
        plt.xlabel("Time (s)")
        plt.ylabel("Pressure")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "pressure_vs_time.png",
            ),
            dpi=300
        )

        plt.close()
                # ===================================================
        # WHP Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(times, whp, linewidth=2)

        plt.title("Wellhead Pressure (WHP)")
        plt.xlabel("Time (s)")
        plt.ylabel("Pressure")
        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "whp_vs_time.png",
            ),
            dpi=300,
        )

        plt.close()

        # ===================================================
        # FLP Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(times, flp, linewidth=2)

        plt.title("Flowline Pressure (FLP)")
        plt.xlabel("Time (s)")
        plt.ylabel("Pressure")
        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "flp_vs_time.png",
            ),
            dpi=300,
        )

        

        # ===================================================
        # BHP Plot
        # ===================================================

        plt.figure(figsize=(10, 5))

        plt.plot(times, bhp, linewidth=2)

        plt.title("Bottom Hole Pressure (BHP)")
        plt.xlabel("Time (s)")
        plt.ylabel("Pressure")
        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                "bhp_vs_time.png",
            ),
            dpi=300,
        )

        plt.close()

        return output_folder