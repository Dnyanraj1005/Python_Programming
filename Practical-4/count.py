def count(str1, sub, bool1):
    len1 = len(str1)
    sublen = len(sub)
    count = 0
    
    i = 0
    while i <= len1 - sublen:
        p = i
        str2 = ""
        for j in range(sublen):
            str2 = str2 + str1[p]
            p = p + 1
            
        if str2 == sub:
            count += 1
            if bool1:
                i += 1  # Move to the next character if overlapping is allowed
            else:
                i += sublen  # Move past the matched substring if overlapping is not allowed
        else:
            i += 1
    
    return count

str1 = input("Enter the String: ")
sub = input("Enter the Substring: ")
bool1 = input("Enter True/False: ").lower() == 'true'

print(count(str1, sub, bool1))

