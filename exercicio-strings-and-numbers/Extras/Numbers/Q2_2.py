#Equipe-02
#Scrum master: Matheus Serrão Uchôa
#Devs:
#Paulo Henrique Munhoz
#Ana Beatriz Pimentel
#Kariny Oliveira


def int_factorial(int_number):                             #Function declaration
    int_factor = 1                                         #Variables int_factor and int_i receive 1
    int_i = 1

    while int_i <= int_number:                             #Repeat loop if value of i is less than and equal to n
        int_factor = int_factor * int_i                    #int_factor accumulator receives the values
        int_i+=1                                           #In each interaction the i is incremented
    print(int_factor)                                      #After the loop is finished, the value is shown on the screen


#main
int_number = int(input("Enter an integer value: "))        #Receiving an integer value
int_factorial(int_number)                               #Calling the fn_factorial function and sending the received value

