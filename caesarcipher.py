##-----CIPHERS-----##

alphabet = list("abcdefghijklmnopqrstuvwxyz")  # the alphabet
alphabet_upper = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
output = []
special_character = list(r"\'!@#$%^&*()[]{}?:;~`¬_-+=/| ")

def decrypt_ceaser_cipher(decrypt_text):
    Mirroralpabet = alphabet[::-1]  # mirrors the alphabet array
    MirrorALPHABET = alphabet_upper[::-1]
    key = input("Enter the key. 1 to 26: ")  # gets the key
    try:  # begin error handling
        key = int(key)
        print("Thank you for entering the key")
    except ValueError:
        print("Invalid input")
        return  ## Error handling end

    while key > 26:
        key -= 26

    for i in range(len(decrypt_text)):
        L = decrypt_text[i]
        if L in special_character:
            output.append(L)
            continue
        elif L not in special_character and L not in alphabet:
            output.append(L)
            continue
        elif L in alphabet_upper:
            V = MirrorALPHABET.index(L)
            X = V + key
            if X >= 26:
                X -= 26
            output.append(MirrorALPHABET[X])
            continue
        elif L in alphabet:
            V = Mirroralpabet.index(L)
            X = V + key
            if X >= 26:
                X -= 26
            output.append(Mirroralpabet[X])  # increases the position of the value V by the provided key

    print("".join(output))

def encyrpt_ceaser_cipher():
    text = input("Enter the text: ") # asks for text to encrypt
    print(text)
    try:  ## Error handling start
        text = str(text)
        print("Thank you for entering text")
    except TypeError:
        print("Invalid input")
        return
    key = input("Enter the key. 1 to 26: ")
    try:
        key = int(key)
        print("Thank you for entering the key")
    except ValueError:
        print("Invalid input")
        return  ## Error handling end

    while key > 26:
        key -= 26  # wrap around

    #clean_list = text.replace(" ", "")  # removes invalid characters from them list
    output = []

    for i in range(len(text)):  # gets length
        L = text[i]  # gets the value at i point in the list
        if L in special_character:
            output.append(L)
            continue
        elif L not in special_character and L not in alphabet:
            output.append(L)
            continue
        elif L in alphabet_upper:
            V = alphabet_upper.index(L)
            X = V + key
            if X >= 26:
                X -= 26
            output.append(alphabet_upper[X])
        else:
            V = alphabet.index(L)  # is the position of the letter from the list
            X = V + key
            if X >= 26:
                X -= 26
            output.append(alphabet[X])  # increases the position of the value V by the provided key

    print("".join(output))

    question = input("Would you like to decrypt the text? (y/n): ").lower()
    if question == "y":
        print("Decrypting...")
        decrypt_ceaser_cipher(output)
    if question == "n":
        print("Thank you for using the cipher")
        return

def ask():
    response = input("What would you like to do? Encrypt/decrypt: ").lower()
    match response:
        case "encrypt":
            encyrpt_ceaser_cipher()
        case "decrypt":
            encyrpt_ceaser_cipher()
        case "1":
            encyrpt_ceaser_cipher()
        case "2":
            decrypt_ceaser_cipher()

ask()
