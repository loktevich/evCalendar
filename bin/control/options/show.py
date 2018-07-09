'''
This module has functions to show data in table form.

@author: Dmitry Loktevich
'''

def show_events(events, date):
    print()
    print("-------------------")
    print("Events for %s:" % date.strftime("%d.%m.%Y"))
    ind = 1
    for event in events:
        print("  %02d   %s" % (ind, event))
        ind += 1
    print("-------------------")
    
def show_calendar(calendar):
    print()
    print("-------------------")
    print("All events:")
    
    sorted_dates = []
    ind = 1
    for calendar_date in calendar.keys():
        sorted_dates.append(calendar_date)
    sorted_dates.sort()    
    for date in sorted_dates:
        for event in calendar[date]:
            print("  %02d   %s   %s" % (ind, date.strftime("%d.%m.%Y"), event))
            ind += 1
    print("-------------------")