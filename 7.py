'''
Escreva um programa que calcule o fatorial de um número recebido como entrada. Lembre-se que o
fatorial de um número é igual ao número multiplicado n sucessivamente por n-1, n-2, .. 1.
Exemplo: fat(6) = 6 x 5 x 4 x 3 x 2 x 1 = 720.
'''

def factorial(num):
    result = 1
    for i in range(1, num+1, 1):
        result *= i
    
    return result

user_input = int(input("Enter a number: "))
print('The factorial of %d is:'%user_input, factorial(user_input))

