from modules.System_users.user_car import Users
from modules.System_Vendas.Venda_car import Venda
from modules.System_Cadastro.Cadastro_car import Carro
from modules.System_Login.Login_user import Login
from modules.System_Loja.Cad_loja import Loja
from modules.System_estatistica.estatistica_car import Estatistica

class Main:
    
    """
    Classe responsável por gerenciar a interação do usuário com o sistema.

    Esta classe inicializa e gerencia todos os componentes principais do sistema, 
    incluindo lojas, usuários, login, veículos, vendas e estatísticas. Fornece 
    um menu de navegação para o usuário interagir com o sistema.

    Atributos:
        lojas (Loja): Sistema de gerenciamento de lojas.
        usuario (Users): Sistema de gerenciamento de usuários.
        Login_usuario (Login): Sistema de login de usuários.
        carro_sistema (Carro): Sistema de gerenciamento de veículos.
        carro_vendas (Venda): Sistema de gerenciamento de vendas.
        Estatistica (Estatistica): Sistema de gerenciamento de estatísticas (usado apenas no modo de administrador).

    Métodos:
        __init__: Inicializa os componentes do sistema e configura o menu de interação.
        carro_config: Exibe o menu de opções para gerenciar veículos.
        user_config: Exibe o menu de opções para gerenciar informações do usuário.
        loja_config: Exibe o menu de opções para gerenciar a loja e as estatísticas.
        menu_inicial: Exibe o menu inicial para cadastro de lojas e login de usuários.
        main_log: Exibe o menu principal após o login, permitindo acessar configurações de veículos ou usuários.

    Exceções:
        ValueError: Captura entradas inválidas do usuário e oferece a opção de tentar novamente.
    """

    def __init__(self):
        self.lojas = Loja()
        self.usuario = Users(self.lojas)
        self.Login_usuario = Login(self.usuario, self.lojas)


    def carro_config(self):
        while True:
            print('-'*5+'Veiculos'+'-'*5)
            print('1. Cadastrar veiculo')
            print('2. Vender veiculo')
            print('3. Editar Nome veiculo')
            print('4. Editar Quantidade')
            print('5. Editar Preço')
            print('6. Listar Veiculos')
            print('7. Listar Vendas')
            print('8. Sair')
            
            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                return self.main_log()
                
            if opcao == 1 :   
                if self.Login_usuario.user_Type == 1:
                    self.carro_sistema.cadastrar_veiculo()
                elif self.Login_usuario.user_Type == 2:
                    print('Usuários Defaults não podem registrar veiculos')
                    # return self.carro_config()
                    continue
            elif opcao == 2:
                if self.carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    self.carro_vendas.realizar_Venda()
            elif opcao == 3:
                if self.carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    self.carro_sistema.atualizar_dados_veiculo('Marca', 1, self.carro_vendas)
                    self.carro_sistema.atualizar_dados_veiculo('Modelo', 1, self.carro_vendas)
            elif opcao == 4:
                if self.carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    self.carro_sistema.atualizar_dados_veiculo('Quantidade', 2, self.carro_vendas)
            elif opcao == 5:
                if self.carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    self.carro_sistema.atualizar_dados_veiculo('Preco', 3, self.carro_vendas)
            elif opcao == 6:
                self.carro_sistema.listar_veiculos(self.Login_usuario.user_login)
            elif opcao == 7:
                self.carro_vendas.listar_vendas(self.Login_usuario.user_login)
            elif opcao == 8:
                print("Saindo")
                return 
            else:
                print('Opcao invalida')
                continue 
        

    def user_config(self):
        while True:

            print(f"{('-'*5)+'Usuário'+('-'*5)}")
            print('1. Alterar nome')
            print('2. Alterar senha')
            print('3. Alterar Data de nascimento')
            print('4. Alterar sexo')
            print('5. Informações do usuário')
            print('6. Sair')
            
            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                # return self.user_config()
                return

            if opcao == 1:
                self.usuario.alterar_user(self.Login_usuario.user_login, 'Nome')
                

            elif opcao == 2:
                self.usuario.alterar_user(self.Login_usuario.user_login, 'Senha')

            elif opcao == 3:
                self.usuario.alterar_user(self.Login_usuario.user_login, 'Data Nascimento')

            elif opcao == 4:
                self.usuario.alterar_user(self.Login_usuario.user_login, 'Sexo')

            elif opcao == 5:
                self.usuario.listar_Informacoes_user(self.Login_usuario.user_login)

            elif opcao == 6:
                print('Saindo...')
                return 
            else:
                print('Opção incorreta.')
                continue
        
    def loja_config(self):
        self.Estatistica = Estatistica(self.usuario, self.carro_sistema, self.carro_vendas, self.lojas,self.Login_usuario)

        while True:

            print('1. Cadastrar usuário')
            print('2. Alterar nome')
            print('3. Alterar senha')
            print('4. Alterar pais')
            print('5. Alterar estado')
            print('6. Cidade')
            print('7. Informações da loja')
            print('8. estátistica da loja da loja')
            print('9. Sair')
            
            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                continue
            

            if opcao == 1:
                if self.Login_usuario.user_Type == 1:
                    self.usuario.cadastro_User(self.Login_usuario.user_login)
                elif self.Login_usuario.user_Type == 2:
                    print('Só Usuarios do Tipo Adim Podem Fazer Cadastro')

            elif opcao == 2:
                self.lojas.alterar_user_admin(self.Login_usuario.user_login, 'Nome_loja')

            elif opcao == 3:
                self.lojas.alterar_user_admin(self.Login_usuario.user_login, 'Senha')

            elif opcao == 4:
                self.lojas.alterar_user_admin(self.Login_usuario.user_login, 'Pais')

            elif opcao == 5:
                self.lojas.alterar_user_admin(self.Login_usuario.user_login, 'Estado')

            elif opcao == 6:
                self.lojas.alterar_user_admin(self.Login_usuario.user_login, 'Cidade')

            elif opcao == 7:
                self.lojas.listar_Informacoes_loja(User_login=self.Login_usuario.user_login, funca_estacia=self.usuario._DataUsers, carro_estacia=self.carro_sistema._DataCadastro)

            elif opcao == 8:
                self.Estatistica.mostrar_estatistica()
            elif opcao == 9:
                print('Saindo...')
                return 

            else:
                print('Opção incorreta.')
                continue

    def menu_inicial(self):
        while True:
            print(f"{('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5)}")
            print('1. Cadastar loja' )
            print('2. Login')
            print('3. sair')

            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                return self.menu_inicial()

            if opcao == 1:
                self.lojas.cadastrar_Loja()

            elif opcao == 2:
                if self.usuario._DataUsers.empty and self.lojas._Loja_Df.empty:
                    print('Não existem contas cadastradas!')
                    
                else:
                    self.Login_usuario.logar()
                    self.carro_sistema = Carro(user_estacia=self.usuario, Loja_estacia=self.lojas,userLogin_estacia=self.Login_usuario)
                    self.carro_vendas = Venda(self.carro_sistema,Login_estacia = self.Login_usuario)
                    self.main_log()

            elif opcao == 3:
                print('Saindo do Sistema')
                break
            
            else:
                print('Opção invalida!!')
                return self.menu_inicial()

    def main_log(self):

        print(f'Bem-vindo(a) {self.Login_usuario.user_login}')

        while True:

            print(('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5))
            print('1. Veiculos')
            print('2. Usuários')
            print('3. Sair')
            
            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                continue
            
            if opcao == 1:
                self.carro_config()

            elif opcao == 2:
                if self.Login_usuario.user_Type == 1:
                    self.loja_config()
                elif self.Login_usuario.user_Type == 2:
                    self.user_config()

            elif opcao == 3:
                self.Login_usuario.logout()
                print('Saindo......')
                break
            else:
                print('Opção invalida!!')
                continue
