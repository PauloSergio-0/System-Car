import pandas as pd


class Carro:
    def __init__(self):
        # lista = {'Carro': ['Monza'], 'Ano': [1992]}
        
        
        
        
        self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade'])
        
        self._DataCadastro = self._DataCadastro.astype({
            'Codigo': 'string',
            'Marca': 'string',
            'Modelo': 'string',
            'Preco': 'float64',
            'Ano': 'int32',
            'Quantidade': 'int32'
        })

    def Cadastrar_veiculo(self):
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0 ] + 1:05d}'
        Marca_Veiculo = input('Informe a Marca: ')
        Modelo_Veiculo = input("Informe o modelo: ")
        Preco_Veiculo = float(input('Informe o preço: '))
        Ano_Veiculo = int(input("Informe o Ano: "))
        Quantidade_veiculo = int(input("Informe quantidade adicionadas: "))
        
        self._DataCadastro.loc[self._DataCadastro.shape[0]] = [
            Codigo_Veiculo,
            Marca_Veiculo,
            Modelo_Veiculo,
            Preco_Veiculo,
            Ano_Veiculo,
            Quantidade_veiculo
        ]
        
    def Atualizar_preco_veiculo(self):
        Codigo_search = input('Imforme o código: ')
        
        if Codigo_search in self._DataCadastro['Codigo'].values:
            
            index = self._DataCadastro[self._DataCadastro['Codigo'] == Codigo_search ].index[0]
            
            self._DataCadastro.at[index,'Preco'] = float(input('Informe o novo preço:'))
            
            print('Valor atualizado')
        else:
            print('Não encontrado')
        
    def listar(self):
        print(self._DataCadastro)
        
if __name__ == '__main__':
    user = Carro()
    user.Cadastrar_veiculo()
    user.Cadastrar_veiculo()
    user.listar()
    user.Atualizar_preco_veiculo()
    user.listar()