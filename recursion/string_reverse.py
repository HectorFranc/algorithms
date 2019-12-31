def string_reverse(string):
    if string == '':
        return ''
    else:
        return string_reverse(string[1:]) + string[0]