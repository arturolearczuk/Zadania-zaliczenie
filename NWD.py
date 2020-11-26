def NWD(x,y):
    while x > 0 and y > 0:    
        x = x % y
        if x == 0:
            break 
        y = y % x 
    if x > y:
        return x
    return y

print(NWD(1231338244, 283746912455238760))