'''
Loads structure and data from the /bin/data.pkl file.

@author: Dmitry Loktevich
'''

import pickle

def load_calendar():  
    with open("data.pkl", "rb") as f:
        calendar = pickle.load(f)
    f.close()    
    return calendar