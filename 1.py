'''
Um problema comum em bioinformática estrutural é a comparação entre estruturas moleculares. 
Nesse exercício, alinhamos estruturalmente dois resíduos de glicina (amarela e roxa - Figura 1) e
apresentamos as coordenadas tridimensionais (x, y, z) (Tabelas 1 e 2).
Considerando estas tabelas de coordenadas x, y, z dos átomos dos dois resíduos de glicina,
calcule o RMSD (Root Mean Square Deviation) entre elas segundo a Equação:

RMSD = sqrt(1/N * ∑(x1 − x 2)² + (y1 − y 2)² + (z1 − z2)²).

Considere N = 4 que é o número de átomos.
'''

import math

def exponential(n1, n2):
   return pow((n1-n2), 2)

def summatory(atomo1, atomo2):
  N = len(atomo1)
  add = 0
  x = 0
  y = 1
  z = 2
  for i in range(N):
    add += exponential(atomo1[i][x], atomo2[i][x]) + exponential(atomo1[i][y], atomo2[i][y]) + exponential(atomo1[i][z], atomo2[i][z])
  return add

at1 = [(108.304, 108.477, 109.907, 110.821), (100.827, 100.389, 100.555, 100.799), (67.992, 69.362, 69.817, 69.027)]
at2 = [(107.670, 108.477, 109.513, 110.667), (101.359, 100.389, 101.001, 100.572), (70.074, 69.362, 68.450, 68.425)]

rmsd = math.sqrt(summatory(at1, at2))
print("RMSD: ", rmsd)

    
