"""
What is cross-validation?¶
In cross-validation, we run our modeling process on different subsets 
of the data to get multiple measures of model quality.

For example, we could begin by dividing the data into 5 pieces,
 each 20% of the full dataset. In this case, we say that we have broken the data into 5 "folds".

Then, we run one experiment for each fold:

1. In Experiment 1, we use the first fold as a validation (or holdout)
set and everything else as training data. This gives us a measure
of model quality based on a 20% holdout set.


2. In Experiment 2, we hold out data from the second fold
 (and use everything except the second fold for training the model)
 . The holdout set is then used to get a second estimate of model quality.

 
 
3 .We repeat this process, using every fold once as the holdout set. Putting this 
together, 100% of the data is used as holdout at some point, and we end up with a
 measure of model quality that is based on all of the rows in the dataset (even if we don't use all rows simultaneously).

"""


import pandas as pd

# Read the data
data = pd.read_csv('../input/melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price


from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])


from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')
#cv = number of folds
print("MAE scores:\n", scores)


print("Average MAE score (across experiments):")
print(scores.mean())



#we can change n_estimators and check which one is best

def get_score(n_estimators):
    my_pipeline = Pipeline(steps=[
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators, random_state=0))
    ])
    scores = -1 * cross_val_score(my_pipeline, X, y,
                                  cv=3,
                                  scoring='neg_mean_absolute_error')
    return scores.mean()


results = {}
for i in range(1,9):
    results[50*i] = get_score(50*i)

import matplotlib.pyplot as plt
#%matplotlib inline

plt.plot(list(results.keys()), list(results.values()))
plt.show()


n_estimators_best = min(results, key=results.get)

print(n_estimators_best)