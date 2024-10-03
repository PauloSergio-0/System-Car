import pandas as pd
from datetime import date, datetime
import os

class Carro:
    
    """
    Classe carro é responsável por gerênciar  os dados de veiculos e interegir com os dados de outros sistemas que são eles:
    Sistema de Usuaários, Lojas e login
    
    Esta classe carrega, cria e manipula dados a partir de arquivos csv e caso estes arquivos não existam o sistema tem capacidade de salvar os dados em .csv a gerado de um novo Dataframe
    
    Atributos:
    
        ._DataCadastro  = Dados dos veiculos
        _DataUsers = Dados dos usuários
        _Loja_Df =  Dados das lojas
        user_login = Dados do login
        user_type = Tipo de usuário (Nivél de acesso)
        loja_user = Loja em que o susário logado está cadastrado
        data_atual = data atual do sistema
        self.info_user = será a linha de um DataFrame filtrado
    """
    
    def __init__(self, user_estacia, Loja_estacia, userLogin_estacia):
        
        """
        Parâmetros:
            user_estacia (object): Objeto que contém os dados de usuários.
            Loja_estacia (object): Objeto que contém os dados das lojas.
            userLogin_estacia (object): Objeto que contém informações do usuário logado (login, tipo e loja).
        
        
        Ações:
            Carregar dados de arquivo .csv, caso contrario cria um Dataframe
        """
        self._DataUsers = user_estacia._DataUsers
        self._Loja_Df = Loja_estacia._Loja_Df
        self.user_login = userLogin_estacia.user_login
        self.user_type = userLogin_estacia.user_Type
        self.loja_user = userLogin_estacia.loja_user
        self.data_atual = date.today()


        if self.user_type == 1:
            self.info_user = self._Loja_Df[self._Loja_Df['Usuario_loja'] == self.user_login].iloc[0]
            
        elif self.user_type == 2:
            self.info_user = self._DataUsers[self._DataUsers['Usuario'] == self.user_login].iloc[0]

    
        if os.path.exists("./src/Data/System_data/Carro_data/Car_system.csv"):
            self._DataCadastro = pd.read_csv("./src/Data/System_data/Carro_data/Car_system.csv",
                sep = ";",
                encoding="UTF-8",
                dtype={
                'Codigo': 'string',
                'Marca': 'string',
                'Modelo': 'string',
                'Preco': 'float64',
                'Ano': 'int32',
                'Quantidade': 'int32',
                'Data Cadastro': 'string',
                'Data Modificacao': 'string',
                'Loja': 'string',
                'Adcionado Por': 'string',
                'Modificado Por': 'string'
            })

        else:
            os.makedirs("./src/Data/System_data/Carro_data", exist_ok=True)

            self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade', 'Data Cadastro', 'Data Modificacao', 'Loja', 'Adcionado Por', 'Modificado Por'])# ==> Loja
            
            self._DataCadastro = self._DataCadastro.astype({# pré define o tipo das colunas
                'Codigo': 'string',
                'Marca': 'string',
                'Modelo': 'string',
                'Preco': 'float64',
                'Ano': 'int32',
                'Quantidade': 'int32',
                'Data Cadastro': 'string',
                'Data Modificacao': 'string',
                'Loja': 'string',
                'Adcionado Por': 'string',
                'Modificado Por': 'string'
            })



        
    def verificar_ano(self):# o ano do veiculo deve ser maior que 1800 e menor que o ano atual
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
        
    def verificador_preco_e_qtd(self,type_): # função para definir o tipo de dados de Preço e Quantidade
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
        

    def cadastrar_veiculo(self):# no cadastro de veiculo será gerado um codigo de acordo com o tamanho do df(linhas)
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0] + 1:05d}'
        
        Marca_Veiculo = input('Informe a Marca: ').capitalize()
        
        Modelo_Veiculo = input("Informe o modelo: ").capitalize()
        
        Preco_Veiculo = self.verificador_preco_e_qtd('Preco')
        Ano_Veiculo = self.verificar_ano() 
        Quantidade_veiculo = self.verificador_preco_e_qtd('Qtd') 
        data_de_cadastro = date.today().strftime('%d/%m/%Y')
        data_de_modificacao = 'Não Modificado' # data de modificação só irá iniciado por None pois só pode ser modificados após ser cadastrado

        if self.user_type == 1:            
            Loja =  self.info_user['Usuario_loja']
            add_user = self.info_user['Type']

        elif self.user_type == 2:
            Loja =  self.info_user['Loja']
            add_user = self.info_user['Nome']

        mod_user = 'Não Aplicável'

        def verificacao_test(): # verifica se já existe o mesmo veiculo já cadastrado
            lista_modelo = self._DataCadastro[
                (self._DataCadastro['Marca'] == Marca_Veiculo) 
                & (self._DataCadastro['Modelo'] == Modelo_Veiculo) 
                & (self._DataCadastro['Loja'] == Loja)
                ].reset_index(drop=True)
            if Ano_Veiculo in lista_modelo['Ano'].values:
                return False
            else:
                return True
        # adcionado ao dataframe
        if verificacao_test():

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
            return self.cadastrar_veiculo()

        self._DataCadastro.to_csv("./src/Data/System_data/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8",index=False)

    def Marca_carro(self): # função para selecionar uma marca a parti da loja do usuário
        print('Informe a marca:')
        num = 0
        cadastro_data = self._DataCadastro.loc[self._DataCadastro['Loja'] == self.loja_user]
        lista_carro = sorted(cadastro_data['Marca'].unique().tolist())
        
        for item in lista_carro:
            num += 1
            print(f"{num}. {item}")

        try:
            opcao = int(input('Escolha opção: '))
            opcao -= 1
            if 0 <= opcao < len(lista_carro):
                return lista_carro[opcao]
            else:
                return self.Marca_carro()
        except (ValueError, AttributeError):
            print('Erro! Por favor, insira um número válido.')
            return self.Marca_carro()

            
    def Modelo_carro(self, Marca_escolha): # Lista os modelos disponiveis de acordo com a loja e marca_escolhida
        lista_modelo = self._DataCadastro[
            (self._DataCadastro['Loja'] == self.loja_user) & 
            (self._DataCadastro['Marca'] == Marca_escolha)
        ]
        modelos_unicos = sorted(lista_modelo['Modelo'].unique().tolist())
        
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
        except (ValueError, AttributeError):
            print('Erro! Por favor, insira um número válido.')
            return self.Modelo_carro(Marca_escolha=Marca_escolha)

    def Codigo_Carro(self): # Captura o código do carro para posibilitar modificação 
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

    def atualizar_valor_colunas_vendas(self, venda_df, type_mod,nome_atual, novo_nome):
        venda_df._DataVenda.loc[venda_df._DataVenda[type_mod] == nome_atual, type_mod] = novo_nome

        venda_df._DataVenda.to_csv("./src/Data/System_data/Venda_data/Vendas_carros.csv", sep = ";", encoding="UTF-8", index=False)

    def atualizar_dados_veiculo(self, Type_mod, type_var, venda_estacia):
        Codigo_search = self.Codigo_Carro()
        try:
            if Codigo_search in self._DataCadastro['Codigo'].values:
                index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search].index[0]
                if type_var == 1:

                    nome_antes = self._DataCadastro.at[index, Type_mod]
                    self._DataCadastro.at[index, Type_mod] = input(f'Informe a {Type_mod}: ')
                    nome_depois = self._DataCadastro.at[index, Type_mod]
                    if Type_mod == 'Marca' or Type_mod == 'Modelo':
                        self.atualizar_valor_colunas_vendas(venda_df=venda_estacia, type_mod=Type_mod, nome_atual=nome_antes,  novo_nome = nome_depois)
                elif type_var == 2:
                    self._DataCadastro.at[index, Type_mod] = int(input(f'Informe a {Type_mod}: '))
                elif type_var == 3:
                    self._DataCadastro.at[index, Type_mod] = float(input(f'Informe a {Type_mod}: '))

                self._DataCadastro.at[index,'Data Modificacao'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                self._DataCadastro.at[index,'Modificado Por'] = self.user_login
                
                print(f"{Type_mod} atualizada")

                self._DataCadastro.to_csv("./src/Data/System_data/Carro_data/Car_system.csv", sep = ";",encoding="UTF-8",index=False)
            else:
                print('Não encontrado')
                return self.Atualizar_qtd_veiculo(Type_mod= Type_mod , type_var= type_var)

        except ValueError:
            print('Erro no valor')
            return self.Atualizar_qtd_veiculo(Type_mod= Type_mod, type_var= type_var)
            
    def listar_veiculos(self, user_login, ):
        data_filter =self._DataCadastro[self._DataCadastro['Loja'] == user_login]
        
        print(data_filter)
