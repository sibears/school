from base64 import b85encode as hashpwd
from base64 import b64encode as base64
from string import ascii_lowercase as alphabet, ascii_uppercase as upper_alphabet

ALPHABET = alphabet + upper_alphabet

class CryptoEngine(object):
    SALT = "salt_does_everything_better"

    __a, __b = 1337, 0xBABE

    @classmethod
    def encrypt(cls, message, password):
        pwd = cls._pbkdf(password + cls.SALT)
        return cls._encrypt(message, pwd)

    @classmethod
    def decrypt(cls, message, password):
        pwd = cls._pbkdf(password + cls.SALT)
        return cls._decrypt(message, pwd)

    @classmethod
    def _encrypt(cls, m, p):
        return ''.join(cls._enc_char(c,p) if c in ALPHABET else c for c in m)

    @classmethod
    def _decrypt(cls, m, p):
        return ''.join(cls._dec_char(c, p) if c in ALPHABET else c for c in m)

    @classmethod
    def _enc_char(cls, c, p):
        if c in alphabet:
            return chr((ord(c) - 0x61 + p) % len(alphabet) + 0x61)
        elif c in upper_alphabet:
            return chr((ord(c) - 0x41 + p) % len(alphabet) + 0x41)
        else:
            raise Exception("Not implemented")

    @classmethod
    def _dec_char(cls, c, p):
        if c in alphabet:
            return chr((ord(c) - 0x61 - p) % len(alphabet) + 0x61)
        elif c in upper_alphabet:
            return chr((ord(c) - 0x41 - p) % len(alphabet) + 0x41)
        else:
            raise Exception("Not implemented")

    @classmethod
    def _pbkdf(cls, p):
        p = hashpwd(p.encode())
        return sum(cls._f(c) for c in p)

    @classmethod
    def _f(cls, p):
        f = cls.__a * (p & 0xff) - cls.__b
        return f & 0xff
