
import pandas as pd

df = pd.read_csv('/Users/Rohan/Desktop/faculty.csv')
import re
df.degree = df.degree.map(lambda x: re.sub(r'\W+', '', x))

df.degree.unique()
##Out[201]: array(['ScD', 'PhD', 'MDMPHPhD', 'BSEdMSPhD', 'JDMAMPHMSPhD', 'PhDScD', '0'], dtype=object)

df.groupby('degree').count()
"""
Out[200]: 
              name  title  email  Unnamed: 4
degree                                      
0                1      1      1           0
BSEdMSPhD        1      1      1           0
JDMAMPHMSPhD     1      1      1           0
MDMPHPhD         1      1      1           0
PhD             27     27     27           0
PhDScD           1      1      1           0
ScD              5      5      5           0
"""
df.title.unique()
#Out[202]: 
array(['Associate Professor of Biostatistics',
       'Professor of Biostatistics',
       'Assistant Professor of Biostatistics',
       'Assistant Professor is Biostatistics'], dtype=object)
      
df.groupby('title').count()
"""
Out[203]: 
                                      name  degree  email  Unnamed: 4
title                                                                
Assistant Professor is Biostatistics     1       1      1           0
Assistant Professor of Biostatistics    11      11     11           0
Associate Professor of Biostatistics    12      12     12           0
Professor of Biostatistics              13      13     13           0

"""
dflist = df.email.tolist()


for i in range(len(dflist)):
    dflist[i] = str(dflist[i])

group=[]
import re
for i in dflist:
    domain = re.search("@[\w.]+", i) 
    group.append(domain.group())
    print (domain.group())

df["domains"] = group

df

df.domains.unique()

##array(['@mail.med.upenn.edu', '@upenn.edu', '@email.chop.edu',
 ##      '@cceb.med.upenn.edu'], dtype=object)

