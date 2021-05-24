def decryptionMessage(cipherText, key):
    decrypt = ''
    cipherText = list(cipherText)
    for i in range(len(cipherText)):
        if (i+key) >= len(cipherText):
            for i in range(len(cipherText) - len(decrypt)):
                decrypt += cipherText[i]
        else:
            decrypt += cipherText[i+key]
    return print(decrypt)

if __name__ == '__main__':
    ciphertext = input()
    key = int(input().strip())
    decryptionMessage(ciphertext, key)