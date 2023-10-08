'''
Para os exercícios desta lista, considere a seguinte lista de sequências e faça programas em Python que
execute as tarefas descritas abaixo:

1. Imprima apenas as sequências com 80 ou mais aminoácidos.
2. Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências.
3. Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P).
4. Identifique e imprima a maior dentre as três sequências a seguir.
5. Imprima as três sequências em ordem crescente de tamanho.
'''

def printSequenceWithLimitOfCaracters(list_of_sequences, limit=80):
    for seq in list_of_sequences:
        if len(seq) >= limit:
            print(seq)

def getSequencesLengthAverage(list_of_sequences):
    average = 0
    for seq in list_of_sequences:
        average += len(seq)
    
    average = average/len(list_of_sequences)

    return int(average)

def printSequencesWithAminoacidsRestriction(list_of_sequences):
    for seq in list_of_sequences:
        if seq.count('H') > 0 and seq.count('P') < 1:
            print(seq)

def printGreatestSequence(list_of_sequences):
    biggest = list_of_sequences[0] #let, by defaut, the biggest sequence the first sequence.
    for seq in list_of_sequences:
        if len(seq) > len(biggest):
           biggest = seq

    print(biggest)

def printSequencesInAscendingOrder(list_of_sequences):
    sorted_list = sorted(list_of_sequences, key=len)

    print(sorted_list)


seqA = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
seqB = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
seqC = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

seqList = [seqA, seqB, seqC]

print('Sequences with 80 ou more aminoacids:')
printSequenceWithLimitOfCaracters(seqList)
print('-------------------------------------------------------------------------------------------------')
print('Sequences with length greater than average of length of sequences:')
limit = getSequencesLengthAverage(seqList)
printSequenceWithLimitOfCaracters(seqList, limit)
print('-------------------------------------------------------------------------------------------------')
print('Sequences with one or more histidine (H) and none proline (P):')
printSequencesWithAminoacidsRestriction(seqList)
print('-------------------------------------------------------------------------------------------------')
print('Print the greatest sequence:')
printGreatestSequence(seqList)
print('-------------------------------------------------------------------------------------------------')
print('Show the three sequences in ascending order:')
printSequencesInAscendingOrder(seqList)