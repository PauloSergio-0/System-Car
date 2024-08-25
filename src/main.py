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
        print(('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5))
        print('1. Cadastar loja')
        print('2. Cadastrar Usuario')
        print('3. Login')
        print('4. sair')
        try:
            opcao = int(input('Informe a opcao: '))
        except ValueError:
            print('Valor Incorreto!!')
            return main()

        if opcao == 1:
            lojas.Cadastrar_Loja()
        elif opcao == 2:
            if lojas._Loja_Df.empty:
                    print('Não existem lojas cadastradas!')
            else:
                usuario.Cadastro_User()
        elif opcao == 3:
            if usuario._DataUsers.empty and lojas._Loja_Df.empty:
                print('Não existem usuarios cadastrados!')
                
            else:
                Login_usuario.logar()
                carro_sistema = Carro(user_estacia=usuario, Loja_estacia=lojas,userLogin_estacia=Login_usuario)
                carro_vendas = Venda(carro_sistema,user_name=Login_usuario.user_login)
                main_log( Login_usuario, carro_sistema, carro_vendas, lojas, usuario)
        elif opcao == 4:
            break
        else:
            print('Opção invalida!!')



def main_log(Login_usuario, carro_sistema, carro_vendas, loja_estacia, user_estacia):
    
    
    print(f'Bem-vindo(a) {Login_usuario.user_login}')

    while True:

        print(('-'*5) + 'ESTOQUE GLOBAL' + ('-'*5))
        print('1. Cadastrar Carro')
        print('2. Vender Carro')
        print('3. Sair')

        try:
            opcao = int(input('Informe a opcao: '))
        except ValueError:
            print('Valor Incorreto!!')
            return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas)

        if opcao == 1:
            
            if Login_usuario.user_Type == 1:
                carro_sistema.Cadastrar_veiculo()
            elif Login_usuario.user_Type == 2:
                print('Usuários Defaults não podem registrar veiculos')
                return main_log(Login_usuario = Login_usuario, carro_sistema = carro_sistema, carro_vendas = carro_vendas)
                
        elif opcao == 2:
            if carro_sistema._DataCadastro.empty:
                print('Não existem Carro cadastrados!')
            else:
                carro_vendas.Realizar_Venda()
        elif opcao == 3:
            Login_usuario.logout()
            print('Saindo......')
            break
        else:
            print('Opção invalida!!')


if __name__ == '__main__':
    main()