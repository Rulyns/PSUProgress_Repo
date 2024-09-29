# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
        >>> rectangle(25, 25)
        False
        >>> rectangle(20, 25)
        5
    """
    #- YOUR CODE STARTS HERE
    # P = 2(w+h) is meant to give you the largest possible sides starting with w = 1 and h being an arbetrary number you iterate through.
    # If you start at 1 for h, you would be able to iterate through all possible values before getting to the most valid answers, but since area is also involved, 
    # this change must be in a sort of "stretchy" manner, meaning as you iterate through w, you also want to subtract from h, and so forth.
    # In other words, you want to start with w at 1, and h at A, this will give you the shortest side at w possible and the longest side of h possible,
    # then you iterate until both w and h multiply to A. Your "check" or while loop in a good case is if P = 2(w+h) AND A = wh, if both are true you have found your answer,
    # and hopefully the longest side.

    # int type conversion
    # 
    # Veriable dump
    w = 1
    h = int(area)
    # loop that checks both to be true
    while not (w*h == area and 2*(w+h) == perimeter):
        if float.is_integer(area/(w+1)): # makes sure to see if the next possible rectangle doesnt have a side with decimals.
            w+=1
            h = (area/w)
        elif (w > h): # if w is ever larger than h, that means that all possible sides were already tested. You only need to test sides until the "halfway point", where the rectangle looks most like a square with equal sides.
            return False
        else:
            w+=1
        # print(h)
        # print(w)
    if (w*h == area and 2*(w+h) == perimeter): # Once loop is done it simply makes sure that everything is in integer form and that h is returned
        h = int(h)
        h //= 1
        return h
    pass


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    # simple code, You initialize OUTSIDE the loop, I was stuck on that part I kept saying x = 0 within the loop.
    sum = 0
    x = 0 
    while oct_num > 0:
        sum += ((8**x)*(oct_num%(10))) # Equation on instructions but in code, uses some modulus to grab remainders from octnum at the 1's place.
        x+=1 # increase x by 1 for the next iteration
        oct_num //= 10 # divides and FLOORS the number you are iterating by 10. Flooring is important, if you dont floor you get yucky floating point nums.
    return sum




def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE
    absofnum = abs(num) #make sure all nums are just positive (is this part of math module??)
    # Same iter as previous method with X and allat, no sum this time.
    if (absofnum // 100 == 0):
        return False
    else:
        while absofnum > 0:
            index = absofnum % 10 # takes first number
            absofnum //= 10 # removes that first number
            if ((absofnum % 100) // 10) == index: # Lets say you have 726585, You removed 5 to be the index so you have 72658, you only want the "5" after the 8, so you modulo for 100, gives you 58, then you floor by 10, to get 5, and check.
                return True
        return False
    pass


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    # This looks like a tough one, but literally loop through both and simplify all of them, then just relate them to one another.
    x = 1
    mod_factor = 10**(x+1)
    div_factor = 10**x
    fnum_1 = 0 # formatted num1 placeholder
    fnum_2 = 0 # formatted num2 placeholder
    index_1 = (num_1 % 10) // 1
    while num_1 > 0:
        if (num_1 % mod_factor) // div_factor == index_1:
            print(f"{num_1}'s has a duplicate num, so {num_1 // div_factor} is being rendered.")
            num_1 //= div_factor # moves the number down without adding to new format
        else:
            print(f"{num_1} removed {index_1} and placed it into {fnum_1}")
            index_1 = (num_1 % mod_factor) // div_factor # next index
            fnum_1 += (index_1 * div_factor) # moves that new index to its decimal factor of 10 within format
        x += 1
    print(fnum_1)
    # while num_2 > 0:
    



    # while num_1 > 0 and num_2 > 0:
    #     if (num_1 % 10 == num_2 % 10):
    #         num_1i = num_1 % 10
    #         num_2i = num_2 % 10
    #         num_1 //= 10
    #         num_2 //= 10
    #     elif (num_1 % 10 == num_1i):
    #         num_1 //= 10
    #     elif(num_2%10 == num_2i):
    #         num_2 //= 10
    pass


def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    hailrock = []
    hailrock.append(num) # adds the num before even doing any operation on the num
    if num == 1:
        return hailrock # first or last num should've been 1 if this is triggered
    else:
        while num != 1:
            if (num % 2 == 0): # even case
                hailrock.append(num//2)
                num //= 2
            else: # odd case
                hailrock.append((3*num)+1)
                num = (3*num +1)
        return hailrock  # remember to be outside the loop
    pass



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True # <-- Whats the True for?
    """
    #- YOUR CODE STARTS HERE
    # list append is allowed (Nice!), If its just a single value, make a list and add both the old and new values to this list, If its already a list, concat to the list the new value.
    d = dict(d)
    if(isinstance(d.get(key), list)):
        if not isinstance(value, list):
            d.get(key) + [value]
        else:
            d.get(key) + value
    else:
        if not isinstance(value, list):
            list(d.get(key)) + [value]
        else:
            list(d.get(key)) + value
    pass


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    # I dont know if I'll have time to code this, But I would run through every employee Id, check their department, and concatenate this information into a new department dict based on all other information, I would also list.append() any employee's in the same department.
    # then I would reconstruct the dict (make a new one because of how immutability works)
    d = dict(d)
    newd = {}
    pass


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    # --- YOU CODE STARTS HERE




def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    pass



def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE



def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    pass




def run_tests():
    import doctest
    # Run start tests in all docstrings
    # doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    # doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()
    by_department({1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},  2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},   3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},   4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},   5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}})