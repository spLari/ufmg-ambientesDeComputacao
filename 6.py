'''
Utilizando as estruturas de repetição, gere e imprima a sequência complemento reverso da seguinte
sequência de DNA:

TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT
'''
def reverse_list(seq_str):
    reverse = []
    for i in reversed(seq_str):
        reverse.append(i)
    
    return ' '.join(reverse)

seq = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
seq_reversed = reverse_list(seq)
#remove the space of reversed sequence
seq_reversed = seq_reversed.replace(" ", "")

print('The sequence: ', seq)
print('The sequence reverse: ', seq_reversed)