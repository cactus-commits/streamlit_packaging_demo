import streamlit as st
from salaries.utils.constants import get_salaries_df, read_textfile
from salaries.utils.constants import MARKDOWN_PATH



def dashboard_layout(): 
    st.markdown("# Salaries dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))
    st.dataframe(get_salaries_df())

# KPI


if __name__ == "__main__":
    dashboard_layout()