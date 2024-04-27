import joblib
import pandas as pd

# Load the saved model
model = joblib.load('models/market_cap_category-best_svm_model.pkl')

# Let's say you have new data for prediction
new_data = pd.read_csv('new_data.csv')  # Replace 'new_data.csv' with your new data file

# Preprocess the new data (ensure it's preprocessed in the same way as the training data)
# For example:
# new_data = preprocess_data(new_data)

# Extract features (X) from the new data
X_new = new_data[['book_value', 'book_to_share_value', 'earnings_per_share', 
                  'debt_ratio', 'current_ratio', 'dividend_yield_ratio', 
                  'price_movement_percent']]

# Make predictions using the loaded model
predictions = model.predict(X_new)

# Assuming predictions are numerical (-1, 0, 1), you may want to map them to their corresponding labels
# For example, if -1 represents 'sell', 0 represents 'hold', and 1 represents 'buy'
label_mapping = {-1: 'sell', 0: 'hold', 1: 'buy'}
predictions_labels = [label_mapping[pred] for pred in predictions]

# Print the predictions
print(predictions_labels)