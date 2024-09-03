from System_users.user_car import Users
from System_Vendas.Venda_car import Venda
from System_Cadastro.Cadastro_car import Carro
from System_Login.Login_user import Login
from System_Loja.Cad_loja import loja


def main():

    lojas = loja()
    usuario = Users(loja_estacia=lojas)
    Login_usuario = Login(usuario, lojas)
    while True:
        print(f"{('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5)}")
        print('1. Cadastar loja' )
        print('2. Login')
        print('3. sair')

        try:
            opcao = int(input('Informe a opcao: '))
        except ValueError:
            print('Valor Incorreto!!')
            return main()

        if opcao == 1:
            lojas.Cadastrar_Loja()

        elif opcao == 2:
            if usuario._DataUsers.empty and lojas._Loja_Df.empty:
                print('Não existem contas cadastradas!')
                
            else:
                Login_usuario.logar()
                carro_sistema = Carro(user_estacia=usuario, Loja_estacia=lojas,userLogin_estacia=Login_usuario)
                carro_vendas = Venda(carro_sistema,Login_estacia = Login_usuario)
                main_log(Login_usuario, carro_sistema, carro_vendas, lojas, usuario)

        elif opcao == 3:
            print('Saindo do Sistema')
            break
        
        else:
            print('Opção invalida!!')
            return main()



def main_log(Login_usuario, carro_sistema, carro_vendas, loja_estacia, user_estacia):

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
                return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas, loja_estacia=loja_estacia, user_estacia=user_estacia)
                
            if opcao == 1 :   
                if Login_usuario.user_Type == 1:
                    carro_sistema.Cadastrar_veiculo()
                elif Login_usuario.user_Type == 2:
                    print('Usuários Defaults não podem registrar veiculos')
                    return Carro_config()
            elif opcao == 2:
                if carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    carro_vendas.Realizar_Venda()
            elif opcao == 3:
                if carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    carro_sistema.Atualizar_dados_veiculo('Marca', 1, carro_vendas)
                    carro_sistema.Atualizar_dados_veiculo('Modelo', 1, carro_vendas)
            elif opcao == 4:
                if carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    carro_sistema.Atualizar_dados_veiculo('Quantidade', 2)
            elif opcao == 5:
                if carro_sistema._DataCadastro.empty:
                    print('Não existem Carro cadastrados!')
                else:
                    carro_sistema.Atualizar_dados_veiculo('Preco', 3)
            elif opcao == 6:
                carro_sistema.listar_veiculos(Login_usuario.user_login)
            elif opcao == 7:
                carro_vendas.listar_vendas(Login_usuario.user_login)
            elif opcao == 8:
                print("Saindo")
                return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas, loja_estacia=loja_estacia, user_estacia=user_estacia)
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
                user_estacia.Alterar_user(Login_usuario.user_login, 'Nome')
                

            elif opcao == 2:
                user_estacia.Alterar_user(Login_usuario.user_login, 'Senha')

            elif opcao == 3:
                user_estacia.Alterar_user(Login_usuario.user_login, 'Data Nascimento')

            elif opcao == 4:
                user_estacia.Alterar_user(Login_usuario.user_login, 'Sexo')

            elif opcao == 5:
                user_estacia.listar_Informacoes_user(Login_usuario.user_login)

            elif opcao == 6:
                print('Saindo...')
                return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas, loja_estacia=loja_estacia, user_estacia=user_estacia)
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
                if Login_usuario.user_Type == 1:
                    user_estacia.Cadastro_User(Login_usuario.user_login)
                elif Login_usuario.user_Type == 2:
                    print('Só Usuarios do Tipo Adim Podem Fazer Cadastro')

            elif opcao == 2:
                loja_estacia.Alterar_user_admin(Login_usuario.user_login, 'Nome_loja')

            elif opcao == 3:
                loja_estacia.Alterar_user_admin(Login_usuario.user_login, 'Senha')

            elif opcao == 4:
                loja_estacia.Alterar_user_admin(Login_usuario.user_login, 'Pais')

            elif opcao == 5:
                loja_estacia.Alterar_user_admin(Login_usuario.user_login, 'Estado')

            elif opcao == 6:
                loja_estacia.Alterar_user_admin(Login_usuario.user_login, 'Cidade')

            elif opcao == 7:
                print('Saindo...')
                return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas, loja_estacia=loja_estacia, user_estacia=user_estacia)

            else:
                print('Opção incorreta.')
                return Loja_config()


            
    print(f'Bem-vindo(a) {Login_usuario.user_login}')

    while True:

        print(('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5))
        print('1. Veiculos')
        print('2. Usuários')
        print('3. Sair')
        
        try:
            opcao = int(input('Informe a opcao: '))
        except ValueError:
            print('Valor Incorreto!!')
            return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas, loja_estacia=loja_estacia, user_estacia=user_estacia)
        
        if opcao == 1:
            Carro_config()

        elif opcao == 2:
            if Login_usuario.user_Type == 1:
                Loja_config()
            elif Login_usuario.user_Type == 2:
                User_config()

        elif opcao == 3:
            Login_usuario.logout()
            print('Saindo......')
            break
        else:
            print('Opção invalida!!')


if __name__ == '__main__':
    main()