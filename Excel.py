import pandas as pd
import numpy as np
import sqlite3
df = pd.read_excel("spreadsheet.xlsx")
result = df.sort_values('CardDescription', ascending=True)
print()
print(result)