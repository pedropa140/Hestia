import os
import csv
from datetime import datetime, timedelta
import time

def check_folder(directory):
    folder_path = os.path.join(directory)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False

def read_div():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, './stockdata/div_info/')
    
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

def ticker_with_div():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, './stockdata/tickers_with_dividends.csv')
    result = {}
    with open(directory, "r") as file:
        info_file = file.readlines()
        for info in info_file:
            info = info.replace("\"", "").replace("\n", "").split(',')
            if info[0] not in result:
                result[info[0]] = "".join(info[1:])
    return result

def plot_shit(filename):
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    # directory = os.path.join(current_dir, './stockdata/div_info/')
    # df = pd.read_csv(directory + "A.csv")

    # # Group the data by 'company_name'
    # groups = df.groupby('ticker')

    # # Plot each group
    # for name, group in groups:
    #     plt.plot(group['start_date'], group['book_value'], label=name)

    # plt.xlabel('Date')
    # plt.ylabel('Book Value')
    # plt.title(f'{filename.replace('.csv', '')}: Book Value Over Time')
    # plt.legend()
    # plt.xticks(rotation=45)
    # plt.show()

    import pandas as pd
    import matplotlib.pyplot as plt

    # Read the CSV file
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, './stockdata/div_info/')
    df = pd.read_csv(directory + filename)
    df.sort_values(by='start_date', inplace=True)

    # Group the data by 'company_name'
    groups = df.groupby('ticker')

    # Plot each group
    plt.figure()
    for name, group in groups:
        plt.plot(group['start_date'], group['dividend_yield_ratio'], label='dividend_yield_ratio')
    plt.xlabel('Date')
    plt.ylabel('Dividend Yield Ratio')
    plt.title(f'{filename.replace('.csv', '')}: Dividend Yield Ratio Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/dividend_yield_ratio_pictures'
    if not os.path.exists(folder_name):
        
        os.makedirs(folder_name)

    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()
    
    plt.figure()
    two_years_ago = datetime.now() - timedelta(days=2*365)
    # print(two_years_ago)

    # Filter the DataFrame based on 'start_date' two years prior
    time = pd.to_datetime(df['start_date'], format='%Y-%m-%d')
    df_filtered = df[time >= two_years_ago]

    for name, group in df_filtered.groupby('ticker'):
        plt.plot(group['start_date'], group['start_open'], label='start_open')
        plt.plot(group['start_date'], group['start_close'], label='start_close')
        plt.plot(group['start_date'], group['start_high'], label='start_high')
        plt.plot(group['start_date'], group['end_open'], label='end_open')
        plt.plot(group['start_date'], group['end_close'], label='end_close')
        plt.plot(group['start_date'], group['end_high'], label='end_high')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(f'{filename.replace('.csv', '')}: Stock Value Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/stock_prices_pictures'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the plot into the folder
    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()

    plt.figure()
    for name, group in groups:
        plt.plot(group['start_date'], group['book_to_share_value'], label='book_to_share_value')
    plt.xlabel('Date')
    plt.ylabel('Book Value To Share Value')
    plt.title(f'{filename.replace('.csv', '')}: Book Value To Share Value Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/book_value_to_share_value_pictures'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the plot into the folder
    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()

    plt.figure()
    for name, group in groups:
        plt.plot(group['start_date'], group['earnings_per_share'], label='earnings_per_share')
    plt.xlabel('Date')
    plt.ylabel('Earnings Per Share')
    plt.title(f'{filename.replace('.csv', '')}: Earnings Per Share Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/earnings_per_share_pictures'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the plot into the folder
    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()

    plt.figure()
    for name, group in groups:
        plt.plot(group['start_date'], group['debt_ratio'], label='debt_ratio')
    plt.xlabel('Date')
    plt.ylabel('Debt Ratio')
    plt.title(f'{filename.replace('.csv', '')}: Debt Ratio Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/debt_ratio_pictures'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the plot into the folder
    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()

    plt.figure()
    for name, group in groups:
        plt.plot(group['start_date'], group['current_ratio'], label='current_ratio')
    plt.xlabel('Date')
    plt.ylabel('Current Ratio')
    plt.title(f'{filename.replace('.csv', '')}: Current Ratio Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.gcf().set_size_inches(20, 10)

    folder_name = './stockdata/stockpictures/current_ratio_pictures'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the plot into the folder
    plt.savefig(os.path.join(folder_name, f'{filename.replace('.csv', '')}.png'))
    print(f"\033[92mCompleted {os.path.join(folder_name, f'{filename.replace('.csv', '')}.png')}\033[0m")
    plt.close()


if __name__ == '__main__':
    print(f"\033[92mProgram Started\033[0m")
    start_time = time.time()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, './stockdata/div_info/')
    
    info_list = []
    if check_folder(directory):

        div_info_files = os.listdir(directory)
        counter = 1
        for filename in div_info_files:
            check_time = time.time()
            check_elapsed_time = check_time - start_time
            check_hours = int(check_elapsed_time // 3600)
            check_minutes = int((check_elapsed_time % 3600) // 60)
            check_seconds = int(check_elapsed_time % 60)
            hours_str = f"{check_hours:02}"
            minutes_str = f"{check_minutes:02}"
            seconds_str = f"{check_seconds:02}"
            print(f'{counter} out of {len(div_info_files)} - Filename: {filename} \t Time elapsed: {hours_str} hours, {minutes_str} minutes, {seconds_str} seconds')
            plot_shit(filename)
            counter += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    hours_str = f"{hours:02}"
    minutes_str = f"{minutes:02}"
    seconds_str = f"{seconds:02}"

    # Print the elapsed time
    print(f"\033[Time elapsed: {hours_str} hours, {minutes_str} minutes, {seconds_str} seconds\033[0m")
    
            # break
            # break
    # # print(ticker_with_div())
    # ticker = ticker_with_div()
    # div = read_div()
    # differences = {}
    # for d in div:
    #     oof = d[-15:]
    #     if oof[0] not in ticker and oof[0] not in differences:
    #         # differences.append(d[0])
    #         differences[oof[0]] = d[:-15]
    # print(differences)
    # print(len(differences))
    
    # # current_dir = os.path.dirname(os.path.realpath(__file__))
    # # directory = os.path.join(current_dir, './stockdata/tickers_with_dividends.csv')
    # # with open(directory, 'a') as file:
    # #     for d in differences:
    # #         writer = csv.writer(file)
    # #         writer.writerow([d[0], d[1:]])
    # def capitalize_words(s):
    # # Split the string into words
    #     words = s.split()

    #     # Capitalize the first letter of each word
    #     capitalized_words = [word.capitalize() for word in words]

    #     # Join the capitalized words back into a single string
    #     return ' '.join(capitalized_words)
    
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    # directory = os.path.join(current_dir, './stockdata/tickers_with_dividends.csv')
    # with open(directory, 'a', newline='') as file:
    #     for d in differences:
    #         string = "".join(differences[d])
    #         writer = csv.writer(file)
    #         writer.writerow([d, capitalize_words(string)])