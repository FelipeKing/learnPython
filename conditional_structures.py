# verificando notas de alunos
# tirando casas depois da virgula
# usando estrutura condicional

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notaFinal = (nota1 + nota2 + nota3) / 3

if notaFinal < 5:
    s = f"Nota final {round(notaFinal,2)}, reprovado."
elif notaFinal < 6:
    s = f"Nota final {round(notaFinal,2)}, encaminhar para exame."
else:
    s = f"Nota final {round(notaFinal,2)}, aprovado."

print(s)
