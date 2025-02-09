# UNIT 2: Decryption Mapping
# Purpose:
# This program decodes messages based on a custom letter-to-number mapping.

def decode_message(encoded):
    mapping = {
        "07": "A", "08": "B", "09": "C", "10": "D", "11": "E",
        "12": "F", "13": "G", "14": "H", "15": "I", "16": "J",
        "17": "K", "18": "L", "19": "M", "20": "N", "21": "O",
        "22": "P", "23": "Q", "24": "R", "25": "S", "26": "T",
        "01": "U", "02": "V", "03": "W", "04": "X", "05": "Y", "06": "Z"
    }
    result = ""
    for i in range(0, len(encoded), 2):
        result += mapping[encoded[i:i+2]]
    return result

def main():
    print("Decryption Mapping Program")
    encoded = input("Enter encoded message (2 digits per letter): ")
    decoded = decode_message(encoded)
    print("Decoded message: " + decoded)

main()
