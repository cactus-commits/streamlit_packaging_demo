import streamlit as st

# to run the app stand in the correct folder and run 'uv run streamlit run app.py
st.markdown("COOL APP")

pages = [
    st.Page("pages/home.py", title = "Home"),
    st.Page("pages/raw_data.py", title = "Raw data"),
    st.Page("pages/dashboard.py", title = "Dashboard")
]

pg = st.navigation(pages)

pg.run()

#st.markdown("# COOL APP")
#st.balloons()

