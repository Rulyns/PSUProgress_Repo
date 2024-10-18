def findroutes(x , y):
    sum = 0
    if x == 1 and y == 1:
        return 1
    elif x > 1 and y > 1:
        return sum + findroutes(x - 1, y) + findroutes(x, y-1)
    elif x > 1:
        return sum + findroutes(x - 1, y)
    else:
        return sum + findroutes(x , y - 1)
    
print(findroutes(8,8))