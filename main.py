import string
from gettext import find


def crypto(text: str, key: int):
    obrazec = string.printable

    newtext = []
    for i in text:
        index = obrazec.find(i)
        if_key = index + key

        if if_key > len(obrazec):
            if_key = if_key % len(obrazec)
        letter = obrazec[if_key]
        newtext.append(letter)
    return "".join(newtext)


# def decrypto(text: str, key: int):
#     obrazec = string.printable
#     newtext = []
#     for i in text:
#         index = obrazec.find(i)
#         letter = obrazec[index - key]
#         newtext.append(letter)
#     return "".join(newtext)


crypto_result = crypto(text="aaaa ,bbbb", key=)
print()
# print(decrypto(text=crypto_result, key=500))
