import pandas as pd
from datetime import date, datetime
import os


class Carro:
    def __init__(self, user_estacia, Loja_estacia, userLogin_estacia): # inicia um dataframe com as colunas vazias
        self._DataUsers = user_estacia._DataUsers
        self._Loja_Df = Loja_estacia._Loja_Df
        self.user_login = userLogin_estacia.user_login
        self.user_type = userLogin_estacia.user_Type
        self.Verificar_fonte()
        self.Tipo_usuario()



    def Verificar_fonte(self):
        if os.path.exists("./src/Datasets/Carro_data/Car_system.csv"):
            self._DataCadastro = pd.read_csv("./src/Datasets/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8")

        else:
            self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade', 'Data Cadastro', 'Data Modificacao', 'loja', 'Adcionado Por', 'Modificado Por'])# ==> loja
            self._DataCadastro = self._DataCadastro.astype({# pré define o tipo das colunas
                'Codigo': 'string',
                'Marca': 'string',
                'Modelo': 'string',
                'Preco': 'float64',
                'Ano': 'int32',
                'Quantidade': 'int32',
                'Data Cadastro': 'string',
                'Data Modificacao': 'string',
                'loja': 'string',
                'Adcionado Por': 'string',
                'Modificado Por': 'string'
            })

    def Tipo_usuario(self):

        if self.user_type == 1:
            self.info_user = self._Loja_Df[self._Loja_Df['Nome_loja'] == self.user_login].iloc[0]
            return self.info_user['Nome_loja'], self.info_user['Type']
        
        elif self.user_type == 2:
            self.info_user = self._DataUsers[self._DataUsers['Nome'] == self.user_login].iloc[0]
            return self.info_user['Nome_loja'], self.info_user['Nome']


    def Cadastrar_veiculo(self):# no cadastro de veiculo será gerado um codifo de acordo com o tamanho do df(linhas)
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0] + 1:05d}'
        Marca_Veiculo = input('Informe a Marca: ')
        Modelo_Veiculo = input("Informe o modelo: ")
        Preco_Veiculo = float(input('Informe o preço: '))
        Ano_Veiculo = int(input("Informe o Ano: "))
        Quantidade_veiculo = int(input("Informe quantidade adicionadas: "))
        data_de_cadastro = date.today().strftime('%d/%m/%Y')
        data_de_modificacao = None # data de modificação só irá iniciado por None pois só pode ser modificados após ser cadastrado

        if self.user_type == 1:            
            Loja =  self.info_user['Nome_loja']
            add_user = self.info_user['Type']

        elif self.user_type == 2:
            Loja =  self.info_user['Loja']
            add_user = self.info_user['Nome']

        mod_user = None
        # adcionado ao dataframe
        self._DataCadastro.loc[self._DataCadastro.shape[0]] = [ 
            Codigo_Veiculo,
            Marca_Veiculo,
            Modelo_Veiculo,
            Preco_Veiculo,
            Ano_Veiculo,
            Quantidade_veiculo,
            data_de_cadastro,
            data_de_modificacao,
            Loja,
            add_user,
            mod_user
        ]

        self._DataCadastro.to_csv("./src/Datasets/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8",index=False)

        
    def Atualizar_preco_veiculo(self):
        Codigo_search = input('Informe o código: ')
        
        if Codigo_search in self._DataCadastro['Codigo'].values: # se o codigo existir na coluna['Codigo'] irá gerar um True oq fará e poderar seguir para a alteração
            
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search ].index[0]# pega o indice para modificar a na raiz do df
            
            self._DataCadastro.at[index,'Preco'] = float(input('Informe o novo preço:'))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            if self.user_type == 1:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome_loja'].values
            elif self.user_types == 2:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome'].values

            
            print('Valor atualizado')
        else:
            print('Não encontrado')
        
    def Atualizar_qtd_veiculo(self):
        Codigo_search = input('Iforme o código: ')
        
        if Codigo_search in self._DataCadastro['Codigo'].values:
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search].index[0]
            self._DataCadastro.at[index, 'Quantidade'] = int(input('Informe quantidade: '))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            if self.user_type == 1:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome_loja'].values
            elif self.user_types == 2:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome'].values

            print("Quantidade atualizada: ")
        else:
            print('Não encontrado')

    def listar(self):
        print(self._DataCadastro)

    def listar_info(self):
        print(self._DataCadastro.info())