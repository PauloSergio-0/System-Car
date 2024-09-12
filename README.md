# Sistema de Estoque Global

Este projeto é um sistema de gerenciamento que permite aos usuários administrar lojas, veículos, usuários e vendas. O sistema inclui funcionalidades de login, permissões de usuário e exibe estatísticas das operações realizadas.

## Funcionalidades

- **Login e Cadastro de Usuários e Lojas**: Administradores podem cadastrar lojas e usuários, enquanto os usuários comuns têm acesso limitado às funcionalidades.
  
- **Gerenciamento de Veículos**:
  - Cadastrar veículos
  - Editar nome, quantidade e preço dos veículos
  - Listar veículos cadastrados
  - Registrar vendas e listar vendas realizadas

- **Gerenciamento de Usuários**:
  - Alterar nome, senha, data de nascimento e sexo
  - Listar informações do usuário logado
  
- **Gerenciamento de Lojas**:
  - Alterar informações da loja (nome, senha, país, estado e cidade)
  - Listar informações da loja e estatísticas das operações realizadas

- **Estatísticas**:
  - Exibir estatísticas sobre usuários, veículos e lojas cadastradas

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
