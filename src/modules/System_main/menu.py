from modules.System_users.user_car import Users
from modules.System_Vendas.Venda_car import Venda
from modules.System_Cadastro.Cadastro_car import Carro
from modules.System_Login.Login_user import Login
from modules.System_Loja.Cad_loja import loja


class main:
    def __init__(self):
        self.lojas = loja()
        self.usuario = Users(self.lojas)
        self.usuario = Users(loja_estacia=self.lojas)
        self.Login_usuario = Login(self.usuario, self.lojas)

    def Menu_inicial(self):
        while True:
            print(f"{('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5)}")
            print('1. Cadastar loja' )
            print('2. Login')
            print('3. sair')

            try:
                opcao = int(input('Informe a opcao: '))
            except ValueError:
                print('Valor Incorreto!!')
                return self.Menu_inicial()

            if opcao == 1:
                self.lojas.Cadastrar_Loja()

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
                return self.Menu_inicial()

            
    def main_log(self):

        def Carro_config():
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
                        self.carro_sistema.Cadastrar_veiculo()
                    elif self.Login_usuario.user_Type == 2:
                        print('Usuários Defaults não podem registrar veiculos')
                        return Carro_config()
                elif opcao == 2:
                    if self.carro_sistema._DataCadastro.empty:
                        print('Não existem Carro cadastrados!')
                    else:
                        self.carro_vendas.Realizar_Venda()
                elif opcao == 3:
                    if self.carro_sistema._DataCadastro.empty:
                        print('Não existem Carro cadastrados!')
                    else:
                        self.carro_sistema.Atualizar_dados_veiculo('Marca', 1, self.carro_vendas)
                        self.carro_sistema.Atualizar_dados_veiculo('Modelo', 1, self.carro_vendas)
                elif opcao == 4:
                    if self.carro_sistema._DataCadastro.empty:
                        print('Não existem Carro cadastrados!')
                    else:
                        self.carro_sistema.Atualizar_dados_veiculo('Quantidade', 2)
                elif opcao == 5:
                    if self.carro_sistema._DataCadastro.empty:
                        print('Não existem Carro cadastrados!')
                    else:
                        self.carro_sistema.Atualizar_dados_veiculo('Preco', 3)
                elif opcao == 6:
                    self.carro_sistema.listar_veiculos(self.Login_usuario.user_login)
                elif opcao == 7:
                    self.carro_vendas.listar_vendas(self.Login_usuario.user_login)
                elif opcao == 8:
                    print("Saindo")
                    return self.main_log()
                else:
                    print('Opcao invalida')
                    return Carro_config()
            

        def User_config():
            
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
                    return User_config()
                

                if opcao == 1:
                    self.usuario.Alterar_user(self.Login_usuario.user_login, 'Nome')
                    

                elif opcao == 2:
                    self.usuario.Alterar_user(self.Login_usuario.user_login, 'Senha')

                elif opcao == 3:
                    self.usuario.Alterar_user(self.Login_usuario.user_login, 'Data Nascimento')

                elif opcao == 4:
                    self.usuario.Alterar_user(self.Login_usuario.user_login, 'Sexo')

                elif opcao == 5:
                    self.usuario.listar_Informacoes_user(self.Login_usuario.user_login)

                elif opcao == 6:
                    print('Saindo...')
                    return self.main_log()
                else:
                    print('Opção incorreta.')
                    return User_config()
            
        def Loja_config():
            while True:

                print('1. Cadastrar usuário')
                print('2. Alterar nome')
                print('3. Alterar senha')
                print('4. Alterar pais')
                print('5. Alterar estado')
                print('6. Cidade')
                print('7. Sair')
                
                try:
                    opcao = int(input('Informe a opcao: '))
                except ValueError:
                    print('Valor Incorreto!!')
                    return Loja_config()
                

                if opcao == 1:
                    if self.Login_usuario.user_Type == 1:
                        self.usuario.Cadastro_User(self.Login_usuario.user_login)
                    elif self.Login_usuario.user_Type == 2:
                        print('Só Usuarios do Tipo Adim Podem Fazer Cadastro')

                elif opcao == 2:
                    self.lojas.Alterar_user_admin(self.Login_usuario.user_login, 'Nome_loja')

                elif opcao == 3:
                    self.lojas.Alterar_user_admin(self.Login_usuario.user_login, 'Senha')

                elif opcao == 4:
                    self.lojas.Alterar_user_admin(self.Login_usuario.user_login, 'Pais')

                elif opcao == 5:
                    self.lojas.Alterar_user_admin(self.Login_usuario.user_login, 'Estado')

                elif opcao == 6:
                    self.lojas.Alterar_user_admin(self.Login_usuario.user_login, 'Cidade')

                elif opcao == 7:
                    print('Saindo...')
                    return self.main_log()

                else:
                    print('Opção incorreta.')
                    return Loja_config()


            
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
                return self.main_log()
            
            if opcao == 1:
                Carro_config()

            elif opcao == 2:
                if self.Login_usuario.user_Type == 1:
                    Loja_config()
                elif self.Login_usuario.user_Type == 2:
                    User_config()

            elif opcao == 3:
                self.Login_usuario.logout()
                print('Saindo......')
                break
            else:
                print('Opção invalida!!')