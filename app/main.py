import streamlit as st
from app.config import DURATION_PRESETS, STYLE_CHECKPOINTS
from app.duration.pipeline import run_pipeline

st.set_page_config(page_title="Animux", page_icon="🎬", layout="centered")

st.title("Animux")
st.caption("Turn a prompt into an anime or cartoon video")

prompt = st.text_area("Prompt", placeholder="a fox exploring a glowing forest at night")

col1, col2 = st.columns(2)
with col1:
    style = st.selectbox("Style", list(STYLE_CHECKPOINTS.keys()))
with col2:
    duration_key = st.selectbox("Duration", list(DURATION_PRESETS.keys()))

if st.button("Generate", type="primary", disabled=not prompt.strip()):
    with st.spinner("Generating video..."):
        output_path = run_pipeline(prompt, duration_key, style)
    st.success("Done")
    st.video(output_path)
    with open(output_path, "rb") as f:
        st.download_button("Download", f, file_name="animux_output.mp4")