'''
This module has functions to check if the input values
(dates and indexes) are valid.

@author: Dmitry Loktevich
'''

import datetime
# import datetime

def validate_date():
    is_valid = False       
    while not is_valid:
        date_str = input("  Date (DD.MM.YYYY): ")    
        try:
            date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
            is_valid = True
        except ValueError:
            print("Date %s is not valid. Try again." % date_str)
            continue
    return date
    
def validate_ind(max_ind):
    is_valid = False
    while not is_valid:
        ind = input("What event (enter the number): ")
        try:
            ind = int(ind)
            if ind <= max_ind:
                is_valid = True
            else:
                print("There are only %d events, not %d. Try again." % (max_ind, ind))
                continue
        except ValueError:
            print("%s is not a number. Try again." % ind)
            continue
    return ind

def validate_key(calendar, date):
    is_valid = False
    while not is_valid:     
        if date in calendar.keys():        
            events = calendar[date]
            is_valid = True            
        else:
            print("There is no events on %s. Try again."\
                  % date.strftime("%d.%m.%Y"))
            date = validate_date()
            continue
    return events