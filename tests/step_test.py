"""
Runs the open-loop step response test.
"""

from scenarios.step_response import StepResponseScenario

from evaluation.metrics import ControllerMetrics
from evaluation.report import ReportGenerator

from visualization.plots import PlotGenerator
from utils.csv_export import CSVExporter


simulator = StepResponseScenario().run()

history = simulator.get_history()

metrics = ControllerMetrics(history)

CSVExporter().export(
    history,
    "results/step_response",
)

ReportGenerator().generate(
    metrics,
    60,
    "results/step_response",
)

PlotGenerator().generate(
    history,
    60,
    "results/step_response",
)

print("\nStep response completed.")