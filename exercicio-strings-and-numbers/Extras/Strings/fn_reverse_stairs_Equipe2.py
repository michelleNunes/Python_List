# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

# Reverse Stairs


def fn_reverse_stairs(str_word):
    for i in range(len(str_word) - 1, 0, -1):  # walk through the string in decremental mode
        print(str_word[:i])


# main
str_s = input("Enter the word")
if len(str_s) <= 20:
    fn_reverse_stairs(str_s)
else:
    print("Word length more than expected")

