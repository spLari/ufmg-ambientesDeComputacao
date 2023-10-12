'''
Utilizando as estruturas de repetição, verifique se as seguintes sequências são uma sequência de 
DNA {A,G, T, C}, RNA {U, C, A, G}, PROTEÍNA {A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y} 
ou nenhuma delas (nesse caso, imprima as letras que não fazem parte do alfabeto):
ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN
TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT
ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN
'''
def check_dna(seq):
    dna = {'A', 'G', 'T', 'C'}
    return seq.difference(dna)

def check_rna(seq):
    rna = {'U', 'C', 'A', 'G'}
    return seq.difference(rna)

def check_protein(seq):
    protein = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}
    return seq.difference(protein)


seq_conj = {'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT',
            'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN'}

for seq in seq_conj:
    seq = set(seq)
    difference_dna = check_dna(seq)
    difference_rna = check_rna(seq)
    diffenrence_protein = check_protein(seq)

    print('Sequence: ', seq)
    if not difference_dna:
        print('The sequence is a DNA sequence')
    else:
        print('The sequence is not a DNA sequence.')
        print('The following letters do not belong: ', difference_dna)
    if not difference_rna:
        print('The sequence is a RNA sequence')
    else:
        print('The sequence is not a RNA sequence.')
        print('The following letters do not belong: ', difference_rna)
    if not diffenrence_protein:
        print('The sequence is a PROTEIN sequence')
    else:
        print('The sequence is not a PROTEIN sequence.')
        print('The following letters do not belong: ', diffenrence_protein)
    print('----------------------------------------------------------------------------------------------------------')
