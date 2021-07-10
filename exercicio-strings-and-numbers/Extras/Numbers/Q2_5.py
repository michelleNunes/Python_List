#Equipe-02
#Scrum master: Matheus Serrão Uchôa
#Devs:
#Paulo Henrique Munhoz
#Ana Beatriz Pimentel
#Kariny Oliveira


def fn_factorial(int_i):                            #Function declaration
    int_factorial = 1                               #Variables int_factorial and int_j receive 1
    int_j = 1

    while int_j <= int_i:                            #Repeat loop if value of int_j is less than and equal to int_i
        int_factorial = int_factorial * int_j        #int_factorial accumulator receives the values
        int_j = int_j+1                              #In each interaction the i is incremented
    return int_factorial                             #Return the result about factorial of the number

def int_superfactorial(n):                          #Function declaration
    mtz_superf = []                                 #Empty matrix
    multiply = 1                                    #variable multiply
    for i in range(1,n+1):                          #Repeat Loop to collect the factorials individuals values
        mtz_superf.append(fn_factorial(i))          #Add the values in the "matrix"  or better vector

    for w in range(0,len(mtz_superf)):              #Repeat Loop of 0 until size of the matrix
        multiply = multiply*mtz_superf[w]           #Multiplication of values
    print(multiply)                                 #Show the result


#main
int_number = int(input("Enter an integer value: "))     #Receives an integer value from the console
int_superfactorial(int_number)       #Calls the int_superfactorial function and passes the value received by the console

