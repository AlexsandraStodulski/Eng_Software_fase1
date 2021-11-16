#"Escreva as seguintes EXPRESSÕES ALGÉBRICAS em Python")
print("a) O somatório dos 5 primeiros números inteiros e positivos:")
n1 = int(input("Digite o 1º número:"))
n2 = int(input("Digite o 2º número:"))
n3 = int(input("Digite o 3º número:"))
n4 = int(input("Digite o 4º número:"))
n5 = int(input("Digite o 5º número:"))
soma= n1+n2+n3+n4+n5
print ("A soma dos números que você digitou é: {}+{}+{}+{}+{}={}".format(n1,n2,n3,n4,n5,soma))
print("b) A média entre 23, 19 e 31")
media=(23+19+31)//3
print("A média entre os números dados é '{}':".format(media))
print("c) O número de vezes que 73 cabe em 403")
cabe=403//73
print("73 cabe '{}' vezes em 403".format(cabe))
print("d) A sobra quando 403 é dividido por 73")
sobra=403%73
print("A sobra da divisão de 403 por 73 é '{}'".format(sobra))
print("e) 2 elevado à 10ª potência")
p=2**10
print("2 elevado à 10ª potência é '{}'".format(p))
print("f) O valor absoluto da diferença entre 54 e 57")
valor_absoluto=abs(54-57)
print("O valor absoluto da diferença entre 54 e 57 é: '{}'".format(valor_absoluto))
print("g) O menor valor entre 34, 29 e 31")
mv=min(34, 29, 31)
print("O menor valor entre os números dados é:'{}'".format(mv))
