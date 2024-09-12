import pandas as pd
from datetime import date
from argon2 import PasswordHasher
import os
import re


class Users():
    def __init__(self, loja_estacia):
        self.data_atual = date.today()
        self._Loja_Df = loja_estacia._Loja_Df

        if os.path.exists("./src/Data/System_data/Usuario_data/Usuario_system.csv"):
            self._DataUsers = pd.read_csv(
                "./src/Data/System_data/Usuario_data/Usuario_system.csv",
                    sep=";",
                    encoding="UTF-8",
                    dtype={
                        'Codigo': 'string',
                        'Loja': 'string',
                        'Nome': 'string',
                        'Data Nascimento': 'string',
                        'Idade': 'int64',
                        'Sexo': 'string',
                        'Usuario': 'string',
                        'Senha': 'string',
                        'Type': 'string'
                    }
                )

        else:
            os.makedirs("./src/Data/System_data/Usuario_data", exist_ok=True)

            self._DataUsers = pd.DataFrame(columns=['Codigo', 'Loja', 'Nome', 'Data Nascimento', 'Idade', 'Sexo', 'Usuario', 'Senha','Type'])

            self._DataUsers = self._DataUsers.astype({
                'Codigo': 'string',
                'Loja': 'string',
                'Nome': 'string',
                'Data Nascimento': 'string',
                'Idade': 'int64',
                'Sexo': 'string',
                'Usuario': 'string',
                'Senha': 'string',
                'Type': 'string'
            })
        

    def registrar_loja(self):
        print('Informe a loja que será cadastrado:')
        num = 0
        lista_loja = self._Loja_Df['Nome_loja'].unique().tolist()
        
        for item in lista_loja:
            num +=1
            print(f"{num}. {item}")

        try:
            opcao = int(input('Escolha opção: '))
            opcao -=1
            if opcao < len(lista_loja):
                return lista_loja[opcao]
            else:
                return self.registrar_loja()
        except ValueError:
            print('erro!!')
            return self.registrar_loja()
        
    def verificar_senha(self): # ADD hash

        """
        Verifica a qualidade da senha com base em vários critérios:
        - Comprimento mínimo de 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número
        - Pelo menos um caractere especial
        - Não deve conter espaços
        """
        ph = PasswordHasher(
            time_cost=2,
            memory_cost=65536,
            parallelism=2
        )
        senha = input('Informe a senha: ')
        
        def Confirmar_senha(senha_vf):
            re_senha = input('Digite a senha novamente:')
            if senha_vf == re_senha:
                print('senha cadastrada')
            else:
                print('Senhas diferentes')
                return Confirmar_senha(senha_vf=senha_vf)
            

        criterios = { # dicionário com os valores da verificação de criterios
            "comprimento_minimo": len(senha) >= 8,
            "letra_maiuscula": re.search(r'[A-Z]', senha) is not None,
            "letra_minuscula": re.search(r'[a-z]', senha) is not None,
            "Contem_numeros": re.search(r'\d', senha) is not None,
            "caractere_especial": re.search(r'[^a-zA-Z0-9]', senha) is not None,
        }
        todos_criterios_satisfeitos = all(criterios.values()) # capta os booleanos gerados

        criterios, valido = criterios, todos_criterios_satisfeitos

        if valido:
            Confirmar_senha(senha)
            print("Senha válida!")
            return ph.hash(senha)
        else:
            print("Senha inválida. Critérios não atendidos:")
            for criterio, atendido in criterios.items():
                if not atendido:
                    print(f"- {criterio.replace('_', ' ').capitalize()}")
                    return self.verificar_senha()
                
    def verificar_usuario(self):

        """
        Verifica a qualidade da senha com base em vários critérios:
        - Comprimento mínimo de 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número
        - Pelo menos um caractere especial
        - Não deve conter espaços
        """
        
        usuario = input('Informe a usuario: ')
        
        
            

        criterios = { # dicionário com os valores da verificação de criterios
            "letra_maiuscula": re.search(r'[A-Z]', usuario) is not None,
            "letra_minuscula": re.search(r'[a-z]', usuario) is not None,
            "caractere_especial": re.search(r'[^a-zA-Z0-9]', usuario) is None,
        }
        todos_criterios_satisfeitos = all(criterios.values()) # capta os booleanos gerados

        criterios, valido = criterios, todos_criterios_satisfeitos

        if valido:
            if not usuario in self._DataUsers['Usuario'].values:
                print("Usuário válido!")
                return usuario
            else:
                print('Usuário já existente')
                return self.verificar_usuario()
        else:
            print("Senha inválida. Critérios não atendidos:")
            for criterio, atendido in criterios.items():
                if not atendido:
                    print(f"- {criterio.replace('_', ' ').capitalize()}")
                    return self.verificar_usuario()
                
    
    def verificar_Nome(self):

        """
        Verifica a qualidade da senha com base em vários critérios:
        - Pelo número
        - Pelo menos um caractere especial
        - Não deve conter
        """
        def confirmacao_nome(nome):
            print(f'\n{nome}\n')
            print('Esse é o Seu nome?')

            print('0. Não')
            print('1. Sim')
            opcao = int(input('Informe a opção: '))
            
            if opcao == 1:
                print('Nome confirmado!')
            elif opcao == 0:
                print('Nome incorreto')
                return self.verificar_Nome()
        try:
            name = input('Informe nome do usuário: ')
            
        except ValueError:
            print('Não é um nome')
            return self.verificar_Nome()

        criterios = { # dicionário com os valores da verificação de criterios
            "letra_maiuscula": re.search(r'[A-Z]', name) is not None,
            "letra_minuscula": re.search(r'[a-z]', name) is not None,
            "numero": re.search(r'\d', name) is None,
            "caractere_especial": re.search(r'[^a-zA-Z0-9\sáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ]', name) is None,
            # "Tem_espaços": re.search(r'\s', name) is not None
        }
        todos_criterios_satisfeitos = all(criterios.values()) # capta os booleanos gerados

        criterios, valido = criterios, todos_criterios_satisfeitos
        
        if valido:
            confirmacao_nome(name)
            
            
            print("nome valido!")
            return name

        else:
            print("nome invalido. Critérios não atendidos:")
            for criterio, atendido in criterios.items():
                if not atendido:
                    print(f"- {criterio.replace('_', ' ').capitalize()}")
                    return self.verificar_Nome()
                


    def alterar_user(self, User_login, type_alteracao):
        index = self._DataUsers[self._DataUsers['Usuario'] == User_login].index[0]
        if type_alteracao == 'Nome':
            self._DataUsers.at[index,type_alteracao] = self.verificar_Nome()

        elif type_alteracao == 'Data Nascimento':
            Data_de_nascimento = self.data_nascimento()
            idade = self.idade_calc(Data_de_nascimento)
            Data_de_nascimento = Data_de_nascimento.strftime('%d/%m/%Y')

            self._DataUsers.at[index,type_alteracao] = Data_de_nascimento
            self._DataUsers.at[index,'Idade']= idade

        elif type_alteracao == 'Sexo':
            self._DataUsers.at[index,type_alteracao] = self.escolha_Sexo()

        elif type_alteracao == 'Senha':
            self._DataUsers.at[index,type_alteracao] = self.verificar_senha()

        self._DataUsers.to_csv("./src/Data/System_data/Usuario_data/Usuario_system.csv", sep = ";", encoding="UTF-8", index=False)

        
    def data_nascimento(self): 
        print('Informe data de nascimento: ')

        def Verificar_datas(Tipo_date, verificacao):
            try:
                valor = int(input(f'{Tipo_date}: '))
                if verificacao(valor):
                    return valor
                else:
                    print('Valor Invalido!')
                    return Verificar_datas(Tipo_date = Tipo_date, verificacao = verificacao)
            except ValueError:
                print("Error: o valor deve ser numero inteiro")
                return Verificar_datas()
            
        def Dia_vf(Dia):
            return not (len(str(Dia)) > 2 and len(str(Dia)) < 1) and not(Dia < 1)
        
        def Mes_vf(Mes):
            return not (len(str(Mes)) > 2 and len(str(Mes)) < 1) and (Mes >= 1 and Mes <= 12)
        
        def Ano_vf(Ano):
            return not (len(str(Ano)) < 4 and len(str(Ano)) > 4) and not (Ano > self.data_atual.year) and (Ano > 1800)

        try:
            dia = Verificar_datas(Tipo_date='Dia', verificacao=Dia_vf) 
            mes = Verificar_datas('Mes',Mes_vf)
            ano = Verificar_datas('Ano', Ano_vf)

            dt_nasc =  date(day = dia, month = mes, year = ano)
            # data_nasc = self.data_nascimento()

            if dt_nasc > self.data_atual:
                print('Não é possivel nascer no futuro!!!!.')
                dt_nasc = self.data_nascimento()

            return dt_nasc
        except ValueError:
                print('Erro no valor inserido:')
                return self.data_nascimento()



    def idade_calc(self, data_nascimento):
    
        idade =  self.data_atual.year - data_nascimento.year

        if (self.data_atual.day , self.data_atual.month) < (data_nascimento.day, data_nascimento.month):
            idade -= 1
        
        return idade
    
    
    def escolha_Sexo(self):
            print('--Escolha o sexo--')
            print("1. Masculino")
            print("2. Feminino")
            try:
                
                opcao = int(input('Escolha uma opcao: '))
                if opcao == 1:
                    return 'Masculino'
                
                elif opcao == 2:
                    return 'Feminino'
            
            except ValueError:
                print('Não é um número das opções')
                return self.escolha_Sexo()
            else:
                print('Item Invalido')
                return self.escolha_Sexo()
            
        
    def cadastro_User(self, loja_name):

        codigo_user = f'USR{self._DataUsers.shape[0]+1:05d}'
        name = self.verificar_Nome() # add verificador de nome

        Data_de_nascimento = self.data_nascimento()
        idade = self.idade_calc(Data_de_nascimento)

        Data_de_nascimento = Data_de_nascimento.strftime('%d/%m/%Y')

        sexo = self.escolha_Sexo()
        usuario = self.verificar_usuario()
        senha = self.verificar_senha() 
        # loja = self.registrar_loja()
        loja = loja_name
        Tipo = 'Default'
        self._DataUsers.loc[self._DataUsers.shape[0]] =[
            codigo_user,
            loja,
            name,
            Data_de_nascimento,
            idade,
            sexo,
            usuario,
            senha,
            Tipo
        ]

        self._DataUsers.to_csv("./src/Data/System_data/Usuario_data/Usuario_system.csv", sep = ";", encoding="UTF-8", index=False)

    def listar_Informacoes_user(self, User_login):
        filtro_user = self._DataUsers.loc[self._DataUsers['Usuario'] == User_login]
        Nome = filtro_user['Nome'].values[0]
        data_n = filtro_user['Data Nascimento'].values[0]
        idade = filtro_user['Idade'].values[0]
        sexo = filtro_user['Sexo'].values[0]
        Loja = filtro_user['Loja'].values[0]

        print(f'{'-'*5} Informações do usuário {'-'*5}\n')

        print(f'Nome do usuário: {Nome}')
        print(f'Sexo do usuário: {sexo}')
        print(f'Data de nascimento: {data_n}')
        print(f'Idade do usuário: {idade}')
        print(f'Loja do usuário: {Loja}')

        print(f'{'-'*34}\n')