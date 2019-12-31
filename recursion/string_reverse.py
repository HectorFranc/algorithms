def string_reverse(string):
    '''
    Returns a string equals to string[::-1]
    Parameters:
    string: str
        String that will be used
    '''
    if string == '':
        return ''
    else:
        return string_reverse(string[1:]) + string[0]
