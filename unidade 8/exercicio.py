# 8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
#uma frase informando a todos o que você está aprendendo neste capítulo.
#Chame a função e certifique-se de que a mensagem seja exibida corretamente.

def greet_user(): """Exibe uma saudação simples."""
print("Hello, user!")

greet_user()     # chama a função



#8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
# um parâmetro title. A função deve exibir uma mensagem como Um dos meus
#livros favoritos é Alice no país das maravilhas. Chame a função e não se
#esqueça de incluir o título do livro como argumento na chamada da função.

def favorite_book():
    print("meu livro favorito e alice no país das maravilhas".title())

favorite_book()

# 8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
# tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
#A função deve exibir uma frase que mostre o tamanho da camiseta e a
#mensagem estampada.
#  Chame a função uma vez usando argumentos posicionais para criar uma
#   camiseta. Chame a função uma segunda vez usando argumentos nomeados.
                
def make_shirt(shirt_type, text_name):
    print("\nO tamanho da camisa " + shirt_type + ".") 
    print("O tamanho da camisa é  " + shirt_type +" o texto na camisa é " + text_name.title() + ".")
make_shirt('m', 'I love java')


#8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
#camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
#uma camiseta grande e outra média com a mensagem default, e uma camiseta
#de qualquer tamanho com uma mensagem diferente.

def make_shirt(shirt_type, text_name):
    print("\no tamanho da camisa " + shirt_type)
    print("O tamanho da camisa é  " + shirt_type +" o texto na camisa é " + text_name.title() + ".")
make_shirt('g','star wars')
make_shirt('m','trem')
make_shirt('p','nave')
#8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
#nome de uma cidade e seu país. A função deve exibir uma frase simples, como
#Reykjavik está localizada na Islândia. Forneça um valor default ao
#parâmetro que representa o país. Chame sua função para três cidades
#diferentes em que pelo menos uma delas não esteja no país default.

def describe_city(type_cidade,type_pais):
    print("A cidade de "+ type_cidade + " está localizada no "  + type_pais)
    
describe_city('são paulo','brasil')
describe_city('vancouver','canada')
describe_city('moscou','russia')

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


#8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
#Exercício 8.9. Escreva uma função chamada make_great() que modifique a
#lista de mágicos acrescentando a expressão o Grande ao nome de cada
#mágico. Chame show_magicians() para ver se a lista foi realmente modificada.

#8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
#Chame a função make_great() com uma cópia da lista de nomes de mágicos.
#Como a lista original não será alterada, devolva a nova lista e armazene-a em
#uma lista separada. Chame show_magicians() com cada lista para mostrar que
#você tem uma lista de nomes originais e uma lista com a expressão o Grande
#adicionada ao nome de cada mágico.