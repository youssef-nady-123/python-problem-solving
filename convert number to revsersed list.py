# convert number to reversed list, array 
# ==============================================

def convert(n):
    # convert to string
    st = str(n)
    
    # create empty list
    result = []
    
    # loop on the string
    for num in st:
        # while loop on the list, change the type to integer 
        result.append(int(num))

    # revserse the list
    result.reverse()
    
    # return the list
    return result

# function call 
print(convert(564454651))   # [1, 5, 6, 4, 5, 4, 4, 6, 5]

# function call 
print(convert(634944571))   # [1, 7, 5, 4, 4, 9, 4, 3, 6]

# ==============================================================


# ================
# == solution 2 == 
# ================

def convertNumToList(num):
    result = []
    for n in str(num):
        
        # while loop, insert the element at the first of the list 
        result.insert(0, int(n))
        
    return result

# function call
print(convertNumToList(634944571))      # [1, 7, 5, 4, 4, 9, 4, 3, 6]

# function call 
print(convertNumToList(564454651))      # [1, 5, 6, 4, 5, 4, 4, 6, 5]