import pandas as pd
from datetime import date,datetime
import os

class Venda():
    def __init__(self, Carro_estancia, user_name):#, user_cad_Dat
        self._DataCadastro = Carro_estancia._DataCadastro
        #self._DataUsers = user_cad_Dat._DataUsers[self._DataUsers['Nome'] == user_name].iloc[0]
        self.user_login = user_name
        self.carro = Carro_estancia

        if os.path.exists('./src/Datasets/Venda_data/Vendas_carros.csv'):
            self._DataVenda= pd.read_csv('./src/Datasets/Venda_data/Vendas_carros.csv', 
                sep=';', 
                encoding='UTF-8',
                dtype={ 
                'Nr_Fatura': 'string',
                'Valor_transacao': 'float64',
                'Marca': 'string',
                'Modelo': 'string',
                'data_transancao': 'string',
                'Metodo Pagamento': 'string',
                'Vendedor': 'string'
            })
            
        else:
            os.makedirs("./src/Datasets/Venda_data", exist_ok=True)

            self._DataVenda = pd.DataFrame(columns=['Nr_Fatura','Loja','Marca', 'Modelo', 'Quantidade_Vendida', 'Valor_transacao', 'Ano', 'data_transancao', 'Metodo Pagamento', 'Vendedor']) # add --> 'Comprador', 'Vendedor' , 'loja'

            self._DataVenda = self._DataVenda.astype({ 
                'Nr_Fatura': 'string',
                'Loja': 'string',
                'Valor_transacao': 'float64',
                'Marca': 'string',
                'Modelo': 'string',
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
                try:
                    ct_opcao = int(input('Escolha uma opção: '))
                    while True:
                        if ct_opcao == 1:
                            return 'CARTAO - CREDITO'
                            
                        elif ct_opcao == 2:
                            return 'CARTAO - DEBITO'
                        else:
                            print('Opção invalida')
                            return self.Metodo_pagamento()
                except ValueError:
                    print("Valor invalido")
                    return self.Metodo_pagamento()

            elif opcao == 3:
                return 'EM DINHEIRO'
            
            elif opcao == 4:
                return 'PAYPAL'

            elif opcao == 5:
                return 'CHEQUE'

            else:
                print("Opção invalida!")
                return self.Metodo_pagamento()


    def Realizar_Venda(self):
        codigo_search = self.carro.Codigo_Carro()
        # codigo_search = input('Informe o código:')
        if codigo_search in self._DataCadastro['Codigo'].values:
            
            

            index = self._DataCadastro[self._DataCadastro['Codigo'] == codigo_search].index[0]
            qtd_vendida =int(input('Informe quantidade vendida: '))

            if qtd_vendida <= 0 :
                print('A quantidade deve ser maior que 0.')

            elif qtd_vendida <= self._DataCadastro.at[index, 'Quantidade']: # ao realizar a venda reduz a quantidade de de items 

                self._DataCadastro.at[index, 'Quantidade'] -= qtd_vendida

                self._DataCadastro.at[index, 'Data Modificacao'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
                

                Codigo_fat = f'FTR{self._DataCadastro.at[index, "Codigo"]}-{self._DataVenda.shape[0] + 1:03d}'
                loja = self._DataCadastro.at[index, 'Loja']
                Marca_Veiculo = self._DataCadastro.at[index, 'Marca']
                Modelo_Veiculo = self._DataCadastro.at[index, 'Modelo']
                Venda_qtd  = qtd_vendida
                Preco_Veiculo = qtd_vendida * self._DataCadastro.at[index, 'Preco']
                Ano_Veiculo = self._DataCadastro.at[index, 'Ano']
                
                data_de_venda = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                metodo_pg_venda = self.Metodo_pagamento()
                usuario = self.user_login

                self._DataVenda.loc[self._DataVenda.shape[0]]=[
                    Codigo_fat ,
                    loja ,
                    Marca_Veiculo ,
                    Modelo_Veiculo ,
                    Venda_qtd  ,
                    Preco_Veiculo ,
                    Ano_Veiculo ,
                    data_de_venda ,
                    metodo_pg_venda,
                    usuario
                ]

                self._DataVenda.to_csv("./src/Datasets/Venda_data/Vendas_carros.csv", sep = ";", encoding="UTF-8", index=False)
                
                print('venda realizada com sucesso!')
            else:
                print('A quantidade é maior que o estoque')
                return self.Realizar_Venda()
        else:
            print("Veiculo não encontrado!!")
            return self.Realizar_Venda()

    def listar_vendas(self, user_login):

        venda_filter = self._DataVenda[self._DataVenda['Vendedor'] == user_login]

        print(venda_filter)