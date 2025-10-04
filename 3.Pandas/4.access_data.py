#to select a coloum we can use . or [] for example

data.Bob 
#or
data["Bob"]

#it will give me like
#	          Bob	
# Product A	  I liked it.
# Product B	  It was awful.


#it will select all the values of the Product A coloum
#now . has a disadvantage it doesnt allow space but [] does allow

#we can select specific ones too

data["Bob"][0]

#I liked it.
