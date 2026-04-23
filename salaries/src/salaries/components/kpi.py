
#%% #skapar jupiter notebook
from salaries.utils.helpers import get_salaries_df
import duckdb 

df = get_salaries_df()

avg_salary = duckdb.sql("""
    FROM df 


""").df()

# %%