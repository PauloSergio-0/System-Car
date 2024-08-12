import pandas as pd
from datetime import date, datetime


class Carro:
    def __init__(self):

        self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade', 'Data Cadastro', 'Data Modificacao'])
        
        self._DataCadastro = self._DataCadastro.astype({
            'Codigo': 'string',
            'Marca': 'string',
            'Modelo': 'string',
            'Preco': 'float64',
            'Ano': 'int32',
            'Quantidade': 'int32',
            'Data Cadastro': 'datetime64[ns]',
            'Data Modificacao': 'datetime64[ns]'
        })

    def Cadastrar_veiculo(self):
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0 ] + 1:05d}'
        Marca_Veiculo = input('Informe a Marca: ')
        Modelo_Veiculo = input("Informe o modelo: ")
        Preco_Veiculo = float(input('Informe o preço: '))
        Ano_Veiculo = int(input("Informe o Ano: "))
        Quantidade_veiculo = int(input("Informe quantidade adicionadas: "))
        data_de_cadastro = date.today().strftime('%d/%m/%Y')
        data_de_modificacao = None
        
        self._DataCadastro.loc[self._DataCadastro.shape[0]] = [
            Codigo_Veiculo,
            Marca_Veiculo,
            Modelo_Veiculo,
            Preco_Veiculo,
            Ano_Veiculo,
            Quantidade_veiculo,
            data_de_cadastro,
            data_de_modificacao
        ]
        
    def Atualizar_preco_veiculo(self):
        Codigo_search = input('Iforme o código: ')
        
        if Codigo_search in self._DataCadastro['Codigo'].values:
            
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search ].index[0]
            
            self._DataCadastro.at[index,'Preco'] = float(input('Informe o novo preço:'))
            self._DataCadastro.at[index,'Data Modificacao'] = datetime.today().strftime('%d/%m/%Y, %H:%M:%S')
            print('Valor atualizado')
        else:
            print('Não encontrado')
        
    def listar(self):
        print(self._DataCadastro)

    def listar_info(self):
        print(self._DataCadastro.info())
        
if __name__ == '__main__':
    user = Carro()
    user.Cadastrar_veiculo()
    user.Cadastrar_veiculo()
    user.listar()
    user.Atualizar_preco_veiculo()
    user.listar()
    user.listar_info()