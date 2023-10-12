'''
Considerando a Tabela 2 que contem dados de defensinas de plantas, obtenha / calcule e imprima:
A) a menor sequência e seu comprimento
B) a maior sequência e seu comprimento
C) a média entre os comprimentos das sequências
D) a mediana entre os comprimentos das sequências
'''
def ascendingOrder(list_of_sequences):
    sorted_list = sorted(list_of_sequences, key=len)

    return sorted_list

def printSmallestSequence(list_of_sequences):
    sequences_list_ascending = ascendingOrder(list_of_sequences)
    print("The smallest sequence is:", sequences_list_ascending[0])
    print("Lenght:", len(sequences_list_ascending[0]))

def printGreatestSequence(list_of_sequences):
    sequences_list_ascending = ascendingOrder(list_of_sequences)
    lenght = len(sequences_list_ascending) - 1
    print("The greatest sequence is:", sequences_list_ascending[lenght])
    print("Lenght:", len(sequences_list_ascending[lenght]))

def average(list_of_sequences):
    result = 0
    for seq in list_of_sequences:
        result += len(seq)
    
    result = result/len(list_of_sequences)

    return result

def middle(list_of_sequences):
    average_list = []
    for seq in list_of_sequences:
        average_list.append(len(seq))

    average_list.sort()
    middle = int(len(average_list)/2)

    return average_list[middle]

seq1 = "KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC"
seq2 = "ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF"
seq3 = "ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN"
seq4 = "ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN"
seq5 = "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN"
seq6 = "ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR"
seq7 = "ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF"

sequences_list = [seq1, seq2, seq3, seq4, seq5, seq6, seq7]

printSmallestSequence(sequences_list)
printGreatestSequence(sequences_list)
print("The average of the lenght:", average(sequences_list))
print("The middle of the lenght is:", middle(sequences_list))



