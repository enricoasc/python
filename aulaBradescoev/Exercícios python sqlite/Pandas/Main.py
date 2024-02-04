import pandas as pd

series_objeto = pd.Series([1,7,9,13,17,99])
print(series_objeto)

series_objeto = pd.Series([1,7,9,13], index=['alfa','beta','gama','teta'])

print(series_objeto)