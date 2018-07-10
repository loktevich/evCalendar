'''
This module saves structure and data to the /bin/data.pkl file.
Repair program if you modified or delete data.pkl - just run this script separately.
Don't run if all is OK - it erase you data!

@author: Dmitry Loktevich
'''

import pickle
from time import sleep

def save_calendar(calendar, data_path = "data\data.pkl"):
    with open(data_path, "wb") as f:
        pickle.dump(calendar, f)   
    f.close()
    
# when running separately it create empty calendar
if __name__ == "__main__":
    from load import load_calendar
    print("This script will repair you data.pkl file.")
    sleep(1)
    print("Analyzing...")
    sleep(1)
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
                sleep(1)
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
        sleep(1)
        save_calendar({}, "data.pkl")
        print("Program was repaired successfully. Goodbye.")
