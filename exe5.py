"""
Uma fábrica de refrigerantes produz dois tipos de
bebidas por meio de um único tanque. Para processar
1000 litros da bebida 1 são necessárias 100 horas do
tanque, enquanto para 1000 litros da bebida 2, são
necessárias 80 horas. A produção de uma bebida em
um dado perı́odo requer a limpeza e resfriamento do
tanque. Esse tempo é de 12 horas para a bebida 1 e
8 horas para a bebida 2. A disponibilidade do tanque
para a fabricação destas bebidas nos próximos 3 meses é
de 250, 320 e 200 horas. O departamento de vendas fez
uma previsão de demanda para os próximos 3 meses. A
demanda de cada bebida e os possı́veis custos envolvidos
são dados na tabela a seguir.
Determine quanto produzir e estocar de cada bebida em
cada perı́odo a fim de minimizar o custo total.
"""

from pymprog import*
 
# Dados de entrada
D = [[900, 1500, 1300],
     [700, 900, 800]] # Demandas das bebidas por período
C = [[1.5, 1.5, 2],
     [0.5, 0.5, 0.8]] # Custo de produção das bebidas por período
CE = [[0.5, 0.25, 0],
      [0.25, 0.25, 0]] # Custo da Estocagem das bebidas por período
CP = [[200, 400, 400], 
      [400, 500, 500]] # Custo de Preparo/Limpeza do tanque por período
T = [(100/1000), (80/1000)] # Tempo de produção por litro das bebidas
TP = [12, 8] # Tempo de Preparo/Limpeza do Tanque por bebida
TD = [250, 320, 200] # Tempo disponível do tanque no período
M = 6100
 
n = len(TP) # número de bebidas
m = len(TD) # número de períodos
 
begin("bebidas") # inicia um modelo
# variáveis de decisão
A = iprod(range(n), range(m)) # índices da variável x e s
B = iprod(range(n), range (-1, m)) # índices da variável y
x = var("x", A) # cria variável x
y = var("y", B) # cria variável y
s = var("s", A, bool) # cria a variável s
 
# função objetivo
minimize(sum(C[i][j] * x[i,j] for i, j in A) + sum(CE[i][j] * y[i,j] for i, j in B) + sum(CP[i][j] * s[i,j] for i, j in A))
 
# restrições
for i,j in A:
    (x[i,j] + y[i,j-1] - y[i,j]) == D[i][j] # atendimento da demanda
 
for i in range(n):
  y[i,-1] == 0 # estoque inicial nulo
 
for j in range(m):
  (sum(T[i] * x[i,j] for i in range(n)) + sum(TP[i] * s[i,j] for i in range(n))) <= TD[j] # tempo do tanque
 
for i,j in A:
  x[i,j] <= (M * s[i,j])
 
# resolvendo
solve()
 
print("Valor ótimo = {}".format(vobj()))
 
for i, j in A:
  print("x[{},{}] = {:.2f}".format(i+1, j+1, x[i,j].primal))
 
for i, j in B:
  print("y[{},{}] = {:.2f}".format(i+1, j+1, y[i,j].primal))
 
end()