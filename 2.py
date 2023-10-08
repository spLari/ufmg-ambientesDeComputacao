'''
Em biologia molecular, o conteúdo GC (guanina e citosina) é o percentual de bases nitrogenadas em uma
molécula de DNA ou RNA que são guanina ou citosina (dentre as quatro bases possíveis). Para as seguintes
sequências calcule usando os operadores vistos em aula o percentual de conteúdo GC, imprimindo os
resultados.
'''

def calcPercent (seq):
    size = len(seq)
    g_content = seq.count('G')
    c_content = seq.count('C')
    percent = (g_content+c_content)/size*100

    return percent

seqA = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
seqB = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'

print('Percent of GC content in sequence A: %0.2f' % calcPercent(seqA))
print('Percent of GC content in sequence B: %0.2f' % calcPercent(seqB))