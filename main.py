#!/usr/bin/env python
from aes import AES


def main():
    # msg = "rozan fadhil alhamdulillah masyaallah subhanallah la ilaha illallah"
    msg = "satutuju"
    key = "abcdefghij12🥲"
    aes_encrypt = AES(key)
    digest = aes_encrypt.encrypt(msg)

    # print("len msg", len(msg))
    # print("digest", digest)
    # print("len digest", len(digest))

    # aes_decrypt = AES(key)

    # decrypted = aes_decrypt.decrypt(digest)
    # print("decrypted", decrypted)


if __name__ == "__main__":
    main()
