# 🤖 Agent Task Manager - Trello AI Assistant

![Python](https://img.shields.io/badge/Python-3.14-yellow?logo=python)
![Status](https://img.shields.io/badge/Status-Finalizado-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/cristianorr38/Agent-Task-Manager-Trello)
![License](https://img.shields.io/badge/License-MIT-brown)

Este projeto é um **Agente de Inteligência Artificial** focado em produtividade, projetado para ajudar você a organizar suas tarefas diárias diretamente no Trello! 🚀

Ele utiliza a API do Trello em conjunto com o modelo Gemini (através da biblioteca `google.adk.agents`) para entender comandos em linguagem natural e executar o gerenciamento dos seus cards automaticamente.

---

## ✨ Funcionalidades

O agente atua como um assistente virtual conversacional e possui as seguintes habilidades ("Tools"):

- ➕ **Adicionar Tarefas:** Cria novos cards contendo nome e descrição diretamente na lista "A FAZER" ou "TO DO".
- 📋 **Listar Tarefas:** Permite consultar suas tarefas, podendo filtrar pelo status atual (Todas, A fazer, Em andamento ou Concluído).
- 🔄 **Atualizar Status:** Move os cards entre as listas de forma autônoma para manter o progresso atualizado (ex: de "A fazer" para "Em andamento").
- 🗑️ **Remover Tarefas:** Exclui permanentemente cards do Trello que não são mais necessários ou foram cancelados.
- 🕰️ **Contexto Temporal:** Possui consciência da data e hora atual para auxiliar no planejamento das atividades.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3**
- 🧠 **Google ADK Agents** (Integração com LLM Gemini)
- 📊 **Trello API** (via `py-trello`)
- 🔐 **python-dotenv** (para gerenciamento seguro de credenciais)

---

## ⚙️ Pré-requisitos

Para que o Agente funcione corretamente, você precisará preparar o seu ambiente e o seu Trello:

1. **Credenciais do Trello:** Acesse o Portal de Desenvolvedores do Trello e gere sua `API Key`, `API Secret` e `Token` de acesso.
2. **Configuração do Trello:**
   - Você **DEVE** ter um board chamado exatamente **`Agent_Trello`**.
   - Dentro desse board, crie as listas padrões de trabalho: `A FAZER` (ou `TO DO`), `EM ANDAMENTO` (ou `DOING`) e `CONCLUÍDO` (ou `DONE`).

---

## 🚀 Instalação e Configuração

1. **Instale as dependências necessárias:**
   ```bash
   pip install py-trello python-dotenv google-adk
   ```

2. **Configure o arquivo de ambiente:**
   Crie um arquivo chamado `.env` na raiz do projeto (`c:\Users\cristiano\Documents\Agent04\`) e adicione as seguintes variáveis, substituindo pelos seus dados reais:

   ```env
   TRELLO_API_KEY=sua_trello_api_key_aqui
   TRELLO_API_SECRET=seu_trello_api_secret_aqui
   TRELLO_TOKEN=seu_trello_token_aqui
   # Caso sua biblioteca do Google exija a chave do Gemini via .env:
   # GEMINI_API_KEY=sua_chave_do_google_ai_studio
   ```

---

## 🎮 Como Usar

Com tudo configurado e o arquivo `agent.py` pronto, basta instanciar o agente em seu script principal (`main.py` ou `app.py`). 

Assim que ativado, o assistente virtual cumprimentará você, identificará o dia atual e perguntará quais tarefas você deseja organizar hoje!

### 📦 Release Notes - v1.0.0

#### 🎯 Título
Versão Final - Agent Task Manager - Trello AI Assistant#

#### 👨‍💻 Autor
**Cristiano**  
Analista de Sistemas focado em **Data Science** e **Engenharia de Dados**.

## 📊 Barra de Progresso

Progresso atual:  
`███████████████████████` **100% Concluído**
