"""
app.py

Honeywell Autonomous Production Optimizer Dashboard

Presentation Layer
------------------
Runs simulation scenarios and visualizes:

• Live KPIs
• Process Trends
• Controller Performance
• Controller Decision
• Safety Status
• Scenario Summary
• Optimization Explorer
• Downloads

No simulation logic exists in this file.
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
# Components
# ---------------------------------------------------------

from components.sidebar import render_sidebar
from components.kpi_cards import render_kpis
from components.charts import render_charts
from components.metrics_panel import render_metrics
from components.decision_panel import render_decision
from components.status_panel import render_status
from components.summary_panel import render_summary
from components.download_panel import render_downloads
from components.optimizer_panel import render_optimizer_panel

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
# Load CSS
# ---------------------------------------------------------

css_file = Path(__file__).parent / "styles" / "style.css"

if css_file.exists():

    with open(css_file) as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True,

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
    # KPI Cards
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
    # Performance + Decision
    # -----------------------------------------------------

    left, right = st.columns([2, 1])

    with left:

        render_metrics(
            metrics,
            target,
        )

    with right:

        render_decision(
            optimizer,
        )

    # -----------------------------------------------------
    # Safety + Summary
    # -----------------------------------------------------

    left, right = st.columns(2)

    with left:

        render_status(
            history,
            target,
        )

    with right:

        render_summary(
            history,
            target,
            scenario,
        )

    # -----------------------------------------------------
    # Optimization Explorer
    # -----------------------------------------------------

    render_optimizer_panel(
        optimizer,
    )

    # -----------------------------------------------------
    # Downloads
    # -----------------------------------------------------

    render_downloads()

    # -----------------------------------------------------
    # Footer
    # -----------------------------------------------------

    st.divider()

    st.caption(

        f"Scenario : {scenario} | "

        f"Target : {target:.1f} bbl/hr | "

        f"Recorded States : {len(history.states)}"

    )