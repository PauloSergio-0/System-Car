import System_Cadastro.Cadastro_car as Cadastro_car
import pandas as pd

class Venda(Cadastro_car.Carro):
    def __init__(self):
        super().__init__()
        self._DataVenda = pd.DataFrame(columns=['Nr_Fatura', 'Valor_transacao', 'Modelo', 'Marca', 'data_transancao', 'Metodo Pagamento']) # add --> 'Comprador', 'Vendedor' ,'loja'
        self._DataVenda= self._DataVenda.astype({
            'Nr_Fatura': 'string',
            'Valor_transacao': 'float64',
            'Modelo': 'string',
            'Marca': 'string',
            'data_transancao': 'string',
            'Metodo Pagamento': 'string'
        })

    def Realizar_Venda(self):
        print('teste VENDAS')
        print(self._DataCadastro)

if __name__ == '__main__':
    sell = Venda()
    sell.Realizar_Venda()
    