import pandas as pd
from datetime import datetime, date
from uuid import uuid5

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
        
        
    def Cadastro_User(self):
        codigo_user = f'USR{self._DataUsers.shape[0]+1:05d}'
        name = input('Informe nome do usuário')
        idade = int(input("Informe a idade: "))
        sexo = input('Informe Sexo')
        senha = input('Informe a senha: ')
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