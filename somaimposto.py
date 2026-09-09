def somarImposto(valor, taxa):
    return valor + (valor * taxa / 100)

valor = float(input("digite o valor do produto: "))
taxa = float(input("digite o valor da taxa: "))

valorImposto = somarImposto(valor, taxa)
print(f"Preço final com imposto: R$ {valorImposto}")