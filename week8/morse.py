encryption_dict = {
    "A": ". -",
    "B": "- . . .",
    "C": "- . - .",
    "D": "- . .",
    "E": ".",
    "F": ". . - .",
    "G": "- - .",
    "H": ". . . .",
    "I": ". .",
    "J": ". - - -",
    "K": "- . -",
    "L": ". - . .",
    "M": "- -",
    "N": "- .",
    "O": "- - -",
    "P": ". - - .",
    "Q": "- - . -",
    "R": ". - .",
    "S": ". . .",
    "T": "-",
    "U": ". . -",
    "V": ". . . -",
    "W": ". - -",
    "X": "- . . -",
    "Y": "- . - -",
    "Z": "- - . .",
    " ": "/"
}
msg = "HI"
encrypted_msg = ""
for c in msg:
    encrypted_msg = encrypted_msg + encryption_dict[c]

print(encrypted_msg)
decryption_dict = {}
for k, v in encryption_dict.items():
    decryption_dict[v] = k

print(decryption_dict)
msg2 = ""
for c in encrypted_msg:
    msg2 = msg2 + decryption_dict[c]

print('the deciphered message is: ', msg2)
