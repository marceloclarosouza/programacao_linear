from pymprog import*

# Dados de entrada
P = [10, 25, 20] # preço de venda por unidade
C = [6, 15, 14] # custo de produção
Qmin = [1000, 0, 100] # produção mínima
Qmax = [6000, 500, 1000] # produção máxima
D = [400, 400, 500, 2000] # disponibilidade de cada recurso
Q = [[0.03, 0.15, 0.1],
     [0.06, 0.12, 0.1],
     [0.05, 0.1, 0.12],
     [0, 2, 1.2]] # quantidade de cada recurso em cada produto


n = len(P) # número de produtos
m = len(D) # número de recursos

begin("utensílios de metal") # inicia um modelo
verbose("True")

# variáveis de decisão
x = var("x", n, int) # cria n variáveis inteiras (x0, x1, x2, ..., xn-1)

# função objetivos
maximize(sum((P[i] - C[i]) * x[i] for i in range(n)))

# retrições
for j in range(m):
  sum(Q[j][i] * x[i] for i in range(n)) <= D[j] # restrições de recursos

for i in range(n):
  x[i] <= Qmax[i]
  x[i] >= Qmin[i] # limite de produção

# resolvendo o modelo
solve()

# apresentando o resultado
print("Valor ótimo = {}".format(vobj()))

# solução ótima
for i in range(n):
  print("x[{}] = {}".format(i+1, x[i].primal))


# recursos utilizados
for j in range(m):
  print("recurso {}: {}".format(j+1,sum(Q[j][i] * x[i].primal for i in range(n))))  # restrições de recursos

end()
