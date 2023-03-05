#!/usr/bin/env python
from sys import getsizeof

from aes import AES


def main():
    # msg = "rozan fadhil alhamdulillah masyaallah subhanallah la ilaha illallah"
    # msg = "satutuju"
    # key = "abcdefghij12🥲"
    # aes_encrypt = AES(key)
    # digest = aes_encrypt.encrypt(msg)

    # print("len msg", len(msg))
    # print("digest", digest)
    # print("len digest", len(digest))

    # aes_decrypt = AES(key)

    # decrypted = aes_decrypt.decrypt(digest)
    # print("decrypted", decrypted)

    print("Selamat datang pada program enkripsi dan dekripsi algoritma SAES2")
    print("Pilih menu")
    print("1. Enkripsi")
    print("2. Dekripsi")
    menu = input("Menu: ")

    while (menu != "1" and menu != "2"):
        print("Menu tidak tersedia. Masukkan menu yang tersedia")
        menu = input("Menu: ")

    print("\nMasukkan teks yang akan dienkripsi")
    msg = input()
    print("\nMasukkan kunci yang akan digunakan sepanjang 128 bit")
    key = input("Kunci: ")
    while (len(key.encode('utf-8')) != 16):
        print("Panjang kunci: ", len(key.encode('utf-8')))
        print("Kunci harus sepanjang 128 bit. Masukkan kembali kunci yang akan digunakan")
        key = input("Kunci: ")

    if menu == "1":
        aes_encrypt = AES(key)
        digest = aes_encrypt.encrypt(msg)
        print("\nHasil enkripsi", digest)
    elif menu == "2":
        # TODO: translasi string of bytes to bytes

        aes_decrypt = AES(key)
        decrypted = aes_decrypt.decrypt(msg)
        print("\nHasil dekripsi", decrypted)


if __name__ == "__main__":
    main()
