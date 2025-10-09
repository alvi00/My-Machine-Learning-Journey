#to drop all unavaiable data

data=melbourne_data.dropna(axis=0)


#Dot notation, which we use to select the "prediction target"
#by convention prediction target is called y
y=melbourne_data.price

#Selecting with a column list, which we use to select the "features"

#the columns that are used to put into our model to make predictions are called features

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

#by convention features are called X

X=melbourne_data[melbourne_features]

X.describe()

X.head()


#building my first model

from sklearn.tree import DecisionTreeRegressor

melbourne_model=DecisionTreeRegressor(random_state=1)

#fit model

melbourne_model.fit(X,y)

#predict

print("Make predictions for this houses")

print(X.head())

print("The predictions are")

print(melbourne_model.predict(X))