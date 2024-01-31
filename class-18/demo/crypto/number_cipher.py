import random

def encrypt(plain, shift):
    encrypted_text = ""

    # 1234 -> 2345 with shift of 1

    for char in plain:
        num = int(char)
        shifted_num = (num + shift) % 10
        encrypted_text += str(shifted_num)

    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


if __name__ == "__main__":
    pins = [
        "1234",
        "9876",
        "0000",
        "9999",
    ]

    for pin in pins:
        shift = random.randint(1, 9)
        print("plain pin", pin)
        encrypted_pin = encrypt(pin, shift)
        print("shift by", shift)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, shift)
        print("decrypted_pin", decrypted_pin)
