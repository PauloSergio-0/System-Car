import os
from datetime import datetime
import pandas as pd


class Estatistica:
    def __init__(self, Users, Carro, Venda, Loja, Log_on):
        self._DataUsers = Users._DataUsers
        self._DataCadastro = Carro._DataCadastro
        self._DataVenda = Venda._DataVenda
        self._Loja_Df = Loja._Loja_Df
        self.Log_on = Log_on

        # Caminho do diretório
        self.dir_estatistica = f'./src/Data/Estatistica_data/{self.Log_on.user_login}_Data'
        self.arquivo_estatistica = f'{self.dir_estatistica}/{self.Log_on.user_login}_data.txt'

        if os.path.exists(self.arquivo_estatistica):
            with open(self.arquivo_estatistica, 'r') as estatistica:
                self.conteudo = estatistica.read()
        else:
            os.makedirs(self.dir_estatistica, exist_ok=True)
            self.conteudo = None

    def realizar_estatistica(self):
        
        # Filtrando os dados
        usuarios_filter = self._DataUsers[self._DataUsers['Loja'] == self.Log_on.user_login]
        Carro_filter = self._DataCadastro[self._DataCadastro['Loja'] == self.Log_on.user_login]
        vendas_filter = self._DataVenda[self._DataVenda['Loja'] == self.Log_on.user_login]
        
        
        index = self._Loja_Df[self._Loja_Df['Usuario_loja'] == self.Log_on.user_login].index[0]

        
        
        # Estatísticas
        
        usuario = usuarios_filter['Usuario'].unique()
        num_usuario = len(usuario)

        vendas_usuario = vendas_filter.groupby(['Loja', 'Vendedor'])['Quantidade_Vendida'].sum()
        
        

        marcas = len(Carro_filter['Marca'].unique())
        modelos = len(Carro_filter['Modelo'].unique())
        total_veiculos_marca = Carro_filter.groupby('Marca')['Quantidade'].sum()
        total_modelos_marca = Carro_filter.groupby('Marca')['Modelo'].nunique()
        total_veiculo_modelo = Carro_filter.groupby(['Marca', 'Modelo'])['Quantidade'].sum()

        # Criar diretório se não existir
        os.makedirs(self.dir_estatistica, exist_ok=True)

        # Escrevendo no arquivo
        with open(self.arquivo_estatistica, 'w', encoding='utf-8') as estatistica:
            estatistica.write(f'Dados Loja: {self.Log_on.user_login}\n')
            estatistica.write(f'Nome da loja: {self._Loja_Df.loc[index,'Nome_loja']}\n')
            estatistica.write(f'Pais da loja: {self._Loja_Df.loc[index,'Pais']}\n')
            estatistica.write(f'Estado da loja: {self._Loja_Df.loc[index,'Estado']}\n')
            estatistica.write(f'Cidade da loja: {self._Loja_Df.loc[index,'Cidade']}\n\n')
            
            estatistica.write('Dados usuários\n')
            estatistica.write(f'Total de vendedores: {num_usuario}\n')
            for (loja,vendedor), qtd_venda in vendas_usuario.items():
                estatistica.write(f'Loja: {loja} Vendedor: {vendedor} Nº vendas: {qtd_venda}\n')
            estatistica.write('\n')
            
            estatistica.write(f'Dados Veiculos\n')
            estatistica.write(f'Números Totais de Veículos: {Carro_filter["Quantidade"].sum()}\n')
            estatistica.write(f'Números Totais de Marcas: {marcas}\n')
            estatistica.write(f'Números Totais de modelos: {modelos}\n\n')

            
            estatistica.write('Total de veículos por marca:\n')
            for marca, qtd in total_veiculos_marca.items():
                estatistica.write(f'{marca}: {qtd} veículos\n')
            estatistica.write('\n')

            estatistica.write('Total de modelos por marcas:\n')
            for marca, qtd_model in total_modelos_marca.items():
                estatistica.write(f'{marca}: {qtd_model} modelos\n')
            estatistica.write('\n')

            estatistica.write('Total de modelo por Marca\n')
            for (marca, modelo), qtd in total_veiculo_modelo.items():
                estatistica.write(f'Marca: {marca} Modelo: {modelo} Quantidade: {qtd}\n')
            estatistica.write('\n')
            
    def mostrar_estatistica(self):
        self.realizar_estatistica()
        with open(self.arquivo_estatistica, 'r', encoding='utf-8') as conteudo:
            self.conteudo = conteudo.read()
            print(f'\n{self.conteudo}')