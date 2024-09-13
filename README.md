# Sistema de Estoque Global

Este projeto é um sistema de gerenciamento que permite aos usuários administrar lojas, veículos, usuários e vendas. O sistema inclui funcionalidades de login, permissões de usuário e exibe estatísticas das operações realizadas.

## Funcionalidades

- **Login e Cadastro de Usuários e Lojas**: Administradores podem cadastrar lojas e usuários, enquanto os usuários comuns têm acesso limitado às funcionalidades.

- **Login**: 
  ## Sistema de Login

  ## Descrição

  A classe `Login` gerencia o processo de autenticação de usuários em um sistema. Ela permite que os usuários façam login e logout, e verifica suas credenciais para determinar se a autenticação foi bem-sucedida.

  ## Funcionalidades

  ### 1. **Inicialização**
    - Recebe instâncias de `users_estacia` e `loja_estacia`.
    - Inicializa variáveis de estado como `Login_successful`, `password_login`, `user_login`, `user_Type`, `id_user`, e `loja_user`.
    - Utiliza a classe `PasswordHasher` para manipulação e verificação de senhas.

  ### 2. **Seleção do Tipo de Usuário**
    - Exibe opções para o tipo de login: Admin ou Default.
    - Solicita ao usuário a escolha e retorna a opção selecionada.
    - Lida com entradas inválidas e solicita nova entrada em caso de erro.

  ### 3. **Login do Usuário**
    - **Verificação do Usuário**:
      - Solicita o nome de usuário e verifica se ele existe nas respectivas bases de dados (Admin ou Default).
      - Se o usuário não for encontrado, solicita uma nova tentativa.
    - **Verificação da Senha**:
      - Solicita a senha e verifica se ela corresponde ao hash armazenado.
      - Se a senha estiver incorreta, solicita uma nova tentativa.
    - Após a autenticação bem-sucedida, define `Login_successful` como `True` e armazena o login do usuário e o tipo de usuário.

  ### 4. **Logout**
    - Define `Login_successful` como `False` e limpa as variáveis relacionadas ao login.
    - Exibe uma mensagem de logout.

- **Gerenciamento de Veículos**:
  ### Classe `Carro`

  A classe `Carro` é responsável pelo gerenciamento de veículos no sistema, incluindo o cadastro, listagem e atualização de dados dos veículos. A seguir, um resumo das principais funcionalidades:

  ### Funcionalidades

  - **Cadastro de Veículos**: Registra novos veículos no sistema, gerando um código único para cada veículo, armazenando informações como marca, modelo, preço, ano e quantidade.
    
  - **Verificação de Ano**: Valida se o ano informado para o veículo é válido, aceitando apenas anos entre 1800 e o ano atual.
    
  - **Verificação de Preço e Quantidade**: Valida o preço e a quantidade de veículos, garantindo que valores inválidos ou negativos sejam tratados corretamente.

  - **Atualização de Dados**: Permite atualizar informações de veículos cadastrados, como marca, modelo, preço e quantidade, além de registrar quem realizou a modificação e a data.

  - **Listagem de Veículos**: Exibe os veículos cadastrados, filtrando por loja e outros critérios.

  - **Interações com Lojas e Usuários**: Integra dados de lojas e usuários para garantir que cada veículo esteja vinculado a uma loja e um responsável pelo cadastro.

  ### Estrutura de Dados

  Os dados dos veículos são armazenados em um DataFrame do `pandas` e salvos em um arquivo CSV (`Car_system.csv`) localizado em `./src/Data/System_data/Carro_data/`. Caso o arquivo não exista, ele será criado automaticamente com as colunas apropriadas.

  ### Arquitetura de Dados

  - `Codigo`: Código único gerado para cada veículo
  - `Marca`: Marca do veículo
  - `Modelo`: Modelo do veículo
  - `Preco`: Preço do veículo
  - `Ano`: Ano de fabricação do veículo
  - `Quantidade`: Quantidade disponível
  - `Data Cadastro`: Data em que o veículo foi cadastrado
  - `Data Modificacao`: Data da última modificação
  - `Loja`: Loja responsável pelo cadastro
  - `Adicionado Por`: Usuário que adicionou o veículo
  - `Modificado Por`: Usuário que modificou o veículo


- **Vendas veiculo**:
  ## Classe `Venda`

  ## Descrição

  A classe `Venda` gerencia as operações relacionadas a vendas de veículos, incluindo a realização de vendas, escolha de métodos de pagamento e listagem de vendas realizadas por um usuário.

  ## Funcionalidades

  ### 1. **Inicialização**
    - Recebe instâncias de `Carro_estancia` e `Login_estacia`.
    - Carrega dados de vendas de um arquivo CSV se existente, ou cria um DataFrame vazio com as colunas necessárias.
    - Inicializa variáveis como `user_login`, `user_type`, e `carro`.

  ### 2. **Método de Pagamento**
    - Exibe opções para o método de pagamento e permite que o usuário selecione uma opção.
    - Se o pagamento for feito com cartão, solicita ao usuário o tipo de cartão (débito ou crédito).
    - Retorna a descrição do método de pagamento escolhido.

  ### 3. **Realizar Venda**
    - Solicita o código do carro e verifica se ele existe no cadastro.
    - Se o carro estiver disponível e a quantidade vendida for válida, atualiza a quantidade no estoque e registra a venda.
    - Cria um código de fatura, calcula o preço total e salva as informações de venda no DataFrame e em um arquivo CSV.
    - Atualiza o arquivo de cadastro de carros com as novas quantidades.

  ### 4. **Listar Vendas**
    - Filtra e exibe as vendas realizadas por um usuário específico.

