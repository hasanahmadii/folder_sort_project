# added the required libraries to the program
import os
import warnings
import yaml
import argparse

# I had a problem using Khayyam's library and it gives us an error because of this
# We used the Warning book to prevent this error

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
    from khayyam import JalaliDatetime
from datetime import datetime

# In this section, we have two values that I use in all functions
# We have defined the global face so that everyone can access it freely

global extension
global list_directory
global data
extension = set()

# In this part, we used the Yaml file, which is like Jason, for better naming
# For this reason, we read the folders that we create in the open file and inside a variable in the form of a partition
# We saved it to use when creating the folder

with open('/home/eugene/Desktop/Project_sort_folder/codes/dataconfig.yaml', 'r') as f:
    global data
    data = yaml.load(f, Loader=yaml.loader.SafeLoader)


def sorted_list(list1):
    """
  In this study, we have three main reasons that we do not want to spread and transfer
    We delete from the main list
  :param list1:
  :return:
  """
    list_de = set(list1)
    list_de.discard('main.py')
    list_de.discard('run.sh')
    list_de.discard('dataconfig.yaml')
    list1 = list(list_de)
    return list1


def get_list(list1):
    """
    In this case, we use the list we made earlier and
    We separate the extension of the files that we have to create the desired folder based on the Open
    and make the transfer
    :param list1:
    :return:
    """
    for ext in list1:
        if not os.path.isdir(ext) and not ext.startswith('.') and not len(ext.split('.')) == 1:
            res = ext.split('.')
            extension.add(res[-1])
    return extension


def get_folder(ext, address):
    """
    In this function, we create our own folders based on the Yaml file and the extensions we extracted in the previous function.
    We do this based on the date of the day
    :param ext:
    :param addres:
    :return:
    """
    date = JalaliDatetime(datetime.now()).strftime('%A%d%B')
    dir_fo = address + '/' + date + '/'
    for item in data:
        temp = data[item]
        for index in ext:
            if not os.path.isdir(dir_fo + item):
                if index in temp:
                    try:
                        os.makedirs(dir_fo + item)
                    except:
                        continue


def get_move(addres):
    """
    In this function, we will create the files based on the extension and folders that we have already created for them
    You make the transfer
    :param addres:
    :return:
    """
    date = JalaliDatetime(datetime.now()).strftime('%A%d%B')
    dir_fo = addres + '/' + date + '/'
    for item in data:
        temp = data[item]
        for i in list_directory:
            if not os.path.isdir(i) and not i.startswith('.') and not len(i.split('.')) == 1:
                res = i.split('.')
                exten = res[-1]
                if exten in temp:
                    try:
                        os.rename(addres + '/' + i, dir_fo + item + '/' + i)
                    except Exception as e:
                        print(e)


def get_move_folder(address):
    """
    In this function, we have a series of folders, except the main folder, which we have to transfer as well
    For this, we make the list once again and do the transfer again
    :param address:
    :return:
    """
    date = JalaliDatetime(datetime.now()).strftime('%A%d%B')
    dir_fo = address + '/' + date + '/'
    list_folder = os.listdir(address)
    for ext in list_folder:
        if os.path.isdir(ext) or len(ext.split('.')) == 1:
            if not (ext == date):
                os.rename(address + '/' + ext, dir_fo + "/" + ext)




if __name__ == "__main__":
    """
    In this part, we will come and cut a certain amount from the side, which is possible in every part 
    If it is executed, we receive it and pass that amount of address to the parts and functions that need it"""
    arg = argparse.ArgumentParser()
    arg.add_argument('A', help="for the address")
    parser = arg.parse_args()
    address = parser.A
    list_directory = os.listdir(address)
    list_directory = sorted_list(list_directory)
    result = get_list(list_directory)
    get_folder(result, address)
    get_move(address)
    get_move_folder(address)
