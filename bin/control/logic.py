'''
This module contains the main logic and all of scenarios of the program.

@author: Dmitry Loktevich
'''

from control.menu import main_menu
from data.load import load_calendar
from control.options.show import show_events, show_calendar
from view.menu import create_menu
from control.options.find import find_event
from control.options.action import choose_action
from data.save import save_calendar
import datetime

# this function starts the calendar
def start():
         
    calendar = load_calendar()    
    # main_menu messages and options      
    main_menu(calendar)
#    today = strftime("%d.%m.%Y")
    today = datetime.datetime.today().date()
    is_main_menu = True
    
    # main menu
    while is_main_menu:
                
        # prompt user for an option
        user_choice = input("Enter the option: ")
        user_choice = user_choice.upper()
        
        # check entered option
        if user_choice not in ['E', 'V', 'A', 'X']:
            print("Option [%s] is invalid. Try again." % user_choice)
            continue
                             
        # option [E]  View events
        elif user_choice == 'E':
            is_e_option = True 
            events = calendar[today]
            
            # table view of events
            show_events(events, today)
            
            # now we can work with event table
            options = ['A', 'U', 'D', 'R', 'X']
            create_menu(options)
            
            # check inputs and perform actions
            while is_e_option:                
                user_choice = input("Enter the option: ")
                user_choice = user_choice.upper()
                if user_choice not in options:
                    print("Option [%s] is invalid. Try again." % user_choice)
                    continue      
                elif user_choice == 'X':
                    is_main_menu = False
                    break         
                else:
                    main_menu(choose_action(user_choice, calendar, today))
                    
                    # return to main menu
                    is_e_option = False
                    continue
            continue    
        
        # option [V]  View calendar
        elif user_choice == 'V':
            is_v_option = True
            show_calendar(calendar)
            
            # now we can work with all events
            options = ['A', 'U', 'D', 'F', 'X']
            create_menu(options)
            
            # check inputs and perform actions
            while is_v_option:                
                user_choice = input("Enter the option: ")
                user_choice = user_choice.upper()
                if user_choice not in options:
                    print("Option [%s] is invalid. Try again." % user_choice)
                    continue   
                
                # option [F]  Find event(s) by date   
                elif user_choice == 'F':
                    is_f_option = True
                    f_date_result = find_event(calendar)
                    
                    # check if there is no events on date
                    if not f_date_result[1]:
                        continue        
                    else:
                        f_date = f_date_result[0]
                    # now we can work with founded events                    
                    options = ['A', 'U', 'D', 'R', 'X']
                    create_menu(options)
                    
                    # check inputs and perform actions
                    while is_f_option:                
                        user_choice = input("Enter the option: ")
                        user_choice = user_choice.upper()
                        if user_choice not in options:
                            print("Option [%s] is invalid. Try again." % user_choice)
                            continue
                        
                        # option [X] from [F] menu 
                        elif user_choice == 'X':
                            is_v_option = False
                            is_main_menu = False    
                            break         
                        else:
                            main_menu(choose_action(user_choice, calendar, f_date))
                            
                            # return to main menu
                            is_f_option = False
                            is_v_option = False
                    continue    
                 
                # option [X] from [V] menu                        
                elif user_choice == 'X':
                    is_main_menu = False
                    break  
                
                # perform one of [A], [U], [D] action     
                else:
                    main_menu(choose_action(user_choice, calendar, None))
                    
                    # return to main menu
                    is_v_option = False
                    continue
            continue   
                    
        # option [X]  Exit the program
        elif user_choice == 'X':
            is_main_menu = False
        
        #option [A]  Add a new event        
        else:
            main_menu(choose_action(user_choice, calendar, None))   
            continue      
    else:
        save_calendar(calendar)
        print("Program is exit.")    
            