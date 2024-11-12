from time import sleep

desconto = 0.1

produtos = [ # Lista de produtos armazenados
    ('camisas', 'vestuario', 100, 50.00)
    ,('calças', 'vestuario', 100, 100.00)
    ,('celular', 'eletronico', 30, 120.00)
    ,('notebook', 'eletronico', 30, 2000.00)
]

# Encomendas
encomendas = {
    'silas':[
        ('camisas', 'vestuario', 10, 50.00)
        ,('calças', 'vestuario', 10, 100.00)
        ,('celular', 'eletronico', 3, 120.00)
        ,('notebook', 'eletronico', 3, 2000.00)
    ]
}

# Ajustando lista de produtos
estoque = {x[0]: [x[1], x[2], x[3]] for x in produtos}
"""
Com isso foi feito um dicionario com uma lista para cada item
Posição da lista
0 - categoria
1 - preço
2 - quantidade
"""

# Ajustando lista de encomendas
encomendas_ajustadas = {}
for x in encomendas:
    linha={}
    for y in encomendas[x]:
        linha[y[0]] = [y[1], y[2], y[3]]
    encomendas_ajustadas[x] = linha
"""
Com isso foi feito um dicionario para cada cliente seguindo o exemplo anterior
Posição da lista
0 - categoria
1 - preço
2 - quantidade
"""

# Ajustando encomendas antes de entrar no loop while
for x in encomendas_ajustadas:
    for y in encomendas_ajustadas[x]:
        estoque[y][1] = estoque[y][1] - encomendas_ajustadas[x][y][1]


