import pandas as pd
import os
import re
from argon2 import PasswordHasher

class loja:
    def __init__(self):

        if os.path.exists("./src/Datasets/Loja_data/Loja_system.csv"):
            self._Loja_Df = pd.read_csv("./src/Datasets/Loja_data/Loja_system.csv", sep=";", encoding="UTF-8")

        else:
            self._Loja_Df = pd.DataFrame(columns=['Nome_loja', 'Pais', 'Estado', 'Cidade','Senha','Type']) # Moeda ??  add ==> type user
            
            self._Loja_Df = self._Loja_Df.astype({
                'Nome_loja': 'string',
                'Pais': 'string',
                'Estado': 'string',
                'Cidade': 'string',
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
                
    def Cadastrar_Loja(self):
        Nm_loja = input('Informe o Nome da Loja: ')
        Pais = input('Informe o país: ')
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        senha = self.verificar_senha()
        Tipo = 'Admin'

        self._Loja_Df.loc[self._Loja_Df.shape[0]] = [
            Nm_loja,
            Pais,
            estado,
            cidade,
            senha,
            Tipo
        ]

        self._Loja_Df.to_csv("./src/Datasets/Loja_data/Loja_system.csv", sep = ";",encoding="UTF-8",index=False)

    def listar_lojas(self):
        print(self._Loja_Df)