import os

def check_folder(directory):
    folder_path = os.path.join(directory)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False

def read_div():
    directory = './stockdata/div_info/'
    
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

if __name__ == '__main__':
    print(read_div())