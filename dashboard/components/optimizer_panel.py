import streamlit as st
import pandas as pd


def render_optimizer_panel(optimizer):

    st.subheader("🧠 Optimization Explorer")

    if optimizer is None:

        st.warning("Optimizer unavailable.")

        return

    if not optimizer.search_history:

        st.info("No optimization history available.")

        return

    df = pd.DataFrame(optimizer.search_history)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )