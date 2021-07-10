# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

#  print the word in ascendent


def fn_ascendent(str_word):
    str_word = str_word.replace(" ", "")  # replace the blank spaces
    str_word = sorted(str_word)  # sort the letters
    str_word = ''.join(str_word)  # join the letters in str_word
    print(str_word)  # print


# main function
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    fn_ascendent(str_s)
else:
    print("Word length more than expected")
