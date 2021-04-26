import pandas as pd
from sklearn.linear_model import LinearRegression

data_path = 'https://github.com/Jack4589/AirBnB-App-BW-TFT9DS/raw/main/Data/listings.csv'

def create_model(data_path):

    nyc_simple = pd.read_csv(data_path)

    # Set target
    target = "price"

    # Create target vector
    y = nyc_simple[target]

    # Create simple (1 variable) feature matrix (vector)
    X = nyc_simple.drop(columns=[target])
    X_feats = ["availability_365"]
    X_simple = X[X_feats]

    # Instantiate model
    model = LinearRegression()

    # Fit model
    model_lr = model.fit(X_simple, y)
    
    return model_lr
  
def predict_price(user_input)
    # Store prediction
    prediction = model_lr.predict(user_input)
    return prediction
