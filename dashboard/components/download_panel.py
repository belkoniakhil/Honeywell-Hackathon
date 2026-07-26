import streamlit as st
from pathlib import Path


def render_downloads():

    st.subheader("📥 Downloads")

    results = Path("results")

    files = [

        ("simulation.csv","📄 Simulation CSV"),

        ("controller_report.txt","📝 Controller Report"),

        ("flow.png","📈 Flow Plot"),

        ("pressure.png","📉 Pressure Plot"),

        ("choke.png","🎛 Choke Plot"),

    ]

    for filename,label in files:

        path = results/filename

        if path.exists():

            with open(path,"rb") as f:

                st.download_button(

                    label,

                    data=f,

                    file_name=filename,

                    use_container_width=True,
                )