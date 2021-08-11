""""
Uma fábrica de alimentos deseja produzir um novo
sabor de barra de cereais. Os requisitos nutricionais
exigem que as barras tenham certas quantidades
mı́nimas e máximas de certos nutrientes principais,
sendo: no mı́nimo 22% de fibra e 7% de proteı́na; e
no máximo 55% de carboidrato e 8% de gordura. Para
produzir as barras, a fábrica usará como ingredientes,
farinha de cereais, mel, soja e banana.

A fábrica deseja determinar em que quantidades os
ingredientes devem ser misturados de modo a produzir
1 kg da barra de cereais que satisfaça as restrições
nutricionais e tenha custo mı́nimo.
"""

from pymprog import*

# Dados de entrada
C = [5.20, 6.80, 7.10, 2.50] # custo das barras
N = [0.22, 0.07, 0.55, 0.08] # necessidade de cada nutriente
Q = [[0.26, 0.01, 0.25, 0.10],
     [0.05, 0.05, 0.26, 0.02],
     [0.60, 0.75, 0.45, 0.24],
     [0.07, 0.00, 0.01, 0.01]] # quantidade de cada nutriente em cada ingrediente

n = len(C) # quantidade de ingredientes
m = len(N) # necessidades de nutrientes
M = 2 # quantidade de requisitos mínimos(o restante é de máximo)

begin("barra de cereal") # inicia um modelo
verbose("True")
# Variáveis de Decisão
x = var("x", n) # cria n váriaveis (x0, x1, ..., xn-1)

# função objetivo
minimize(sum(C[i] * x[i] for i in range(n)))

# retrições
for j in range(m):
  if j < M:
    sum(Q[j][i] * x[i] for i in range(n)) >= N[j]
  elif j >= M:
    sum(Q[j][i] * x[i] for i in range(n)) <= N[j]

sum(x[i] for i in range(n)) == 1

# resolvendo o modelo
solve()

#Apresentando a Solução
print("Valor ótimo: {}".format(vobj()))
print("Solução ótima")
for i in range(n):
  print("x[{}] = {:.2f}".format(i+1, x[i].primal))

#Recursos Utilizados
for j in range(m):
  print("Recurso {}: {:.2f}".format(j+1, sum(Q[j][i] * x[i].primal for i in range(n))))

end()