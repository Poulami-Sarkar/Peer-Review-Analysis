import pandas as pd
import numpy as numpy
import csv as csv
df = pd.read_csv('../personreview.csv')
t=10
df =  df.sort_values(['date'], ascending=[True])
first = df['date'].head(1)
last  = df['date'].tail(1)
#df.groupby('id').head(2)
##################################################################################
#                         Reviews commented by one person                        #
##################################################################################
#for i in (df['issue'].unique()):
df = df.drop_duplicates(subset=['sender','issue'])
#print(df.head(50))
r1 = df['issue'].unique()
#print(r1)
##################################################################################
#                         Reviews commented by two people                        #
##################################################################################
r2 = df[['issue','sender']]
r2[['issue']] = r2.groupby('issue')['issue'].filter(lambda x: len(x) >= 2)
#print(r2)
r2 = r2.groupby('issue').count()
##################################################################################
#                       Reviews commented by three people                        #
##################################################################################
r3 = df[['issue','sender']]
r3[['issue']] = r3.groupby('issue')['issue'].filter(lambda x: len(x) >= 3)
#print(r3)
r3 = r3.groupby('issue').count()

##################################################################################
#                      People who commented on one review                        #
##################################################################################

#print(df)
p1 = df['sender'].unique()
#print(p1)
##################################################################################
#                      People who commented on two reviews                       #
##################################################################################
p2 = df[['issue','sender']]
p2[['sender']] = p2.groupby('sender')['sender'].filter(lambda x: len(x) >= 2)
#print(p2)
p2 = p2.groupby('sender').count()
##################################################################################
#                    People who commented on three reviews                       #
##################################################################################
p3 = df[['issue','sender']]
p3[['sender']] = p3.groupby('sender')['sender'].filter(lambda x: len(x) >= 3)
#print(p3)
p3 = p3.groupby('sender').count()

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['first',''])
    first.to_csv(f,header=False)
    writer.writerow(['last', ''])
    last.to_csv(f, header=False)
    writer.writerow(['r1','r2','r3'])
    writer.writerow([r1.shape[0],r2.shape[0],r3.shape[0]])
    writer.writerow(['p1','p2','p3'])
    writer.writerow([p1.shape[0],p2.shape[0],p3.shape[0]])
f.close()
