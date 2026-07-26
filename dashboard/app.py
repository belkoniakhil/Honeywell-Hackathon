"""
app.py

Honeywell Autonomous Production Optimizer Dashboard

Presentation Layer

Responsibilities
----------------
• Execute simulation scenarios
• Display live KPIs
• Display process trends
• Display controller metrics
• Display controller decisions
• Provide report downloads

NOTE:
No simulation logic should exist in this file.
"""

import sys
from pathlib import Path

# ---------------------------------------------------------
# Add Project Root
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# ---------------------------------------------------------
# Streamlit
# ---------------------------------------------------------

import streamlit as st

# ---------------------------------------------------------
# Dashboard Components
# ---------------------------------------------------------

from components.sidebar import render_sidebar
from components.metrics_panel import render_metrics
from components.optimizer_table import render_optimizer_table
from components.kpi_cards import render_kpis
from components.charts import render_charts
from components.decision_panel import render_decision
from components.download_panel import render_downloads
# Coming Next
# from components.metrics_panel import render_metrics
# from components.download_panel import render_downloads
# from components.status_panel import render_status

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Honeywell Autonomous Production Optimizer",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🏭 Honeywell Autonomous Production Optimizer")

st.markdown(
    """
### Digital Twin + Autonomous Production Optimization System

Industrial autonomous choke controller powered by a Digital Twin.
"""
)

st.divider()

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

history, metrics, target, scenario, optimizer = render_sidebar()

# ---------------------------------------------------------
# Waiting Screen
# ---------------------------------------------------------

if history is None:

    st.info(
        "👈 Select a scenario from the sidebar and click **Run Simulation**."
    )

# ---------------------------------------------------------
# Dashboard
# ---------------------------------------------------------

else:

    st.success(f"✅ Simulation Completed • {scenario}")

    # -----------------------------------------------------
    # Live KPIs
    # -----------------------------------------------------

    render_kpis(
        history,
        target,
    )

    # -----------------------------------------------------
    # Interactive Charts
    # -----------------------------------------------------

    render_charts(
        history,
        target,
    )

    # -----------------------------------------------------
    # Bottom Dashboard
    # -----------------------------------------------------

    left, right = st.columns([2, 1])

    # -------------------------------
    # Performance
    # -------------------------------

    with left:

        render_metrics(
            metrics,
            target,
        )

        st.metric(
            "RMSE",
            f"{metrics.rmse(target):.3f}",
        )

        st.metric(
            "Maximum Error",
            f"{metrics.max_error(target):.3f}",
        )

        st.metric(
            "Steady-State Error",
            f"{metrics.steady_state_error(target):.3f}",
        )

        st.metric(
            "Overshoot",
            f"{metrics.overshoot(target):.3f}",
        )

    # -------------------------------
    # Decision Panel
    # -------------------------------

    with right:

        render_decision(
            optimizer,
        )
        st.divider()

        render_optimizer_table(
            optimizer,
        )

    # -----------------------------------------------------
    # Placeholder Row
    # -----------------------------------------------------

    left2, right2 = st.columns([2, 1])

    with left2:

        st.subheader("📈 System Status")

        st.success("🟢 Simulation completed successfully.")

    with right2:

            render_downloads()

    # -----------------------------------------------------
    # Footer
    # -----------------------------------------------------

    st.divider()

    st.caption(
        f"Scenario : {scenario} | "
        f"Recorded States : {len(history.states)}"
    )