import streamlit as st

st.title("DPM Converter")

build_file = st.file_uploader(
    "Build Answers",
    type=["json"]
)

questions_file = st.file_uploader(
    "Questions",
    type=["json"]
)

if build_file and questions_file:

    profile = build_profile(
        build_file,
        questions_file
    )

    me_md = render_markdown(profile)

    st.markdown(me_md)

    st.download_button(
        "Download me.md",
        me_md,
        file_name="me.md"
    )
