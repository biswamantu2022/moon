import pandas as pd
import numpy as np
import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='biswadb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()
query='select * from employee'
cursor.execute(query)
cursor.fetchall()
l=cursor.fetchall()
s1=[]
s2=[]
for i in l:
    for k,v in i.items():
        s1.append(k)
        s2.append(v)
        
dict={'field':s1,'value':s2}
df=pd.DataFrame(dict)
df1=df.loc[df['field']=='id'].set_index(pd.Series(range(10))).rename(columns={'value':'emp_id'})
df1
df2=df.loc[df['field']=='salary'].set_index(pd.Series(range(10))).rename(columns={'value':'emp_salary'})
df2
df3=df.loc[df['field']=='name'].set_index(pd.Series(range(10))).rename(columns={'value':'emp_name'})
df3
df_new=pd.concat([df1,df2,df3],axis=1)
df_new=df_new[[#'field', 
    'emp_id', #'field', 
    'emp_salary', #'field', 
    'emp_name']]
df_new.dtypes
df_new=df_new.convert_dtypes()
df_new.dtypes
import pickle
with open ('df_new.pickle','wb') as f:
    pickle.dump(df_new,f)
with open ('df_new.pickle','rb') as f:
    obj=pickle.load(f)
obj
