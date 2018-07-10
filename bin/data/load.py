'''
This module loads structure and data from the /bin/data.pkl file.

@author: Dmitry Loktevich
'''

import pickle

def load_calendar(data_path = "data\data.pkl"):  
    with open(data_path, "rb") as f:
        calendar = pickle.load(f)
    f.close()    
    return calendar