- **Gerenciamento de Usuários**:
  ### Sistema de Gestão de Usuários

  ### Descrição

  Este projeto é um sistema para gerenciar usuários de uma loja. Ele permite registrar novos usuários, alterar informações de usuários existentes e listar informações detalhadas sobre um usuário.

  ### Funcionalidades

  #### 1. Registro de Loja
  Permite ao usuário escolher e registrar uma loja dentre as opções disponíveis.

  ### 2. Verificação de Senha
  Valida a qualidade da senha com base em critérios como comprimento mínimo, presença de letras maiúsculas e minúsculas, números, caracteres especiais e ausência de espaços. A senha é então criptografada usando o `argon2`.

  ### 3. Verificação de Nome
  Verifica a validade do nome do usuário, garantindo que ele não contenha números ou caracteres especiais e confirmando a entrada com o usuário.

  ### 4. Alteração de Dados do Usuário
  Permite alterar diferentes informações do usuário, como nome, data de nascimento, sexo e senha. Atualizações são salvas em um arquivo CSV.

  ### 5. Cadastro de Usuário
  Registra um novo usuário com informações como nome, data de nascimento, idade, sexo, nome de usuário e senha. Os dados são salvos em um arquivo CSV.

  ### 6. Listar Informações do Usuário
  Exibe informações detalhadas sobre um usuário específico, incluindo nome, sexo, data de nascimento, idade e loja associada.

  ## Estrutura do Projeto

  - `src/Data/System_data/Usuario_data/Usuario_system.csv`: Arquivo CSV que armazena os dados dos usuários.
  - `Users.py`: Arquivo contendo a classe `Users` com todas as funcionalidades descritas.
  
- **Gerenciamento de Lojas**:
  ## Sistema de Gerenciamento de Lojas

  ## Funcionalidades

  ### 1. **Cadastro de Loja**
    - Adiciona uma nova loja ao sistema.
    - Solicita informações como nome da loja, estado, cidade, usuário e senha.
    - A senha é verificada para garantir que atende a critérios de segurança.
    - O usuário é verificado para garantir que não exista um usuário com o mesmo nome.
    - Armazena as informações da loja em um arquivo CSV.

  ### 2. **Verificação de Senha**
    - Verifica a qualidade da senha com base nos seguintes critérios:
      - Comprimento mínimo de 8 caracteres
      - Pelo menos uma letra maiúscula
      - Pelo menos uma letra minúscula
      - Pelo menos um número
      - Pelo menos um caractere especial
      - Não deve conter espaços
    - Utiliza a biblioteca `argon2` para hash da senha.

  ### 3. **Verificação de Usuário**
    - Verifica se o usuário atende aos seguintes critérios:
      - Pelo menos uma letra maiúscula
      - Pelo menos uma letra minúscula
      - Não contém caracteres especiais
    - Verifica se o usuário já existe no sistema.

  ### 4. **Alteração de Dados do Usuário**
    - Permite alterar a senha ou outros dados de um usuário existente.
    - Atualiza os dados no arquivo CSV.

  ### 5. **Listagem de Lojas**
    - Exibe todas as lojas cadastradas no sistema.

  ### 6. **Listagem de Informações da Loja**
    - Exibe informações detalhadas sobre uma loja específica:
      - Nome da loja
      - País
      - Estado
      - Cidade
      - Total de veículos
      - Total de funcionários

- **Estatísticas**:
  ## Sistema de Estatísticas de Lojas

  ## Descrição

  A classe `Estatistica` é responsável por gerar e armazenar estatísticas relacionadas aos usuários, veículos e vendas de uma loja específica. Os dados são filtrados e analisados com base no login do usuário atual, e os resultados são salvos em um arquivo de texto.

  ## Funcionalidades

  ### 1. **Inicialização**
    - Recebe instâncias de `Users`, `Carro`, `Venda`, `Loja`, e `Log_on`.
    - Define o diretório e arquivo para armazenar os dados estatísticos.
    - Cria o diretório se ele não existir.

  ### 2. **Realização de Estatísticas**
    - Filtra dados com base no login do usuário atual.
    - Calcula estatísticas sobre:
      - **Usuários**: Total de vendedores e vendas por vendedor.
      - **Veículos**:
        - Total de veículos, marcas e modelos.
        - Total de veículos por marca.
        - Total de modelos por marca.
        - Quantidade de veículos por combinação de marca e modelo.
    - Salva as estatísticas em um arquivo de texto.

  ### 3. **Mostrar Estatísticas**
    - Gera as estatísticas e exibe o conteúdo do arquivo de texto na tela.

## Tipos de Usuários

- **Admin**: Pode cadastrar lojas e usuários, gerenciar todos os dados e realizar vendas.
- **Usuário Comum**: Pode gerenciar suas próprias informações e visualizar veículos, mas não pode cadastrar novos veículos ou lojas.

## Estrutura de Menus

1. **Menu Inicial**: 
   - Cadastrar loja
   - Login
   - Sair

2. **Menu Principal (pós-login)**:
   - Gerenciamento de veículos
   - Gerenciamento de usuários (dependendo do tipo de usuário)
   - Sair

## Requisitos

- Python 3.8+
- Bibliotecas necessárias listadas em `requirements.txt`

## Como Usar

1. Clone o repositório.
2. Execute o script principal `main.py` para iniciar o sistema.
3. Navegue pelos menus interativos para gerenciar usuários, veículos, lojas e vendas.
