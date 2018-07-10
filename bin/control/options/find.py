'''
This module searches for events on entered date.

@author: Dmitry Loktevich
'''

from control.options.show import show_events
from control.validator import validate_date

def find_event(calendar):
    print("Finding the events:")
    
    # check if date is valid
    date = validate_date()
    
    # check if there is a key == date
    if date in calendar.keys():
        show_events(calendar[date], date)
        find_date = [date, True]
    else:
        print("There is no events on %s" % date.strftime("%d.%m.%Y"))
        find_date = [date, False]
        
    return find_date