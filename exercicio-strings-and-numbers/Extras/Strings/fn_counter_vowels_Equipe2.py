# Equipe-02
# Scrum master: Matheus Serrão Uchôa
# Devs:
# Paulo Henrique Munhoz
# Ana Beatriz Pimentel
# Kariny Oliveira

# vowels and consonants


# function to count the elements
def fn_counter(str_word):
    str_word = str_word.lower()  # change to lower case
    str_word = str_word.replace(" ", "")  # replace the blank spaces
    mat_str_vowels = 'aeiouAEIOU'  # dictionary of vowels
    int_countvowels, int_countconsonants = 0, 0  # initialize the counters

    for i in str_word:  # walk through the word
        if i in mat_str_vowels:  # compares with the dictionary
            int_countvowels += 1
        else:  # if consonant
            int_countconsonants += 1

    print("Vowels: ", int_countvowels, "Consonants: ", int_countconsonants)


# main
str_s = input("Enter the word: ")
if len(str_s) <= 20:
    fn_counter(str_s)
else:
    print("Word length more than expected")
