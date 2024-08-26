import pandas as pd
from datetime import date, datetime
import os


class Carro:
    def __init__(self, user_estacia, Loja_estacia, userLogin_estacia): # inicia um dataframe com as colunas vazias
        self._DataUsers = user_estacia._DataUsers
        self._Loja_Df = Loja_estacia._Loja_Df
        self.user_login = userLogin_estacia.user_login
        self.user_type = userLogin_estacia.user_Type
        self.data_atual = date.today()
        self.Verificar_fonte()
        self.Tipo_usuario()



    def Verificar_fonte(self):
        if os.path.exists("./src/Datasets/Carro_data/Car_system.csv"):
            self._DataCadastro = pd.read_csv("./src/Datasets/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8")

        else:
            os.makedirs("./src/Datasets/Carro_data", exist_ok=True)

            self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade', 'Data Cadastro', 'Data Modificacao', 'loja', 'Adcionado Por', 'Modificado Por'])# ==> loja
            
            self._DataCadastro = self._DataCadastro.astype({# pré define o tipo das colunas
                'Codigo': 'string',
                'Marca': 'string',
                'Modelo': 'string',
                'Preco': 'float64',
                'Ano': 'int32',
                'Quantidade': 'int32',
                'Data Cadastro': 'string',
                'Data Modificacao': 'float64',
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
            return self.info_user['Loja'], self.info_user['Nome']
        
    def verificar_ano(self):
        try:
            Ano_Veiculo = int(input("Informe o Ano: "))
            if (Ano_Veiculo >= 1800) and (Ano_Veiculo <= self.data_atual.year):
                return Ano_Veiculo
            else:
                print('Ano Inválido')
                return self.verificar_ano()
        except ValueError:
            print("Valor inconpátivel")
            return self.verificar_ano()
        
    def verificador_preco_e_qtd(self,type_):
        try:
            if type_ == 'Preco':
                valor = float(input('Informe o preço: '))
            elif type_ == 'Qtd':
                valor = int(input('Informe quantidade adicionadas: '))
            if valor >0:
                
                return valor
            else:
                return self.verificador_preco_e_qtd(type_=type_)
        except ValueError:
            print("Valor inconpátivel")
            return self.verificador_preco_e_qtd(type_=type_)
        

    def Cadastrar_veiculo(self):# no cadastro de veiculo será gerado um codifo de acordo com o tamanho do df(linhas)
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0] + 1:05d}'
        
        Marca_Veiculo = input('Informe a Marca: ')
        
        Modelo_Veiculo = input("Informe o modelo: ")
        
        Preco_Veiculo = self.verificador_preco_e_qtd('Preco')
        Ano_Veiculo = self.verificar_ano() 
        Quantidade_veiculo = self.verificador_preco_e_qtd('Qtd') 
        data_de_cadastro = date.today().strftime('%d/%m/%Y')
        data_de_modificacao = None # data de modificação só irá iniciado por None pois só pode ser modificados após ser cadastrado

        if self.user_type == 1:            
            Loja =  self.info_user['Nome_loja']
            add_user = self.info_user['Type']

        elif self.user_type == 2:
            Loja =  self.info_user['Loja']
            add_user = self.info_user['Nome']

        mod_user = None

        def Verificacao_test():
            lista_modelo = self._DataCadastro[(self._DataCadastro['Marca'] == Marca_Veiculo) & (self._DataCadastro['Modelo'] == Modelo_Veiculo) & self._DataCadastro['loja'] == Loja].reset_index(drop=True)
            if Ano_Veiculo in lista_modelo['Ano'].values:
                return False
            else:
                return True
        # adcionado ao dataframe
        if Verificacao_test():
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
            
        else:
            print('Veiculo existente')
            return self.Cadastrar_veiculo()

        self._DataCadastro.to_csv("./src/Datasets/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8",index=False)

    def Marca_carro(self):
        print('Informe a marca que será vendida:')
        num = 0
        lista_carro = self._DataCadastro['Marca'].unique().tolist()
        
        for item in lista_carro:
            num += 1
            print(f"{num}. {item}")

        try:
            opcao = int(input('Escolha opção: '))
            opcao -= 1
            if 0 <= opcao < len(lista_carro):
                return lista_carro[opcao]
            else:
                return self.Registrar_loja()
        except ValueError:
            print('Erro! Por favor, insira um número válido.')
            return self.Registrar_loja()
            
    def Modelo_carro(self, Marca_escolha):
        lista_modelo = self._DataCadastro[self._DataCadastro['Marca'] == Marca_escolha]
        modelos_unicos = lista_modelo['Modelo'].unique().tolist()
        
        for num, modelo in enumerate(modelos_unicos, start=1):
            print(f"{num}. {modelo}")
        
        try:
            opcao = int(input('Escolha opção: '))
            opcao -= 1
            if 0 <= opcao < len(modelos_unicos):
                return modelos_unicos[opcao]
            else:
                print("Opção inválida. Por favor, escolha novamente.")
                return self.Modelo_carro(Marca_escolha=Marca_escolha)
        except ValueError:
            print('Erro! Por favor, insira um número válido.')
            return self.Modelo_carro(Marca_escolha=Marca_escolha)
        
    def Codigo_Carro(self):
        marca = self.Marca_carro()
        modelo = self.Modelo_carro(marca)
        
        carro_search = self._DataCadastro[
            (self._DataCadastro['Marca'] == marca) & 
            (self._DataCadastro['Modelo'] == modelo)
        ].reset_index(drop=True)
        
        if not carro_search.empty:
            codigo_carro = carro_search.iloc[0]['Codigo']
            return codigo_carro
        else:
            print(f'Veículo com marca: {marca} e modelo: {modelo} não encontrado.')
            return self.Codigo_Carro()
        
    def Atualizar_preco_veiculo(self):
        Codigo_search = self.Codigo_Carro()
        
        if Codigo_search in self._DataCadastro['Codigo'].values: # se o codigo existir na coluna['Codigo'] irá gerar um True oq fará e poderar seguir para a alteração
            
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search ].index[0]# pega o indice para modificar a na raiz do df
            
            self._DataCadastro.at[index,'Preco'] = float(input('Informe o novo preço:'))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.now()

            if self.user_type == 1:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome_loja'].values
                
            elif self.user_types == 2:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome'].values

            
            print('Valor atualizado')
        else:
            print('Não encontrado')
        
    def Atualizar_qtd_veiculo(self):
        Codigo_search = self.Codigo_Carro()
        
        if Codigo_search in self._DataCadastro['Codigo'].values:
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search].index[0]
            self._DataCadastro.at[index, 'Quantidade'] = int(input('Informe quantidade: '))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.now()

            if self.user_type == 1:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome_loja'].values
            elif self.user_types == 2:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome'].values

            print("Quantidade atualizada: ")
        else:
            print('Não encontrado')
            
    def Atualizar_dados_veiculo(self, Type_mod):
        Codigo_search = self.Codigo_Carro()
        
        if Codigo_search in self._DataCadastro['Codigo'].values:
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search].index[0]
            self._DataCadastro.at[index, Type_mod] = int(input(f'Informe a {Type_mod}: '))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.now()

            if self.user_type == 1:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome_loja'].values
            elif self.user_types == 2:
                self._DataCadastro.at[index,'Modificado Por'] = self.info_user['Nome'].values

            print(f"{Type_mod} atualizada: ")
        else:
            print('Não encontrado')

    def listar(self):
        print(self._DataCadastro)

    def listar_info(self):
        print(self._DataCadastro.info())