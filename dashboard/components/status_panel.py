import streamlit as st


def render_status(history, target):

    state = history.last()

    st.subheader("🛡 Safety Status")

    whp = "✅ SAFE" if 200 <= state.whp <= 300 else "❌ LIMIT"

    flp = "✅ SAFE" if 150 <= state.flp <= 200 else "❌ LIMIT"

    bhp = "✅ SAFE" if 2800 <= state.bhp <= 3200 else "❌ LIMIT"

    if target > 160:

        overall = "🟠 TARGET UNATTAINABLE"

    else:

        overall = "🟢 SAFE"

    st.metric("WHP", whp)
    st.metric("FLP", flp)
    st.metric("BHP", bhp)

    st.success(overall)