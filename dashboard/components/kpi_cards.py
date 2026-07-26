"""
kpi_cards.py

Displays the latest well measurements.
"""

import streamlit as st


def render_kpis(history, target):

    state = history.last()

    st.subheader("📊 Live Well Status")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Flow Rate",
        f"{state.flow:.2f} bbl/hr",
    )

    col2.metric(
        "Well Head Pressure",
        f"{state.whp:.2f} psi",
    )

    col3.metric(
        "Flow Line Pressure",
        f"{state.flp:.2f} psi",
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Bottom Hole Pressure",
        f"{state.bhp:.2f} psi",
    )

    col5.metric(
        "Choke Opening",
        f"{state.choke:.1f} %",
    )

    # ---------------------------------------
    # Controller Status
    # ---------------------------------------

    error = abs(state.flow - target)

    if error <= 2:

        status = "🟢 TRACKING"

    elif error <= 8:

        status = "🟡 RECOVERING"

    else:

        status = "🔴 OFF TARGET"

    col6.metric(
        "Controller",
        status,
    )

    st.divider()