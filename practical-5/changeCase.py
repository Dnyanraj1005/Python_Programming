def change_case(string, style):
    if(style == 'c' or style == 'C'):
        return capital_case(string)
    elif(style == 's' or style == 'S'):
        return small_case(string)
    elif(style == 'r' or style == 'R'):
        return reverse_case(string)
    elif(style == 'u' or style == 'U'):
        return alter_case(string)
    else:
        return "Select valid style"gft


def capital_case(string):
    
    new = ""
    
    for i in range(len(string)):
        if(string[i] >= chr(65) and string[i] <= chr(90)):
            new = new + string[i]
        elif(string[i] >= chr(97) and string[i] <= chr(122)):
            temp = chr(ord(string[i]) - 32)
            new = new + temp
        else:
            new = new + string[i]
        
    return new
    
def small_case(string):
    new = ""
    
    for i in range(len(string)):
        if(string[i] >= chr(97) and string[i] <= chr(122)):
            new = new + string[i]
        elif(string[i] >= chr(65) and string[i] <= chr(90)):
            temp = chr(ord(string[i]) + 32)
            new = new + temp
        else:
            new = new + string[i]
    return new 

def reverse_case(string):
    new = ""
    for i in range(len(string)):
        if(string[i] >= chr(65) and string[i] <= chr(90)):
            temp = chr(ord(string[i]) + 32)
            new = new + temp
        elif(string[i] >= chr(97) and string[i] <= chr(122)):
            temp = chr(ord(string[i]) - 32)
            new = new + temp
        else:
            new = new + string[i]
    return new

def is_small(s):
    if(ord(s) >= 97 and ord(s) <= 122):
        return True
    return False

def alter_case(string):
    new = ""
    if (string[0] >= chr(97) and string[0] <= chr(122)):
        for i in range(len(string)):
            if(i % 2 == 0):
                if(is_small(string[i]) == True):
                    new = new + string[i]
                else:
                    temp = chr(ord(string[i]) + 32)
                    new = new + temp
            else:
                if(is_small(string[i]) == True):
                    temp = chr(ord(string[i]) - 32)
                    new = new + temp
                else:
                    new = new + string[i]
    elif(string[0] >= chr(65) and string[0] <= chr(90)):
        for i in range(len(string)):
            if(i % 2 == 0):
                if(is_small(string[i]) == True):
                    temp = chr(ord(string[i]) - 32)
                    new = new + temp
                else:
                    new = new + string[i]
            else:
                if(is_small(string[i]) == True):
                    new = new + string[i]
                else:
                    temp = chr(ord(string[i]) + 32)
                    new = new + temp 
    else:
        new = new + string[i]                       
    return new

print(change_case('DnYaN', 'C'))

