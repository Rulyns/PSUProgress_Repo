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
    # DISCLAIMER: Most comments currently are notes and debugging for personal learning, I got like a 42.5 On this Homework lol.
    x = 0 # start at 10's place because we pre-calculated the ones place (for the first num)
    y = 0 # same as x, just for the second num.
    fnum_1 = 0 # formatted num1 placeholder
    fnum_2 = 0 # formatted num2 placeholder
    # num 1 formatting
    print(f"{num_1}, preformatted")
    index_1 = (num_1 % 10)  # first "index" of nonformatted num
    fnum_1 += index_1 # will put firt index in "ones place"
    num_1 //= 10 # This index is removed from the num
    # print(f"{num_1}, post formatted")
    # num 2 formatting
    # print(f"{num_2}, preformatted")
    index_2 = (num_2 % 10)  # first "index" of nonformatted num
    fnum_2 += index_2 # will put firt index in "ones place"
    num_2 //= 10 # This index is removed from the num
    # print(f"{num_2}, post formatted")
    while num_1 > 0:
        if (num_1 % 10) == index_1: # if next index is equal to num
            # print(f"{num_1}'s has a duplicate num {index_1}, so {num_1 // 10} is the new num, without {index_1} being added to formatted num.")
            num_1 //= 10 # moves the number down without adding to new format
        else:
            # print(f"{index_1} before change")
            index_1 = (num_1 % 10) # next index
            # print(f"{index_1} post change")
            num_1 //= 10
            x += 1 # increment the 10's place
            # print(f"{num_1} removed {index_1} and placed it into {fnum_1 + (index_1 * 10**x)}")
            fnum_1 += (index_1 * 10**x) # moves that new index to its decimal factor of 10 within format
        # print(f"current 10's factor: {x}")
    # print(fnum_1)
    while num_2 > 0:
        if (num_2 % 10) == index_2: # if next index is equal to num
            # print(f"{num_2}'s has a duplicate num {index_2}, so {num_2 // 10} is the new num, without {index_2} being added to formatted num.")
            num_2 //= 10 # moves the number down without adding to new format
        else:
            # print(f"{index_2} before change")
            index_2 = (num_2 % 10) # next index
            # print(f"{index_2} post change")
            num_2 //= 10
            y += 1 # increment the 10's place
            # print(f"{num_2} removed {index_2} and placed it into {fnum_2 + (index_2 * 10**y)}")
            fnum_2 += (index_2 * 10**y) # moves that new index to its decimal factor of 10 within format
        # print(f"current 10's factor: {y}")
    # print(fnum_2)
    print(fnum_2 == fnum_1)
    return fnum_1 == fnum_2
is_identical(2023,2023)
