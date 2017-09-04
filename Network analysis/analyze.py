import pandas as pd
import numpy as np
import datetime as datetime
import csv 
df = pd.read_csv('../personreview.csv')
df1 = pd.read_csv('../result.csv')
head = datetime.datetime.strptime('2008-09-02 20:13:34.526552', '%Y-%m-%d %H:%M:%S.%f') 
tail = datetime.datetime.strptime('2012-10-31 03:02:05.619400', '%Y-%m-%d %H:%M:%S.%f') 
step = (tail-head)/50
df['date'] = df['date'].apply(pd.to_datetime, errors='coerce')       #typecasts the column date to type datetime
df=df.sort_values(by='date')                                   #Sorts the dataframe in ascending order of dates
#print(df.dtypes)

def create(start, end):
    pr = df.set_index(['date'])                                         #Required for the next step.  Sets date as an index
    pr = pr.loc[start:end]  
    review = pr.drop_duplicates(['issue'],keep = 'first')
    res = df1.loc[review['issue']]
    noOfReview =review.shape[0]
    noOfComments = pr.shape[0]
    noOfPersons = pr.drop_duplicates(['sender'],keep = 'first')
    noOfPersons =noOfPersons.shape[0]
    avComments = noOfComments/noOfPersons
    noOfApprovals = pr['approvals'].sum()
    avApprovals = noOfApprovals/noOfPersons
    avClosureTime = (res['no_of_days'].sum())/noOfReview
    print(noOfReview,noOfComments,noOfApprovals,avComments,avApprovals,avClosureTime)
    with open('aug22.csv', 'a', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        data = [[noOfReview,noOfComments,noOfApprovals,avComments,avApprovals,avClosureTime]]
        a.writerows(data)
    d = pd.DataFrame(res)
    filename = 'aug.csv'
    d.to_csv(filename, index=False, encoding='utf-8')
#create(head,head+ (1*step))
for i in range (1,51):
    create(head,head+ (i*step))
