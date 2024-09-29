# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -
    pass
    charlist = [chars for chars in txt.lower()]
    chardict = {}
    chardict.update()
    # turning list into dictionary with value of 0
    for frequent in charlist:
        if frequent.isalpha():
            chardict.update({frequent: 0})
    # counting using the starting list and values, this was annoyingly hard, but hey it happens.
    for x in charlist:
        val = chardict.get(x)
        if val.__class__ == int:
            chardict.update({x : (val + 1)})
    return chardict

print("Newchange")


def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    pass
    # example: 
    # inv_d = {} inverted dict
    # for key in d: 
    #              value = d[key] value at index, no matter if its string or int.
    #                   if value in inv_d:  if value is in the inverted version, things that must be removed due to having multiple keys
    #                       must_remove.append(value)    
    #                   else:        
    #                       inv_d[value] = key 
    #                       for key in must_remove:    
    #                   del inv_d[key]
    #                   return inv_d
    # Not my own work, given to me by Dr. Kambhampaty
    d = dict(d)
    invertedict = {}
    removelist = list()
    for key in d:
        invertedict.update({d.get(key): key})
    for key in d: 
        value = d[key] 
        if value in invertedict:  
            removelist.append(value)    
        else:        
            invertedict[value] = key 
            for key in removelist:    
                del invertedict[key]
    return invertedict
# Tired, will retry tommorow.





def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """ 
    # - YOUR CODE STARTS HERE -
    pass
    # Reminder, No new employee's are being added to this dictionary, because that would require us to know their starting salary.
    # Strategy : Establish current years and year to be added, probably using the update method, your values are dicts within the main dict.
    # Variable establishment : d = maindict, d.keys() = years, for x in d.keys is an iretable of every year, d.get(x) is the dict for that specific year, and d.get(x).keys() should be the names of all the employee's
    # Finally, the tuple we deal with is d.get(x).get(y) (this requires a nested for loop, but in reality, we only need the most recent year, which can be found by sorting the main list in descending order rather than ascending order)
    # EXAMPLE:
    # d = dict(d)
    # year = int(year)
    # print(d, " maindict")
    # print(d.keys(), " years")
    # for x in d.keys():
    #     print(x, " year") #years
    #     print(d.get(x), " list for year") # full list of names and info, (the second dict)
    #     print(d.get(x).keys(), " names") # just the names
    #     for y in d.get(x).keys():
    #         print(d.get(x).get(y)) # just the info
    # Also, since its a tuple, and tuples are immutable, we have to change it into a to change it.
    # Paste and try to see info more clearly.
    # !!! TL - DR !!! just all the variables and what they should mean.
    d = dict(d)
    year = int(year)
    years = d.keys() # start from highest year with pop
    pastyear = list(years).pop()
    pastdict = d.get(pastyear) # dict of current year, also get so that no errors arise.
    # the problem with copying dictionaries is due to its mutable nature, any copies are shallow and will save across different dicts if not taken care of.
    #deepcopy 
    import copy
    copydict = copy.deepcopy(pastdict)
    templst = tuple(pastdict.values()) # turns it into a list to give raise
    for y in templst:
        y[2] += bonus # salary
    d.update({year : pastdict})
    d.update({pastyear: copydict}) #readd the year used to avoid both dictionaries getting changed.
    return d

def run_tests():
    import doctest

    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    # you have to its good to explain you dont need to do all this im just autistic.
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace frequency with the name of the function you want to test
    # doctest.run_docstring_examples(invert, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()

