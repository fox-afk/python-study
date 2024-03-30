# 8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
#uma frase informando a todos o que você está aprendendo neste capítulo.
#Chame a função e certifique-se de que a mensagem seja exibida corretamente.

def greet_user():print("Hello, user!")
greet_user()     # chama a função

#8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
# um parâmetro title. A função deve exibir uma mensagem como Um dos meus
#livros favoritos é Alice no país das maravilhas. Chame a função e não se
#esqueça de incluir o título do livro como argumento na chamada da função.

#def favorite_book():print("meu livro favorito e alice no país das maravilhas".title())
#favorite_book()

# 8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
# tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
#A função deve exibir uma frase que mostre o tamanho da camiseta e a
#mensagem estampada.
#  Chame a função uma vez usando argumentos posicionais para criar uma
#   camiseta. Chame a função uma segunda vez usando argumentos nomeados.
                
#def make_shirt(shirt_type, text_name):
#    print("\nO tamanho da camisa " + shirt_type + ".") 
#    print("O tamanho da camisa é  " + shirt_type +" o texto na camisa é " + text_name.title() + ".")
#make_shirt('m', 'I love java')


#8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
#camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
#uma camiseta grande e outra média com a mensagem default, e uma camiseta
#de qualquer tamanho com uma mensagem diferente.

#def make_shirt(shirt_type, text_name):
 #   print("\no tamanho da camisa " + shirt_type)
  #  print("O tamanho da camisa é  " + shirt_type +" o texto na camisa é " + text_name.title() + ".")
#make_shirt('g','star wars')
#make_shirt('m','trem')
#make_shirt('p','nave')

#8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
#nome de uma cidade e seu país. A função deve exibir uma frase simples, como
#Reykjavik está localizada na Islândia. Forneça um valor default ao
#parâmetro que representa o país. Chame sua função para três cidades
#diferentes em que pelo menos uma delas não esteja no país default.

#def describe_city(type_cidade,type_pais):print("A cidade de "+ type_cidade + " está localizada no "  + type_pais)    
#describe_city('são paulo','brasil')
#describe_city('vancouver','canada')
#describe_city('moscou','russia')

# 8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
#aceite o nome de uma cidade e seu país. A função deve devolver uma string
#formatada assim: "Santiago, Chile"
#Chame sua função com pelo menos três pares cidade-país e apresente o valor
#devolvido.

#typecidade = input("Digite o nome da cidade: ")
#typepais = input("Digite o nome do pais: ")
#def city_country(typecidade,typepais):print(typecidade,typepais)
#city_country(typecidade,typepais)

#8.7 – Álbum: Escreva uma função chamada make_album() que construa um
#dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
#artista e o título de um álbum e deve devolver um dicionário contendo essas
#duas informações. Use a função para criar três dicionários que representem
#álbuns diferentes. Apresente cada valor devolvido para mostrar que os
#dicionários estão armazenando as informações do álbum corretamente.
#Acrescente um parâmetro opcional em make_album() que permita armazenar
#o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
#valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
#Faça pelo menos uma nova chamada da função incluindo o número de faixas
#em um álbum.

#album= input("Digite o album: ")
#artista= input("Digite o nome do artista (banda): ")
#def make_album(artista,album):print(artista,album)
#make_album(artista,album)

#8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
#Escreva um laço while que permita aos usuários fornecer o nome de um artista e
#o título de um álbum. Depois que tiver essas informações, chame make_album()
#com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
#um valor de saída no laço while.


#8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
#função chamada show_magicians() que exiba o nome de cada mágico da lista.
def show_magicians(magicians):
    """Exibe o nome de cada mágico na lista."""
    for magician in magicians:
        print(magician)

# Lista de nomes de mágicos
magicians = ['Merlin', 'Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

# Chamando a função para mostrar os mágicos
show_magicians(magicians)

#8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
#Exercício 8.9. Escreva uma função chamada make_great() que modifique a
#lista de mágicos acrescentando a expressão o Grande ao nome de cada
#mágico. Chame show_magicians() para ver se a lista foi realmente modificada.

def make_great(magicians2):
    """Exibe o nome de cada mágico na lista."""
    for magician in magicians2:
        print("É um grande magico "+ magician)
magicians2= ['Merlin', 'Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']
make_great( magicians2)

#8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
#Chame a função make_great() com uma cópia da lista de nomes de mágicos.
#Como a lista original não será alterada, devolva a nova lista e armazene-a em
#uma lista separada. Chame show_magicians() com cada lista para mostrar que
#você tem uma lista de nomes originais e uma lista com a expressão o Grande
#adicionada ao nome de cada mágico.

# def show_magicians():

#8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
#pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
#tantos itens quantos forem fornecidos pela chamada da função e deve
#apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
#um número diferente de argumentos a cada vez.

def fazer_sanduiche(*ingredientes):
    print("Resumo do sanduíche:")
    if ingredientes:
        print("Pão")
        for ingrediente in ingredientes:
            print("- " + ingrediente)
        print("Pão")
    else:
        print("Este sanduíche está vazio!")

# Chamadas da função com diferentes números de argumentos
fazer_sanduiche("Queijo", "Presunto", "Alface")
print()

fazer_sanduiche("Frango", "Tomate", "Maionese")
print()

fazer_sanduiche("Salame")

#8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
#210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
#e o sobrenome, além de três outros pares chave-valor que o descrevam.

def build_profile(first,last,**user_info):
    profile={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('bruce','wayne',location='gotham',field='rich')
print(user_profile)  
#8.14 – Carros: Escreva uma função que armazene informações sobre um carro
#em um dicionário. A função sempre deve receber o nome de um fabricante e um
#modelo. Um número arbitrário de argumentos nomeados então deverá ser
#aceito. Chame a função com as informações necessárias e dois outros pares
#nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
#apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
#color=’blue’, tow_package=True)  Mostre o dicionário devolvido para garantir
#que todas as informações foram armazenadas corretamente.

# EXEMPLO: 
        #       car = make_car(‘subaru’, ‘outback’,color=’blue’, tow_package=True)
def build_car(car,color,**user_info):
    profile={}
    profile['car'] = car
    profile['color'] = color
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_car('fiat','white',year=2012)
print(user_profile)  

    

#8.15 – Impressão de modelos: Coloque as funções do exemplo print_models.py
#em um arquivo separado de nome printing_functions.py. Escreva uma instrução
#import no início de print_models.py e modifique o arquivo para usar as funções
#importadas.



#8.16 – Importações: Usando um programa que você tenha escrito e que
#contenha uma única função, armazene essa função em um arquivo separado.
#Importe a função para o arquivo principal de seu programa e chame-a usando
#cada uma das seguintes abordagens: import nome_do_módulo from
#nome_do_módulo import nome_da_função from nome_do_módulo import
#nome_da_função as nf import nome_do_módulo as nm from nome_do_módulo import *

#8.17 – Estilizando funções: Escolha quaisquer três programas que você escreveu
#neste capítulo e garanta que estejam de acordo com as diretrizes de estilo
#descritas nesta seção.