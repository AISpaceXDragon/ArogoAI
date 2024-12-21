import streamlit as st
import requests

st.title("Image Description App")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Description"):
        files = {'image': uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/describe", files=files)

        if response.status_code == 200:
            st.success(f"Description: {response.json()['description']}")
        else:
            st.error(f"Error: {response.json()['error']}")
