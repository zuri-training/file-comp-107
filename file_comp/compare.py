import pandas as pd
import numpy as np
# pd is just a short name for referencing pandas
# dftest1/2 means dataframe with the excel name in my folder

dftest1=pd.read_excel('files/test1.xlsx'
)

dftest2=pd.read_excel('files/test2.xlsx')

print(dftest1.equals(dftest2))


