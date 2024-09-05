import sys
from dict import MORSE_ENCODE, MORSE_DECODE


def encoder(s):
    """Encode a string to morse code"""
    encoded = ""
    for c in s:
        if c.isalnum() or c == ' ':
            encoded += MORSE_ENCODE[c.upper()] + " "
    print(encoded[:-1])


def decoder(s):
    """Decode a string from morse code"""
    decoded = ""
    for c in s.split():
        if c in MORSE_DECODE:
            decoded += MORSE_DECODE[c]
    print(decoded)


def isalphaspace(s):
    """Check if a string is composed of alphanumeric characters and spaces"""
    s = s.upper()
    for c in s:
        if c not in MORSE_ENCODE and c != ' ':
            return False
    return True


def ismorsechar(s):
    """Check if a string is composed of morse code characters and spaces"""
    for c in s:
        if c not in MORSE_DECODE and c != ' ':
            return False
    return True


def valid_conversion(args):
    """Check if the arguments are valid for conversion"""
    for s in args:
        valid = False
        if isalphaspace(s):
            valid = True
        elif ismorsechar(s):
            valid = True
        if not valid:
            return False
    return True


def main():
    args = sys.argv[1:]

    try:
        assert valid_conversion(args), "the arguments are bad"
        assert [len(arg) > 0 for arg in args], "the arguments are bad"
    except AssertionError as e:
        print(e)
        return 1

    for arg in args:
        if isalphaspace(arg):
            encoder(arg)
        else:
            decoder(arg)
    return 0


if __name__ == "__main__":
    main()
