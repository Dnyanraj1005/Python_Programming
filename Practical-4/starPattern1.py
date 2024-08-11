def starPattern(n):
	for i in range(3*n-n):
		for j in range(2*n+3):
			if(i==0 and j==n+1):
				print("*",end="")
			elif(i+j==n+1 and i<n+1 and j<n+1):
				print("*",end="")
			elif(j-i==n+1 and i<n+1 and j>n+1):
				print("*",end="")
			elif(i==n and j==n+1):
				print(n,end="")
			elif(i-j==n-1 and i>n and j<n+1):
				print("*",end="")
			elif(i+j==3*n+1 and i>n and j>n+1):
				print("*",end="")
			else:
				print(" ",end="")
		print()
	
	for i in range(n):
		for j in range(2*n+3):
			print("*",end="")
		print()
	
print(starPattern(4)).
	

				
