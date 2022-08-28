#hello

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

df_pd=pd.DataFrame(cursor.fetchall())
df_pd
connection.close()

