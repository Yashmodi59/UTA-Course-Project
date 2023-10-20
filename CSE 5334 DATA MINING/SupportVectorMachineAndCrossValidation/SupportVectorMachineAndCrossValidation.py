import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print("\n- - - - - - - - -  - - - TASK 1 - - - - - - - - - -- - - - - - - - - - - -\n")
print("CLASSIFICATION USING SVM")
nba_dataset =  pd.read_csv('nba2021.csv') #Load data set
nba_dataset = nba_dataset[(nba_dataset['MP'] > 1)]


original_headers = list(nba_dataset.columns.values) # list column value
print("No. of players in each Position")
print(nba_dataset.loc[:, 'Pos'].value_counts())

print("Shape of dataset")
print(nba_dataset.shape)

print("Columns in dataset")
print(nba_dataset.columns)
#ignore Player Pos age TM for feature
## Here Player name, team name, age  is not important for classification so we cannot include them as feature
feature_column_list = [ 'FG%',  '3P%',  '2P%', 'eFG%',  'FT%', 'ORB',
 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
print("Feature Column List")
print(feature_column_list)
#Class attribute
class_column_name = 'Pos'
print("Class column name:   ",class_column_name)

# Split feature columns and class column
nba_feature = nba_dataset[feature_column_list]
nba_class_col = nba_dataset[class_column_name]
# scaler = MinMaxScaler()
# X_scaler = scaler.fit(nba_feature)

# nba_feature_scaled = X_scaler.transform(nba_feature)

print(nba_feature.head())

#train-feature has 75% data of nba_feature
#test_feature has 25% data of nba_feature
X_train, X_test, Y_train,Y_test = train_test_split(nba_feature, nba_class_col,  train_size=0.75, test_size=0.25)
model = svm.SVC(kernel='linear', C=1000, gamma=0.0001)
model = model.fit(X_train, Y_train)
predictions = model.predict(X_test)
print("Prediction:")
print(predictions)
print("\n- - - - - - - - -  - - - TASK 2 - - - - - - - - - -- - - - - - - - - - - -\n")
print("Accuracy: ")
svm1_accuracy_score = accuracy_score(Y_test, predictions)
print("Training set accuracy: ",accuracy_score(Y_train,model.predict(X_train)))
print("Test Set Accuracy: ", svm1_accuracy_score)

print("\n- - - - - - - - -  - - - TASK 3 - - - - - - - - - -- - - - - - - - - - - -\n")
print("Confusion matrix:")
print(pd.crosstab(Y_test, predictions, rownames=['True'], colnames=['Predicted'], margins=True))

print("\n- - - - - - - - -  - - - TASK 4 - - - - - - - - - -- - - - - - - - - - - -\n")
print("10-fold stratified cross-validation")
# apply 10-fold stratified cross-validation instead of 75-25% split. scores are stored in a list scores.
scores = cross_val_score(model, nba_feature, nba_class_col, cv=10)
print("\n- - - - - - - - -  - - - TASK 5 - - - - - - - - - -- - - - - - - - - - - -\n")
print("Mean of 10-fold stratified cross-validation")

# Print out the accuracy of each fold in 4).
print("Cross-validation scores: {}".format(scores))
# Print out the average accuracy across all the folds in 4).
print("Average cross-validation score: {:.3f}".format(scores.mean()))

