from values import morse_code_dict
def encode():
    text=input("What do you want to encode into morse code? ").upper()
    morse_word=""
    for characters in text:
        new_letter=morse_code_dict[characters]
        morse_word+=f"{new_letter} "
    print(f"Your message encoded in morse is- {morse_word}")

def decode():
    new_word=""
    code = input("What do you want to decode from morse code? ")
    morse_letters = code.split()
    for i in morse_letters:
        while i not in morse_code_dict.values():
            code=input("Please enter actual morse code: ")
        original_letter = next((k for k, v in morse_code_dict.items() if v == i))
        new_word+=original_letter
    print(f"Decoded message is- {new_word}")

def decide():
    while True:
        choice=input("Do you want to encode(e) or decode (d) morse code or quit(q)? ").lower()
        if choice == "e":
            encode()

        elif choice == "d":
            decode()

        elif choice == "q":
            print("Thank you for using morse code translator!")
            break
        else:
            print("Enter either e for encode or d for decode!")

decide()