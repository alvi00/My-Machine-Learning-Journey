#pandas has its own accessor operators, loc and iloc

#iloc
# iloc : index-based selection
#it is row first then coloum second

#so if i wanna see first three row and one coloum

data.iloc[[0,1,2],0]

#or

data.iloc[0:3,0]

#if i wanna like all rows and one coloum

data.iloc[:,0]

#if i want last 5 rows and all coloums

data.iloc[-5:]


#loc
#loc= label-based selection
#it is also row first then coloum second

#so to get the first row and first coloum

data.loc[0,"country"]

#or like all rows and specific coloums

data.loc[:,["country","name","id"]]



#iloc : the start is included, the stop is excluded
#loc: both start and end are included


#if we want to change the index of the dataframe then

data.set_index("country")


#we can also select with condition like

data.loc[data.country=="italy"]

data.loc[(data.country=="italy") & (data.id>=90)]



# there are lot prebuilt function is pandas. two examples are below

#isin

data.loc[data.country.isin(["italy","Bangladesh"])]

#notnull

data.loc[data.price.notnull()]


#Assigning data


data["country"]="Bangladesh"

