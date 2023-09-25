#Enc.

Text = input().strip()
CipherText = ""
for i in range(0,len(Text)):
	CipherText += Text[i]*(i+1)
print(CipherText)

#Dec.

Text = input().strip()
index = 0
for i in range(len(Text)):
	index += i
	if index < len(Text):
		print(Text[index],end="")

#PROGRAM

#Enc part

Text = input().strip()
CipherText = ""
for i in range(len(Text)):
	CipherText += Text[i]*(i+1)
print("PLAIN TEXT :",Text)
print("CIPHER TEXT :",CipherText)

# Dec part 

print("Decripted Word :",end=" ")
index = 0
for j in range(len(CipherText)):
	index += j
	if index < len(CipherText):
		print(CipherText[index],end="")


# INPUT : HELP ME
# OUTPUT:
#	PLAIN TEXT : HELP ME
#	CIPHER TEXT : HEELLLPPPP     MMMMMMEEEEEEE
#	Decripted Word : HELP ME
