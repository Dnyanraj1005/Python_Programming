def char_to_value(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 10
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 10
    return -1

def value_to_char(value):
    if 0 <= value <= 9:
        return chr(value + ord('0'))
    elif 10 <= value <= 35:
        return chr(value - 10 + ord('a'))
    return ''

def base(text, text_base, output_base):
    
    decimal_value = 0
    power = 1
    for i in range(len(text) - 1, -1, -1):  
        value = char_to_value(text[i])
        decimal_value += value * power
        power *= text_base
    
    
    result = ""
    if decimal_value == 0:
        return "0"
    
    while decimal_value > 0:
        remainder = decimal_value % output_base
        result = value_to_char(remainder) + result
        decimal_value //= output_base
    
    return result


print(base("1a", 16, 10))  
print(base("10", 2, 10))   
print(base("2a", 36, 16))  

