#Equipe-02
#Scrum master: Matheus Serrão Uchôa
#Devs:
#Paulo Henrique Munhoz
#Ana Beatriz Pimentel
#Kariny Oliveira


def fn_palindrome(str_number):                                       #Function declaration
    str(int_number)                                                  #Parse integer to String
    int_inverter = int_number[::-1]                                  #Inverts the number
    if int_number == int_inverter:                                   #Compare the original value with the inverted value
        print("IT'S PALINDROME!")                                    #Show on the screen: "IT'S PALINDROME!"
    else:
        print("IT IS NOT PALINDROME!")                               #Show on the screen: "IT IS NOT PALINDROME!"


#main
int_number = input("Enter an integer value: ")                   #Receives an integer value from the console
fn_palindrome(int_number)                                      #Call the palindrome function and send the informed value

