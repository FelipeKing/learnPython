# varificar idade

print("Vamos concatenar para entrar no Bar!!!\n\n\n")

name = str(input("Digite o seu nome: "))
print("Bem vindo " + name + "\n\n")

number = int(input("digite o ano que você nasceu: "))
idade = int(2022 - number)

if idade >= 18:
    print(name + ", você tem " + str(idade) + " e pode entrar no bar!")
else:
    print(name + ", você tem " + str(idade) + " e não pode entrar no bar!")
