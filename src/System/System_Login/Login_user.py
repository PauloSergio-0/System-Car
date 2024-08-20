from argon2 import PasswordHasher 


class Login():
    def __init__(self, users_estacia):
        self.Login_successful = False
        self.password_login = None
        self.user_login = None
        self._DataUsers  = users_estacia._DataUsers
        self.ph = PasswordHasher()
        
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
                self.password_login = input("Senha: ")
                
                if self.password_login == '':
                    return Verificar_senha(usuario_index=usuario_index, user=user)
            except ValueError:
                print("Senha incorreta!!")
                return Verificar_senha(usuario_index=usuario_index, user=user)
            
            try:
                self.ph.verify(self._DataUsers['Senha'][usuario_index], password=self.password_login)
                print('Login feito!!')
                self.Login_successful = True
                return self.Login_successful
            except:
                print("Senha Invalida!!")
                return Verificar_senha(usuario_index=usuario_index, user=user)
        
        def Enter_accout():
            usuario_index, self.user_login = Verificar_usuario()
            Verificar_senha(usuario_index, self.user_login)
            
        return Enter_accout()
    

    def logout(self):
        self.Login_successful = False
        self.password_login = None
        self.user_login = None
        print("Logout!!")