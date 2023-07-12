# README - Executando uma aplicação Django

Este documento descreve os passos necessários para executar uma aplicação Django localmente.

## Pré-requisitos

Antes de executar a aplicação Django, verifique se você tem os seguintes pré-requisitos instalados:

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação do Django

Se você ainda não tem o Django instalado, siga as etapas abaixo:

1. Abra o terminal ou prompt de comando.

2. Execute o seguinte comando para instalar o Django:

```
pip install django
```

## Configuração do Ambiente

1. Navegue até o diretório raiz do projeto:

```
cd .\project_inventory\
```

2. Crie um ambiente virtual para isolar as dependências do projeto:

```
python3 -m venv myenv
```

4. Ative o ambiente virtual:
- No Linux ou macOS:
  ```
  source myenv/bin/activate
  ```
- No Windows:
  ```
  myenv\Scripts\activate
  ```

5. Instale as dependências do projeto usando o Pip:

```
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Se a aplicação requer um banco de dados, siga estas etapas para configurá-lo:

1. Abra o arquivo `settings.py` localizado na pasta do projeto.

2. Procure a seção de configuração do banco de dados e ajuste as configurações conforme necessário.

3. Crie as migrações para preparar as alterações no banco de dados:

```
python manage.py makemigrations
```

4. Execute as migrações para criar as tabelas no banco de dados:

```
python manage.py migrate
```

## Executando a Aplicação

1. A partir do diretório raiz do projeto, execute o servidor de desenvolvimento do Django:

```
python manage.py runserver
```

2. Abra o navegador da web e acesse `http://localhost:8000/` para visualizar a aplicação em execução.

## Finalizando a Execução

Para parar a execução da aplicação, pressione `Ctrl + C` no terminal onde o servidor de desenvolvimento está sendo executado.

