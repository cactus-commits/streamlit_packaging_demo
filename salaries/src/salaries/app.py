import streamlit as st 

# to run the app stand in the correct folder and run 'uv run streamlit run app.py
pages = [
    st.Page("pages/home.py", title = "Home"),
    st.Page("pages/dashboard.py", title = "Dashboard"),
    st.Page("pages/raw_data.py", title = "Raw data"),
]

pg = st.navigation(pages)

pg.run()

