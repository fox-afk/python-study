# 5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
# frase que descreva o teste e o resultado previsto para cada um. Seu código
#deverá ser semelhante a: car = 'subaru'

#       print("Is car == 'subaru'? I predict True."): print(car == 'subaru')
#       print("\nIs car == 'audi'? I predict False."): print(car == 'audi') 

# • Observe atentamente seus resultados e certifique-se de que compreende por que cada linha é avaliada como True ou False.
# • Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e outros cinco avaliados como False.
car = 'subaru'

#1.print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') 




# 5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que criar em dez. 
# Se quiser testar mais comparações, escreva outros testes e acrescente-os em conditional_tests.py.
# Tenha pelo menos um resultado True e umFalse para cada um dos casos a seguir: 

#                                           • testes de igualdade e de não igualdade com strings; 
#                                           • testes usando a função lower();
#                                           • testes numéricos queenvolvam igualdade e não igualdade, 
#                                              maior e menor que, maior ou igual a e menor ou igual a; 
#                                           • testes usando as palavras reservadas and e or; 
#                                           • testes para verificar se um item está em uma lista; 
#                                           • testes para verificar se um item não está em uma lista.

idade ='18'
print(idade=='19'.lower())
print(idade=='18'.lower())

# 5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser atingido em um jogo. 
#Crie uma variável chamada alien_color e atribua-lhe um valor igual a 'green', 'yellow' ou 'red'.

#                       • Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
#                       mostre uma mensagem informando que o jogador acabou de ganhar cinco pontos.
#                       • Escreva uma versão desse programa em que o teste if passe e outro em que
#                       ele falhe. (A versão que falha não terá nenhuma saída.) 

alien_color='green'

print("qual e a cor?")
if alien_color  is 'red':
    print("vermelho")
else:
    print("é verde")
   
#5.4 – Cores de alienígenas : Escolha uma cor para um alienígena, como foi feito no Exercício 5.3, e escreva uma cadeia if-else.

#       • Se a cor do alienígena for verde, mostre uma frase informando que o jogador acabou de ganhar cinco pontos por atingir o alienígena.
#       • Se a cor do alienígena não for verde, mostre uma frase informando que o jogador acabou de ganhar dez pontos.
#       • Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else.
if alien_color is 'green':
    print("O alien e verde,+5 pontos")
else:
    print("A cor do alien não é verde,ganhou 10 pontos")
# 5.5 – Cores de alienígenas: Transforme sua cadeia if-else do Exercício 5.4 em uma cadeia if-elif-else.

#       • Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
#       • Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
#       • Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
#       • Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.

if alien_color is 'green':
    print("o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos")
if alien_color is 'yellow':
    print(" o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos")
if alien_color is 'red':    
    print("o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos")

# 5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o estágio da vida de uma pessoa.
# Defina um valor para a variável age e então: 
#                           • Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
#                           • Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança.
#                           • Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem dizendo que ela é um(a) garoto(a).
#                           • Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensagem dizendo que ela é um(a) adolescente.
#                           • Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem dizendo que ela é adulto.
#                           • Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa pessoa é idoso.


# 5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma
# série de instruções if independentes que verifiquem se determinadas frutas estão em sua lista.
#                          • Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
#                          • Escreva cinco instruções if. Cada instrução deve verificar se uma
#                          determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
#                          frase, por exemplo, Você realmente gosta de bananas!
favore_fruits=['banana','maça','pera']
if 'banana' in favore_fruits: print("banana")
if 'maça' in favore_fruits:print("maça")
if 'pera' in favore_fruits:("pera")