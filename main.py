from art import logo

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z']

print(logo)
condition = False

while not condition:

    direction = input("Type 'encode' to encrypt, type 'decode' to dcrypt the message\n").lower()
    text = input("Enter the message\n").lower()
    shift = int(input("Type the shift number.\n"))


    def ceaser(original_text, shift_amount, ceaser_text):
        cypher_text = ''
        for letter in original_text:
            if letter not in alphabets:
                cypher_text += letter
                continue
            if ceaser_text == "decode":
                shift_amount *= -1
            value = alphabets.index(letter) + shift_amount
            value %= len(alphabets)
            cypher_text += alphabets[value]
        print(f"Here is the {direction}d result, {cypher_text}.")


    ceaser(text, shift, direction)
    cont_conditon = input("Press 'yes' if you want to continue again.\n")
    if cont_conditon != 'yes':
        condition = True