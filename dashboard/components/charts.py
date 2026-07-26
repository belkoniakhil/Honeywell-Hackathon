"""
charts.py

Interactive process trend charts.
"""

import streamlit as st
import plotly.graph_objects as go


def render_charts(history, target):

    times = history.get_times()

    flows = history.get_flows()

    whp = history.get_whp()
    flp = history.get_flp()
    bhp = history.get_bhp()

    chokes = history.get_chokes()

    # =====================================================
    # Row 1
    # =====================================================

    left, right = st.columns(2)

    # -----------------------------------------------------

    with left:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=times,
                y=flows,
                mode="lines",
                name="Flow",
                line=dict(width=3),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=times,
                y=[target] * len(times),
                mode="lines",
                name="Target",
                line=dict(
                    dash="dash",
                    color="red",
                ),
            )
        )

        fig.update_layout(

            title="Flow Rate",

            xaxis_title="Time (s)",

            yaxis_title="Oil Rate (bbl/hr)",

            height=350,

            template="plotly_dark",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # -----------------------------------------------------

    with right:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=times,
                y=chokes,
                mode="lines",
                name="Choke",
                line=dict(width=3),
            )
        )

        fig.update_layout(

            title="Choke Position",

            xaxis_title="Time (s)",

            yaxis_title="Opening (%)",

            height=350,

            template="plotly_dark",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # =====================================================
    # Row 2
    # =====================================================

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=times,
            y=whp,
            mode="lines",
            name="WHP",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=times,
            y=flp,
            mode="lines",
            name="FLP",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=times,
            y=bhp,
            mode="lines",
            name="BHP",
        )
    )

    fig.update_layout(

        title="Pressure Trends",

        xaxis_title="Time (s)",

        yaxis_title="Pressure (psi)",

        height=400,

        template="plotly_dark",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )