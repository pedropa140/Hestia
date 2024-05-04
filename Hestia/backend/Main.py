import flask
import joblib
import numpy as np
import pandas as pd

app = flask.Flask(__name__, template_folder='templates')
data = pd.read_csv('../frontend/public/stockdata/full_combined_quarterly_reports.csv', header=0, delimiter=',')
data_reduced = data[['ticker', 'market_cap_category']]
data_unique_tickers = data_reduced.drop_duplicates(subset=['ticker'])
data_unique_tickers.reset_index(drop=True, inplace=True)

svm_models = {
    'Small-cap': joblib.load('../frontend/public/stockdata/models/Small-cap-best_svm_model.pkl'),
    'Mid-cap': joblib.load('../frontend/public/stockdata/models/Mid-cap-best_svm_model.pkl'),
    'Large-cap': joblib.load('../frontend/public/stockdata/models/Large-cap-best_svm_model.pkl'),    
    'Mega-cap': joblib.load('../frontend/public/stockdata/models/Mega-cap-best_svm_model.pkl'),    
    'Micro-cap': joblib.load('../frontend/public/stockdata/models/Micro-cap-best_svm_model.pkl')
}

def preprocess_input(data):
    ticker = data[-1]
    data_array = np.array(data[:-1], dtype=float)
    return ticker, data_array

@app.route('/model', methods=['POST'])
def main():
    if flask.request.method == 'POST':
        json_data = flask.request.get_json(force=True)     
        ticker, input_data = preprocess_input(json_data)
        ticker_data = data_unique_tickers[data_unique_tickers['ticker'] == ticker]
        model = ticker_data.iloc[0]['market_cap_category']

        input_data = input_data.reshape(1, -1)
        prediction = svm_models[model].predict(input_data)
        prediction_str = str(prediction[0])
        return flask.jsonify({"prediction": prediction_str})
    else:
        return "Only POST requests are allowed"

if __name__ == '__main__':
    app.run()
