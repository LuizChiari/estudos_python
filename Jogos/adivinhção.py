print("********************************")
print("Bem vindo ao jogo da adivinhção!")
print("********************************")

numero_secreto = 42

chute_str = input("Digite seu Numero")

print("Voçê digitou", chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Voçê acertou!")
else:
    print ("Voçê errou!")

print("Fim de Jogo" )