def slice(obj, start=None, end=None, step=1):
    
    if start is None:
        start = 0
    elif start < 0:
        start = len(obj) + start
    
    if end is None:
        end = len(obj)
    elif end < 0:
    	end = len(obj) + end 
        
    
   
    result = []
    i = start
    while (i < end and step > 0) or (i > end and step < 0):
        result.append(obj[i])
        i += step
    
    if isinstance(obj, str):
        return ''.join(result)
    elif isinstance(obj, list):
        return result
    elif isinstance(obj, tuple):
        return tuple(result)
    elif isinstance(obj, bytes):
        return bytes(result)
    elif isinstance(obj, bytearray):
        return bytearray(result)
    else:
        raise TypeError("Unsupported data type for slicing")


print(slice("hello", 1, 4))  
print(slice((10, 20, 30, 40), 1, None, 2)) 