while True:

    # Pegando cliente na lista de encomandas
    while True:
        try:
            print('Encomendas disponiveis:\n0 - Sair.')
            for numero in range(len(encomendas_ajustadas.keys())):
                cliente = list(encomendas_ajustadas.keys())[0]
                print(f'{numero+1} - {cliente}')

            numero = int(input('Escolha uma encomenda para alteração: '))-1
            if numero == -1:
                cliente = 'parar'
                print('Encerrando.')
                break

            cliente = list(encomendas_ajustadas.keys())[numero]
            print(f'Cliente {cliente} localizado')
            break
        except:
            print('Selecione uma encomenda valida.')


    if cliente == 'parar':
        break
    
    # Definindo valores para ação
    print(f'\nQual ação deseja para o(a) cliente {cliente}:')
    print('1 - Adicionar produtos à encomenda.\n2 - Remover produtos da encomenda.\n0 - Sair.')
    
    while True:
        acao = int(input('Digite uma ação: '))
        if acao in [0,1,2]:
            break
        print('Digite uma ação valida.')

    # Fazendo logica para ação 1
    continuar = True
    if acao == 1:
        while continuar:
            print('\nQual produto deseja adicionar?\n0 - Ver saldo estoque.\n1 - Novo produto.')
            
            for num_produto in range(len(encomendas_ajustadas[cliente].keys())):
                nome_produto = list(encomendas_ajustadas[cliente].keys())[num_produto]
                qtd_produto_encomenda = encomendas_ajustadas[cliente][nome_produto][1]
                print(f'{num_produto+2} - {nome_produto}: {qtd_produto_encomenda}')
            
            num_produto = int(input())
            while True:
                if num_produto in range(0, len(encomendas_ajustadas[cliente].keys())+2):
                    break
                num_produto = int(input('Digite um produto valido: '))

            if num_produto == 0:
                print('Estoque disponivel:')
                for num_produto_etq in range(len(estoque.keys())):
                            nome_produto_etq = list(estoque.keys())[num_produto_etq]
                            qtd_produto_etq = estoque[nome_produto_etq][1]
                            if qtd_produto_etq > 0:
                                print(f'{nome_produto_etq}: {qtd_produto_etq}')
            
            elif num_produto == 1:
                novo_produto = input('Qual o nome do produto que deseja adicionar? ').lower().strip()
                while True:
                    while True:
                        try:
                            categoria = estoque[novo_produto][0]
                            qtd_estoque = estoque[novo_produto][1]
                            preco_uni = estoque[novo_produto][2]
                            break
                        except:
                            print(f'Produto {novo_produto} não existe.\nProdutos disponiveis:')
                            print('\n'.join(list(estoque.keys())))
                            novo_produto = input('Digite um produto valido: ').lower().strip()

                    qtd_encomenda = 0
                    if novo_produto in list(encomendas_ajustadas[cliente].keys()):
                        print(f'Protuto {novo_produto} já existe na encomenda de {cliente}')
                        qtd_encomenda = encomendas_ajustadas[cliente][novo_produto][1]
                        print(f'Quantidade encomendada: {qtd_encomenda}')
                    
                    print(f'Saldo em estoque para {novo_produto}: {qtd_estoque}')
                    nova_qtd = int(input('Qual o acréscimo para a encomenda? '))

                    while nova_qtd > qtd_estoque or nova_qtd < 0:
                        if nova_qtd < 0:
                            print('Digite uma quantidade maior ou igual a 0.')
                        else:
                            print('A quantidade solicitada é superior ao nosso estoque')
                        nova_qtd = int(input('Entre com uma quantidade valida ou digite 0 para não alterar a encomenda: '))
                    
                    print(f'A quantidade da encomenda de {novo_produto} de {cliente} sera alterada de {qtd_encomenda} para {qtd_encomenda + nova_qtd}')
                    alterar = input('Deseja continuar [Y/N] ').lower().strip()
                    while True:
                        if alterar in ['y', 'n']:
                            break
                        else:
                            print('opção invalida')
                            alterar = input('Deseja continuar [Y/N] ').lower().strip()
                    
                    if alterar == 'y':
                        # Ajustando quantidade na encomenda
                        encomendas_ajustadas[cliente][novo_produto] = [categoria , qtd_encomenda + nova_qtd, preco_uni]
                        print(f'Encomenda de {cliente} atualizada com sucesso.')

                        # Ajustando quantidade no estoque
                        estoque[novo_produto][1] = qtd_estoque - nova_qtd
                        print(f'Estoque de {novo_produto} atualizado com sucesso.')
                        break
                    else:
                        print('Estoque e encomenda não foram alterados.')

                
                # Validar se deseja alterar outro produto
                alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
                while True:
                    if alterar_outro in ['y', 'n']:
                        break
                    else:
                        print('opção invalida')
                        alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
                
                if alterar_outro == 'n':
                    break

                    
                        

            elif num_produto > 1:
                num_produto = num_produto-2
                novo_produto = list(encomendas_ajustadas[cliente].keys())[num_produto]

                categoria = estoque[novo_produto][0]
                qtd_estoque = estoque[novo_produto][1]
                preco_uni = estoque[novo_produto][2]

                qtd_encomenda = encomendas_ajustadas[cliente][novo_produto][1]


                print(f'Saldo em estoque para {novo_produto}: {qtd_estoque}')
                nova_qtd = int(input('Qual o acréscimo para a encomenda? '))

                while nova_qtd > qtd_estoque or nova_qtd < 0:
                    if nova_qtd < 0:
                        print('Digite uma quantidade maior ou igual a 0.')
                    else:
                        print('A quantidade solicitada é superior ao nosso estoque')
                    nova_qtd = int(input('Entre com uma quantidade valida ou digite 0 para não alterar a encomenda: '))
                
                print(f'A quantidade da encomenda de {novo_produto} de {cliente} sera alterada de {qtd_encomenda} para {qtd_encomenda + nova_qtd}')
                alterar = input('Deseja continuar [Y/N] ').lower().strip()
                while True:
                    if alterar in ['y', 'n']:
                        break
                    else:
                        print('opção invalida')
                        alterar = input('Deseja continuar [Y/N] ').lower().strip()
                
                if alterar == 'y':
                    # Ajustando quantidade na encomenda
                    encomendas_ajustadas[cliente][novo_produto] = [categoria , qtd_encomenda + nova_qtd, preco_uni]
                    print(f'Encomenda de {cliente} atualizada com sucesso.')

                    # Ajustando quantidade no estoque
                    estoque[novo_produto][1] = qtd_estoque - nova_qtd
                    print(f'Estoque de {novo_produto} atualizado com sucesso.')
                    break
                else:
                    print('Estoque e encomenda não foram alterados.')
            
            # Validar se deseja alterar outro produto
            alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
            while True:
                if alterar_outro in ['y', 'n']:
                    break
                else:
                    print('opção invalida')
                    alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
            
            if alterar_outro == 'n':
                break

    elif acao == 2:
        while True:
            print('\nQual produto deseja remover?\n0 - Sair.')
            
            for num_produto in range(len(encomendas_ajustadas[cliente].keys())):
                nome_produto = list(encomendas_ajustadas[cliente].keys())[num_produto]
                qtd_produto_encomenda = encomendas_ajustadas[cliente][nome_produto][1]
                print(f'{num_produto+1} - {nome_produto}: {qtd_produto_encomenda}')

            num_produto = int(input())
            while True:
                if num_produto in range(0, len(encomendas_ajustadas[cliente].keys())+1):
                    break
                num_produto = int(input('Digite um produto valido: '))
            
            if num_produto == 0:
                break

            elif num_produto != 0:
                novo_produto = list(encomendas_ajustadas[cliente].keys())[num_produto-1]
                qtd_encomenda = encomendas_ajustadas[cliente][novo_produto][1]

                qtd_estoque = estoque[novo_produto][1]
                
                nova_qtd = int(input(f'Qual o remoção para {novo_produto}? '))

                while nova_qtd > qtd_encomenda or nova_qtd < 0:
                    if nova_qtd < 0:
                        print('Digite uma quantidade maior ou igual a 0.')
                    else:
                        print('A quantidade solicitada é superior ao da encomenda')
                    nova_qtd = int(input('Entre com uma quantidade valida ou digite 0 para não alterar a encomenda: '))
                
                print(f'A quantidade da encomenda de {novo_produto} de {cliente} sera alterada de {qtd_encomenda} para {qtd_encomenda - nova_qtd}')
                alterar = input('Deseja continuar [Y/N] ').lower().strip()

                while True:
                    if alterar in ['y', 'n']:
                        break
                    else:
                        print('opção invalida')
                        alterar = input('Deseja continuar [Y/N] ').lower().strip()

                if alterar == 'y':
                    # Ajustando quantidade na encomenda
                    encomendas_ajustadas[cliente][novo_produto][1] = qtd_encomenda - nova_qtd
                    print(f'Encomenda de {cliente} atualizada com sucesso.')

                    # Ajustando quantidade no estoque
                    estoque[novo_produto][1] = qtd_estoque + nova_qtd
                    print(f'Estoque de {novo_produto} atualizado com sucesso.')
                    break
                else:
                    print('Estoque e encomenda não foram alterados.')

                # Validar se deseja alterar outro produto
                alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
                while True:
                    if alterar_outro in ['y', 'n']:
                        break
                    else:
                        print('opção invalida')
                        alterar_outro = input('Deseja alterar outro produto [Y/N] ').lower().strip()
                
                if alterar_outro == 'n':
                    break