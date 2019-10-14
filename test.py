import pandas as pd

# Reading excel file
df = pd.read_excel("C:/Users/hylz/Desktop/test_2019_10_14/hola.xlsm")

# Group total cost according to '月'
df_sum = df.groupby('月')['Total Cost'].sum()

# Output to 'jaja.xlsm'
df_sum.to_excel("C:/Users/hylz/Desktop/test_2019_10_14/jaja.xlsx")