# Donation Management BE

O Donation Management BE é a parte do servidor responsável por fornecer as APIs necessárias para gerenciar doações realizadas de empresas para pessoas físicas.

## Pre-requisitos

- Verifique a instalação do MySql e criar um user root com a senha root (ou modificar em `model\db.py` o user e a senha de conexão com o banco de dados)
- Verifique a instalação de Python 3.x
- Verifique a instalação de Virtualenv

## Instruções de Execução

### Mac/Linux

1. Clone este repositório:

```bash
git clone https://github.com/o-flores/MVP-back.git
cd MVP-back
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

### Windows

1. Clone este repositório:

```bash
git clone https://github.com/o-flores/MVP-back.git
cd MVP-back
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.\venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script para criação de dados iniciais:

```bash
python initialize.py
```

5. Execute a aplicação:

```bash
python app.py
```
