#we can know datatype by

data.points.dtype

#or all dtype at once

data.dtype

#to change a data type

data.points.astype("float64")


#how to deal with missing data

#to see the missing values


data[pd.isnull(data.country)]  

#can replace the null values with something

data.country.fillna("dk")


#also can replace one value with another

data.country.replace("pak","ban")