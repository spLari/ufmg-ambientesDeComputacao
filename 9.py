'''
Considerando a seguinte sequência e tabela de massas dada, escreva um programa em Python que
calcule a massa molar da sequência.
'''

def calculate_mol(sequence):
    molecular_weight = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
                        'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K':  128.09496, 'L': 113.08406, 
                        'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
                        'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
    converted_seq = set(sequence)
    weight = 0

    for molecule in converted_seq:
        if molecule in molecular_weight:
            repetions = sequence.count(molecule)
            weight += repetions * molecular_weight[molecule]

    return weight

seq = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"
molar_mass = calculate_mol(seq)

print("The molar mass of ", seq, "is ", molar_mass)