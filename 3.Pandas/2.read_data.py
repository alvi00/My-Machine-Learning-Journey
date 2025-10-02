#reading the data

data=pd.read_csv("path of the csv")

#to check the number of rows and coloumbs
data.shape

#to check the first 5 rows

data.head()

#now lets suppose we pandas didnt pick up the auto index from the csv 
#to pick that


data=pd.read_csv("path of the csv",index_col=0)