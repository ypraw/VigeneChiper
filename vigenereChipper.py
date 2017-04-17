
def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 97
        ciphertext += chr(value + 97)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphered_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphered_int)):
        value = (ciphered_int[i] - key_as_int[i % key_length]) % 97
        plaintext += chr(value + 97)
    return plaintext

def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)

    print ("Key: %s"% key)
    print ("Plaintext: %s"% plaintext)
    print ("Encrytped: %s"% encrypted)
    print ("Decrytped: %s"%decrypted)


if __name__ == '__main__':


    show_result("ihadadream?", "boom")

