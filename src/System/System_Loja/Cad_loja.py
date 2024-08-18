import pandas as pd

class loja:
    def __init__(self):
        self._Loja_Df = pd.DataFrame(columns=['Nome_loja', 'Pais', 'Estado', 'cidade']) # Moeda ??
        
        self._Loja_Df = self._Loja_Df.astype({
            'Nome_loja': 'String',
            'Pais': 'String',
            'Estado': 'String',
            'Cidade': 'String'
        })
        
        
    def Cadastrar_Loja(self):
        Nm_loja = input('Informe o Nome da Loja: ')
        Pais = input('Informe o país: ')
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        
        self._Loja_Df.loc[self._Loja_Df.shape[0]] = [
            Nm_loja,
            Pais,
            estado,
            cidade
        ]
        
    def listar_lojas(self):
        print(self._Loja_Df)
        
    
    