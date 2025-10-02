#create table


#DataFrame


#There are two core objects in pandas: the DataFrame and the Series.

"""
DataFrame
A DataFrame is a table. It contains an array of individual entries,
each of which has a certain value. 
Each entry corresponds to a row (or record) and a column.
"""


import pandas as pd

pd. DataFrame({"Yes":[50,21],"No":[131,2]})

#for row level it will give 0,1.... as row

#   Yes   No
# 0  50   131
# 1  21     2

# this how the table is gonna look

#but if i wanna have custom row then



pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
               'Sue': ['Pretty good.', 'Bland.']},
            index=["Product A","Product B"])

#	          Bob	            Sue
# Product A	  I liked it.	    Pretty good.
# Product B	  It was awful.	    Bland.

#this is how table gonna look



#series

pd.Series([30,35,40],index=['2015 Sales', '2016 Sales', '2017 Sales'],name="Product A")

"""
table's gonna look like this

2015 Sales    30
2016 Sales    35
2017 Sales    40
Name: Product A, dtype: int64

"""