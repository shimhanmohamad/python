alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
       position = alphabet.index(letter)
       new_position = position + shift_amount
       new_letter =alphabet[new_position]
       cipher_text += new_letter

    print(cipher_text)

def decrypt(other_text,shift_other):
    decode_text = ""
    for letter in other_text:
       position = alphabet.index(letter)               
       new_position = position - shift_other
       new_letter =alphabet[new_position]
       decode_text += new_letter

    print(decode_text)

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt : \n")
if (direction == 'encode'):
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n"))
    shift = shift % 25
    encrypt(text,shift)
    cont = input("If you want to continue 'yes' or 'no' : \n")
    while (cont =='yes' ):
            direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt : \n")
            if (direction == 'encode'):
                text = input("Type your message : \n").lower()
                shift = int(input("Type the shift number : \n"))
                shift = shift % 25
                encrypt(text,shift)
                cont = input("If you want to continue 'yes' or 'no' : \n")
            elif (direction == 'decode'):
                text = input("Type your message : \n").lower()
                shift = int(input("type the shift number : \n"))
                shift = shift % 25
                decrypt(text,shift)
                cont = input("If you want to continue 'yes' or 'no' : \n")
    print("Thank you")

                


elif (direction == 'decode'):
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n"))
    shift = shift % 25
    decrypt(text,shift)
    cont = input("If you want to continue 'yes' or 'no' : \n")
    while (cont == 'yes'):
        direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt : \n")
        if (direction == 'encode'):
            text = input("Type your message : \n").lower()
            shift = int(input("Type the shift number : \n"))
            shift = shift % 25
            encrypt(text,shift)
            cont = input("If you want to continue 'yes' or 'no' : \n")
        elif (direction == 'decode'):
            text = input("Type your message : \n").lower()
            shift = int(input("type the shift number : \n"))
            shift = shift % 25
            decrypt(text,shift)
            cont = input("If you want to continue 'yes' or 'no' : \n")
    print("Thank you")

else:
    print("Invalid option")
    
