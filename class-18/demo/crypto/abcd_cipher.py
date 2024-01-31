def encrypt(plain, shift):
    encrypted_text = ""

    # ABCD -> BCDA with shift of 1
    # ABCD -> CDAB with shift of 2

    # We're intentionally restricting to 4 characters A,B,C and D
    # What if we wanted whole alphabet?
    # How could you account for case?
    # What about non letters?
    # Is there some way of determining if a character "is alpha" ?

    number_of_characters = 4
    base_character = "A"

    for char in plain:
        base_code = ord(base_character)
        current_code = ord(char)
        current_position = current_code - base_code
        shifted_position = (current_position + shift) % number_of_characters
        shifted_char = base_code + shifted_position
        encrypted_text += chr(shifted_char)

    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


if __name__ == "__main__":
    pins = [
        "AAAA",
        "BBBB",
        "ABCD",
        "ABAB",
    ]

    for i, pin in enumerate(pins):
        shift = i + 1
        print("plain pin", pin)
        print("shift by", shift)
        encrypted_pin = encrypt(pin, shift)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, shift)
        print("decrypted_pin", decrypted_pin)
        print()
