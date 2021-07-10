# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

# reverse string


# function that check the word
def fn_reverse(str_word):
    str_reverse = str_word[::-1]  # reverse the word
    print(str_reverse)  # print


# main function
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    fn_reverse(str_s)
else:
    print("Word length more than expected")
