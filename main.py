"""
Honeywell Autonomous Production Optimizer

Entry point of the application.
"""

from evaluation.metrics import ControllerMetrics
from evaluation.report import ReportGenerator
from visualization.plots import PlotGenerator
from utils.csv_export import CSVExporter


def main():

    print("\nChoose Scenario")
    print("-" * 30)
    print("1. Startup")
    print("2. Target Tracking")
    print("3. Impossible Target")

    choice = input("\nEnter Choice : ")

    # ---------------------------------------------------------
    # Run Selected Scenario
    # ---------------------------------------------------------

    if choice == "1":

        from scenarios.startup import StartupScenario

        simulator = StartupScenario().run()

        target = 140
        output_folder = "results/startup"

    elif choice == "2":

        from scenarios.target_tracking import TargetTrackingScenario

        simulator = TargetTrackingScenario().run()

        target = 150          # Final target for reporting
        output_folder = "results/target_tracking"

    elif choice == "3":

        from scenarios.impossible_target import ImpossibleTargetScenario

        simulator = ImpossibleTargetScenario().run()

        target = 180
        output_folder = "results/impossible_target"

    else:

        print("Invalid Choice")
        return

    # ---------------------------------------------------------
    # Evaluation
    # ---------------------------------------------------------

    history = simulator.get_history()

    metrics = ControllerMetrics(history)

    # ---------------------------------------------------------
    # Export Results
    # ---------------------------------------------------------

    csv_path = CSVExporter().export(
        history,
        output_folder,
    )

    report_path = ReportGenerator().generate(
        metrics,
        target,
        output_folder,
    )

    PlotGenerator().generate(
        history,
        target,
        output_folder,
    )

    # ---------------------------------------------------------
    # Console Summary
    # ---------------------------------------------------------

    print("\n" + "=" * 70)
    print("Controller Performance")
    print("=" * 70)

    print(f"RMSE                : {metrics.rmse(target):.3f}")
    print(f"Maximum Error       : {metrics.max_error(target):.3f}")
    print(f"Steady State Error  : {metrics.steady_state_error(target):.3f}")
    print(f"Overshoot           : {metrics.overshoot(target):.3f}")

    print("\nGenerated Files")
    print("-" * 70)
    print(f"CSV Report   : {csv_path}")
    print(f"Text Report  : {report_path}")
    print(f"Plots        : {output_folder}")

    print("=" * 70)


if __name__ == "__main__":
    main()