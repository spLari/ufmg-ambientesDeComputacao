'''
Escreva um programa que liste a tabuada (produtos) dos números de 1 a 15.
'''

def multiplication_table(num):
    for i in range(10):
        print(num, 'x', i, '=', num*i)


for i in range(1, 16, 1):
    print("Multiplication table of ", i)
    multiplication_table(i)
    print('-----------------------------------------')
