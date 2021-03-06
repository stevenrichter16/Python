# -*- coding: utf-8 -*-
"""Handling Categorical Variables.ipynb
  This notebook goes through three ways of handling categorical variables in a dataset. 
Three ways to handle a column with categorical values:
    1. Drop the column
    2. Label encode the values if they are ordinal ('Never', 'Rarely', 'Somtimes', 'Always')
    3. One-Hot encode the values if they are nominal ('Red', 'Blue', 'Green')
"""

# Imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# First read in the data 
df = pd.read_csv(r"..\datasets\salary.csv")

# There are three categorical variables we need to encode
df.head()

"""# Method 1: Drop the column

Instead of converting the categorical values to numerical values you can simply get rid of all the columns with categorical values. This method is not ideal as the dataset loses a lot of valuable data and insight.
"""

# Find all columns with categorical values
cats = df.dtypes == 'object'
cats

drop_df = df.select_dtypes(exclude=['object'])

drop_df.head()

"""# Method 2: Label Encoding

If the categorical data is ordinal then use Label Encoding.

## Label Encoding Part 1: Multiple Columns
"""

# Read in the data
df = pd.read_csv(r"..\datasets\salary.csv")

# Instantiate the label encoder
le = LabelEncoder()

# Create a categorical boolean mask to capture the categorical columns    dtype: series
categorical_mask = df.dtypes == 'object'

# Filter the categorical columns using the mask                           dtype: pandas.core.indexes.base.Index
categorical_cols = df.columns[categorical_mask].tolist()

# Finally apply the label encoder to the categorical columns
df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))

df.head()

"""## Label Encoding Part 2: One Column"""

# Read in the data
df = pd.read_csv(r"..\datasets\salary.csv")

# Encode the values of JUST the dg column
df['dg'] = le.fit_transform(df.dg.values)

# 0's are doctorates and 1's are masters
df.head()

"""# Method 3: One-Hot Encoding"""

# Read in the data
df = pd.read_csv(r"..\datasets\salary.csv")

# Create a categorical boolean mask to capture the categorical columns    dtype: series
categorical_mask = df.dtypes == 'object'

# Instantiate the One-Hot Encoder
ohe = OneHotEncoder(categorical_features = categorical_mask, sparse=False)

# Apply the One-Hot Encoder to the categorical features
df_ohe = ohe.fit_transform(df)

