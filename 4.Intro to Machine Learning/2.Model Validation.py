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

