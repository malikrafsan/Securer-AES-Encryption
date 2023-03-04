#!/usr/bin/env python
from aes import AES


def main():
    msg = "rozan fadhil alhamdulillah masih hidup"
    key = "abcdefghij123456"
    aes = AES(key)
    digest = aes.encrypt(msg)

    print("digest", digest)

    decrypted = aes.decrypt(digest)
    print("decrypted", decrypted)


if __name__ == "__main__":
    main()
