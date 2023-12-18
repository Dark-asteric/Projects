import re

your_data = input("Enter your cipher to decode : ")
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def rot_47(secret):
    rot_const = 47
    decode = ""
    for it in secret:
        index = alphabet.find(it)
        original_index = (index + rot_const)% len(alphabet)
        decode += alphabet[original_index]
    return decode
ans = rot_47(your_data)
ans1 = re.sub('O'," ",ans)
print(ans1)