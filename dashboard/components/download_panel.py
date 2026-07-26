"""
download_panel.py

Download generated simulation artifacts.
"""

import streamlit as st
from pathlib import Path


def render_downloads():

    st.subheader("📥 Reports & Downloads")

    results = Path("results")

    files = [
        ("simulation.csv", "📄 Simulation CSV"),
        ("controller_report.txt", "📝 Controller Report"),
        ("flow_plot.png", "📈 Flow Plot"),
        ("pressure_plot.png", "📉 Pressure Plot"),
        ("choke_plot.png", "🎛 Choke Plot"),
    ]

    for filename, label in files:

        path = results / filename

        if path.exists():

            with open(path, "rb") as f:

                st.download_button(
                    label=label,
                    data=f,
                    file_name=filename,
                    use_container_width=True,
                )