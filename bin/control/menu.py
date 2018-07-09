'''
This module generates main menu options and messages.

@author: Dmitry Loktevich
'''

import datetime
from bin.view.menu import create_menu

def main_menu(calendar):
    today_str = datetime.datetime.today().strftime("%d.%m.%Y")
    
    # datetime.date object
    today = datetime.datetime.strptime(today_str, "%d.%m.%Y").date()
    print("-------------------")
    print("Today is %s" % today.strftime("%d.%m.%Y"))
    
    menu_options = [
        'E', # [E]  View events for today
        'V', # [V]  View calendar
        'A', # [A]  Add a new event
        'X'  # [X]  Exit the program
        ]
    
    # check if we need option [V]
    if len(calendar) == 0:
        print("Your calendar is empty. Please add events.")
        menu_options.remove('V')
    
    # check if we need option [E]
    event_count = 0
    for date in calendar.keys():
        if (date == today):
            event_count = len(calendar[date])
    if event_count == 1:
        print("You have 1 event today")
    elif event_count > 1:
        print("You have %d events today" % event_count)
    else:
        menu_options.remove('E')       
    
    # creating menu options
    create_menu(menu_options) 