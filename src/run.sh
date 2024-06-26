
# In this part
# we will find the address of the location where this script is executed and deliver it to our Python file.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
set -e

# From this part, we enter this folder because the script we want is located there

cd /home/eugene/Documents/folder_sort_project/src/

# We turn on our own Python virtual machine

source "/home/eugene/Documents/folder_sort_project/.virenv/bin/activate"

# And finally we run our own Python file

python -u /home/eugene/Documents/folder_sort_project/src/main.py "$DIR"

#Be careful, when the car is turned on, it can only use the libraries installed on the car
