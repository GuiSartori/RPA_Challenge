# Automação do RPA Challenge com Selenium

Este projeto contém um bot desenvolvido em Python com a biblioteca Selenium para resolver o desafio proposto no site [RPA Challenge](https://rpachallenge.com/).

O robô lê os dados de uma planilha Excel, navega até o site do desafio, preenche os formulários dinâmicos com os dados lidos e conclui todas as rodadas.

## 🚀 Funcionalidades

-   **Leitura de Dados**: Carrega as informações a serem inseridas no desafio a partir de um arquivo `challenge.xlsx`.
-   **Navegação Web**: Utiliza o Selenium para abrir o navegador (Microsoft Edge), acessar o site e interagir com os elementos da página.
-   **Preenchimento de Formulário**: Localiza os campos do formulário (que mudam de posição a cada rodada) e insere os dados correspondentes.
-   **Logging**: Cria e atualiza um arquivo de log para registrar o progresso da automação, incluindo o início, o fim, cliques em botões, rodadas concluídas e possíveis erros.

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem de programação principal.
-   **Selenium**: Biblioteca para automação de navegadores web.
-   **Pandas**: Biblioteca para leitura e manipulação de dados do arquivo Excel.
-   **Microsoft Edge**: Navegador utilizado para a automação.

## 📋 Pré-requisitos

Antes de executar, certifique-se de que você tem o seguinte instalado:
-   Python 3.x
-   As bibliotecas listadas no arquivo `requirements.txt`.
-   Microsoft Edge.
-   O `msedgedriver.exe` correspondente à sua versão do Microsoft Edge, localizado na pasta `src/utils/`.

## ⚙️ Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Verifique o arquivo de dados:**
    Certifique-se de que o arquivo `challenge.xlsx` está presente na pasta `data/`.

5.  **Execute o script principal:**
    ```bash
    python main.py
    ```
    O robô iniciará, abrirá o navegador e começará a preencher o desafio. Ao final, você poderá consultar o arquivo de log gerado para ver os detalhes da execução.

## 📁 Estrutura do Projeto
Markdown

# Automação do RPA Challenge com Selenium

Este projeto contém um bot desenvolvido em Python com a biblioteca Selenium para resolver o desafio proposto no site [RPA Challenge](https://rpachallenge.com/).

O robô lê os dados de uma planilha Excel, navega até o site do desafio, preenche os formulários dinâmicos com os dados lidos e conclui todas as rodadas.

## 🚀 Funcionalidades

-   **Leitura de Dados**: Carrega as informações a serem inseridas no desafio a partir de um arquivo `challenge.xlsx`.
-   **Navegação Web**: Utiliza o Selenium para abrir o navegador (Microsoft Edge), acessar o site e interagir com os elementos da página.
-   **Preenchimento de Formulário**: Localiza os campos do formulário (que mudam de posição a cada rodada) e insere os dados correspondentes.
-   **Logging**: Cria e atualiza um arquivo de log para registrar o progresso da automação, incluindo o início, o fim, cliques em botões, rodadas concluídas e possíveis erros.

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem de programação principal.
-   **Selenium**: Biblioteca para automação de navegadores web.
-   **Pandas**: Biblioteca para leitura e manipulação de dados do arquivo Excel.
-   **Microsoft Edge**: Navegador utilizado para a automação.

## 📋 Pré-requisitos

Antes de executar, certifique-se de que você tem o seguinte instalado:
-   Python 3.x
-   As bibliotecas listadas no arquivo `requirements.txt`.
-   Microsoft Edge.
-   O `msedgedriver.exe` correspondente à sua versão do Microsoft Edge, localizado na pasta `src/utils/`.

## ⚙️ Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd seu-repositorio
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Verifique o arquivo de dados:**
    Certifique-se de que o arquivo `challenge.xlsx` está presente na pasta `data/`.

5.  **Execute o script principal:**
    ```bash
    python main.py
    ```
    O robô iniciará, abrirá o navegador e começará a preencher o desafio. Ao final, você poderá consultar o arquivo de log gerado para ver os detalhes da execução.

## 📁 Estrutura do Projeto
```
.
├── data/
│   └── challenge.xlsx      # Planilha com os dados de entrada
├── src/
│   └── utils/
│       ├── msedriver.exe   # Driver do Microsoft Edge
│       ├── custom_log.py   # Funções de logging
│       └── data_utils.py   # Funções de manipulação de dados
├── logs/                     # Pasta onde os logs são gerados
├── main.py                   # Script principal da automação
└── README.md                 # Este arquivo
```
