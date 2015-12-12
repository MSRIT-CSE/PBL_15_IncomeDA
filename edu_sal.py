import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('/home/chiru/data/pums/ss13pusa.csv',usecols=['SCHL','WKL','AGEP'])
df2 = pd.read_csv('/home/chiru/data/pums/ss13pusb.csv',usecols=['SCHL','WKL','AGEP'])
df = DataFrame(pd.concat([df1,df2],axis=0))

# Only select people who have worked in the last year (WKL) and are in their thirties
df = df[(df['SCHL']>14)&(df['WKL']==1)&(30<df['AGEP'])&(40>df['AGEP'])]


fig = plt.figure();

# plot wages
df.boxplot(column='WAGP',by='SCHL')

plt.xticks(np.arange(1,11),['No HS','HS','GED','<1 year college','>1 year college, n degree','associate\'s','Bachelor\'s','Master\'s','Professional degree','Doctorate'],rotation=90)

plt.xlabel('Level of education')
plt.ylabel('Wages in dollars/year')
plt.title('Yearly wages for different education levels')
plt.ylim([0,300000])
plt.savefig('Salary.png')




