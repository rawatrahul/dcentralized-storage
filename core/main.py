import hashlib as hash
import os
import sys
sys.path.append('../')

from utils.encryption import decrypt_file,encrypt_file

def main():
    print("Login to node ")
    password = input("Enter your password: ")
    key =  hash.sha256(password.encode()).hexdigest()[:16]

    while True:
        o = input("Select your option:\n1. Download file\n2. Upload file\n3. Logout/Exit\n")
        if o == '2':
            os.chdir("../data")
            print(os.listdir())
            filename = input("Enter filename to upload\n")
            if filename in os.listdir():
                print("Encrypting file", filename)
                encrypt_file(key=key, in_filename=filename)
                
            else:
                print("Invalid filename")

        if o == '1':
            print("Decrypting file...")
            decrypt_file(key=key, in_filename=filename + ".enc", out_filename="../data/dec.png")

        if o == '3':
            exit(0)


if __name__ == '__main__':

    main()