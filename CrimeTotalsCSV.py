import pandas as pd
import numpy
# Load the raw data 
df = pd.read_csv('CrimeTotals.csv')

#reshapes dataframe from wide to long format and renames columns
reshape = pd.melt(df,id_vars=['Region', 'Division', 'State'],var_name='Year', value_name='Total')

#produce a csv file of the 'reshape' output
reshape.to_csv('output.csv')

print("Output file created.")