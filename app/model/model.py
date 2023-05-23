import pickle
import re
import scaler
from pathlib import Path
from datetime import datetime, timezone

__version__ = "1.0.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


def preprocess_date(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    utc_date = date.replace(tzinfo=timezone.utc)
    return utc_date.strftime("%Y-%m-%d")

# ALSO CHANGE THE NAME OF THE FILE HERE SHREYAS
with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl","rb") as f:
    model = pickle.load(f)
    
result = ["A good company", "Will likely not survive"]

def predict_pipeline(category, total_funding, country_code, total_funding_rounds, first_funding_date, last_funding_date):
    # processed_category = re.sub(r'\W+', ' ', category).lower()
    processed_first_funding_date = preprocess_date(first_funding_date)
    processed_last_funding_date = preprocess_date(last_funding_date)

    #MAKE THE PANDAS DATAFRAME BELOW THIS USING THE PARAMETERS FROM ABOVE AND ALSO SEE SPECIFICALLY SO THAT EVEN ORDER MATCHES WITH X_TRAIN
    
    # Create a feature vector based on the input parameters THE X_test_con IS THE FINAL FROM THE COPY PASTING THE CODE
    feature_vector = X_test_con

    # Make a prediction using the loaded model
    prediction = model.predict([feature_vector])[0]

    # Return the prediction as 1 or 0
    return int(prediction)