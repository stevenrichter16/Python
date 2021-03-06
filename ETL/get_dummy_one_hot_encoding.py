# -*- coding: utf-8 -*-
"""get_dummy One-Hot Encoding.ipynb
  This notebook is to demonstrate one-hot encoding
"""

import pandas as pd

df = pd.read_csv(r"..\datasets\salary.csv")

df.head()

"""# We need to one-hot encode the sx column"""

# Returns a DataFrame with the columns encoded
dummy = pd.get_dummies(df['sx'])

dummy.head()

"""# Now we need to concatenate the new dummy DataFrame onto our dataset"""

df = pd.concat([df, dummy], axis=1)
df.head()

"""# Now we need to drop the old sx column"""

df.drop('sx', axis=1, inplace=True)

df.head()

"""# Now we will encode the rk column"""

dummy = pd.get_dummies(df['rk'])

dummy.head()

df = pd.concat([df, dummy], axis=1)

df.head()

df.drop('rk', axis=1, inplace=True)

df.head()

"""# Now we will encode the dg column"""

dummy = pd.get_dummies(df['dg'])

dummy.head()

df = pd.concat([df, dummy], axis=1)

df.head()

df.drop('dg', axis=1, inplace=True)

"""# Now all the categorical variables are converted to numerical"""

df.head()
