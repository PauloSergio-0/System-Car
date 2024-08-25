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
            self._DataVenda= pd.read_csv('./src/Datasets/Venda_data/Vendas_carros.csv', sep=';', encoding='UTF-8')
            
        else:
            os.makedirs("./src/Datasets/Venda_data", exist_ok=True)

            self._DataVenda = pd.DataFrame(columns=['Nr_Fatura','Marca', 'Modelo', 'Quantidade_Vendida', 'Valor_transacao', 'Ano', 'data_transancao', 'Metodo Pagamento', 'Vendedor']) # add --> 'Comprador', 'Vendedor' , 'loja'

            self._DataVenda = self._DataVenda.astype({ 
                'Nr_Fatura': 'string',
                'Valor_transacao': 'float64',
                'Marca': 'string',
                'Modelo': 'string',
                'data_transancao': 'float64',
                'Metodo Pagamento': 'string',
                'Vendedor': 'string'
            })

    # def Marca_carro(self):
    #     print('Informe a marca que será vendida:')
    #     num = 0
    #     lista_carro = self._DataCadastro['Marca'].unique().tolist()
        
    #     for item in lista_carro:
    #         num += 1
    #         print(f"{num}. {item}")

    #     try:
    #         opcao = int(input('Escolha opção: '))
    #         opcao -= 1
    #         if 0 <= opcao < len(lista_carro):
    #             return lista_carro[opcao]
    #         else:
    #             return self.Registrar_loja()
    #     except ValueError:
    #         print('Erro! Por favor, insira um número válido.')
    #         return self.Registrar_loja()
            
    # def Modelo_carro(self, Marca_escolha):
    #     lista_modelo = self._DataCadastro[self._DataCadastro['Marca'] == Marca_escolha]
    #     modelos_unicos = lista_modelo['Modelo'].unique().tolist()
        
    #     for num, modelo in enumerate(modelos_unicos, start=1):
    #         print(f"{num}. {modelo}")
        
    #     try:
    #         opcao = int(input('Escolha opção: '))
    #         opcao -= 1
    #         if 0 <= opcao < len(modelos_unicos):
    #             return modelos_unicos[opcao]
    #         else:
    #             print("Opção inválida. Por favor, escolha novamente.")
    #             return self.Modelo_carro(Marca_escolha=Marca_escolha)
    #     except ValueError:
    #         print('Erro! Por favor, insira um número válido.')
    #         return self.Modelo_carro(Marca_escolha=Marca_escolha)
        
    # def Codigo_Carro(self):
    #     marca = self.Marca_carro()
    #     modelo = self.Modelo_carro(marca)
        
    #     carro_search = self._DataCadastro[
    #         (self._DataCadastro['Marca'] == marca) & 
    #         (self._DataCadastro['Modelo'] == modelo)
    #     ].reset_index(drop=True)
        
    #     if not carro_search.empty:
    #         codigo_carro = carro_search.iloc[0]['Codigo']
    #         return codigo_carro
    #     else:
    #         print(f'Veículo com marca: {marca} e modelo: {modelo} não encontrado.')
    #         return self.Codigo_Carro() 

        
    
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
                
                self._DataCadastro.at[index, 'Data Modificacao'] =  pd.to_datetime(datetime.now().replace(microsecond=0), format='%Y-%m-%d %H:%M:%S')

                # self._DataCadastro.at[index, 'Data Modificacao'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S') 
                

                Codigo_fat = f'FTR{self._DataCadastro.at[index, "Codigo"]}-{self._DataVenda.shape[0] + 1:03d}'
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
                    Marca_Veiculo ,
                    Modelo_Veiculo ,
                    Venda_qtd  ,
                    Preco_Veiculo ,
                    Ano_Veiculo ,
                    data_de_venda ,
                    metodo_pg_venda,
                    usuario
                ]

                self._DataVenda.to_csv("./src/Datasets/Venda_data/Vendas_carros.csv", sep = ";",encoding="UTF-8",index=False)
                
                print('venda realizada com sucesso!')
            else:
                print('A quantidade é maior que o estoque')
                return self.Realizar_Venda()
        else:
            print("Veiculo não encontrado!!")
            return self.Realizar_Venda()

    def listar_vendas(self):
        print(self._DataVenda)