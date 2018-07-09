'''
Generates program menu depending on selected options.

@author: Dmitry Loktevich
'''

def create_menu(options):
    menu_options = []
    for option in options:
        if option == 'E':
            menu_options.append("  [ E ]  View events for today")
        if option == 'V':
            menu_options.append("  [ V ]  View calendar")
        if option == 'A':
            menu_options.append("  [ A ]  Add a new event")
        if option == 'U':
            menu_options.append("  [ U ]  Update existing event")
        if option == 'D':
            menu_options.append("  [ D ]  Delete the event")
        if option == 'F':
            menu_options.append("  [ F ]  Find event(s) by date")    
        if option == 'R':
            menu_options.append("  [ R ]  Return to main menu")        
        if option == 'X':
            menu_options.append("  [ X ]  Exit the program")
    for option in menu_options:
        print(option)