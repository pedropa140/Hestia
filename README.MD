Read Me

Hello

There are a few things left to finish for this project

1) UI for the dividend data
2) UI for the company financial data
3) SVM data

tickers_with_dividends.csv has all the tickers that I support with the ticker symbol and name page 1,2,3 will need a dropdown or search bar to complete to select a ticker.
int he div_info folder a dividend's information will be present. This contains the dividend info and the company financial info in a csv format. the fields are as follows :

Dividend Info:
company_name,ticker,start_date,end_date,dividend_yield_ratio,start_open,start_close,start_high,end_open,end_close,end_high


Dividend Info:
For dividend data we just need to plot the dividend yield ratio as well as the prices over the past 2 years. The pages should have graphs that update when the ticker changes.


Company Financial Info:
company_name,ticker,start_date,end_date,book_value,book_to_share_value,earnings_per_share,debt_ratio,current_ratio, start_open,start_close,start_high,end_open,end_close,end_high

Company Financial Info:
Should have a graph tracking all the ratios (book_to_share_value,earnings_per_share,debt_ratio, current_ratio)