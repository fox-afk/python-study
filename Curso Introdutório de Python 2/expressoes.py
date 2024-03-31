#1. Calcule o resto da divisão de 10 por 3

def calculo():
  print(  10 / 3)
calculo()

# tabuada do 13

def tabuada13 ():
    for i in range(1,11): 
        resultado=13*i
    print(f"13 x",i, "=",resultado)
tabuada13()
#Davi não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber
#quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

# 1 mes tem 4 semananas


#Você e os outros integrantes da sua república (Julius, Michael, David e Jack) foram no supermercado e
#compraram alguns itens:

#• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
#• 2 pacotes de macarrão: R$ 8,73 cada
#• 1 pacote de Molho de tomate: R$ 3,45
#• 420g Cebola: R$ 5,40/kg
#• 250g de Alho: R$ 30/kg
#• 450g de pães franceses: R$ 25/kg
#Calcule quanto ficou para cada um.

latas=2.20 *75 # 165
macarrao=2*8.73 # 17,45
tomate=3.45
cebola= 0.42 *5.40 # 2.268
alho=0.25*30
pao=0.45*25

calculo=latas+macarrao+cebola+alho+pao+tomate
divi=calculo/4
print(f"total: {calculo} se for dividido fica {divi}")

