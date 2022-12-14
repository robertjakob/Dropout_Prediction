import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the data into a pandas DataFrame
df = pd.read_csv('data.csv')

# Split the data into features (X) and target (y)
X = df.drop(columns='churn')
y = df['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy:.2f}')

# Make predictions on new data
new_data = ... # Load the new data here
new_predictions = model.predict(new_data)

#This code trains a logistic regression model on the training data, evaluates its performance on the test data, and then uses the trained model to make predictions on new data.

#Of course, this is just one example of how you could approach this problem using machine learning. There are many other algorithms and techniques that you could use to build a model for binary classification. The specific approach that you choose will depend on the specific characteristics of your data and the goals of your project.
