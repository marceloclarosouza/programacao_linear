"""
Uma fabricante de bebidas possui dois centros de
produção localizados em Ribeirão Preto-SP e em
Cariacica-ES. A demanda para a próxima semana de
mercados consumidores situados em São Paulo, Belo
Horizonte e Rio de Janeiro são apresentadas abaixo,
bem como o custo unitário de se transportar 1 fardo
de bebida de cada centro de produção a cada mercado
consumidor, juntamente com as quantidades disponı́veis
em cada centro de produção.
A empresa deseja planejar qual a melhor forma de
atender à demanda de cada centro de consumo ao menor
custo de transporte possı́vel. Determine um modelo
de otimização e o implemente de forma a resolver o
problema proposto.
"""

from pymprog import*

# Dados de entrada
D = [960, 510, 895] # demandas
E = [1100, 1800] # estoques
C = [[3.7, 4.3, 6.1],
     [9.8, 6.9, 2.1]] # custos

n = len(E) # número de fábricas
m = len(D) # número de clientes

begin("transporte")

# variáveis
A = iprod(range(n), range(m)) # construindo os índices das variáveis
x = var('x', A, int) # cria nxm variáveis inteiras (x00, x01...x12)

# funçao objetiva
minimize(sum(C[i][j]*x[i,j]for i,j in A))

# restriçoes
for j in range(m):
    sum(x[i,j] for i in range(n)) == D[j] # atendimento da demanda

for i in range(n):
    sum(x[i,j] for j in range(m)) <= E[i] # estoque

# resolvendo
solve()

print("valor ótimo = {}".format(vobj()))

for i,j in A:
    print("x[{},{}] = {}".format(i+1, j+1, x[i,j].primal))

end()
