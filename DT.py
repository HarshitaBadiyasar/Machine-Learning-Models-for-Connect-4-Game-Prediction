!wget https://archive.ics.uci.edu/ml/machine-learning-databases/connect-4/connect-4.data.Z
!uncompress connect-4.data.Z


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from scipy.stats import randint
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

import pandas as pd
from sklearn.metrics import accuracy_score

#df = pd.read_csv('connect-4.data', header=None)

# Define mapping for 'b', 'o', and 'x'
mapping = {'b': 0, 'o': 1, 'x': 2}

# Read dataset and replace values with integers
df = pd.read_csv('connect-4.data', header=None)
df.replace(mapping, inplace=True)

# Define mapping for 'won', 'loss', and 'draw'
outcome_mapping = {'win': 1, 'loss': 0, 'draw': 2}

# Replace outcome values with integers
df.replace(outcome_mapping, inplace=True)

# Separate the target variable from the rest of the data
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

#X=pd.get_dummies(X)
#y=pd.get_dummies(y)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeClassifier

# Create and fit a DecisionTreeClassifier model
print("______________dt on gini_______")
model = DecisionTreeClassifier(criterion = "gini", random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy_model_on_test:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# Evaluate the performance of the model using k-fold cross-validation
scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"Accuracy_cross: {scores.mean():.2f} +/- {scores.std():.2f}")
# Tune the hyperparameters using grid search

params = {
    'max_depth': [2, 4, 6, 8, 10],
    'min_samples_split': [2, 4, 6, 8, 10]
}
grid_search = GridSearchCV(model, params, cv=5)
grid_search.fit(X_train, y_train)
print(f"Best parameters: {grid_search.best_params_}")
print(f"Accuracy: {grid_search.best_score_:.2f}")
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Accuracy_grid:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# Tune the hyperparameters using random search
param_dist = {
    'max_depth': randint(3, 10),
    'min_samples_leaf': randint(1, 9)
}
random_search = RandomizedSearchCV(model, param_dist, cv=5, n_iter=10)
random_search.fit(X_train, y_train)
print(f"Best parameters: {random_search.best_params_}")
print(f"Accuracy: {random_search.best_score_:.2f}")
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Accuracy_rnd_param:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))



# Create and fit a DecisionTreeClassifier model
print("______________dt on entropy_______")
model = DecisionTreeClassifier(criterion = "entropy", random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy_model_on_test:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# Evaluate the performance of the model using k-fold cross-validation
scores = cross_val_score(model, X_train, y_train, cv=5)
print(f"Accuracy_cross: {scores.mean():.2f} +/- {scores.std():.2f}")
# Tune the hyperparameters using grid search

params = {
    'max_depth': [2, 4, 6, 8, 10],
    'min_samples_split': [2, 4, 6, 8, 10]
}
grid_search = GridSearchCV(model, params, cv=5)
grid_search.fit(X_train, y_train)
print(f"Best parameters: {grid_search.best_params_}")
print(f"Accuracy: {grid_search.best_score_:.2f}")
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Accuracy_grid:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# Tune the hyperparameters using random search
param_dist = {
    'max_depth': randint(3, 10),
    'min_samples_leaf': randint(1, 9)
}
random_search = RandomizedSearchCV(model, param_dist, cv=5, n_iter=10)
random_search.fit(X_train, y_train)
print(f"Best parameters: {random_search.best_params_}")
print(f"Accuracy: {random_search.best_score_:.2f}")
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Accuracy_rnd_param:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall:", recall_score(y_test, y_pred, average='macro'))
print("F1-score:", f1_score(y_test, y_pred, average='macro'))
#print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
