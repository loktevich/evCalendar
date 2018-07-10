'''
This module updates existing events in the calendar.

@author: Dmitry Loktevich
'''

from control.options.show import show_events
from control.validator import validate_date, validate_ind, validate_key
from data.save import save_calendar

def update_event(calendar, date):
    print("Updating the existing event:")
    if date is None:
        
        # prompt to enter the date and check if it is valid
        date = validate_date()
            
        # check if there is entries on entered date and return them     
        events = validate_key(calendar, date)
        show_events(events, date)
        
    else:
        print("  Date:  %s" % date.strftime("%d.%m.%Y"))
        events = calendar[date]   
    
    ind = 1
    if len(events) > 1:    
        
        # prompt to enter the number and check if it is valid
        ind = validate_ind(len(events))
                    
    event = input("  Event: ")        
    calendar[date][ind - 1] = event
    
    save_calendar(calendar)
    print("The event was successfully updated.")
    return calendar