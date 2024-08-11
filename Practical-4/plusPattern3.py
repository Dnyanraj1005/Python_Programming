def plusPattern(n):
    size = 2 * n + 1

    for i in range(size):
        for j in range(size):
        	if(j==n and i==0):#?
        		print("+",end=" ")
        	elif(i+j==n and i<n+1):
        		print("+",end=" ")
        	elif(j-i==n):
        		print("+",end=" ")
        	
        	elif(i-j==n):
        		print("-",end=" ")
        	elif(i+j==3*n):
        		print("-",end=" ")
        	else:
        		print(" ",end=" ")
        print()
 

print((plusPattern(3)))
