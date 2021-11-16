#DESENVOLVA UM ALGORITMO QUE SOLICITE AO USUÁRIO
# O PREÇO DE UM PRODUTO
# E UM PERCENTUAL DE DESCONTO A SER APLICADO A ELE
# CALCULE E EXIBA O VALOR DO DESCONTO E O PREÇO FINAL DO PRODUTO
# APOSTILA - EXERCÍCIO AULA 2
nome=input("Digite seu nome: ")
produto=input("Digite o nome do produto: ")
preco=float(input("Digite o valor do produto R$:"))
percentual=int(input("Digite o percentual (de 0 a 100 %) de desconto para este produto:"))
v_desconto=abs(preco*percentual)/100
total=preco-v_desconto
print("{} calculando o desconto de {}% no produto escolhido temos: {} - {}={}".format(nome,percentual,preco,v_desconto,total))

#SOLUÇÃO PROFESSOR
valor = float(input("Digite o preço do produto:"))
p= float(input("Digite o percentual de desconto (0-100)%:"))

desconto= valor * (p / 100)
final = valor - desconto

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto,final))