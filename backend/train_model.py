import numpy as np    # handles numerical operations
import pandas as pd   # handles operations with structured data like CSVs
import joblib 
# Scikit-learn (sklearn) is a powerful open-source machine learning library in Python that comes with a lot of algorithms which we can use in our implmentations
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


# Data Source: Kaggle (https://www.kaggle.com/datasets/samikshadalvi/pcos-diagnosis-dataset)
data = pd.read_csv('data/pcos_dataset.csv')

# dimensions
print(data.shape)

# top 5 data cases 
print(data.head())

# statistical description of the data
print(data.describe())


# checks for missing values, and returns the count of missing values by summing over the instances
print(data.isnull().sum()) # the output given below

# replace missing values with the mean of the respective column
data.fillna(data.mean(), inplace=True)


# separating data and label
X = data.drop('PCOS_Diagnosis', axis=1) # When dropping a column, set axis = 1. When dropping a row, set axis = 0.
y = data['PCOS_Diagnosis']

print(X)
print()
print(y)
print()

# Normalize / standardise the data to bring all column values in the same range
scaler = StandardScaler() # we imported Standard Scalar from sklearn
X = scaler.fit_transform(X)

# splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

model = LogisticRegression()
model.fit(X_train, y_train)
print('Model trained successfully.')

# accuracy on the training data
X_train_pred = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_pred, y_train)
print("Training Accuracy: ", training_data_accuracy)
print()

# accuracy on the test data
X_test_pred = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_pred, y_test)
print("Testing Accuracy: ", testing_data_accuracy)
print()


feature_names = ["Age", "BMI", "Menstrual_Irregularity", "Testosterone_Level(ng/dL)", "Antral_Follicle_Count"]


new_input = np.asarray((29,29.7,1,98.7,14))

input_df = pd.DataFrame([new_input], columns=feature_names)

input_data_scaled = scaler.transform(input_df)

prediction = model.predict(input_data_scaled)
print("Predicted Output: ", prediction)

if prediction[0] == 0:
  print("The person does not have PCOS")
else:
  print("The person has PCOS")

joblib.dump(model, 'pcos_model.pkl')  
joblib.dump(scaler, 'scaler.pkl')  