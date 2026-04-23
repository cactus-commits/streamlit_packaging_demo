import streamlit as st
from salaries.utils.constants import IMAGE_PATH

st.markdown("# HOME")

def home(): 
    st.markdown("# RAW DATA")
    st.image(IMAGE_PATH / "salaries_data_engineers.webp")

if __name__ == "__main__":
    home()