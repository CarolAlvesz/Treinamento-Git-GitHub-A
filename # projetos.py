# projetos 
print ('Aluguel de Carros')

nome = input('Informe o seu nome')
idade = int(input('Informe sua idade'))
if idade < 18:
    print("\n Desculpe, o cliente não pode alugar um carro por ser menor de idade.")
else:
    placa = input("Digite a placa do carro: ")
    valor_diaria = 150.00  
    dias = int(input("Quantos dias o carro será alugado? "))
  
# Cálculo do valor total
    valor_total = valor_diaria * dias

    # Exibição 
    print("\n--- Resumo do Aluguel ---")
    print(f"Nome do cliente: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Placa do carro: {placa}")
    print(f"Dias de uso: {dias}")
    print(f"Valor da diária: R$ {valor_diaria:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")

    print("\n Obrigado por utilizar nosso sistema!")
