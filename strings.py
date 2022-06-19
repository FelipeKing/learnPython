# metodos de strings

name = str(input("Digite seu nome: ")).strip().capitalize()
lastName = str(input("Digite seu sobrenome: ")).strip().capitalize()

fullName = f"{name} {lastName}"

lenName = len(name)
lenLastName = len(lastName)

totalLen = lenName + lenLastName

s = f"Olá {fullName}, seu nome tem {totalLen} caracteres."
print(s)
