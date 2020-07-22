"""
Student: Asaf Yosef Ben Shabat
ID: 312391774
Assignment no. 4
Program: crypto.py
"""
action = input("Enter k for random keys generator\nEnter e for encrypt\nEnter d for decrypt"
               "\npress nothing to exit:")
abc = 'abcdefghijklmnopqrstuvwxyz'
while True:
    if action == 'k':
        from random import sample

        f = open("key.txt", "w")
        random_encryption_key = sample(set(abc), 26)  # generates an abc dict with no duplication of letters
        f.write(''.join(random_encryption_key))
        f.close()
        action = input("Enter letter for using other action, press any else key to exit:")
    if action == 'e':
        keys_list = [c for c in open('key.txt').read().lower() if c != '\n' if c != ' ']
        values = [i for i in abc]
        encrypt_dict = dict(zip(keys_list, values))  # creating an encrypt dict of abc by the letters in ket.txt
        char_list = [ch for ch in open('plaintext.txt').read().lower() if ch in abc]
        # char_list comprehension used to encrypt letters only and capital letters as lowers .
        f = open("ciphertext.txt", "w")
        data_list = [encrypt_dict[i] for i in char_list]  # encrypting char_list
        for letter in data_list:
            f.write(letter)
        f.close()
        action = input("Enter letter for using other action, press any else key to exit:")
    if action == 'd':
        keys_list = [c for c in open('key.txt').read().lower() if c != '\n' if c != ' ']
        values = [i for i in abc]
        encrypt_dict = dict(zip(keys_list, values))
        # overwrite encrypt_dict to use the correct keys in key.txt if client did not used "k"
        keys_list = [c for c in open('ciphertext.txt').read().lower()]
        m = []
        for i in keys_list:  # writing the decrypted string in decrypted.txt
            m.append("".join([k for k, v in encrypt_dict.items() if v == i]))  # finds keys by values
        f = open("decrypted.txt", "w")
        for i in m:
            f.write(i)
        f.close()
        print()
        action = input("Enter letter for using other action, press any else key to exit:")
    else:
        break
