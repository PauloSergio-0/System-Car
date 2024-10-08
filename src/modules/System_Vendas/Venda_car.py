import pandas as pd
from datetime import date,datetime
import os

class Venda():
    """
    Classe responsável por gerenciar o processo de vendas de veículos.

    A classe utiliza dados previamente cadastrados no sistema e permite 
    realizar vendas, listar vendas realizadas e definir métodos de pagamento.

    Atributos:
    ----------
    _DataCadastro : pandas.DataFrame
        DataFrame contendo o cadastro de veículos.
    user_login : str
        Nome de usuário do login atual.
    user_type : str
        Tipo de usuário atual (admin ou comum).
    carro : object
        Instância da classe `Carro`, contendo dados dos veículos.
    _DataVenda : pandas.DataFrame
        DataFrame contendo os dados de vendas de veículos.
    """
    def __init__(self, Carro_estancia, Login_estacia,):#, user_cad_Dat
        self._DataCadastro = Carro_estancia._DataCadastro
        self.user_login = Login_estacia.user_login
        self.user_type = Login_estacia.user_Type
        self.carro = Carro_estancia

        if os.path.exists('./src/Data/System_data/Venda_data/Vendas_carros.csv'):
            self._DataVenda = pd.read_csv('./src/Data/System_data/Venda_data/Vendas_carros.csv', 
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
            os.makedirs("./src/Data/System_data/Venda_data", exist_ok=True)

            self._DataVenda = pd.DataFrame(columns=['Nr_Fatura','Loja','Marca', 'Modelo', 'Quantidade_Vendida', 'Valor_transacao', 'Ano', 'data_transancao', 'Metodo Pagamento', 'Vendedor']) # add --> 'Comprador',

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

    
    def metodo_pagamento(self):
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
                            return self.metodo_pagamento()
                except ValueError:
                    print("Valor invalido")
                    return self.metodo_pagamento()

            elif opcao == 3:
                return 'EM DINHEIRO'
            
            elif opcao == 4:
                return 'PAYPAL'

            elif opcao == 5:
                return 'CHEQUE'

            else:
                print("Opção invalida!")
                return self.metodo_pagamento()


    def realizar_Venda(self):
        codigo_search = self.carro.Codigo_Carro()
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
                metodo_pg_venda = self.metodo_pagamento()
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

                self._DataVenda.to_csv("./src/Data/System_data/Venda_data/Vendas_carros.csv", sep = ";", encoding="UTF-8", index=False)
                self._DataCadastro.to_csv("./src/Data/System_data/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8",index=False)
                
                print('venda realizada com sucesso!')
            else:
                print('A quantidade é maior que o estoque')
                return self.realizar_Venda()
        else:
            print("Veiculo não encontrado!!")
            return self.realizar_Venda()
        

    def listar_vendas(self, user_login):

        venda_filter = self._DataVenda[self._DataVenda['Vendedor'] == user_login]

        print(venda_filter)