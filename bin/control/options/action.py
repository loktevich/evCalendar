'''
This module define main actions depending on scenarios.

@author: Dmitry Loktevich
'''

from control.options.add import add_event
from control.options.update import update_event
from control.options.delete import delete_event

def choose_action(user_choice, calendar, date):
    
    # option [A]  Add a new event
    if user_choice == 'A':
        calendar = add_event(calendar, date)
        
    # option [U]  Update existing event
    elif user_choice == 'U':
        calendar = update_event(calendar, date)

    # option [D]  Delete the event
    elif user_choice == 'D':
        calendar = delete_event(calendar, date)

    # option [R]  Return to main menu
    elif user_choice == 'R':
        return calendar
    
    return calendar