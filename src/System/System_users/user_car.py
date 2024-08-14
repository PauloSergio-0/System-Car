import pandas as pd
from datetime import datetime, date
from uuid import uuid5
import re

class Users():
    def __init__(self):
        self._DataUsers = pd.DataFrame(columns=['Codigo','Nome', 'idade', 'Sexo', 'Senha']) # add ==> loja
        
        self._DataUsers = self._DataUsers.astype({
            'Codigo': 'string',
            'Nome': 'string',
            'idade': 'int64',
            'Sexo': 'string',
            'Senha': 'string'
        })
        

    def verificar_senha(self): # ADD module uuid() hash

        """
        Verifica a qualidade da senha com base em vários critérios:
        - Comprimento mínimo de 8 caracteres
        - Pelo menos uma letra maiúscula
        - Pelo menos uma letra minúscula
        - Pelo menos um número
        - Pelo menos um caractere especial
        """
        senha = input('Informe a senha: ')

        criterios = { # dicionário com os valores da verificação de criterios
            "comprimento_minimo": len(senha) >= 8,
            "letra_maiuscula": re.search(r'[A-Z]', senha) is not None,
            "letra_minuscula": re.search(r'[a-z]', senha) is not None,
            "numero": re.search(r'\d', senha) is not None,
            "caractere_especial": re.search(r'[^a-zA-Z0-9]', senha) is not None,
            "Tem_espaços": re.search(r'\s', senha) is None
        }
        todos_criterios_satisfeitos = all(criterios.values()) # capta os booleanos gerados

        criterios, valido = criterios, todos_criterios_satisfeitos

        if valido:
            print("Senha válida!")
            return senha
        else:
            print("Senha inválida. Critérios não atendidos:")
            for criterio, atendido in criterios.items():
                if not atendido:
                    print(f"- {criterio.replace('_', ' ').capitalize()}")
                    return self.verificar_senha()


    def Editar_nome(self):
        Codigo_seach = input('Informe o codigo: ')
        if Codigo_seach in self._DataUsers['Codigo'].values:
            index = self._DataUsers[self._DataUsers['Codigo'] == Codigo_seach].index[0]
            new_name = input('Informe Novo nome:')
            self._DataUsers.at[index,'Nome'] = new_name

            print('Nome Atualizado!!')
        else:
            print('Código não encontrado')
            return self.Editar_nome()


    def Cadastro_User(self):
        codigo_user = f'USR{self._DataUsers.shape[0]+1:05d}'
        name = input('Informe nome do usuário: ')
        idade = int(input("Informe a idade: "))
        sexo = input('Informe Sexo: ')
        senha = self.verificar_senha() 
        self._DataUsers.loc[self._DataUsers.shape[0]] =[
            codigo_user,
            name,
            idade,
            sexo,
            senha
        ]


    def listar(self):
        print(self._DataUsers)

if __name__ == '__main__':
    test = Users()
    test.Cadastro_User()
    test.listar()
    test.Editar_nome()
    test.listar()