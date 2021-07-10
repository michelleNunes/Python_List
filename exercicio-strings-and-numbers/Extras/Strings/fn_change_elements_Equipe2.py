# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

# change the elements position


def fn_change(str_word):
    str_word = str_word.replace(" ", "")  # replace the blank spaces
    ctr_x = str_word[0]  # receive the first element
    ctr_x = str_word[1:(len(str_word))] + ctr_x  # change the elements and the first one will be the last
    print(ctr_x)


# main
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    fn_change(str_s)
else:
    print("Word length more than expected")

