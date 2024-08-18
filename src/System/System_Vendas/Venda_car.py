import pandas as pd
from datetime import date,datetime

class Venda():
    def __init__(self, Carro_estancia, User_login_estancia):
        self._DataCadastro = Carro_estancia._DataCadastro
        self.user_login = User_login_estancia.user_login
        self._DataVenda = pd.DataFrame(columns=['Nr_Fatura','Marca', 'Modelo', 'Quantidade_Vendida', 'Valor_transacao', 'Ano', 'data_transancao', 'Metodo Pagamento', 'Vendedor']) # add --> 'Comprador', 'Vendedor' , 'loja'

        self._DataVenda = self._DataVenda.astype({ 
            'Nr_Fatura': 'string',
            'Valor_transacao': 'float64',
            'Modelo': 'string',
            'Marca': 'string',
            'data_transancao': 'string',
            'Metodo Pagamento': 'string',
            'Vendedor': 'string'
        })


    def Metodo_pagamento(self):
        print('1. PIX')
        print('2. CARTÃO')
        print('3. EM DINHEIRO')
        print('4. PAYPAL')
        print('5. CHEQUE')
        opcao = int(input('Escolha uma opção: '))

        while True:
            if opcao == 1:
                return 'PIX'

            elif opcao == 2:
                print('1. DEBITO')
                print('2. CREDITO')
                ct_opcao = int(input('Escolha uma opção: '))
                while True:
                    if ct_opcao == 1:
                        return 'CARTAO - CREDITO'
                        
                    elif ct_opcao == 2:
                        return 'CARTOA - DEBITO'
                    else:
                        print('Opção invalida')

            elif opcao == 3:
                return 'EM DINHEIRO'
            
            elif opcao == 4:
                return 'PAYPAL'

            elif opcao == 5:
                return 'CHEQUE'

            else:
                print("Opção invalida!")


    def Realizar_Venda(self):
        codigo_search = input('Informe o código:')
        if codigo_search in self._DataCadastro['Codigo'].values:

            index = self._DataCadastro[self._DataCadastro['Codigo'] == codigo_search].index[0]
            qtd_vendida =int(input('Informe quantidade vendida: '))

            if qtd_vendida == 0:
                print('A quantidade deve ser maior que 0.')

            elif qtd_vendida <= self._DataCadastro.at[index, 'Quantidade']: # ao realizar a venda reduz a quantidade de de items 

                self._DataCadastro.at[index, 'Quantidade'] -= qtd_vendida
                self._DataCadastro.at[index, 'Data Modificacao'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                print('venda realizada com sucesso!')

                Codigo_fat = f'FTR{self._DataCadastro.at[index, "Codigo"]}-{self._DataCadastro.shape[0] +1:03d}'
                Marca_Veiculo = self._DataCadastro.at[index, 'Marca']
                Modelo_Veiculo = self._DataCadastro.at[index, 'Modelo']
                Venda_qtd  = qtd_vendida
                Preco_Veiculo = qtd_vendida * self._DataCadastro.at[index, 'Preco']
                Ano_Veiculo = self._DataCadastro.at[index, 'Ano']
                
                data_de_venda = date.today().strftime('%d/%m/%Y')
                metodo_pg_venda = self.Metodo_pagamento()
                

                self._DataVenda.loc[self._DataVenda.shape[0]]=[
                    Codigo_fat ,
                    Marca_Veiculo ,
                    Modelo_Veiculo ,
                    Venda_qtd  ,
                    Preco_Veiculo ,
                    Ano_Veiculo ,
                    data_de_venda ,
                    metodo_pg_venda,
                    self.user_login
                ]

            else:
                print('A quantidade é maior que o estoque')

    def listar_vendas(self):
        print(self._DataVenda)