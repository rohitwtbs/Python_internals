def swap_case(s):
    return_string = ""
    for i in s:
        if(i.islower()):
            c = i.upper()
        else:
            c = i.lower()
        # print(i.casefold())
        return_string = return_string + c
    return return_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)