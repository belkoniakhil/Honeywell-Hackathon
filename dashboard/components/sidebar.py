"""
sidebar.py

Sidebar for selecting and running simulation scenarios.
"""

import streamlit as st

from scenarios.startup import StartupScenario
from scenarios.target_tracking import TargetTrackingScenario
from scenarios.impossible_target import ImpossibleTargetScenario

from evaluation.metrics import ControllerMetrics


def render_sidebar():

    with st.sidebar:

        st.header("🏭 Simulation Control")

        scenario = st.selectbox(
            "Select Scenario",
            [
                "Startup",
                "Target Tracking",
                "Impossible Target",
            ],
        )

        run = st.button(
            "▶ Run Simulation",
            use_container_width=True,
        )

    # ---------------------------------------------------------
    # Nothing selected yet
    # ---------------------------------------------------------

    if not run:
        return (
            None,
            None,
            None,
            None,
            None,
        )

    # ---------------------------------------------------------
    # Execute Selected Scenario
    # ---------------------------------------------------------

    if scenario == "Startup":

        simulator = StartupScenario().run()
        target = 140

    elif scenario == "Target Tracking":

        simulator = TargetTrackingScenario().run()
        target = 150

    else:

        simulator = ImpossibleTargetScenario().run()
        target = 180

    # ---------------------------------------------------------
    # Collect Simulation Results
    # ---------------------------------------------------------

    history = simulator.get_history()

    metrics = ControllerMetrics(history)

    # ---------------------------------------------------------
    # Controller / Optimizer
    # ---------------------------------------------------------

    optimizer = None

    if hasattr(simulator, "controller"):

        optimizer = simulator.controller.optimizer

    # ---------------------------------------------------------
    # Return Everything Needed by Dashboard
    # ---------------------------------------------------------

    return (
        history,
        metrics,
        target,
        scenario,
        optimizer,
    )