# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lists.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 03:35:49 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 04:07:47 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Vamos faloar sobre listas")
print("Lista é uma struct e pode aceitar mais de um\ntipo de variável")
print("\nExemplo:")
lista_exemplo = ["Luís", 0, True]
print("Considere a lista_exemplo = [\"Luís\", 0, True]")
print("Irá retorna para lista_exemplo[0], " + str(lista_exemplo[0]))
print("para lista_exemplo[1], " + str(lista_exemplo[1]))

friends = ["Peu", "Caio", "Ramon", "Pedro", "Walter"]

print("\nExemplo de lista de 'strins':")
print("friends = [\"Peu\", \"Caio\", \"Ramon\", \"Pedro\", \"Walter\"]")
print("print(friends) = " + str(friends))
print("print(friends[0]) = " + str(friends[0])) # = Peu
print("print(friends[-1]) = " + str(friends[-1])) # = Walter
print("print(friends[1:]) = " + str(friends[1:])) # = ['Peu', 'Caio', 'Ramon', 'Pedro']
print("print(friends[1:3]) = " + str(friends[1:3]))
print("\nPodemos mudar os elementos de uma lista\ncom a atribuição friends[0] = \"Pedro\"")
friends[0] = "Pedro"
print("Nossa lista fica: " + str(friends))
