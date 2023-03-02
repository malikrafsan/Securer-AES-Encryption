#!/usr/bin/env python
from aes import AES


def main():
    print("halo")

    msg = "rozan fadhil alhamdulillah"
    aes = AES(0x2b7e151628aed2a6abf7158809cf4f3c)
    digest = aes.encrypt_all_msg(msg)

    print(digest)

    decrypted = aes.decrypt_all_msg(digest)
    print("decrypted", decrypted)


if __name__ == "__main__":
    main()
