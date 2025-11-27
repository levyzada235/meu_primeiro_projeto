# início do programa que pergunta o nome do usuário
# e exibe uma mensagem de boas vindas
name = str(input("Olá! Qual é o seu nome? "))
print(f"Muito prazer em te conhecer, {name}!")
           
# idade do programa
bot_age = 3
# pergunta ao usuário quantos anos ele tem
# e logo em seguida exibe a diferença de idade entre os dois, caso haja
age = int(input(f"E quantos anos você tem {name}? "))
age_difference = (age - bot_age)
if age == bot_age:
  print(f"Que coincidência! Eu também tenho {bot_age} anos!")
else:            
  print(f"Caramba! Então você é {age_difference} anos mais velho que eu. Eu só tenho {bot_age} anos.")

# cor favorita do programa
bot_color = ("Vermelho" and "vermelho")
# pergunta a cor favorita do usuário
# e exibe uma mensagem personalizada de acordo com a resposta do usuário
color = str(input("Qual é a sua cor preferida? "))
if color == bot_color:
  print(f"Que bom gosto você tem! A minha cor favorita também é {bot_color}!")
else:
  print(f"Realmente {color} é uma cor muito bonita! A minha cor favorita é {bot_color}!")
            
