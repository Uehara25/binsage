import sys

def encode(message):
    ret = ""
    for char in message:
        decimal = ord(char)
        if decimal > 255:
            print("can't convert " + char, file=sys.stderr)
            continue;

        eight_digit_binary = bin(decimal).split("0b")[1].zfill(8)
        ret += eight_digit_binary
    return ret

def decode(message):
    ret = ""

    tmp = ""
    for i in range(len(message)):
        tmp += message[i]
        if i % 8 == 7:
            tmp += ","

    for binary in tmp.split(",")[:-1]:
        decimal = int(binary, 2)

        if decimal > 255:
            print("can't convert " + binary, file=sys.stderr)
            continue

        ret += chr(decimal)

    return ret

if __name__ == "__main__":
    inputs = []
    try:
        inputs = sys.argv[1:]
    except:
        print("usage: binsage.py ** or binsage.py [-d] **")
        sys.exit(0)

    firstarg = inputs[0]
    if firstarg == '-d':
        seconde = ""
        inputs.pop(0)
        s = "".join(inputs)
        print(decode(s))
    else:
        print(encode(" ".join(inputs)))
