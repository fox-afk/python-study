# 7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário
# qual tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse
# carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”

carro = input("Qual carro deseja?") 
print("\nÉ um " + carro + " que você deseja")
# 7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
# quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
# oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
# contrário, informe que sua mesa está pronta.
number = int (input("Quantas pessoas? ")  )
if number >= 8:
    print("Vão ter que esperar a mesa ficar pronta")
else:
    print("a mesa está pronta")
# 7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
# número é múltiplo de dez ou não
    
# Solicita ao usuário que insira um número
numero = int(input("Por favor, insira um número: "))

# Verifica se o número é múltiplo de dez
if numero % 10 == 0:
    print(f"O número {numero} é múltiplo de dez.")
else:
    print(f"O número {numero} não é múltiplo de dez.")


# 7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
# fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
# fornecido. À medida que cada ingrediente é especificado, apresente uma
# mensagem informando que você acrescentará esse ingrediente à pizza.


# 7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
# de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
# ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
# dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
# informe-lhes o preço do ingresso do cinema.

print('menos de 3 anos entrada gratuita')
print('3 e 12 anos custa 10 dolares')
print('mais de 12 anos custa 15 dolares')
ingresso= int(input("Digite a idade : "))

if ingresso < 3 :print('Ingresso gratuito')
if ingresso == 3  or ingresso  <= 12:print('10 dolares dolares')
if ingresso > 12:print('custa 15 dolares')

# 7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
# 7.5 que faça o seguinte, pelo menos uma vez: 
#   • use um teste condicional na instrução while para encerrar o laço; 
#   • use uma variável active para controlar o tempo que o laço executará;
#   • use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.
active = True

while active:
    idade = input("Por favor, informe a idade ou digite 'quit' para sair: ")
    
    if idade == 'quit':
        active = False
    else:
        idade = int(idade)
        
        if idade < 3:
            print("O ingresso é gratuito.")
        elif 3 <= idade <= 12:
            print("O ingresso custa $10 dólares.")
        else:
            print("O ingresso custa $15 dólares.")
# 7.7 – Infinito: Escreva um laço que nunca termine e execute-o. (Para encerrar o
# laço, pressione CTRL-C ou feche a janela que está exibindo a saída.

while True:
    print("Este é um loop infinito!")   

# 7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
# os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
# finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
# mostre uma mensagem para cada pedido, por exemplo, Preparei seu
# sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
# para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
# prontos, mostre uma mensagem que liste cada sanduíche preparado.

# Cria a lista de pedidos de sanduíches
sandwich_orders = ["sanduíche de frango", "sanduíche de carne", "sanduíche vegetariano", "sanduíche de presunto"]

# Cria a lista de sanduíches prontos
finished_sandwiches = []

# Percorre a lista de pedidos de sanduíches
for sandwich in sandwich_orders:
    print(f"Preparando seu {sandwich}...")
    # Simula a preparação do sanduíche
    print(f"Sanduíche de {sandwich} pronto!")
    # Transfere o sanduíche preparado para a lista de sanduíches prontos
    finished_sandwiches.append(sandwich)

# Mostra uma mensagem com os sanduíches preparados
print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)


# 7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
# que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
# Acrescente um código próximo ao início de seu programa para exibir uma
# mensagem informando que a lanchonete está sem pastrami e, então, use um
# laço while para remover todas as ocorrências de 'pastrami' e
# sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
# finished_sandwiches.
  
sandwich_orders = ["pastrami", "sanduíche de frango", "pastrami", "sanduíche de carne", "sanduíche de presunto", "pastrami", "sanduíche vegetariano"]

# Exibe mensagem informando que a lanchonete está sem pastrami
print("Desculpe, estamos sem pastrami.")

# Usa um laço while para remover todas as ocorrências de 'pastrami' de sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Cria a lista de sanduíches prontos
finished_sandwiches = []

# Percorre a lista de pedidos de sanduíches
for sandwich in sandwich_orders:
    print(f"Preparando seu {sandwich}...")
    # Simula a preparação do sanduíche
    print(f"Sanduíche de {sandwich} pronto!")
    # Transfere o sanduíche preparado para a lista de sanduíches prontos
    finished_sandwiches.append(sandwich)

# Mostra uma mensagem com os sanduíches preparados
print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)

# 7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
# férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
# pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
# código que apresente os resultados da enquete.