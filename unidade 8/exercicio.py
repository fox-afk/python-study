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
