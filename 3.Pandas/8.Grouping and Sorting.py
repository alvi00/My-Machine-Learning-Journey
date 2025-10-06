# we can use groupby 

data.groupby("points").points.count()

#this will like group points with points and then give me the count of each


#we can groupby points with price and take the min price of each point

data.groupby("points").price.min()

#we can also use apply method too

def alvi():
    return data.tittle.iloc[0]

data.groupby("winery").app(alvi)

#there is a function agg

data.groupby("country").price.agg([len, min, max])



#we can use Multi-indexes

alvi=data.groupby(['country', 'province']).description.agg([len])

#converting back to a regular index

alvi.reset_index()


#Sorting

alvi.sort_values(by="len",ascending=False)

#to sort by index

alvi.sort_index()

#also can sort with more than one column

alvi.sort_values(by=["country", "len"])