# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira


# palindrome or not


# function that check the word
def fn_palindrome(str_word):
    str_word_min = str_word.lower()  # word in lower case
    str_word_min = str_word_min.replace(" ", "")  # replace the blank spaces
    str_word_rev = str_word_min[::-1]  # reverse the word

    if str_word_min == str_word_rev:  # compares with the word
        print("IS PALINDROME!")
    else:
        print("NOT PALINDROME!")


# main function
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    fn_palindrome(str_s)
else:
    print("Word length more than expected")

