import pandas as pd


class Carro:
    def __init__(self):
        # lista = {'Carro': ['Monza'], 'Ano': [1992]}
        
        
        
        
        self._DataCadastro = pd.DataFrame(columns=['Codigo', 'Marca', 'Modelo', 'Preco', 'Ano', 'Quantidade'])
        # self._DataCadastro = pd.DataFrame({
        #     'Codigo': pd.Series(dtype=str),
        #     'Marca': pd.Series(dtype=str),
        #     'Modelo': pd.Series(dtype=str),
        #     'Preco': pd.Series(dtype=float),
        #     'Ano': pd.Series(dtype=int),
        #     'Quantidade': pd.Series(dtype=int)
        #     })

    def Cadastrar_veiculo(self):
        Codigo_Veiculo = f'CRR{self._DataCadastro.shape[0 ] + 1:05d}'
        Marca_Veiculo = input('Informe a Marca: ')
        Modelo_Veiculo = input("Informe o modelo: ")
        Preco_Veiculo = float(input('Informe o preço: '))
        Ano_Veiculo = int(input("Informe o Ano: "))
        Quantidade_veiculo = int(input("Informe quantidade adicionadas: "))
        
        New_Row = {
            'Codigo':Codigo_Veiculo,
            'Marca': Marca_Veiculo,
            'Modelo': Modelo_Veiculo,
            'Preco': Preco_Veiculo,
            'Ano': Ano_Veiculo,
            'Quantidade': Quantidade_veiculo
        }
        
        self._DataCadastro = pd.concat([self._Cadastrar_veiculo, New_Row], ignore_index=True)
        
        
        
    def listar(self):
        print(self._pas)
        
if __name__ == '__main__':
    porst = Carro()
    porst.listar()