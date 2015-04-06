from string import maketrans

class Rot13():
    def __init__(self):
        fromCharset = "abcdefghijklmnopqrstuvwxyz"
        toCharset = "nopqrstuvwxyzabcdefghijklm"
        
        plain = fromCharset + fromCharset.upper()
        encrypted = toCharset + toCharset.upper()
        self.transtab = maketrans(plain, encrypted)
        
    def encrypt(self, s):
        return s.translate(self.transtab)