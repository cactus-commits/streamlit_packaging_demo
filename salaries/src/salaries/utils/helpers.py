from salaries.utils.constants import DATA_PATH
import pandas as pd

# funktion som gör följande - varje gång vi lägger in en path så hämtar den härifrån
def read_textfile(path):
    with open(path) as file: 
        return file.read()
    

def get_salaries_df():
    return pd.read_csv(DATA_PATH / "salaries.csv")