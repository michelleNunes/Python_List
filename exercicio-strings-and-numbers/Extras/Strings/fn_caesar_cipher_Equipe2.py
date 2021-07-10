# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

# Caesar cipher

# Caesar cipher aims to encrypt a text using rotation, so it moves the elements of the text forward based on
# the number of rotations, so the developed function uses the ASCII value (ord - python) of each element to
# know if after the displacement is still within the limit of the alphabet Z. Otherwise after the Z it returns
# the letter A to continue scrolling.


def fn_encrypt(str_text, int_key):  # receive the text and key

    str_new = ""  # initialize the variable of the text after the encrypt
    for int_i in str_text:  # walk through the text
        if 'A' <= int_i <= 'Z':  # if the element is on upper case alphabet
            if ord(int_i) + int_key > ord('Z'):  # if the letter after moved exceed the letter Z
                str_new += chr((ord('A') + int_key - (ord('Z') + 1 - ord(int_i))))  # receive the new letter
            else:  # if the letter not exceed the letter Z
                str_new += chr(ord(int_i) + int_key)  # receive the new letter after rotation
        elif 'a' <= int_i <= 'z':  # if the letter is on lower case alphabet
            if ord(int_i) + int_key > ord('z'):
                str_new += chr((ord('a') + int_key - (ord('z') + 1 - ord(int_i))))
            else:
                str_new += chr(ord(int_i) + int_key)
        else:  # if is a number
            str_new += int_i
    print(str_new)


# main
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    int_key = int(input('Enter the number of rotations: '))
    fn_encrypt(str_s, int_key)
else:
    print("Word length more than expected")

