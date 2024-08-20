from System_users.user_car import Users
from System_Vendas.Venda_car import Venda
from System_Cadastro.Cadastro_car import Carro
from System_Login.Login_user import Login
from System_Loja.Cad_loja import loja



if __name__ == '__main__':
    lojas = loja()
    lojas.Cadastrar_Loja()


    user = Users(loja_estacia=lojas)
    user.Cadastro_User()


    user.listar()

    test = Carro()
    test.Cadastrar_veiculo()
    test.listar()

    log = Login(user)
    log.logar()

    vendendo = Venda(test, log)
    vendendo.Realizar_Venda()
    vendendo.listar_vendas()


    print(log.Login_successful)
    print(log.user_login)

    print('Fim do projeto!!')