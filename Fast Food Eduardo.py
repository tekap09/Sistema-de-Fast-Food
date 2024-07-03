print('1. Hamburguer - R$10,00')
print('2. Batata Frita - R$5,00')
print('3. Refrigerante - R$4,00')
print('4. Sorvete - R$2,00')

n1 = float(input('digite sua opção: '))
n2 = float(input('digite a quantidade: '))
if n1 == 1:
    print("O pedido está em andamento.")
    print("15 minutos.")
    total = 10 * n2
    print('o total da sua compra é: ' ,total)

if n1 == 2:
    print("O pedido está em andamento.")
    print("5 minutos.")
    total = 5 * n2
    print('o total da sua compra é: ' ,total)
 
if n1 == 3:
    print("O pedido está em andamento.")
    print("1 minuto.")
    total = 4 * n2
    print('o total da sua compra é: ' ,total)
 
if n1 == 4:
    print("O pedido está em andamento.")
    print("30 segundos.")
    total = 2 * n2
    print('o total da sua compra é: ' ,total)
