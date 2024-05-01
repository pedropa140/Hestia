# import os

# def check_folder(directory):
#     folder_path = os.path.join(directory)
#     if os.path.exists(folder_path) and os.path.isdir(folder_path):
#         return True
#     else:
#         return False

# def read_div():
#     current_dir = os.path.dirname(os.path.realpath(__file__))
#     directory = os.path.join(current_dir, '../../stockdata/div_info/')

#     info_list = []
#     if check_folder(directory):

#         div_info_files = os.listdir(directory)
#         for filename in div_info_files:
#             with open(directory + filename, 'r') as file:
#             # with open(directory + 'WSFS.csv', 'r') as file:
#                 ignore_line = file.readline()
#                 lines = file.readlines()
#                 for line in lines:
#                     line = line.replace('\n', '').replace('\"', '').split(',')
#                     info_list.append(line[-15:])
#     return info_list

# def ticker_with_div():
#     # Get the current directory where the script is located
#     current_dir = os.path.dirname(os.path.realpath(__file__))
#     directory = os.path.join(current_dir, '../../stockdata/tickers_with_dividends.csv')

#     result = {}
#     with open(directory, "r") as file:
#         info_file = file.readlines()
#         for info in info_file:
#             info = info.replace("\"", "").replace("\n", "").split(',')
#             if info[0] not in result:
#                 result[info[0]] = "".join(info[1:])
#     return result


# # if __name__ == '__main__':
# #     print(ticker_with_div())
import concurrent.futures
import os
import logging
from app.models import CompanyTicker

logging.basicConfig(level=logging.INFO)

def check_folder(directory):
    folder_path = os.path.join(directory)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False

def read_div():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, '../../stockdata/div_info/')
    
    info_list = []
    if check_folder(directory):

        div_info_files = os.listdir(directory)
        for filename in div_info_files:
            with open(directory + filename, 'r') as file:
            # with open(directory + 'WSFS.csv', 'r') as file:
                ignore_line = file.readline()
                lines = file.readlines()
                for line in lines:
                    line = line.replace('\n', '').replace('\"', '').split(',')
                    info_list.append(line)

    return info_list

def process_csv_row(row):
    info = row.replace("\"", "").replace("\n", "").split(',')
    ticker, company_name = info[0], "".join(info[1:])
    ticker=ticker.upper()
    logging.info(f"Processing ticker: {ticker}")
    return CompanyTicker(ticker=ticker, company_name=company_name.strip())

def read_csv_multithreaded():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, '../../stockdata/tickers_with_dividends.csv')
    company_tickers = []

    with open(directory, "r") as file:
        info_file = file.readlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Process each row in parallel using threads
        futures = [executor.submit(process_csv_row, row) for row in info_file]

        # Collect results from threads and append CompanyTicker objects to the list
        for future in concurrent.futures.as_completed(futures):
            company_ticker = future.result()
            company_tickers.append(company_ticker)

    return company_tickers