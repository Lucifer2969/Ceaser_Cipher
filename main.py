alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to dcrypt the message\n").lower()
text = input("Enter the message\n").lower()
shift = int(input("Type the shift number.\n"))

def ceaser(original_text, shift_amount, ceaser_text):
    cypher_text = ''
    for letter in original_text:
        if letter == ' ':
            cypher_text += ' '
            continue
    if ceaser_text == "decode":
        shift_amount *= -1
    value = alphabets.index(letter) + shift_amount
    value %= len(alphabets)
    cypher_text += alphabets[value]
    print(cypher_text)     
     

ceaser(text, shift, direction)