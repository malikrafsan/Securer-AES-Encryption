#!/usr/bin/env python
from aes import AES


def main():
    msg = "rozan fadhil alhamdulillah"
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    aes = AES(key)
    digest = aes.encrypt(msg)

    print("digest", digest)

    decrypted = aes.decrypt(digest)
    print("decrypted", decrypted)


if __name__ == "__main__":
    main()
