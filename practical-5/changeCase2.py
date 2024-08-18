def change_case(string,style):
	if(style=='c' or style=='C'):
		return capital_case(string)
	elif(style=='s' or style=='S'):
		return small_case(string)
	elif(style=='r' or style=='R'):
		return reverse_case(string)
	elif(style=='u' or style=='U'):
		return alter_case(string)
	else:
		return "Invalid style"


def capital_case(string):
	new=""
	
	for char in string:
		if('a'<=char<='z'):
			new = new + chr(ord('A')+(ord(char)-ord('a')))
		else:
			new = new +char
	return new 


def small_case(string):
	new=""
	for char in string:
		if('A'<=char<='Z'):
			new = new + chr(ord('a') + (ord(char) - ord('A')))
		else:
			new = new + char 
	return new 
	
def reverse_case(string):
	new =""
	for char in string:
		if('a'<=char<='z'):
			new = new + chr(ord('A')+(ord(char)-ord('a')))
		elif('A'<=char<='Z'):
			new = new + chr(ord('a')+(ord(char)-ord('A')))
		else:
			new = new +char
	return new

def alter_case(string):
    new = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            if 'a' <= char <= 'z':
                new =new + chr(ord('A') + (ord(char) - ord('a')))
            else:
                new =new+  char
        else:
            if 'A' <= char <= 'Z':
                new = new +chr(ord('a') + (ord(char) - ord('A')))
            else:
                new = new+ char
    return new

print(change_case('Dnyan','u'))
