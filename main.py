#!/usr/bin/env python
from aes import AES


def main():
    msg = "rozan fadhil alhamdulillah masyaallah subhanallah la ilaha illallah"
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    aes = AES(key)
    digest = aes.encrypt(msg)

    print("len msg", len(msg))
    print("digest", digest)
    print("len digest", len(digest))

    decrypted = aes.decrypt(digest)
    print("decrypted", decrypted)


if __name__ == "__main__":
    main()
