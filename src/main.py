from System_users.user_car import Users
from System_Vendas.Venda_car import Venda
from System_Cadastro.Cadastro_car import Carro



if __name__ == '__main__':
    user = Users()
    user.Cadastro_User()
    # user.Editar_nome()

    user.listar()

    test = Carro()
    test.Cadastrar_veiculo()
    test.listar()

    vendendo = Venda(test)
    vendendo.Realizar_Venda()
    vendendo.listar_vendas()


print('Fim do projeto!!')