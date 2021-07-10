#Equipe-02
#Scrum master: Matheus Serrão Uchôa
#Devs:
#Paulo Henrique Munhoz
#Ana Beatriz Pimentel
#Kariny Oliveira


def fn_hyperfactorial(int_number):                              #Function declaration
    int_result = 1                                              #Accumulator int_result is set to 1
    for i in range (int_number + 1):                            #The repeat loop goes from 1 to the last element
        int_result =int_result * pow(i,i)                       #Result always accumulates the powers of each value

    print(int_result)                                           #Show the result

#main
int_number =int(input("Enter an integer value: "))              #Receives an integer value from the console
fn_hyperfactorial(int_number)                  #Calls the hyperfat function and passes the value received by the console

