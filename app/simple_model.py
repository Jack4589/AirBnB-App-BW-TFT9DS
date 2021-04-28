import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data_path = 'https://github.com/Jack4589/AirBnB-App-BW-TFT9DS/raw/main/Data/listings.csv'


nyc_simple = pd.read_csv(data_path)

# Set target
target = "price"

# Create target vector
y = nyc_simple[target]

# Create simple (1 variable) feature matrix (vector)
X = nyc_simple.drop(columns=[target])
X_feats = ["availability_365", "minimum_nights"]
X_simple = X[X_feats]

# Instantiate model
model = LinearRegression()

# Fit model
model_lr = model.fit(X_simple, y)
    

  
def predict_price(user_input):
    # Store prediction
    user_input_ = np.array(user_input)
    user_input = user_input_.reshape(1, -1)
    prediction = model_lr.predict(user_input)
    return prediction
