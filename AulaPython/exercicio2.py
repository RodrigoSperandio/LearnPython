
print("Qual a idade da pessoa?")

idade = input("Idade? ")
idade = int(idade)

if idade < 16:
    print("Menor de idade")
elif idade > 18:
    print("Maior de idade")
elif idade < 18 > 17:
    print("Emancipado")

print(f'A pessoa tem a idade de: {idade} anos' )