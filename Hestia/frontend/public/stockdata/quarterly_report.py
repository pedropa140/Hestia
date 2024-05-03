import pandas as pd
import numpy as np 

class QuarterlyReport:
    def __init__(self, data):
        self.id = data['id']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.ticker = data['tickers'][0]
        self.company_name = data['company_name'].lower()
        self.financials = data['financials']
        self.income_statement = data['financials'].get('income_statement', {})
        self.balance_sheet = data['financials'].get('balance_sheet', {})
        self.cash_flow_statement = data['financials'].get('cash_flow_statement', {})
        self.comprehensive_income = data['financials'].get('comprehensive_income', {})

    def set_start_prices(self, openS, highS, lowS, closeS):
        self.s_open = openS
        self.s_close = closeS
        self.s_low = lowS
        self.s_high = highS

    def set_end_prices(self, openE, highE, lowE, closeE):
        self.e_open = openE
        self.e_close = closeE
        self.e_low = lowE
        self.e_high = highE

    def safe_get_value(self, key_chain):
        try:
            value = self.financials
            for key in key_chain:
                value = value[key]
            return value['value']
        except (KeyError, TypeError):
            return np.nan

    def calculate_book_value(self):
        total_assets = self.safe_get_value(['balance_sheet', 'assets'])
        total_liabilities = self.safe_get_value(['balance_sheet', 'liabilities'])
        if np.isnan(total_assets) or np.isnan(total_liabilities):
            return np.nan
        return total_assets - total_liabilities

    def calculate_book_to_share_value(self):
        book_value = self.calculate_book_value()
        basic_shares = self.safe_get_value(['income_statement', 'basic_average_shares'])
        if np.isnan(book_value) or np.isnan(basic_shares) or basic_shares == 0:
            return np.nan
        return book_value / basic_shares

    def calculate_earnings_per_share(self):
        net_income = self.safe_get_value(['income_statement', 'net_income_loss_available_to_common_stockholders_basic'])
        basic_shares = self.safe_get_value(['income_statement', 'basic_average_shares'])
        if np.isnan(net_income) or np.isnan(basic_shares) or basic_shares == 0:
            return np.nan
        return net_income / basic_shares

    def calculate_price_to_earnings_ratio(self, market_price_per_share):
        earnings_per_share = self.calculate_earnings_per_share()
        if np.isnan(earnings_per_share) or market_price_per_share == 0:
            return np.nan
        return market_price_per_share / earnings_per_share

    def calculate_debt_ratio(self):
        total_debt = self.safe_get_value(['balance_sheet', 'liabilities'])
        total_assets = self.safe_get_value(['balance_sheet', 'assets'])
        if np.isnan(total_debt) or np.isnan(total_assets) or total_assets == 0:
            return np.nan
        return total_debt / total_assets

    def calculate_current_ratio(self):
        current_assets = self.safe_get_value(['balance_sheet', 'current_assets'])
        current_liabilities = self.safe_get_value(['balance_sheet', 'current_liabilities'])
        if np.isnan(current_assets) or np.isnan(current_liabilities) or current_liabilities == 0:
            return np.nan
        return current_assets / current_liabilities

    def calculate_dividend_yield_ratio(self, market_price_per_share):
        annual_dividends = self.safe_get_value(['cash_flow_statement', 'net_cash_flow_from_financing_activities'])
        basic_shares = self.safe_get_value(['income_statement', 'basic_average_shares'])
        if np.isnan(annual_dividends) or np.isnan(basic_shares) or basic_shares == 0 or market_price_per_share == 0:
            self.dividend_yield_ratio = np.nan
        else: 
            annual_dividends_per_share = annual_dividends / basic_shares
            self.dividend_yield_ratio = annual_dividends_per_share / market_price_per_share

       	

    def get_df(self):
        book_value = self.calculate_book_value()
        book_to_share_value = self.calculate_book_to_share_value()
        earnings_per_share = self.calculate_earnings_per_share()
        debt_ratio = self.calculate_debt_ratio()
        current_ratio = self.calculate_current_ratio()

        data = {
            'company_name': [self.company_name],
            'ticker': [self.ticker],
            'start_date': [self.start_date],
            'end_date': [self.end_date],
            'book_value': [book_value],
            'book_to_share_value': [book_to_share_value],
            'earnings_per_share': [earnings_per_share],
            'debt_ratio': [debt_ratio],
            'current_ratio': [current_ratio],
            'dividend_yield_ratio': [self.dividend_yield_ratio],
            'start_open': [self.s_open],
            'start_close': [self.s_close],
            'start_high': [self.s_high],
            'start_close': [self.s_close],
            'end_open': [self.e_open],
            'end_close': [self.e_close],
            'end_high': [self.e_high],
            'end_close': [self.e_close]

        }

        return pd.DataFrame(data)