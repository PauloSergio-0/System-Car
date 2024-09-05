import os
from datetime import datetime
import pandas as pd

from modules.System_users.user_car import Users
from modules.System_Vendas.Venda_car import Venda
from modules.System_Cadastro.Cadastro_car import Carro
from modules.System_Login.Login_user import Login
from modules.System_Loja.Cad_loja import loja


class Estatistica:
    def __init__(self, Users, Carro, Venda, Log_on):

        self._DataUsers =  Users._DataUsers
        self._DataCadastro = Carro._DataCadastro
        self._DataVenda = Venda._DataVenda
        self.Log_on = Log_on
        self.conteudo  

        if os.path.exists(f'./src/Data/Estatistica_data/{self.Log_on.user_login}_Data/{self.Log_on.user_login}_data.txt'):

            with open(f'./src/Data/Estatistica_data/{self.Log_on.user_login}_Data/{self.Log_on.user_login}_data.txt', 'r') as estatistica:
                self.conteudo = estatistica.read()
        else:
                self.conteudo = None
            
    def Realizar_estatistica(self):
        usuarios_filter = self._DataUsers[self._DataUsers['Loja'] == self.Log_on.user_login]
        Carro_filter = self._DataCadastro[self._DataCadastro['Loja'] == self.Log_on.user_login]
        vendas_filter = self._DataVenda[self._DataVenda['Loja'] == self.Log_on.user_login]

        marcas = Carro_filter['Marca'].unique()
        modelos = len(marcas)

        total_veiculos_marca = Carro_filter.groupby('Marca')['Quantidade'].sum()

        total_modelos_marca = Carro_filter.groupby('Marca')['Modelo'].nunique()

        total_veiculo_modelo = Carro_filter.groupby(['Marca', 'Modelo'])['Quantidade'].sum()

        
        with open(f'./src/Data/Estatistica_data/{self.Log_on.user_login}_Data/{self.Log_on.user_login}_data.txt', 'w') as estatistica:
            estatistica.write(f'Números Totais de Veiculos: {sum(Carro_filter['Quantidade'])}\n\n')

            estatistica.write('Total de de vaiculos por marca:\n')
            for marca, qtd in total_veiculos_marca.items():
                estatistica.write(f'{marca}: {qtd} veiculos\n')
            estatistica.write('\n')

            estatistica.write('Total de modelos por marcas:\n')
            for marca, qtd_model in total_modelos_marca.items():
                estatistica.write(f'{marca}: {qtd_model} modelos\n')
            estatistica.write('\n')
            
            estatistica.write('Total de modelo por Marca')
            for marca, modelo, qtd in total_veiculo_modelo.items():
                estatistica.write(f'Marca: {marca} Modelo: {modelo} Quantidade: {qtd}\n')
            estatistica.write('\n')

            print(estatistica)


