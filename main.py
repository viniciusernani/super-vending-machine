## Super Vending Machine v0.1.0

# Definindo os produtos
produtos = ['Água Mineral','Pepsi Lata','Del Valle Goiaba','Água Tônica','Água de Coco','KitKat','Cheetos Bola','Amendoim Japonês','Pururuca']
preços = [3,5.5,4.8,4,5.2,6,6.3,4.5,4]

# Começando o programa
print("Bem-vindo!")

# Loop de escolha
certeza="N"

while certeza != "S":
	print("O que deseja?")
	
	# Mostrando lista de produtos
	print(f"1 - {produtos[0]} - Preço: R$ {preços[0]}")
	print(f"2 - {produtos[1]} - Preço: R$ {preços[1]}")
	print(f"3 - {produtos[2]} - Preço: R$ {preços[2]}")
	print(f"4 - {produtos[3]} - Preço: R$ {preços[3]}")
	print(f"5 - {produtos[4]} - Preço: R$ {preços[4]}")
	print(f"6 - {produtos[5]} - Preço: R$ {preços[5]}")
	print(f"7 - {produtos[6]} - Preço: R$ {preços[6]}")
	print(f"8 - {produtos[7]} - Preço: R$ {preços[7]}")
	print(f"9 - {produtos[8]} - Preço: R$ {preços[8]}")
	
	# Dando a escolha para o usuário
	escolha = int(input("Digite o número do produto que você deseja: \n"))
	
	# Mostrando o produto escolhido para o usuário
	print(f"Você escolheu: {escolha} - {produtos[escolha-1]}")
	print(f"O total será: R$ {preços[escolha-1]}")
	
	certeza = input("Tem certeza? Digite S para continuar")

# Pagamento
pagamento = float(input("Digite o valor de pagamento: \n"))

# Verificar o pagamento
if pagamento >= preços[escolha-1]:
	# Calculando o troco
	troco = round(pagamento - preços[escolha-1],2)
	print(f"Aqui está o seu troco: R$ {troco}")
	
	# Finalizando
	print("Volte sempre!")
else:
	print("Você não pagou o suficiente!")
	print("Valor devido: R$" + str(round(preços[escolha-1],2)))
	print("Valor pago: R$" + str(round(pagamento,2)))
	print("Falta: R$" + str(round((preços[escolha-1] - pagamento),2)))

