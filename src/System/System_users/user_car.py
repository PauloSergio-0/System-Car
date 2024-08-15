import pandas as pd
from datetime import datetime, date
from uuid import uuid5
import re


class Users():
    def __init__(self):
        self._DataUsers = pd.DataFrame(columns=['Codigo','Nome', 'Data Nascimento', 'idade', 'Sexo', 'Senha']) # add ==> loja
        
        self._DataUsers = self._DataUsers.astype({
            'Codigo': 'string',
            'Nome': 'string',
            'Data Nascimento': 'string',
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
        

        def data_idade():
            data_atual = date.today()
            def data_nascimento(): #=> verificador de inputs (dt_nasc ==> dia, mes,ano)
                
                print('Informe data de nascimento: ')
                
                    
                def Dia_vf():
                    try:
                        dia = int(input('Dia: '))
                    except ValueError:
                        print("Error: o valor deve ser numero inteiro")
                        return Dia_vf()
                    if not (len(str(dia)) > 2 and len(str(dia)) < 1) and not(dia < 1):
                        return dia
                    else:
                        return Dia_vf()

                def Mes_vf():
                    try:
                        mes = int(input('Mes: '))
                    except ValueError:
                        print("Error: o valor deve ser numero inteiro")
                        return Mes_vf()
                    if not (len(str(mes)) > 2 and len(str(mes)) < 1) and (mes >= 1 and mes <= 12):
                        return mes
                    else:
                        return Mes_vf()

                def Ano_vf():
                    try:
                        ano = int(input('Ano: '))

                    except ValueError:
                        print("Error: o valor deve ser numero inteiro")
                        return Ano_vf()
                    
                    if not (len(str(ano)) < 4 and len(str(ano)) > 4) and not (ano > data_atual.year) and (ano > 1800):
                        return ano
                    else:
                        return Ano_vf()

                try:
                    dia = Dia_vf() 
                    mes = Mes_vf()
                    ano = Ano_vf()

                    dt_nasc =  date(day = dia, month = mes, year = ano)
                    return dt_nasc
                except ValueError:
                        print('Erro no valor inserido?')
                        return data_nascimento()
                


            def Idade_calc(data_nascimento):
                
                
                idade =  data_atual.year - data_nasc.year

                if (data_atual.day , data_atual.month) < (data_nasc.day, data_nasc.month):
                    idade -= 1
                
                return idade
            
            data_nasc = data_nascimento()
            if data_nasc > data_atual:
                print('Sua data de Nascimento é invalida pois é maior que a o ano atual.')
                data_nasc = data_nascimento()

            
            idade = Idade_calc(data_nasc)
            data_nasc = data_nasc.strftime('%d/%m/%Y')

            return data_nasc, idade


        codigo_user = f'USR{self._DataUsers.shape[0]+1:05d}'
        name = input('Informe nome do usuário: ')
        Data_de_nascimento,idade = data_idade()
        sexo = input('Informe Sexo: ')
        senha = self.verificar_senha() 
        self._DataUsers.loc[self._DataUsers.shape[0]] =[
            codigo_user,
            name,
            Data_de_nascimento,
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