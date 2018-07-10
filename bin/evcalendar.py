'''
Start module for program.

@author: Dmitry Loktevich
'''

import pickle
from control.logic import start

try:
    start()

# if loading is fail    
except pickle.UnpicklingError:
    print("Sorry =(\n\
You data file was modified or deleted.\n\
\n\
Please run data\repair.py script")
    