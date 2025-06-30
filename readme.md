# Meu Letterboxd Simplificado com Bottle

Este é um projeto de aplicação web simplificada, inspirada no Letterboxd, desenvolvido utilizando o micro-framework **Bottle** em Python. Ele serve como um excelente ponto de partida para entender a Programação Orientada a Objetos (POO) e a arquitetura MVC (Model-View-Controller) em um contexto web.

---

## Primeiros Passos

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Configuração do Ambiente Virtual

É **essencial** utilizar um ambiente virtual para isolar as dependências do projeto.

1.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu_projeto_letterboxd
    ```
    (Substitua `seu_projeto_letterboxd` pelo nome real da pasta do seu projeto.)

2.  **Crie o ambiente virtual (se ainda não tiver um):**
    ```bash
    python -m venv venv
    ```
    (Este comando cria uma pasta chamada `venv` dentro do seu projeto.)

3.  **Ative o ambiente virtual:**
    * **No Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    * **No Windows (Prompt de Comando - CMD):**
        ```cmd
        venv\Scripts\activate
        ```
    * **No Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    Você saberá que o ambiente está ativo quando vir `(venv)` no início da linha de comando.

### 2. Instalação das Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias para o projeto:

```bash
pip install -r requirements.txt