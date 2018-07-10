'''
This module repairs program if you modified or delete data.pkl - just run this script separately.
Don't run if all is OK - it erase you data!

@author: Dmitry Loktevich
'''

import pickle
from time import sleep

if __name__ == "__main__":
    from load import load_calendar
    from save import save_calendar
    print("This script will repair you data.pkl file.")
    sleep(0.5)
    print("Analyzing...")
    sleep(0.5)
    try:
        load_calendar("data.pkl")
        user_choice = input("\nYou have active calendar.\n\
Are you sure to create new and erase all data? Y / N: ")
        
        # check user choice
        is_exit = False
        while not is_exit:
            user_choice = user_choice.upper()
            if user_choice == "Y":
                
                # create empty calendar (this erase all existed data)
                save_calendar({}, "data.pkl")
                print("Creating empty calendar...\n")
                sleep(0.5)
                print("New calendar is ready. All previous data is lost. Goodbye.")
                is_exit = True
                
                # exit script
            elif user_choice == "N":
                print("\nGoodbye.")
                is_exit = True
                
            else:
                user_choice = input("Choose the option. Y / N: ")
                
    # if loading is fail            
    except pickle.UnpicklingError:
        
        # repair data.pkl file
        print("Repairing...\n")
        sleep(0.5)
        save_calendar({}, "data.pkl")
        print("Data file was repaired successfully. Goodbye.")
