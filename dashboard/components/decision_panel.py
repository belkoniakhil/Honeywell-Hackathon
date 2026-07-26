"""
decision_panel.py

Displays the optimizer's latest decision.
"""

import streamlit as st


def render_decision(optimizer):

    st.subheader("🧠 Controller Decision")

    if optimizer is None:

        st.warning("Optimizer not available.")

        return

    decision = optimizer.last_decision

    if decision is None:

        st.info("No optimization decision available.")

        return

    st.metric(
        "Chosen Choke",
        f"{decision['chosen_choke']} %",
    )

    st.metric(
        "Predicted Flow",
        f"{decision['predicted_flow']:.2f} bbl/hr",
    )

    st.metric(
        "Predicted WHP",
        f"{decision['predicted_whp']:.2f} psi",
    )

    st.metric(
        "Tracking Cost",
        f"{decision['tracking_cost']:.2f}",
    )

    st.metric(
        "Pressure Cost",
        f"{decision['pressure_cost']:.2f}",
    )

    st.metric(
        "Movement Cost",
        f"{decision['movement_cost']:.2f}",
    )

    st.metric(
        "Total Cost",
        f"{decision['total_cost']:.2f}",
    )

    if "warning" in decision:

        st.error(decision["warning"])

    else:

        st.success("Decision satisfies all safety constraints.")