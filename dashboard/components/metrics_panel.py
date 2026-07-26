"""
metrics_panel.py

Displays controller performance metrics.
"""

import streamlit as st


def render_metrics(metrics, target):

    st.subheader("📊 Controller Performance")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "RMSE",
            f"{metrics.rmse(target):.3f}",
        )

        st.metric(
            "Maximum Error",
            f"{metrics.max_error(target):.3f}",
        )

    with col2:

        st.metric(
            "Steady-State Error",
            f"{metrics.steady_state_error(target):.3f}",
        )

        st.metric(
            "Overshoot",
            f"{metrics.overshoot(target):.3f}")

    st.divider()