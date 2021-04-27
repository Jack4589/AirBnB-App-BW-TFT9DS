import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from category_encoders import OneHotEncoder

data_path = 'https://github.com/Jack4589/AirBnB-App-BW-TFT9DS/raw/main/Data/listings.csv.gz'


nyc_large = pd.read_csv(data_path, compression='gzip', 
                        header=0, sep=',', quotechar='"', error_bad_lines=False,
                        index_col='id')

# Set columns to keep, designate features and target
columns_keep = ["availability_365", "minimum_nights", "room_type", "bathrooms", "bedrooms", "beds", "price"]
target = ["price"]
features = ["availability_365", "minimum_nights", "room_type", "bathrooms", "bedrooms", "beds"]

nyc = nyc_large[columns_keep]

# Drop NAs
nyc = nyc.dropna()

# Convert price from object to float
nyc["price"] = nyc["price"].replace('[\$,]', '', regex=True).astype(float)

# Convert bathrooms, bedrooms, and beds from float to int
nyc = nyc.astype({'bathrooms': int, 'bedrooms': int, 'beds': int})

# Create target vector
y = nyc[target]

# Create feature matrix 
X = nyc[features]

# Instantiate and apply One Hot Encoder to room_type
ohe = OneHotEncoder(use_cat_names=True)
X_transform = ohe.fit_transform(X)

# Instantiate model
model = LinearRegression()

# Fit model
model_lr = model.fit(X_transform, y)
    

  
def predict_price(user_input):
    # Store prediction
    user_input_ = np.array(user_input)
    user_input = user_input_.reshape(1, -1)
    prediction = model_lr.predict(user_input)
    return prediction
