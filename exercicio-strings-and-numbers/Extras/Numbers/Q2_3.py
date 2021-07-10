#Equipe-02
#Scrum master: Matheus Serrão Uchôa
#Devs:
#Paulo Henrique Munhoz
#Ana Beatriz Pimentel
#Kariny Oliveira


def fn_inverter(int_number):                           #Function declaration
    int_number = str(int_number)                       #Converts the number to a string, received by the variable rebmun
    str_rebmun = int_number[::-1]                      #Invert the word
    print(str_rebmun)                                  #Print the result


#main
int_number =int(input("Enter an integer value: "))   #Receive an integer value from the console
fn_inverter(int_number)                              #Calls the fn_inverter function and sends the entire received value

