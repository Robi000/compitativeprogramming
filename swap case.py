def swap_case(s):
    new = ""
    for x in s:
        if x.isupper():
            new += x.lower()
        else:
            new += x.upper()
    # print (new)
    return new

if __name__ == '__main__':
