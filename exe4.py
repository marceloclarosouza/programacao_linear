''' 



'''

# Exercício 4
from pymprog import*

# Dados
P = [80, 90] # capacidade produtiva
D = [50, 40, 65] # demanda
CFP = [[10, 12, 20],
      [15, 8, 11]] # custos de fazenda para centros processamento
CPC = [[7, 7, 20],
      [8, 9, 10],
      [24, 8, 6]] # custos de centros de processamentos para clientes

n = len(P) # número de fazendas
l = len(D) # número de clientes
m = len(CPC) # número de centros de processamentos

begin("carnes") # iniciando um modelo
# variaveis de decisao
A = iprod(range(n), range(m)) # cria os indices da variavel x 
x = var("x", A) # cria a variavel x

B = iprod(range(m), range(l)) #cria os indices da variavel y
y = var("y", B) # cria a variavel y

# funcao objetivo
minimize(sum(CFP[i][j]*x[i,j] for i, j in A) + sum(CPC[j][k]*y[j,k] for j, k in B))

# restricoes
for k in range(l):
    sum(y[j,k] for j in range(m)) == D[k] # demanda

for i in range(n):
    sum(x[i,j] for j in range(m)) <= P[i] # capacidade produtiva

for j in range(m):
    sum(x[i,j] for i in range(n)) == sum(y[j,k] for k in range(l)) # fluxo 

# resolvendo
solve()

# apresentado a solução
print("Valor ótimo = {}".format(vobj()))

for i,j in A:
  print("x[{},{}] = {}".format(i+1,j+1,x[i,j].primal))

for j,k in B:
  print("y[{},{}] = {}".format(j+1,k+1,y[j,k].primal))

end()
