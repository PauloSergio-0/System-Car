from argon2 import PasswordHasher 


class Login():
    """
    Classe responsável pela autenticação de usuários e gerenciamento de sessões de login.

    Esta classe permite que os usuários façam login como administrador ou usuário padrão, verificando 
    suas credenciais e gerenciando o estado de autenticação. Também inclui métodos para logout e 
    gerenciamento de sessões.

    Atributos:
        Login_successful (bool): Indica se o login foi bem-sucedido.
        password_login (str): Senha fornecida pelo usuário durante o login.
        user_login (str): Nome de usuário fornecido durante o login.
        user_Type (int): Tipo de usuário (1 para Admin, 2 para Default).
        id_user (int): Identificador do usuário (não utilizado atualmente).
        loja_user (str): Nome da loja associada ao usuário.
        _DataUsers (DataFrame): Dados dos usuários.
        _Loja_Df (DataFrame): Dados das lojas.
        ph (PasswordHasher): Instância do `PasswordHasher` para verificação de senhas.

    Métodos:
        __init__: Inicializa a classe com dados de usuários e lojas, configurando atributos necessários.
        login_type: Solicita ao usuário que escolha um tipo de login (Admin ou Default) e retorna a escolha.
        logar: Processa o login do usuário verificando o nome de usuário e a senha, e atualiza o estado de login conforme o sucesso ou falha.
        logout: Desfaz o login do usuário, redefinindo os atributos relacionados ao login e exibindo uma mensagem de logout.

    Exceções:
        O método `logar` pode gerar erros se as credenciais fornecidas estiverem incorretas ou se houver 
        problemas ao verificar a senha. A exceção específica não é capturada dentro da classe, mas 
        erros genéricos são tratados com mensagens de erro apropriadas.
    """
    def __init__(self, users_estacia, loja_estacia):#
        self.Login_successful = False
        self.password_login = None
        self.user_login = None
        self.user_Type = None
        self.id_user = None
        self.loja_user = None
        self._DataUsers  = users_estacia._DataUsers
        self._Loja_Df = loja_estacia._Loja_Df
        self.ph = PasswordHasher()


    def login_type(self):
        print('---Login---')
        print('1. Admin')
        print('2. Default')

        try:
            opcao=int(input('Informe a escolha: '))
            if opcao == 1:
                self.user_Type = opcao
                return opcao
            elif opcao == 2:
                self.user_Type = opcao
                return opcao
            else:
                print('opção invalida')
                return self.login_type()
        except ValueError:
            print('Apenas Números')
            return self.login_type()
        
    def logar(self):

        def Verificar_usuario():
            tipo_login = self.login_type()

            try:
                self.user_login = input('Usuário: ')
                if self.user_login == '':
                    print('Usuario não pode ser vazio!!')
                    return Verificar_usuario()
            except ValueError:
                return Verificar_usuario()
            
            if tipo_login == 1:
                if self.user_login in self._Loja_Df['Usuario_loja'].values:
                    index = self._Loja_Df[self._Loja_Df['Usuario_loja'] == self.user_login].index[0]
                    self.loja_user = self._Loja_Df.loc[index ,'Usuario_loja']
                    return index, self.user_login, tipo_login
                else:
                    print(f"Usuario Admin não encontrado!!")
                    return Verificar_usuario()
                
            if tipo_login == 2:
                if self.user_login in self._DataUsers['Usuario'].values:
                    index =self._DataUsers[self._DataUsers['Usuario'] == self.user_login].index[0]
                    self.loja_user = self._DataUsers.loc[index, 'Loja']
                    return index , self.user_login, tipo_login
                else:
                    print("Usuario Default não encontrado!!")
                    return Verificar_usuario()
                    
        
        def Verificar_senha(usuario_index, user, type_user):
            try:
                self.password_login = input("Senha: ")
                
                if self.password_login == '':
                    return Verificar_senha(usuario_index=usuario_index, user=user)
            except ValueError:
                print("Senha incorreta!!")
                return Verificar_senha(usuario_index=usuario_index, user=user)
            
            try:
                if type_user == 1:
                    self.ph.verify(self._Loja_Df['Senha'][usuario_index], password=self.password_login)
                    print('Login Feito')
                    self.Login_successful = True
                    return self.Login_successful
                elif type_user == 2:
                    self.ph.verify(self._DataUsers['Senha'][usuario_index], password=self.password_login)
                    print('Login feito!!')
                    self.Login_successful = True
                    return self.Login_successful
            except:
                print("Senha Invalida!!")
                return Verificar_senha(usuario_index=usuario_index, user=user, type_user=type_user)
        
        def Enter_accout():
            usuario_index, self.user_login, tipo_usuario = Verificar_usuario()
            Verificar_senha(usuario_index, self.user_login, tipo_usuario)
            
        return Enter_accout()
    

    def logout(self):
        self.Login_successful = False
        self.password_login = None
        self.user_login = None
        self.user_Type = None

        print("Logout!!")