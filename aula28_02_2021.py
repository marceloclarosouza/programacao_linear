"""
Uma metalúrgica produz dois tipos de ligas metálicas. 
Cada liga é composta de proporções diferentes de cobre, zinco e chumbo, os quais estão disponíveis em quantidades 
limitadas em estoque. Deseja-se determinar quanto produzir de cada liga, de modo a maximizar a receita bruta, 
satisfazendo as seguintes composições das ligas e a disponibilidade de matéria-prima em estoque:

"""

from pymprog import*

# Dados de entrada
r = [3, 2] # receita de cada liga
d = [3, 1, 3] #estoque de cada materia prima
p = [[0.5, 0.3],
     [0.1, 0.2],
     [0.4, 0.5]] # percentuais das materias primas nas ligas
n = len(r) # numero de ligas
m = len(d) # numero de materias primas


begin("ligas") # particularidade do pacote pymathprog p iniciar o modelo ligas

# variaveis de decisao

x = var("x", n) # cria n variaveis continuas (x0, x1, ... xn-1)

# funcao objetivo
maximize(sum(r[i]*x[i] for i in range(n)))

# restricoes
for j in range(m):
sum(p[j][i]*x[i] for i in range(n)) <= d[j]

# resolvendo o modelo
solve()

# apresentando a solucao
print(f"Valor otimo: {vobj()}")

print("Solucao otima")

for i in range(n):
print("x[{}] = {:.3f}". format(i+1, x[i].primal))

end()
