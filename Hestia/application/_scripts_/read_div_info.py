import os

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
                    info_list.append(line[-15:])
    return info_list

def ticker_with_div():
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_dir, '../../stockdata/tickers_with_dividends.csv')

    result = {}
    with open(directory, "r") as file:
        info_file = file.readlines()
        for info in info_file:
            info = info.replace("\"", "").replace("\n", "").split(',')
            if info[0] not in result:
                result[info[0]] = "".join(info[1:])
    return result


# if __name__ == '__main__':
#     print(ticker_with_div())