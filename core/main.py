from Crypto import Random
import os
import sys
sys.path.append('../')

from utils.encryption import decrypt_file,encrypt_file

def main():
    key = Random.new().read(16)
    print(os.listdir())
    filename = "../data/Bot.png"
    print("Encrypting file", filename )
    encrypt_file(key=key,in_filename=filename)
    print("Decrypting file...")
    decrypt_file(key=key,in_filename=filename+".enc",out_filename="../data/dec.png")


if __name__ == '__main__':
    main()