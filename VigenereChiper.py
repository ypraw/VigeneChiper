#  VigenereChiper.py on  artificialIntelligence Project
__author__ = " Yunindyo Prabowo "
__date__ = "Apr 15, 2017  01.20 "

#initializing Dictionary of Alphabet
abjadDictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plaintext, key):
    """Encrypt the string and return the ciphertext"""
    keyLength = len(key)
    keyinDict = [abjadDictionary.index(i) for i in key]
    plaintextDict = [abjadDictionary.index(i) for i in plaintext]
    result = ''

    for i in range(len(plaintext)):
        value = (plaintextDict[i] + keyinDict[i % keyLength])
        result+= abjadDictionary[value%52]

    return result

def decrypt(ciphertext, key):
    """Decrypt the string and return the plaintext"""
    keyLength = len(key)
    keyinDict = [abjadDictionary.index(i) for i in key]
    chipherDict = [abjadDictionary.index(i) for i in ciphertext]
    result = ''

    for i in range(len(ciphertext)):
        value = (chipherDict[i] - keyinDict[i % keyLength])
        result += abjadDictionary[value % 52]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)

    print("Vigenere Chipper")
    print("Key: %s" % key)
    print("Plaintext: %s" % plaintext)
    print("Encrytped: %s" % encrypted)
    print("Decrytped: %s" % decrypted)


if __name__ == '__main__':
    k="abcde"
    kunci = [abjadDictionary.index(i) for i in k]
    print(kunci)
    #show_result("yunIndYo","kUnci")

