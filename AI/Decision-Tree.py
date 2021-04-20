# -*- coding: utf-8 -*-

import pandas as pd
import sklearn
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("train.csv")

X = df.drop("age", axis=1)
y = df.age

X_num = X.drop("sex",axis=1)
scaler = StandardScaler().fit(X_num)
X_scaled = pd.DataFrame(scaler.transform(X_num))

dummy = pd.get_dummies(X["sex"])

dummy.head()

X = pd.concat([X_scaled,dummy], axis=1)

X.head()

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2)

"""## Decision Tree """

from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(X_train, y_train)

"""Mean squared error of our model on the test data"""

from sklearn.metrics import mean_squared_error

predictions = tree_reg.predict(X_test)
tree_mse = mean_squared_error(y_test, predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse

"""Cross Validation"""

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())
    
from sklearn.model_selection import cross_val_score
tree_scores = cross_val_score(tree_reg, X, y,
                             scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-tree_scores)
display_scores(tree_rmse_scores)

"""# NB"""

from sklearn.naive_bayes import CategoricalNB
#clf = Categorical()
#clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
clf_mse = mean_squared_error(y_test, predictions)
clf_rmse = np.sqrt(clf_mse)
clf_rmse

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())
    
from sklearn.model_selection import cross_val_score
clf_scores = cross_val_score(clf, X, y,
                             scoring="neg_mean_squared_error", cv=10)
clf_rmse_scores = np.sqrt(-tree_scores)
display_scores(tree_rmse_scores)


X_cat = X.sex
X_cat.head()

categorical_mask = X.dtypes == 'object'

ohe = OneHotEncoder(categorical_features=categorical_mask, sparse=False)
ohe

df_ohe = ohe.fit(X)


X_num = X.copy()
X_num = X.drop("sex", axis=1)# must drop this non-numeric attribute before next steps

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
    ])

X_num = num_pipeline.fit_transform(X_num)

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

num_attribs = list(X_num)
cat_attribs = ["sex"]

full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(sparse=False), cat_attribs),
    ])

X_prepared = full_pipeline.fit_transform(X)

pip freeze

