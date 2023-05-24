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

    }

    X_train = pd.DataFrame(data)
    

    #I found this code snipped through tutorial and chatgpt- CHECK this commented section @mantej if this is needed: 
    ### separate the 3 tpye of features ###
    
    X_train_text = X_train.category_list
    X_train_country = X_train.country_code
    X_train_nums = X_train.drop(columns=['category_list','country_code'])

#     X_dev_text = X_dev.category_list
#     X_dev_country = X_dev.country_code
#     X_dev_nums = X_dev.drop(columns=['category_list','country_code'])

#     X_test_text = X_test.category_list
#     X_test_country = X_test.country_code
#     X_test_nums = X_test.drop(columns=['category_list','country_code'])

    # encode text feature
    X_train.category_list = X_train.category_list.astype(str)
    vectorizer1 = CountVectorizer(min_df=5)
    vectorizer1.fit(X_train.category_list)
    X_train_text = vectorizer1.transform(X_train.category_list)

#     X_dev_text = vectorizer1.transform(X_dev.category_list)
#     X_test_text = vectorizer1.transform(X_test.category_list)
    # encode categorical feature
    X_train.country_code= X_train.country_code.astype(str)
    vectorizer2 = CountVectorizer(min_df=1)
    vectorizer2.fit(X_train.category_list)
    X_train_country = vectorizer2.transform(X_train.country_code)

#     X_dev_country = vectorizer2.transform(X_dev.country_code)
#     X_test_country = vectorizer2.transform(X_test.country_code)

    
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(X_train_nums)
    X_train_nums = scaler.transform(X_train_nums)
#     X_dev_nums = scaler.transform(X_dev_nums)
#     X_test_nums = scaler.transform(X_test_nums)
    X_train_con = hstack([X_train_nums, X_train_country, X_train_text])


    # Make a prediction using the loaded model
    feature_vector = X_test_con
    prediction = model.predict([feature_vector])[0]
    
    
    # Return the prediction as 1 or 0
    return int(prediction)
