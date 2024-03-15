#3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
#chamada names. Exiba o nome de cada pessoa acessando cada elemento da
# lista, um de cada vez

names=['a','b','c','d']
print("nome:" + names[0])
print("nome:" + names[1])
print("nome:" + names[2])
print("nome:" + names[3])

# 3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
#  simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
#  O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
#  estar personalizada com o nome da pessoa.

saudacao=['bom dia','boa tarde','boa noite','ohayo']
print("Saudações:" + saudacao[0])
print("Saudações:" + saudacao[1])
print("Saudações:" + saudacao[2])
print("Saudações:" + saudacao[3])

# 3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
# motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
# lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
#  uma moto Honda”.

nomes_motos=['honda','yamaha','dafra','bmw']

print("nome de motos:"+ nomes_motos[0])
print("nome de motos:"+ nomes_motos[1])
print("nome de motos:"+ nomes_motos[2])
print("nome de motos:"+ nomes_motos[3])


#3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
#jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
#que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
#exibir uma mensagem para cada pessoa, convidando-a para jantar.

lista_pessoas_convidados=['jobs','jack','ryan']
print(lista_pessoas_convidados)
#3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para
# convidar.
#            • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
#                   no final de seu programa, especificando o nome do convidado que não
#                                                                     poderá comparecer.
#                 • Modifique sua lista, substituindo o nome do convidado que não poderá
#                          comparecer pelo nome da nova pessoa que você está convidando.
#                  • Exiba um segundo conjunto de mensagens com o convite, uma para cada
#                                              pessoa que continua presente em sua lista.



del lista_pessoas_convidados[1]  # eliminei um item da lista
print(lista_pessoas_convidados)   # exibe quem ira comparecer


# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.
#                                  • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
#                                      uma instrução print no final de seu programa informando às pessoas que
#                                                                   você encontrou uma mesa de jantar maior.

#                                 • Utilize insert() para adicionar um novo convidado no início de sua lista.
#                                   • Utilize insert() para adicionar um novo convidado no meio de sua lista.
#                                  • Utilize append() para adicionar um novo convidado no final de sua lista.
#                • Exiba um novo conjunto de mensagens de convite, uma para cada pessoaque está em sua lista.
lista_pessoas_convidados.insert(0,'pablo')
lista_pessoas_convidados.insert(0,'lucas')
lista_pessoas_convidados.insert(0,'eduardo')
print(lista_pessoas_convidados)


# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
#dois convidados.
#                                  • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
#                                     mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
#                                  • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
#                                     que apenas dois nomes permaneçam em sua lista. Sempre que remover um
#                                     nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
#                                          saiba que você sente muito por não poder convidá-la para o jantar.
#                                  • Apresente uma mensagem para cada uma das duas pessoas que continuam
#                                     na lista, permitindo que elas saibam que ainda estão convidadas.
#                                  • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
#                                     tenha uma lista vazia. Mostre sua lista para  garantir que você realmente tem uma lista vazia no final de seu programa.


del lista_pessoas_convidados[2]

print(lista_pessoas_convidados)