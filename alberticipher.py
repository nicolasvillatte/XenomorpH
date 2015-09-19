# TBW Operation NIGHFALL http://archive.blackwatchmen.com/search/99BBF2
# Took an existing program for cesar cipher text and modified it
#http://www.stealthcopter.com/blog/2009/12/python-cryptography-caesar-shift-encryption-shift-cipher/
def caesar(plaintext,shift):

	alphabet=["A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"]

	#Create our substitution dictionary
	dic={}
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

	#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext.upper():
		if l in dic:
			l=dic[l]
		ciphertext+=l

	return ciphertext

code="002AA47 5D9739C"
decoded=""
counter=0
# SECRET KEY is 2R, 5L, 3L, 1R, 4R, 2L, 4L
indexcadran=[14,3,6,5,1,3,7]
print "Plaintext:", code
for i in code:
	if i !=" ":
		print counter
		decoded+=caesar(i,indexcadran[counter])
		if counter <6:
			counter+=1
		else:
			counter=0
	else: 
		decoded=decoded+" "
print decoded
