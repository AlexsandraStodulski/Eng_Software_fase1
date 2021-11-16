#EXECUTE AS SEGUINTES ATRIBUIÇÕES:
s1= 'ant'
s2= 'bat'
s3= 'cod'
print("Declaradas as variáveis com seus respectivos valores, temos: '{}','{}'e '{}'".format(s1,s2,s3))
print("UTILIZANDO OPERADORES + E *, CRIE AS SAÍDAS A SEGUIR:")
#a) 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3)
#b) 'ant ant ant ant ant ant ant ant ant ant'
print(10 * (s1 + ' '))
#c) 'ant bat bat cod cod cod'
print(s1 + ' ' + 2*(s2 + ' ') + 3*(s3 + ' ') )
#d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(7*(s1 + ' ' + s2+ ' '))
#d) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(5*(s2+s2+s3+' '))
