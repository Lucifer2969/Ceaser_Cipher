from art import logo

# List of Alphabets
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z']

print(logo)
condition = False

# Function Defination -- Inside the function as per the given conditional loop Encoding and Decoding happens with the help of shift and output is 
# printed as result.
def ceaser(original_text, shift_amount, ceaser_text):
    cypher_text = ''
    if ceaser_text == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            cypher_text += letter
            continue
        value = alphabets.index(letter) + shift_amount
        value %= len(alphabets)
        cypher_text += alphabets[value]
    print(f"Here is the {direction}d result, {cypher_text}.")

# Condition While to get the inputs from the User to get the shift_amount,text and direction(weather the user want's to get input as Encode or Decode).
while not condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to dcrypt the message\n").lower()
    text = input("Enter the message\n").lower()
    shift = int(input("Type the shift number.\n"))

    ceaser(text, shift, direction)

# Take user Input if 'YES'to repeat with the same process if 'NO' program ends.
    cont_conditon = input("Press 'yes' if you want to continue again and 'no' to exit.\n").lower()

    if cont_conditon != 'yes':
        condition = True