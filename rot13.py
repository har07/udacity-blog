from string import maketrans

class Rot13():
	def __init__(self):
		lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
		upper_alphabet = lower_alphabet.upper()
		encrypted = ""
		
		plain = lower_alphabet + upper_alphabet
		for c in lower_alphabet:
			encrypted += self.encryptChar(lower_alphabet, c)
		for c in upper_alphabet:
			encrypted += self.encryptChar(upper_alphabet, c)
		self.transtab = maketrans(plain, encrypted)
		
	def encryptChar(self, charset, char):
		if not(char in charset):
			return char
		index = charset.index(char)
		return charset[(index+13)%len(charset)]
		
	def encrypt(self, s):
		return s.translate(self.transtab)