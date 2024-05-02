Read Me

Hello

## How to run
*Make sure your `venv` has not been created*
1. Global install necessary packages 
   `pip install Django django-cors-headers`
   `pip install -U scikit-learn`
2. Create your `.venv` environment through the VSCode interface or terminal.
3. Install all requirements from `requirements.txt`.

### Setup Backend

4. Navigate to the `application` directory from the current root.
5. Setup database/backend with `py manage.py setup_db` following any necessary instructions.
6. Start the development server with `py manage.py runserver`.

### Setup Frontend

7. Navigate to the `frontend` directory.
8. Install any necessary packages using `npm install`.
9. Run frontend with `npm start`.

## Context

A "ticker" is a unique symbol or abbreviation used to identify a publicly traded company's stock on a stock exchange. Each publicly traded company is assigned a specific ticker symbol, which is used to easily reference and trade that company's stock.

## Tasks

1. **UI for the Dividend Data**
   - Create a user interface (UI) to display dividend data for supported stock tickers.
   - The dividend data is stored in CSV files within the `div_info` folder.
   - The UI should have a dropdown or search bar functionality to allow users to select a specific stock ticker.
   - The UI should display graphs plotting the following data for the selected ticker:
     - Dividend yield ratio
     - Stock prices (open, close, high) for the past 2 years
   - The graphs should update dynamically when the selected ticker is changed.

2. **UI for the Company Financial Data**
   - Create a UI to display company financial data for supported stock tickers.
   - The company financial data is stored in CSV files within the `div_info` folder.
   - The UI should have a dropdown or search bar functionality to allow users to select a specific stock ticker.
   - The UI should display a graph tracking the following financial ratios for the selected ticker:
     - Book value to share value
     - Earnings per share
     - Debt ratio
     - Current ratio

3. **SVM Data**
   - Work with Support Vector Machine (SVM) data, which is a type of machine learning model.
   - The nature of the task is not entirely clear from the provided information. More context or clarification regarding the specific requirements for this task is needed.

## Data Sources

1. `tickers_with_dividends.csv`
   - Contains a list of supported stock tickers and company names.

2. CSV files in the `div_info` folder
   - Contains dividend information and company financial data for each supported stock ticker.

### Dividend Info CSV Fields
- `company_name`
- `ticker`
- `start_date`
- `end_date`
- `dividend_yield_ratio`
- `start_open`
- `start_close`
- `start_high`
- `end_open`
- `end_close`
- `end_high`

### Company Financial Info CSV Fields
- `company_name`
- `ticker`
- `start_date`
- `end_date`
- `book_value`
- `book_to_share_value`
- `earnings_per_share`
- `debt_ratio`
- `current_ratio`
- `start_open`
- `start_close`
- `start_high`
- `end_open`
- `end_close`
- `end_high`

tickers_with_dividends.csv has all the tickers that I support with the ticker symbol and name page 1,2,3 will need a dropdown or search bar to complete to select a ticker. int he div_info folder a dividend's information will be present. This contains the dividend info and the company financial info in a csv format. the fields are as follows :

Dividend Info: company_name,ticker,start_date,end_date,dividend_yield_ratio,start_open,start_close,start_high,end_open,end_close,end_high

Dividend Info: For dividend data we just need to plot the dividend yield ratio as well as the prices over the past 2 years. The pages should have graphs that update when the ticker changes.

Company Financial Info: company_name,ticker,start_date,end_date,book_value,book_to_share_value,earnings_per_share,debt_ratio,current_ratio, start_open,start_close,start_high,end_open,end_close,end_high

Company Financial Info: Should have a graph tracking all the ratios (book_to_share_value,earnings_per_share,debt_ratio, current_ratio)
