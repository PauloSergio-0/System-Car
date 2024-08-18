class Login():
    def __init__(self, users_estacia):
        self.Login_successful = False
        self.password = None
        self.user_login = None
        self._DataUsers  = users_estacia._DataUsers
        
    def logar(self):
        
        def Verificar_usuario():
            try:
                self.user_login = input('Usuário: ')
                if self.user_login == '':
                    print('Usuario não pode ser vazio!!')
                    return Verificar_usuario()
            except ValueError:
                return Verificar_usuario()
            
            if self.user_login in self._DataUsers['Nome'].values:
                index =self._DataUsers[self._DataUsers['Nome'] == self.user_login].index[0]
                return index , self.user_login
            else:
                print("erro")
                return Verificar_usuario()
                
        
        def Verificar_senha(usuario_index, user):
            try:
                self.password = input("Senha: ")
                
                if self.password == '':
                    return Verificar_senha()
            except ValueError:
                print("Valor incorreto!!")
                return Verificar_senha()
            
            if self._DataUsers['Senha'][usuario_index] == self.password:
                print('Login feito!!')
                self.Login_successful = True
                return True
            else:
                print("Senha Invalida!!")
                return Verificar_senha(usuario_index=usuario_index, user=user)
        
        def Enter_accout():
            usuario_index, self.user_login = Verificar_usuario()
            Verificar_senha(usuario_index, self.user_login)
            
        return Enter_accout()
            