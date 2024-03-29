#9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
#de Restaurant deve armazenar dois atributos: restaurant_name e
#cuisine_type. Crie um método chamado describe_restaurant() que mostre
#essas duas informações, e um método de nome open_restaurant() que exiba
#uma mensagem informando que o restaurante está aberto.
#Crie uma instância chamada restaurant a partir de sua classe. Mostre os
#dois atributos individualmente e, em seguida, chame os dois métodos.

class Restaurant0:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Tipo de cozinha: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name} está aberto.")

# Criando uma instância da classe Restaurant
restaurant = Restaurant0("Nome do Restaurante", "Tipo de Cozinha")

# Mostrando os atributos individualmente
print("Nome do Restaurante:", restaurant.restaurant_name)
print("Tipo de Cozinha:", restaurant.cuisine_type)

# Chamando os métodos
restaurant.describe_restaurant()
restaurant.open_restaurant()

        
#9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
#instâncias diferentes da classe e chame describe_restaurant() para cada
#instância.

class Restaurant2:
    def __init__(self,restaurant_name2,cuisine_type2):
        self.restaurant_name2= restaurant_name2
        self.cuisine_type2=cuisine_type2  
    def describe_restaurant(self):
        print(f"Nome do restaurante: {self.restaurant_name}")
        print(f"Tipo de cozinha: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} está aberto!")

restaurant3=Restaurant0("pizza hot","USA")
restaurant4=Restaurant0("fogão dourado","brasil")
restaurant5=Restaurant0("clown joker","usa")

restaurant3.describe_restaurant()
restaurant4.describe_restaurant()
restaurant5.describe_restaurant()
#9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
#first_name e last_name e, então, crie vários outros atributos normalmente
#armazenados em um perfil de usuário. Escreva um método de nome
#describe_user() que apresente um resumo das informações do usuário. Escreva
#outro método chamado greet_user() que mostre uma saudação personalizada
#ao usuário.
#Crie várias instâncias que representem diferentes usuários e chame os dois
#métodos para cada usuário

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"O usuario tem e supervisor e faz aniversario em maio e vem trabalhar de bike")
    def greet_user(self):
        print(f"Como vai")
matthew=User("matthew",21)
zac=User("zac",24)
bruce=User("bruce",30)

matthew.describe_user()

zac.describe_user()
bruce.describe_user()

#9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
#225). Acrescente um atributo chamado number_served cujo valor default é 0.
#Crie uma instância chamada restaurant a partir dessa classe. Apresente o
#número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
#exiba-o novamente.
#Adicione um método chamado set_number_served() que permita definir o
#número de clientes atendidos. Chame esse método com um novo número e
#mostre o valor novamente.
#Acrescente um método chamado increment_number_served() que permita
#incrementar o número de clientes servidos. Chame esse método com qualquer
#número que você quiser e que represente quantos clientes foram atendidos, por
#exemplo, em um dia de funcionamento.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # novo atributo

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Criando uma instância da classe Restaurant
restaurant = Restaurant("The Best Restaurant", "Italian")
# Apresentando o número de clientes atendidos pelo restaurante
print("Número de clientes atendidos inicialmente:", restaurant.number_served)
# Alterando o número de clientes atendidos e exibindo-o novamente
restaurant.set_number_served(50)
print("Número de clientes atendidos após definir:", restaurant.number_served)
# Incrementando o número de clientes atendidos e exibindo-o novamente
restaurant.increment_number_served(20)
print("Número de clientes atendidos após incrementar:", restaurant.number_served)

#9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
#sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
#increment_login_attempts() que incremente o valor de login_attempts em 1.
#Escreva outro método chamado reset_login_attempts() que reinicie o valor de
#login_attempts com 0.
#Crie uma instância da classe User e chame increment_login_attempts()
#várias vezes. Exiba o valor de login_attempts para garantir que ele foi
#incrementado de forma apropriada e, em seguida, chame
#reset_login_attempts(). Exiba login_attempts novamente para garantir que
#seu valor foi reiniciado com 0.

