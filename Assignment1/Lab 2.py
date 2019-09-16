import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

data = pd.read_csv('https://raw.githubusercontent.com/tofighi/MachineLearning/master/datasets/heart.csv')

# X = feature values, all the columns except the last column
X = data.iloc[:, :-1]

# y = target values, last column of the data frame
y = data.iloc[:, -1]

# filter out if the person got heart disease
yes = data.loc[y == 1]

# filter out the person didn't get heart disease
no = data.loc[y == 0]

# Find missing data
missing = data.isnull().sum().sum()
print(missing)

# categorial = data.select_dtypes(exclude=["number","bool_","object_"])
print(data.info())

# Find percentage of class 0 and class 1
count = 1
yhd = 0
nhd = 0
for point in y:
    count += 1
    if (point == 1):
        yhd += 1
    elif (point == 0):
        nhd += 1

pyhd = yhd / count
pnhd = nhd / count

print(count)
print(pyhd)
print(pnhd)

# Correlation matrix
corr = data.corr()
fig, ax = plt.subplots(figsize=(10, 10))
ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns);
plt.yticks(range(len(corr.columns)), corr.columns);

# Plot the data
plt.figure(2)
plt.scatter(yes.iloc[:, 0], yes.iloc[:, 1], s=10, label='yes')
plt.scatter(no.iloc[:, 0], no.iloc[:, 1], s=10, label='No')
plt.legend()
plt.show()

# Filter out categorical features
cat_data = data.select_dtypes(include=['object']).copy()
print(cat_data.head())

# One Hot encoding
cat_data_onehot = cat_data.copy()
cat_data_onehot = pd.get_dummies(cat_data_onehot, columns=['famhist'], prefix=['famhist'])

print(cat_data_onehot.head())

# Standardization

# Drop Categorical feature column
X_new = X.drop(['famhist'], axis=1)
print(X_new)


# Standardize remaining feature columns which are not categorial
# Get Column names
# names = X_new.columns

# Create Scaler Object
# scaler = preprocessing.StandardScaler()

# Fit data in scaler object
# scaled_df = scaler.fit_transform(X_new)
# scaled_df = pd.DataFrame(scaled_df, columns=names)

# print(scaled_df)


def standardize(data):
    # Store the data's original shape
    shape = data.shape
    # Flatten the data to 1 dimension
    data = np.reshape(data, (-1,))
    # Find mean and standard deviation
    mean = np.mean(data)
    std = np.std(data)
    # Create a new array for storing standardized values
    standardized_values = list()
    # Iterate through every value in data
    for x in data:
        # standardize
        x_normalized = (x - mean) / std
        # Append it in the array
        standardized_values.append(x_normalized)
    # Convert to numpy array
    n_array = np.array(standardized_values)
    # Reshape the array to its original shape and return it.
    return np.reshape(n_array, shape)


X_std = standardize(X_new)
print(X_std)







































