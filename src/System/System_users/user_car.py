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
                    return not (len(str(Ano)) < 4 and len(str(Ano)) > 4) and not (Ano > data_atual.year) and (Ano > 1800)

                try:
                    dia = Verificar_datas(Tipo_date='Dia', verificacao=Dia_vf) 
                    mes = Verificar_datas('Mes',Mes_vf)
                    ano = Verificar_datas('Ano', Ano_vf)

                    dt_nasc =  date(day = dia, month = mes, year = ano)
                    return dt_nasc
                except ValueError:
                        print('Erro no valor inserido:')
                        return data_nascimento()

            def Idade_calc(data_nascimento):
            
                idade =  data_atual.year - data_nasc.year

                if (data_atual.day , data_atual.month) < (data_nasc.day, data_nasc.month):
                    idade -= 1
                
                return idade
            
            data_nasc = data_nascimento()
            if data_nasc > data_atual:
                print('Não é possivel nascer no futuro!!!!.')
                data_nasc = data_nascimento()

            
            idade = Idade_calc(data_nasc)
            data_nasc = data_nasc.strftime('%d/%m/%Y')

            return data_nasc, idade
        
        def Escolha_Sexo():
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
                return Escolha_Sexo()
            else:
                print('Item Invalido')
                return Escolha_Sexo()



        codigo_user = f'USR{self._DataUsers.shape[0]+1:05d}'
        name = input('Informe nome do usuário: ') # add verificador de nome
        Data_de_nascimento,idade = data_idade()
        sexo = Escolha_Sexo()
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