def encrypt(word):
	"""This function takes a string as input 
	and gives the encrypted string as output based on Caesar Cypher"""
	
	print('Encrypted message is ')
	for bit in word:
		unicode=ord(bit)
		#print(unicode)
		#unicode for A-Z = 65-90, unicode for a-z = 97-122 (both inclusive)
		
		if(65<=unicode and unicode<=90):
		    print(chr(((unicode-65)+3)%26+65))
		elif(97<=unicode and unicode<=122):
			print(chr(((unicode-97)+3)%26+97))
		else:
		    print("Invalid Input. Needs to be a-z or A-Z.")
		    break

def decrypt(word):
	"""This function takes a string as input 
	and gives the decrypted string as output based on Caesar Cypher"""
	
	print('Decrypted message is ')
	for bit in word:
		unicode=ord(bit)
		#print(unicode)
		#unicode for A-Z = 65-90, unicode for a-z = 97-122 (both inclusive)
		
		if(65<=unicode and unicode<=90):
		    print(chr(((unicode-65)-3)%26+65))
		elif(97<=unicode and unicode<=122):
			print(chr(((unicode-97)-3)%26+97))
		else:
		    print("Invalid Input. Needs to be a-z or A-Z.")
		    break
				
	
	