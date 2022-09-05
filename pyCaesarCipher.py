from curses.ascii import isdigit

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''
 .o88b.  .d8b.  d88888b .d8888.  .d8b.  d8888b.       .o88b. db    db d8888b. db   db d88888b d8888b. 
d8P  Y8 d8' `8b 88'     88'  YP d8' `8b 88  `8D      d8P  Y8 `8b  d8' 88  `8D 88   88 88'     88  `8D 
8P      88ooo88 88ooooo `8bo.   88ooo88 88oobY'      8P       `8bd8'  88oodD' 88ooo88 88ooooo 88oobY' 
8b      88~~~88 88~~~~~   `Y8b. 88~~~88 88`8b        8b         88    88~~~   88~~~88 88~~~~~ 88`8b   
Y8b  d8 88   88 88.     db   8D 88   88 88 `88.      Y8b  d8    88    88      88   88 88.     88 `88. 
 `Y88P' YP   YP Y88888P `8888Y' YP   YP 88   YD       `Y88P'    YP    88      YP   YP Y88888P 88   YD 
''')
while ( 1 ) :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 52

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text :
            if letter == " " or isdigit(letter) :
                end_text += letter
            else :
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
        print(f"The {cipher_direction}d text is {end_text}")
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    choice = input (print ("Do you want to continue ciphering ? yes/no"))
    if choice == "no" :
        break