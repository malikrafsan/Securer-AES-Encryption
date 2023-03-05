#!/usr/bin/env python
from aes import AES
import base64


def main():
    # sender
    msg = "MalikAkbarRafsanTidakKenalDenganMalikAkbarRafsanGan"
    key = "abcdefghij123456"
    aes = AES(key)
    digest = aes.encrypt(msg)

    # receiver
    decrypted = aes.decrypt(digest)
    print("decrypted", decrypted)

    # intruder
    print("digest", digest)
    print("len(digest)", len(digest))
    decoded = base64.b64decode(digest)
    splitted = [decoded[i:i+16] for i in range(0, len(decoded), 16)]
    print("splitted", splitted)
    print("message block 1 == 3", splitted[0] == splitted[2])


if __name__ == "__main__":
    main()
