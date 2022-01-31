from simplecrypt import encrypt, decrypt

encrypted = open("encrypted.bin", "rb").read()
passwords = open("passwords.txt").readlines()

for p in passwords:
    p = p.strip()
    try:
        s = decrypt(p, encrypted)
    except:
        continue

    print(s.decode('utf-8'))
