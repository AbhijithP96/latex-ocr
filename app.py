"""
Streamlit app to convert images of mathematical equations to LaTeX code using NVIDIA AI Models.
"""

import os
import streamlit as st
from PIL import Image
from src.backend import run_inference

st.set_page_config(
    page_title="LaTeX Equation From Images",
    page_icon=Image.open("./images/equation-latex-svgrepo-com.png"),
    layout="wide",
    initial_sidebar_state="expanded",
)

# title
st.title("LaTeX Equation From Images :page_facing_up:")

# clear button
col1, col2 = st.columns([6, 1])
uploaded_file = None
with col2:
    if st.button("Clear", icon=":material/delete:"):
        if "result" in st.session_state:
            del st.session_state["result"]
            del st.session_state["uploaded_image"]
        st.rerun()

# description
st.markdown(
    "<p> Upload an image containing mathematical equations, and get the corresponding LaTeX code generated using NVIDIA AI Models.</p>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file", type=["png", "jpg", "jpeg", "bmp", "tiff"]
    )
    st.markdown("---")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        st.session_state["uploaded_image"] = image

        if st.button("Generate LaTeX Code", icon=":material/rocket_launch:"):
            with st.spinner("Generating LaTeX code..."):
                try:
                    result = run_inference(uploaded_file.getvalue())
                    st.session_state["result"] = result

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if "result" in st.session_state:
    st.markdown("---")
    st.markdown("### Generated LaTeX Code")
    st.code(st.session_state["result"], language="latex")
    st.markdown("You can copy the above LaTeX code and use it in your documents.")
    st.markdown("---")

    st.markdown("### Rendered LaTeX Equation")
    st.latex(st.session_state["result"].replace(r"\[", "").replace(r"\]", ""))

else:
    st.info(
        'Upload an image and click on "Generate LaTeX Code" to see the results here.'
    )

st.markdown("---")
st.markdown(
    '<p style="text-align: center;"> Made with Llama-3.2-Vision-Instruct </p>',
    unsafe_allow_html=True,
)
