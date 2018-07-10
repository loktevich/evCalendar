'''
This module adds events to the calendar.

@author: Dmitry Loktevich
'''

from control.validator import validate_date
from data.save import save_calendar

def add_event(calendar, date):
    print("Adding new event:")
    if date is None:
        
        # prompt to enter the date and check if it is valid
        date = validate_date()    
        
        event = input("  Event: ")
        
        # adding to existed or new entry (date)
        if date in calendar.keys():    
            calendar[date].append(event)
        else:
            events = []
            events.append(event)
            calendar[date] = events
    
    # adding to existed entry (date)      
    else:
        print("  Date:  %s" % date.strftime("%d.%m.%Y"))    
        event = input("  Event: ")       
        calendar[date].append(event)
        
    save_calendar(calendar)   
    print("New event was successfully added.")
    return calendar
    