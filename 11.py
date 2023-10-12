'''
Considerando as assinaturas moleculares (fingerprints) hipotéticas das tabelas, calcule a distância
de Tanimoto conforme a equação a seguir:

D = A^B/ AvB
'''

def operador_and(m1, m2):
    result = []
    for i in range (len(m1)):
        if m1[i] == m2[i] and m2[i] == '1':
            result.append('1')
        else:
            result.append('0')

    return result

def operador_or(m1, m2):
    result = []
    for i in range (len(m1)):
        if m1[i] == '1' or m2[i] == '1':
            result.append('1')
        else:
            result.append('0')

    return result

def tanimoto_distance(v1, v2):
    numerator = v1.count('1')
    denominator = v2.count('1')

    return numerator/denominator

fingerprints_m1 = "001001101101"
fingerprints_m2 = "010011011000"

result_and = operador_and(fingerprints_m1, fingerprints_m2)
result_or = operador_or(fingerprints_m1, fingerprints_m2)

distance = tanimoto_distance(result_and, result_or)

print("Tanimoto Distance: ", distance)
