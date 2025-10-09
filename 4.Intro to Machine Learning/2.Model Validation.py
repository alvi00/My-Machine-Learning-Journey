#Model Validation

#lets build a model first

import pandas as pd

# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

# Filter rows with missing price values

filtered_melbourne_data= melbourne_data.dropna(axis=0)

# Choose target and features

y=filtered_melbourne_data.price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']

X=filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor

#define model

melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model

melbourne_model.fit(X,y)

predicted_home_prices = melbourne_model.predict(X)


#Now we will use MAE matrics to evaluate our model


from sklearn.metrics import mean_absolute_error

mean_absolute_error(y,predicted_home_prices)



# as it is bad to evaluate a model on traning data 
# we gonna use validation data

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.

train_X,val_X,train_y,val_Y=train_test_split(X,y,random_state=0)

#define model
melbourne_model = DecisionTreeRegressor()

#fit model

melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data


val_predictions=melbourne_model.predict(val_X)

print(mean_absolute_error(val_Y,val_predictions))
