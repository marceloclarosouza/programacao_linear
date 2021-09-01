# Exercício 6
"""
Uma empresa possui 6 operadores que precisam
processar um conjunto de tarefas com tempos distintos
de execução. Cada tarefa pode ser realizada por
qualquer operador. Uma vez iniciada, a tarefa é
executada totalmente pelo operador. Determine uma
alocação de tarefas que minimize o makespan do
processo. Os tempos de execução das tarefas estão
presentes no arquivo tempos.txt no diretório Listas de
exercı́cios no Teams.
"""
from pymprog import*

# Dados de entrada
T = [54, 83, 15, 71, 77, 36, 53, 38, 27, 87, 76, 91, 14, 29, 12, 77, 32, 87, 
     68, 94, 79, 3, 11, 99, 56, 70, 99, 60, 5, 56, 3, 61, 73, 75, 47, 14, 21,
     86, 5, 77, 16, 89] # tempos de realização das tarefas

n = 6 # número de operadores
m = len(T) # número de tarefas

begin("tarefas") # inicia um modelo
# variáveis de decisão
A = iprod(range(n), range(m)) # indices da variável x
x = var('x', A, bool) # cria variável x
z = var('z') # cria variável para o makespan (variavel continua)


# funcao objetivo
minimize(z)

# restricoes
for j in range(m):
  sum(x[i,j] for i in range(n)) == 1 # alocacao de tarefas

for i in range(n):
  sum(T[j]*x[i,j] for j in range(m)) <= z # definicao do mekspan


# resolvendo
solve()
print("Valor ótimo = {}".format(vobj()))

for i in range(n):
  print("Operador {}: ".format(i+1), end=" ")
  for j in range(m):
    if round(x[i,j].primal) == 1:
      print("{} ({})   ".format(j+1,T[j]), end=" ")
  print()
  print()

end()
