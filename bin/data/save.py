'''
Saves structure and data to the /bin/data.pkl file.

@author: Dmitry Loktevich
'''

import pickle

def save_calendar(calendar):   
    with open("data.pkl", "wb") as f:
        pickle.dump(calendar, f)   
    f.close()
    