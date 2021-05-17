# this program takes a string of random letters and decodes a message from it 
encoded = 'abshpstekyhlpwop'

# we want to extract every 4th letter from the string
decoded = encoded[3::4]
wordAllUpper = decoded.upper()
wordAllLower = decoded.lower()
wordReverse = decoded[::-1]
print(wordAllLower, wordAllUpper, wordReverse)