"""
optimizer_table.py

Displays all evaluated optimizer candidates.
"""

import streamlit as st
import pandas as pd


def render_optimizer_table(optimizer):

    st.subheader("🔍 Optimizer Search")

    if optimizer is None:

        st.warning("Optimizer unavailable.")

        return

    if not hasattr(optimizer, "last_candidates"):

        st.info("No candidate information available.")

        return

    if len(optimizer.last_candidates) == 0:

        st.info("No candidates evaluated.")

        return

    df = pd.DataFrame(
        optimizer.last_candidates
    )

    # Sort by total cost

    df = df.sort_values(
        by="total_cost"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )