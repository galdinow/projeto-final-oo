
# Sistema de Gerenciamento de Filmes Vistos

## Descrição da Solução e Funcionalidades

Este projeto é uma **aplicação web desenvolvida em Python com o micro-framework Bottle**, que permite aos usuários gerenciar sua própria coleção de filmes já assistidos.

A aplicação foi desenvolvida seguindo o padrão arquitetural **MVC (Model-View-Controller)**, garantindo uma clara separação de responsabilidades e facilitando a organização do código. A persistência dos dados é realizada em arquivos JSON simples.

### Funcionalidades Implementadas:

* **Cadastro de Usuários:** Permite que novos usuários se registrem na plataforma com nome de usuário, email e senha.
* **Login de Usuários:** Usuários cadastrados podem autenticar-se para acessar as funcionalidades exclusivas da aplicação. (Atualmente, a autenticação é gerenciada no lado do cliente via `localStorage` devido a restrições de tempo, com consciência dos riscos de segurança para um ambiente de produção).
* **Gestão de Filmes:**
    * **Cadastro de Filmes:** Usuários logados podem adicionar novos filmes à sua coleção, registrando informações como título, descrição, diretor e URL de pôster.
    * **Visualização de Filmes:** Exibição detalhada de cada filme cadastrado.
    * (Se você implementou) **Listagem de Filmes:** Listagem de todos os filmes na coleção do usuário.
    * (Se você implementou) **Edição de Filmes:** Funcionalidade para alterar os detalhes de um filme já cadastrado.
    * (Se você implementou) **Exclusão de Filmes:** Permite remover filmes da coleção.

### Pilares da Orientação a Objetos:

O projeto demonstra a aplicação dos quatro pilares da Programação Orientada a Objetos:

* **Abstração:** Classes como `Usuario` e `Movie` abstraem entidades do mundo real com seus atributos e comportamentos essenciais.
* **Encapsulamento:** Atributos de classes são acessados e modificados através de métodos ou propriedades, controlando o acesso direto aos dados.
* **Herança:** Utilização de uma `BaseModel` para compartilhar comportamentos comuns (como `to_dict`) entre diferentes modelos (`Usuario`, `Movie`), promovendo o reuso de código e o polimorfismo.
* **Polimorfismo:** Implementação de métodos com o mesmo nome em classes diferentes que se comportam de maneira específica para cada tipo (ex: `to_dict` em `Usuario` e `Movie`).

---

## Modelagem de Dados


---

## Instalação e Execução

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local.

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # .\venv\Scripts\activate  # No Windows
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Lembre-se de criar o arquivo `requirements.txt` usando `pip freeze > requirements.txt` no seu terminal, dentro do ambiente virtual ativado, antes de enviar o projeto.)*

4.  **Execute a Aplicação:**
    ```bash
    python3 main.py
    ```

5.  **Acesse no Navegador:**
    Abra seu navegador e acesse: `http://localhost:8080`

---

## Autores

* **Pedro Galdino**
* **Carolina Becker**
