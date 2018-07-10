'''
This module saves structure and data to the /bin/data.pkl file.

@author: Dmitry Loktevich
'''

import pickle

def save_calendar(calendar, data_path = "data\data.pkl"):
    with open(data_path, "wb") as f:
        pickle.dump(calendar, f)   
    f.close()
    