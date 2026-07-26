import streamlit as st


def render_summary(history, target, scenario):

    state = history.last()

    st.subheader("📋 Scenario Summary")

    st.write(f"**Scenario** : {scenario}")

    st.write(f"**Target Flow** : {target:.1f} bbl/hr")

    st.write(f"**Final Flow** : {state.flow:.2f} bbl/hr")

    st.write(f"**Final Choke** : {state.choke:.1f} %")

    st.write(f"**Simulation Length** : {len(history.states)-1} sec")

    st.write(f"**Recorded States** : {len(history.states)}")