# 6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
#que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
#cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
#age e city. Mostre cada informação armazenada em seu dicionário.

first_name={'bruce'}
last_name={'wayne'}
age={18}
city={'gotham'}
print(first_name)
print(last_name)
print(age)
print(city)

#6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
# de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
# dicionário. Pense em um número favorito para cada pessoa e armazene cada
# um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
# número favorito. Para que seja mais divertido ainda, faça uma enquete com
#alguns amigos e obtenha alguns dados reais para o seu programa.

numbers_favorites= {
    'andre':'10',
    'bruce':'2',
    'carlos':'3',
    'daniel':'5',}

for name , numero in numbers_favorites.items():
    print(name+ numero) 
    

# 6.3 – Glossário: Um dicionário Python pode ser usado para modelar um
#dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
#glossário.

# • Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores. Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
# • Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
# significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra
# de linha (\n) para inserir uma linha em branco entre cada par palavrasignificado em sua saída

glossario={'python':'saida','ruby':'entrada','js':'entrada','java':'entrada','c++':'game'}

print("Este e o glassario:"+ glossario['c++'].title())  # se mudar o que esta dentro do [] muda o que ira monstrar 

# 6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
# um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
# sequência de instruções print por um laço que percorra as chaves e os valores
# do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
# cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
#essas palavras e significados novos deverão ser automaticamente incluídos na
# saída.

glossario2={'pascal':1970,'basic':1960,'cobol':1950,'lisp':'I.A','fortran':'anciã'}

for key, value in glossario2.items():
    print("\nLinguagens:"+ key, value)


# 6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
# cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.

# • Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
# • Use um laço para exibir o nome de cada rio incluído no dicionário.
# • Use um laço para exibir o nome de cada país incluído no dicionário.

rios={'nilo':'egito','amazonas':'brasil','ganges':'india'}

for chave, valor in rios.items():
    print( chave, ":", valor)

# 6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).

# • Crie uma lista de pessoas que devam participar da enquete sobre linguagem
# favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.

# • Percorra a lista de pessoas que devem participar da enquete. Se elas já
#tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
#responder. Se ainda não participaram da enquete, apresente uma mensagem
#convidando-as a responder.


# 6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
# (página 147). Crie dois novos dicionários que representem pessoas diferentes e
# armazene os três dicionários em uma lista chamada people. Percorra sua lista
# de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
# você sabe sobre cada pessoa.

pessoas1={}

pessoas2={}

#6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
# dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
# o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
# chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
# fizer isso, apresente tudo que você sabe sobre cada animal de estimação.

animals={'mia':'brito','barry':'araujo','vi':'pereira'}

for chave , valor in animals.items():
   print(chave, ":",valor) 
# 6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
# três nomes para usar como chaves do dicionário e armazene de um a três
# lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
# interessante, peça a alguns amigos que nomeiem alguns de seus lugares
# favoritos. Percorra o dicionário com um laço e apresente o nome de cada
# pessoa e seus lugares favoritos.

favorite_places={
 'brasil':['cristo redentor','jardim botanico'],
 'eua':['estatua liberdade','central park','cataratas niagara'],
 'japão':['tokyo skytree','santuario meiji','itsukushima'],
 }   
for x , y in favorite_places.items():
    print("\n"+ x.title() +"  e pontos turisticos:" )
    for z in y:
        print("\t "+ z.title())
# 6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
# 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
# apresente o nome de cada pessoa, juntamente com seus números favoritos.
        
numbers_favorites2= {
    'ben':['10','24'],
    'gwen':['2','77'],
    'mary':['3','40'],
    'fiji':['8','22'],
            }
for name , numero2 in numbers_favorites2.items():
    print( name +" numeros favoritos:" )
    for xx in numero2:
        print("\t" + xx.title())
# 6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
# cidades como chaves em seu dicionário. Crie um dicionário com informações
# sobre cada cidade e inclua o país em que a cidade está localizada, a
# população aproximada e um fato sobre essa cidade. As chaves do dicionário
# de cada cidade devem ser algo como country, population e fact. Apresente o
# nome de cada cidade e todas as informações que você armazenou sobre ela.

cities={
    'japão':{
        'first':'kyoto','last':'asian','location':'tecnologia',},
    'brasil':{
        'first':'brasilia','last':'america do sul','location':'dance',},
    'espanha':{
        'first':'madrid','last':'europa','location':'churros',},      
}
for country,  population in cities.items:
    print("\nUsername: " + country)
    x= population['first'] + " " + population['last']
    location= population['location']
    print("\n"+ x )
    print("/tLocation: " + x)


# 6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
# bastante para poderem ser estendidos de várias maneiras. Use um dos
# programas de exemplo deste capítulo e estenda-o acrescentando novas chaves
# e valores, alterando o contexto do programa ou melhorando a formatação da saída.