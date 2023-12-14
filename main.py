def isPolindrome(x):
    if x<0:
        return False
    list_number = list(str(x))
    list_number.reverse()
    list_number = ''.join(list_number)
    int_number = int(list_number)
    return(int_number==x)



