def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    
    for char in message:
        is_capital = char in alphabet.upper()
        letter = char
        
        if char in alphabet or is_capital:
            index = alphabet.index(char.lower()) + 13
            alphabet_length = len(alphabet)
            letter_index = index if index < alphabet_length else (index % alphabet_length)
            letter = alphabet[letter_index]
        
        encrypted_message += letter.upper() if is_capital else letter

    print(encrypted_message)
    return encrypted_message
