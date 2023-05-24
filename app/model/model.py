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
    #Mantej, parameters are matching with the X train - Same order

    
    category = input("Enter category: ")
    total_funding = float(input("Enter total funding: "))
    country_code = input("Enter country code: ")
    total_funding_rounds = int(input("Enter total funding rounds: "))
    first_funding_date = input("Enter first funding date (YYYY-MM-DD): ")
    last_funding_date = input("Enter last funding date (YYYY-MM-DD): ")

    processed_first_funding_date = preprocess_date(first_funding_date)
    processed_last_funding_date = preprocess_date(last_funding_date)


    # Create a feature vector based on the input parameters THE X_test_con IS THE FINAL FROM THE COPY PASTING THE CODE
    data = {
    'category': [category],
    'total_funding': [total_funding],
    'country_code': [country_code],
    'total_funding_rounds': [total_funding_rounds],
    'first_funding_date': [processed_first_funding_date],
    'last_funding_date': [processed_last_funding_date]

    df = pd.DataFrame(data)
    feature_vector = X_test_con

    #I found this code snipped through tutorial and chatgpt- CHECK this commented section @mantej if this is needed: 
    """
    # Assuming you have already processed X_test_nums, X_test_country, and X_test_text

    # Concatenate the processed numeric features
    X_test_nums_processed = X_test_nums

    # Concatenate the processed country features
    X_test_country_processed = X_test_country

    # Concatenate the processed text features
    X_test_text_processed = X_test_text

    # Assuming the processed DataFrame is stored in df
    # Preprocess the 'category' column to match the format of X_test_con
    df['category'] = df['category'].str.lower()

    # Preprocess the 'total_funding' column (e.g., scaling or normalization) to match the format of X_test_con
    df['total_funding'] = df['total_funding']  # Apply your preprocessing steps here

    # Preprocess the 'country_code' column to match the format of X_test_con
    df['country_code'] = df['country_code']  # Apply your preprocessing steps here

    # Preprocess the 'total_funding_rounds' column (e.g., scaling or normalization) to match the format of X_test_con
    df['total_funding_rounds'] = df['total_funding_rounds']  # Apply your preprocessing steps here

    # Preprocess the 'first_funding_date' column to match the format of X_test_con
    df['first_funding_date'] = preprocess_date(df['first_funding_date'])

    # Preprocess the 'last_funding_date' column to match the format of X_test_con
    df['last_funding_date'] = preprocess_date(df['last_funding_date'])

    # Concatenate all the processed features
    feature_vector = hstack([X_test_nums_processed, X_test_country_processed, X_test_text_processed])
    """
}
 

    
    
    
    
    

    # Make a prediction using the loaded model
    prediction = model.predict([feature_vector])[0]

    # Return the prediction as 1 or 0
    return int(prediction)
