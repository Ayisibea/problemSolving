def swap_case(s):
    m =''
    for i in s:
     if i.isupper():
        a=i.lower()
     elif i.islower():
        a = i.capitalize()
     else:
         a = i   
     m += a
    return m 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)