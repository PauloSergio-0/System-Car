import pandas as pd
import os
import re
from argon2 import PasswordHasher

class Loja:
    
    """
    Classe responsável pela gestão de lojas, incluindo cadastro, alteração de dados, e visualização de informações.

    Esta classe permite que você cadastre novas lojas, altere informações de lojas existentes, verifique 
    a validade de senhas e usuários, e liste informações detalhadas sobre uma loja específica. Além disso, 
    gerencia a leitura e escrita de dados em um arquivo CSV.

    Atributos:
        _Loja_Df (DataFrame): DataFrame contendo informações sobre as lojas, carregado de um arquivo CSV ou criado vazio.

    Métodos:
        __init__: Inicializa a classe, carregando dados de lojas de um arquivo CSV se disponível, ou criando um DataFrame vazio para novos dados.
        verificar_senha: Verifica a validade de uma senha com base em critérios de segurança, como comprimento, caracteres maiúsculos e minúsculos, números, e caracteres especiais. Retorna o hash da senha se válido.
        verificar_usuario: Verifica se um nome de usuário atende a critérios de segurança e se é único. Retorna o nome de usuário se válido.
        alterar_user_admin: Altera a senha ou outro dado de uma loja existente. Salva as alterações no arquivo CSV.
        cadastrar_Loja: Cadastra uma nova loja com informações fornecidas pelo usuário e salva no arquivo CSV.
        listar_lojas: Exibe a lista de todas as lojas.
        listar_Informacoes_loja: Exibe informações detalhadas sobre uma loja específica, incluindo total de veículos e funcionários.

    Exceções:
        - A classe lida com a criação e manipulação de arquivos CSV, portanto, pode enfrentar erros relacionados a operações de I/O.
        - Métodos que solicitam entradas do usuário podem enfrentar erros se entradas inválidas forem fornecidas.
    """
    def __init__(self):

        if os.path.exists("./src/Data/System_data/Loja_data/Loja_system.csv"):
            self._Loja_Df = pd.read_csv(
                "./src/Data/System_data/Loja_data/Loja_system.csv",
                sep=";",
                encoding="UTF-8",
                dtype={
                'Nome_loja': 'string',
                'Pais': 'string',
                'Estado': 'string',
                'Cidade': 'string',
                'Usuario_loja': 'string',
                'Senha': 'string',
                'Type': 'string'
            })

        else:
            os.makedirs("./src/Data/System_data/Loja_data", exist_ok=True)

            self._Loja_Df = pd.DataFrame(columns=['Nome_loja', 'Pais', 'Estado', 'Cidade', 'Usuario_loja', 'Senha', 'Type']) 
            self._Loja_Df = self._Loja_Df.astype({
                'Nome_loja': 'string',
                'Pais': 'string',
                'Estado': 'string',
                'Cidade': 'string',
                'Usuario_loja': 'string',
                'Senha': 'string',
                'Type': 'string'
            })
        
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
            if senha == re_senha:
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
            if not usuario in self._Loja_Df['Usuario_loja'].values:
                print("Usuário válido")
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


    def alterar_user_admin(self, User_login, type_alteracao):
        index = self._Loja_Df[self._Loja_Df['Usuario_loja'] == User_login ].index[0]
        if type_alteracao == 'Senha':
            self._Loja_Df.at[index,type_alteracao] = self.verificar_senha()
        else:
            self._Loja_Df.at[index,type_alteracao] = input(f'Informe {type_alteracao} da loja: ')

        print(f'{type_alteracao} Alterado(a)')

        self._Loja_Df.to_csv("./src/Data/System_data/Loja_data/Loja_system.csv", sep = ";",encoding="UTF-8",index=False)

    def cadastrar_Loja(self):
        Nm_loja = input('Informe o Nome da Loja: ')
        Pais = 'Brasil'
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        usuario = self.verificar_usuario()
        senha = self.verificar_senha()
        Tipo = 'Admin'

        self._Loja_Df.loc[self._Loja_Df.shape[0]] = [
            Nm_loja,
            Pais,
            estado,
            cidade,
            usuario,
            senha,
            Tipo
        ]

        self._Loja_Df.to_csv("./src/Data/System_data/Loja_data/Loja_system.csv", sep = ";",encoding="UTF-8",index=False)


    def listar_lojas(self):
        print(self._Loja_Df)

    def listar_Informacoes_loja(self, User_login, funca_estacia, carro_estacia):
        filtro_user = self._Loja_Df.loc[self._Loja_Df['Usuario_loja'] == User_login]

        total_funca = funca_estacia[funca_estacia['Loja'] == User_login].shape[0]

        filter_carro = carro_estacia[carro_estacia['Loja'] == User_login]
        total_carro = filter_carro['Quantidade'].sum()

        Nome = filtro_user['Nome_loja'].values[0]
        pais = filtro_user['Pais'].values[0]
        Estado = filtro_user['Estado'].values[0]
        Cidade = filtro_user['Cidade'].values[0]


        print(f'{'-'*5} Informações do usuário {'-'*5}\n')

        print(f'Nome da loja: {Nome}')
        print(f'País: {pais}')
        print(f'Estado: {Estado}')
        print(f'Cidade: {Cidade}')
        print(f'Total de veiculos: {total_carro}')
        print(f'Total de funcionários: {total_funca}')

        print(f'{'-'*34}\n')