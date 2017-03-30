def char_to_binary(msg):
    """
    Function converts a type 'str' message into a base 2 integer, by converting
    each character and space into an 8 bit binary decimal, combining them into
    one large string, and converting this decimal into a base 2 integer
    @param msg : type 'str' message to convert
    @return : base 2 'int'
    """
    decimal_str = ''
    for char in msg:
        decimal_str += '{0:08b}'.format(ord(char))
    return int(decimal_str, 2)


def modular_exponentiation(base, expo, n):
    """
    Function for modular exponentiation (ensures against integer overflow),
    computes (base^expo) mod n
    @param base : used as base
    @param expo : used as expo
    @param n : used to mod
    @return result : result = ((base^expo) mod n)
    """
    val = 1
    base %= n

    while expo > 0:
        # the case that expo is odd, make sure to multiply by one base
        if expo % 2 == 1:
            val = (val * base) % n
        # repeated squaring
        base = (base * base) % n
        expo //= 2
    return val % n


def rsa_encode(n, e, msg):
    """
    Encodes a message into a decimal using a public RSA key and prints
    x, the message converted into decimal, and the final RSA encoded message
    @param n : type 'int', first value in the pair (n, e) in public key
    @param e : type 'int', second value in public key pair
    @msg msg : type 'str', message to encode
    """
    x = char_to_binary(msg)
    print 'Decimal:', x
    print 'Encoded message:', modular_exponentiation(x, e, n)


n = 46947848749720430529628739081
e = 37267486263679235062064536973
msg = 'Give me an A'

rsa_encode(n, e, msg)
