# 🤖 Agent Task Manager - Trello AI Assistant

![Python](https://img.shields.io/badge/Python-3.14-silver?logo=python)
![Python](https://img.shields.io/badge/Gemini-gold?logo=google)
![Python](https://img.shields.io/badge/Trello-violet?logo=trello)
![Status](https://img.shields.io/badge/Status-Finalizado-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/cristianorr38/Agent-Task-Manager-Trello)
![License](https://img.shields.io/badge/License-MIT-brown)

Um agente de **Inteligência Artificial** focado em produtividade, projetado para organizar suas tarefas diárias diretamente no **Trello** 🚀.  
Ele utiliza a **API do Trello** em conjunto com o modelo **Gemini (Google ADK Agents)** para entender comandos em linguagem natural e gerenciar seus cards automaticamente.

---

## ✨ Funcionalidades

- ➕ **Adicionar Tarefas**: Cria novos cards contendo nome e descrição diretamente na lista **A FAZER / TO DO**.  
- 📋 **Listar Tarefas**: Consulta suas tarefas, filtrando por status (Todas, A Fazer, Em Andamento, Concluído).  
- 🔄 **Atualizar Status**: Move cards entre listas de forma autônoma (ex: de *A Fazer* → *Em Andamento*).  
- 🗑️ **Remover Tarefas**: Exclui permanentemente cards que não são mais necessários.  
- 🕰️ **Contexto Temporal**: Consciência da data e hora atual para auxiliar no planejamento.  

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.7+**  
- 🧠 **Google ADK Agents (LLM Gemini)**  
- 📊 **Trello API (via py-trello)**  
- 🔐 **python-dotenv** (gerenciamento seguro de credenciais)  

---

## ⚙️ Pré-requisitos

- Conta ativa no **Trello**  
- **Python 3.7+** instalado  
- **pip** (gerenciador de pacotes)  
- Navegador web  

---

## 📦 Instalação e Configuração

   - Instale as **dependências**
     
   ```bash
   pip install -r requirements.txt
   ```

   - Arquivo requirements.txt
   
   ```bash
      google-adk
      py-trello
      datetime
      dotenv
   ```

---

## ⚙️ Configuração do Trello

- Crie um board chamado **Agent_Trello**.  
- Dentro dele, crie as listas:  
  - **A FAZER / TO DO**  
  - **EM ANDAMENTO / DOING**  
  - **CONCLUÍDO / DONE**  

---

## 🔐 Credenciais do Trello

- Gere sua **API Key**, **API Secret** e **Token de acesso** no [Portal de Desenvolvedores Trello](https://trello.com/power-ups/admin/).  
- Crie um arquivo `.env` na raiz do projeto (exemplo: `c:\Users\cristiano\Documents\Agent04\`) com o seguinte conteúdo:

```bash
   TRELLO_API_KEY=sua_trello_api_key_aqui
   TRELLO_API_SECRET=seu_trello_api_secret_aqui
   TRELLO_TOKEN=seu_trello_token_aqui
   GEMINI_API_KEY=sua_chave_do_google_ai_studio
```

---

## 🚀 Como Usar

Com tudo configurado:

- Execute **agent.py** a partir do seu script principal (**main.py** ou **app.py**).  
- O assistente virtual cumprimentará você, identificará o dia atual e perguntará quais tarefas deseja organizar hoje.  

---

## 🔑 Registro e Autorização no Trello

### 1. Criar Power-Up
- Acesse o [Portal Power-Ups Trello](https://trello.com/power-ups/admin/).  
- Clique em **Criar novo Power-Up** e preencha os dados (nome, workspace, email, suporte, autor).  

### 2. Obter API Key e Secret
- Após criar, copie sua **API Key** e **Secret**.  
- Guarde em local seguro.  

### 3. Gerar Token de Autorização
- Use a URL:  

```bash
https://trello.com/1/authorize?expiration=never&name=AppDio&scope=read,write&response_type=token&key=SUA_API_KEY
```

---

## 🔑 Escopos disponíveis

- `read` → leitura de boards/cards  
- `write` → criação/edição/exclusão  
- `account` → acesso à conta  

---

##& 4. Autorizar Aplicativo

- Cole a URL no navegador, revise permissões e clique em **Permitir**.  

---

### 5. Obter Token

- Copie o token exibido e guarde com segurança.  

---

## 📂 Estrutura do Projeto

```bash
📦 Agent-Task-Manager-Trello
 ┣ 📂 SCRIPTS
 ┃   ┗ 📜 agent.py
 ┣ 📂 DOCS
 ┃   ┣ 📜 Instruções_projeto.txt
 ┃   ┗ 📜 requirements.txt
 ┣ 📂 IMAGES
 ┣ 📜 LICENSE
 ┗ 📜 README.md
```

---

### 🖼️ Teste de Execução no VSCode

*(Inserir captura de tela mostrando o agente sendo executado no VSCode)*

---

### 🌐 Interação com o Agente no Browser

*(Inserir captura de tela mostrando a interface do agente funcionando no navegador)*

---

### 📋 Execução das Tarefas no Trello

*(Inserir captura de tela mostrando as listas A FAZER, EM ANDAMENTO e CONCLUÍDO com ca

---

## 👨‍💻 Autor

**Cristiano Rodrigues Rosa**  
Analista de Sistemas focado em **Data Science, Engenharia de Dados e Machine Learning**.  

---

## 📊 Release Notes

**Versão Final - v1.0.0** 

Progresso atual:  
███████████████████████ 100% Concluído

---

## 🚀 Propostas de Melhorias Futuras

- 🔔 **Notificações inteligentes**: integração com e-mail ou Slack para alertar sobre prazos e mudanças nos cards.  
- 📅 **Integração com calendário**: sincronizar tarefas com Google Calendar ou Outlook.  
- 🤝 **Colaboração avançada**: permitir atribuição automática de tarefas a membros da equipe.  
- 📈 **Relatórios e métricas**: dashboards com estatísticas de produtividade e progresso.  
- 🌐 **Suporte multilíngue**: expandir para diferentes idiomas além do português.  
- 🧩 **Plugins adicionais**: integração com outras ferramentas de produtividade como Jira, Asana ou Notion.  

---

## 📜 Licença

Este projeto está licenciado sob os termos da MIT License.
