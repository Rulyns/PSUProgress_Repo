def frequency(txt):
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
def invert(d):
    d = dict(d)
    invertd = {}
    vals = list(d.values())
    vals.sort()
    print(len(vals))
    x = 1
    while x in range(1,len(vals)):
        print(vals)
        print("currently at x: ", x)
        if vals[x-1] == vals[x]:
            print(vals[x], 'removed twice')
            vals.pop(x)
            vals.pop(x-1)
            x -= 1
        else:
            print('Afterward: ', vals)
        x += 1
    print(d)
    for x in d:
        if d.get(x) in vals:
            print(d.get(x))
            print(list(d.keys()))
            invertd = invertd.fromkeys(vals, d.get(x))
    return invertd

           

                



    
    



# dis = {"a": 2, "a": 6, "b": 4, "b": 5, "c": 5,"a": 2, "a": 6, "b": 4, "b": 5, "g": 5, "f" : 7} 
# newlis = {}

# print(dis.values())
# print(dis.keys())
# for x in dis.values():
#     if x1 == x:
#         dis.popitem()
#     x1 = x
# for x in dis.keys():
#     newlis.update({dis.get(x): x})

# def invert(d):
#     """
#         >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
#         {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#         >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
#         {3: 'three'}
#         >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
#         {'Sara': '123-456-78', 'sara': '258715'}
#     """
#     # - YOUR CODE STARTS HERE -
    # d = dict(d)
    #  #flip the dictionary by using a new dictionary
    # flipped = {}
    # for value in list(d.values()):
    #     print(value)
    # print(flipped)
    # pass
    
        
    
def employee_update(d, bonus, year):
    d = dict(d)
    year = int(year)
    years = d.keys() # start from highest year with pop
    pastyear = list(years).pop() # returns and removes highest year(?)
    pastdict = d[pastyear] # dict of current year
    import copy
    copydict = copy.deepcopy(pastdict)
    # print(id(pastdict))
    # print(id(copydict)) (to check the memory location of the dicts)
    templst = tuple(pastdict.values()) # turns it into a list to give raise
    for y in templst:
        y[2] += bonus
    d.update({year: pastdict})
    d.update({pastyear: copydict}) #readd the year used to avoid both dictionaries getting changed.
    return d
        
    



records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
print(invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3, "quatro":4, "tres": 3}))
