# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables.
# Use recursion, otherwise no credit will be given
# No helper functions allowed!

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    ## YOUR CODE STARTS HERE
    
    if num == 1:                        # Any base to the power of 0 must equal one.
        return True                     # We also assume that 0^0 = 1, although some might argue that it should be left undefined.
    elif (base == 1 and num > base) or (num == 0):
        return False                    # 1 to any power is always 1, so if they give a num > 1 with 1 as the base, its not possible.
                                        # Also checks for any case where num = 0. There is no positive exponent that gives you 0.
    elif num == base:                     # Our "base case"
        return True
    elif num % base == 0:               # all base^exponent pairs should be nicely divisible by their base number.
        return is_power_of(base, (num // base)) # Will check it all the way down to if num ever == 1 or num == base.
    else:
        return False                    # If it fails both statements it isnt a power of it.
    pass                   




def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
	"""
    ## YOUR CODE STARTS HERE
    returnlist = []
    if len(a_list) >= 1: # If list is equal to or greater than 1 ...
        if a_list[0] >= 0:
            returnlist += [a_list[0]] # add any positivw number plus the rest of the list
            return returnlist + cut(a_list[1:])
        else:
            return returnlist + cut(a_list[abs(a_list[0]):]) # Dont add the numbers and skip whatever amount the negative number was.
    else:
        return returnlist
    
    pass




def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    ## YOUR CODE STARTS HERE
    # Base case
    if len(num_list) == 2:
        if num_list[1] > num_list[0]: # if the right number is bigger, the left number is discarded and a list of 2 right numbers are returned
            return [num_list[1], num_list[1]]
        else:                         # if the right number is smaller, the list is sent as is.
            return num_list
    # If not base case
    if num_list[0] < right_max(num_list[1:])[0]:
        return [right_max(num_list[1:])[0]] + right_max(num_list[1:]) # Repeats the "large" number at the top of the list if the right max is larger than the left number
    else:
        return [num_list[0]] + right_max(num_list[1:]) 
    pass





def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    ## YOUR CODE STARTS HERE
    num = int(num)
    if (num < 10):
        return False # If the num ever drops down below a 10, return false
    elif num % 10 == (num % 100) // 10:
        return True # if the digit in in the "10s" place is the same as the diget in the "1s" place return true
    else:
        return consecutive_digits(num // 10) # Will run through until it either drops under 10 or satisfies the true statement.
    pass



def only_evens(num):
    """
        >>> only_evens(4386112)
        4862
        >>> only_evens(0)
        0
        >>> only_evens(357997555531)
        0
        >>> only_evens(13847896213354889741236)
        84862488426
    """
    ## YOUR CODE STARTS HERE
    if num == 0 or num == None: # in case where nothing (or 0) is given
        return 0
    index = num % 10 # take out index to check
    if index % 2 == 1: # check if odd
        return only_evens(num // 10) # skips to next digit if odd
    else:
        return index + only_evens(num // 10) * 10 # if even, call the function again at the digit place it is supposed to be and add it to the index.
                                                    # The important part is to add the * 10 in order to make sure you werent adding in the same spot.
        
    pass



def run_tests():
    import doctest

    #- Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    #- Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function you want to test
    doctest.run_docstring_examples(only_evens, globals(), name='LAB3',verbose=True)

if __name__ == "__main__":
    run_tests()
    