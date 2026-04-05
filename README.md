# segunda-fase-jr

# VitaClin — Sistema de Gestão de Pacientes

Sistema web desenvolvido como solução para o case da segunda fase do processo seletivo da InsperJr.

**Acesso ao sistema:** https://vitaclin.onrender.com

>**Atenção:** O sistema utiliza o plano gratuito do Render. Se ficar inativo por mais de 15 minutos, a primeira requisição pode levar até 50 segundos para carregar, isso é normal e esperado. Após esse tempo, o sistema funciona normalmente.

**Credenciais de acesso:**
- Usuário: `vitaclin`
- Senha: `vitaclin2026`

## Acesso pelo Celular

Escaneie o QR Code abaixo para acessar o VitaClin diretamente pelo celular:

![QR Code VitaClin](static/img/qrcode.png)

Ou, após fazer login, acesse o menu **QR Code** para escanear e abrir o sistema no celular.

---

## Sobre o Projeto

A VitaClin é uma clínica que oferece atendimentos em **Fisioterapia**, **Nutrição** e **Psicologia**. Este sistema permite que um usuário autenticado gerencie o cadastro de pacientes de forma simples, visual e eficiente.

### Funcionalidades

- Login com autenticação obrigatória
- Listagem de pacientes em cards visuais por especialidade
- Filtro por especialidade (Fisioterapia, Nutrição, Psicologia)
- Cadastro de novos pacientes com seleção de especialidade
- Visualização da ficha completa do paciente
- Edição de dados existentes
- Remoção de pacientes com confirmação
- QR Code para acesso pelo celular
- Interface responsiva (funciona em desktop e mobile)

---

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Back-end | Python + Django |
| Banco de dados | MongoDB Atlas (pymongo) |
| Front-end | Django Templates + CSS |
| Deploy | Render |
| Autenticação | Django Authentication |

---

## Conexão com a Disciplina TecWeb (Insper 2026/1)

Este projeto aplica diretamente os conhecimentos adquiridos na disciplina de Tecnologias Web:

- **Django** (Aula 04) — estrutura completa com views, templates e formulários
- **CRUD** (Projeto 1B) — o mesmo padrão de criar, listar, editar e remover aplicado a pacientes
- **Deploy no Render** (Aula 06) — publicação com Gunicorn, WhiteNoise e variáveis de ambiente
- **CSS** (Aula 02 / Desafio CSS) — interface responsiva 
- **Filtro por especialidade** — inspirado no sistema de tags do Projeto 1B

A principal adaptação foi o uso de **MongoDB + pymongo** no lugar do SQLite/PostgreSQL, aplicando os mesmos conceitos de persistência aprendidos na disciplina em um banco NoSQL conforme solicitado pelo case.

---

## Como Rodar Localmente

### Pré-requisitos
- Python 3.11+
- Git

### Passos
```bash
# Clone o repositório
git clone https://github.com/helonogueira/segunda-fase-jr.git
cd segunda-fase-jr

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com:
# MONGO_URI=sua_connection_string_do_mongodb_atlas
# MONGO_DB=vitaclin
# SECRET_KEY=sua_chave_secreta
# DEBUG=True

# Rode as migrações
python manage.py migrate

# Crie um usuário
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

---

Desenvolvido por **Heloísa Nogueira** · InsperJr 2026
