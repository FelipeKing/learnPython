# alguel carro
# parametros: 60 reais por dia e 0,15 por km

days = int(input("Digite quantos diárias foram usadas: "))
kms = float(input("Quilometros percorridos: "))

valor = days * 60 + kms * 0.15
s = f"Deverá ser pago {valor} reais"
print(s)
