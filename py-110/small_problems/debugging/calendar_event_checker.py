"""
We have a list of events and want to check whether a specific date is available (i.e., no events planned for that date). 
However, the function always returns the wrong value.

We're quite literally doing the opposite of what we intend to. When we use the in keywords with dictionaries, we are correctly
checking whether the parameter date is within the keys of the events dictionary, however, we're looking for dates that aren't
actually in the dictionary today, as that means that there are no events planned for that date. 

A simple fix would be to use the 'not in' keyword instead.

"""

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date not in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True