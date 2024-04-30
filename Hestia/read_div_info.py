import os
import csv

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


if __name__ == '__main__':
    # print(ticker_with_div())
    ticker = ticker_with_div()
    div = read_div()
    differences = {}
    for d in div:
        oof = d[-15:]
        if oof[0] not in ticker and oof[0] not in differences:
            # differences.append(d[0])
            differences[oof[0]] = d[:-15]
    print(differences)
    print(len(differences))
    
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    # directory = os.path.join(current_dir, './stockdata/tickers_with_dividends.csv')
    # with open(directory, 'a') as file:
    #     for d in differences:
    #         writer = csv.writer(file)
    #         writer.writerow([d[0], d[1:]])
    def capitalize_words(s):
    # Split the string into words
        words = s.split()

        # Capitalize the first letter of each word
        capitalized_words = [word.capitalize() for word in words]

        # Join the capitalized words back into a single string
        return ' '.join(capitalized_words)
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, './stockdata/tickers_with_dividends.csv')
    with open(directory, 'a', newline='') as file:
        for d in differences:
            string = "".join(differences[d])
            writer = csv.writer(file)
            writer.writerow([d, capitalize_words(string)])