import smtplib,time
itens = [['1- Arroz','2- Feijão','3- Farinha','4- Macarrão','5- Açucar','6- Oleo','7- Biscoito água e sal','8- Sal','9- Biscoito recheado','10- Leite','11- café','12- Creme de leite','13- Leite condensado','14- Maionese','15- Katchup','16- azeitona','17- nescau','18- ovo','19- miojo'],['1- Banana (unidade)','2- goiaba (unidade)','3- Laranja comum ( Unidade)','4- Abacaxi (Unidade)','5- Maracujá (unidade)','6- laranja cravo (unidade)','7- Limão(unidade)','8- Caju(unidade)','9- Acerola(unidade)'],['1- Batata doce (kg)','2- Cará (kg)','3- Cenoura','4- Jerimum (kg)','5- Macaxeira (kg)','6- Rabanete','7- Quiabo (15 Un)','8- Tomate (kg)','9- Cebola(kg)','10- Pepino(unidade)','11- Coentro(unidade)','12-Alface (unidade)','13- coco(unidade)'],['1- Sanitária','2-Sabão','3- Sabonete','4- Detergente','5- desinfetante', '6- Contonete','7- Algodão','8- Fósforo','9- Acetona','10- Bombril','11- Papel higiênico','12- Creme dental']]
precos = [[4.30,5.50,2.80,3.20,2.50,9.50,2.50,3.50,1.00,3.50,3.50,2.85,5.00,2.50,2.50,1.50,3.75,6.00,0.80],[0.25,1.20,0.50,7.00,1.80,1.50,0.99,0.50,0.80],[4.00,5.00,3.00,1.60,4.00,2.50,2.00,2.50,2.25,0.80,0.90,0.75,3.00],[4.80,3.20,0.80,2.50,4.25,0.80,0.75,0.80,1.20,0.80,2.30,1.50]]
estoque = [[100, 100, 100, 100, 100, 50, 25, 50, 25, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100], [50,50,100,100 ,50, 100, 190, 150 , 100],[150, 100, 50, 100, 150, 140, 450, 150, 100, 100, 100, 100, 120],[110, 100, 100, 100, 10, 100, 100, 100, 100, 100, 100, 100]]

setores = ['1- Cesta básica','2- frutas','3- Verdura ','4- Material de limpeza']
carrinho = list()
quantidade = list()
total = 0
notafiscal = str()
g = 0
zip(itens, estoque)
print(" ")
print('****************************************************')
print(" ")
print('                  BEM VINDO(A)')
print(" ")
print('ESCOLHA UM SETOR PARA COMEÇAR A FAZER SUAS COMPRAS')
print(" ")
print('****************************************************')
time.sleep(3)
op = 1
while op != 0 :
    print("Setores")
    print(" ")
    print("0- Sair")
    for i in range(0,len(setores)) :
        print(setores[i])
    print("5- Finalizar Compra\n6- Abrir estoque")

    print(" ")
    op = int(input("Insira Número do Setor: "))
    print(" ")
    if op != 0 and op < 5 :
        i = op -1
        for j in range(0,len(precos[i])) :
            print('-- itens---valor-------estoque\n')
            print(itens[i][j],'   ',precos[i][j],'      ', estoque[i][j],'\n')
        opcao = 1
        while opcao != 0 :
            print(" ")
            opcao = int(input("Nº do Iten ou Digite 0 para Voltar: "))
            print(" ")
            h = opcao -1
            if opcao != 0 :
                quantidade = (int(input("Insira a Quantidade do Produto: ")))
                print(" ")
                if quantidade <= estoque[i][h] :
                  estoque[i][h] -= quantidade
                  carrinho.append(f'{itens[i][h]:<25}{precos[i][h]:<7}{quantidade:<5}{precos[i][h]*quantidade}\n')
                  total += precos[i][h]*quantidade
                  g += 1
                  print("Total do Carrinho: ",total)
                else:
                  print('Quantidade insuficiente ')
    elif op != 0 and op == 5 :
        print(" ")
        nome = str(input('Insira Nome do Cliente: '))
        print(" ")
        endereco = str(input("Insira Endereço do Cliente: "))
        print(" ")
        pagamento = str(input("Insira Forma de Pagamento (Dinheiro),(Débito) ou (Crédito): "))
        op = 0
        print(" ")
 
            
        
notafiscal += str("------------------------------------------------\n")
notafiscal += str("---------------nota fiscal------------------\n")
notafiscal += str("------------------------------------------------\n")
notafiscal += str(f'Nome                   Preco  Qnt  Total\n')

for i in carrinho:
    notafiscal += i
notafiscal += str("------------------------------------------------\n")
notafiscal += str(f'total a ser pago{total:>25}\n\n')
notafiscal += str(f'Nome: {nome}\n')
notafiscal += str(f'Endereco: {endereco}\n')
notafiscal += str(f'Pagamento: {pagamento}\n')
print(notafiscal)   

arquivo = open(f'{nome}notafiscal.txt', "w+", encoding= 'utf8')
arquivo.write(notafiscal)


smtp0bj = smtplib.SMTP('smtp.gmail.com', 587)
res_ehlo = smtp0bj.ehlo
print (res_ehlo)

res_starttls = smtp0bj.starttls()
print (res_starttls) 

res_login = smtp0bj.login('testepythonMSI@gmail.com', 'testepythonPL')
print (res_login)

email_destino = str(input('Inserir Email:'))
smtp0bj.sendmail('testepythonMSI@gmail.com', email_destino, 'Subject:Nota Fiscal\n'+str(notafiscal))

smtp0bj.quit()
time.sleep(2)

print(' ')
print('Email Enviado com Sucesso!!!')
print(' ')
print('Volte Sempre')