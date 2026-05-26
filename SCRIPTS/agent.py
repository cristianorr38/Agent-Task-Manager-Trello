from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

api_key = os.getenv('TRELLO_API_KEY')
api_secret = os.getenv('TRELLO_API_SECRET')
token = os.getenv('TRELLO_TOKEN')

def get_temporal_context():
    now = datetime.now()
    return now.strftime('%Y/%m/%d %H:%M:%S')

def adicionar_tarefa(nome_task: str, descricao_task: str, due_date: str):
    try:
        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token
        )

        client.list_boards()
        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'Agent_Trello'][0]
        if not meu_board:
            return "❌ Erro: Board 'Agent_Trello' não encontrado."

        listas = meu_board.list_lists()

        minha_lista = [l for l in listas if l.name.upper() == 'TO DO' or l.name.upper()== 'A FAZER'][0]
        if not minha_lista:
            return "❌ Erro: Lista 'A FAZER' ou 'TO DO' não encontrada."
        
        minha_lista.add_card(
            name=nome_task,
            desc=descricao_task,
            due=due_date
        )

        return f"✅ Tarefa '{nome_task}' adicionada com sucesso."
    
    except Exception as e:
        return f"❌ Erro ao adicionar tarefa: {str(e)}"

def listar_tarefas(status: str= "todas"):
    try:
        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token
        )

        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'Agent_Trello'][0]
        if not meu_board:
            return "❌ Erro: Board 'Agent_Trello' não encontrado."
            
        listas = meu_board.list_lists()

        if status.lower() == 'todas':
            listas_filtradas = listas
        elif status.lower() == 'a fazer':
            listas_filtradas = [l for l in listas if l.name.upper() in ['A FAZER', 'TO DO', 'TODO']]
        elif status.lower() == 'em andamento':
            listas_filtradas = [l for l in listas if l.name.upper() in ['EM ANDAMENTO', 'DOING']]
        elif status.lower() == 'concluído':
            listas_filtradas = [l for l in listas if l.name.upper() in ['CONCLUÍDO', 'CONCLUIDO', 'DONE']]
        else:
            listas_filtradas = listas
        
        tarefas = []

        for lista in listas_filtradas:
            cards = lista.list_cards()
            for card in cards:
                tarefas.append({
                    'nome': card.name,
                    'descricao': card.desc,
                    'vencimento': card.due,
                    'status': lista.name,
                    'id': card.id
                })
        
        return tarefas
    
    except Exception as e:
        return f"❌ Erro ao listar tarefas: {str(e)}"

def mudar_status_tarefa(nome_task: str, novo_status: str) -> str:
    try:
        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token
        )

        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == 'Agent_Trello'][0]
        if not meu_board:
            return "❌ Erro: Board 'Agent_Trello' não encontrado."
            
        listas = meu_board.list_lists()

        status_map = {
            'a fazer': 'A FAZER',
            'em andamento': 'EM ANDAMENTO',
            'concluído': 'CONCLUÍDO'
        }

        nome_lista_destino = status_map.get(novo_status.lower())

        if not nome_lista_destino:
            return f"❌ Status '{novo_status}' não reconhecido. Use 'A fazer', 'Em andamento' ou 'Concluído'."
        
        lista_destino = next(
            (l for l in listas if l.name.upper() == nome_lista_destino.upper()),
            None
        )

        if not lista_destino:
            return f"❌ Lista para status '{novo_status}' não encontrada no Trello."
        
        card_encontrado = None
        lista_origem = None

        for lista in listas:
            cards = lista.list_cards()
            card_encontrado = next(
                (c for c in cards if c.name.lower() == nome_task.lower()),
                None
            )
            if card_encontrado:
                lista_origem = lista
                break

        if not card_encontrado:
            return f"❌ Tarefa '{nome_task}' não encontrada em nenhuma lista do Trello."
        
        card_encontrado.change_list(lista_destino.id)
        return f"✅ Tarefa '{nome_task}' movida para '{novo_status}' com sucesso."
    
    except Exception as e:
        return f"❌ Ocorreu um erro ao tentar mudar o status da tarefa: {str(e)}"

def remover_tarefa(nome_task: str):
    try:
        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token
        )

        boards = client.list_boards()
        meu_board = next((b for b in boards if b.name == 'Agent_Trello'), None)
        if not meu_board:
            return "❌ Erro: Board 'Agent_Trello' não encontrado."
        
        listas = meu_board.list_lists()
        
        for lista in listas:
            cards = lista.list_cards()
            for card in cards:
                if card.name.lower() == nome_task.lower():
                    card.delete()
                    return f"✅ Tarefa '{nome_task}' removida com sucesso."
                    
        return f"❌ Tarefa '{nome_task}' não encontrada no Trello."
    
    except Exception as e:
        return f"❌ Erro ao remover tarefa: {str(e)}"
        
root_agent = Agent(
    model='gemini-1.5-flash',
    name='root_agent',
    description='Agente de organização de tarefas',
    instruction="""
        Você é um agente de organização de tarefas. Sua função é receber uma tarefa e criar um card no Trello com o nome de descrição da tarefa,
        Antes de você começar a perguntar sobre as tarefas, você deve cumprimentar o usuário e se apresentar, explicando que você é um agente de organização de tarefas e que irá ajudar a organizar as tarefas do dia no Trello.
        Você deve perguntar as ativiades que tenho no dia e criar um card para cada atividade, com o nome da atividade e a descrição da atividade.
        Você inicia a conversa assim que for ativado, perguntando quais são as tarefas do dia.
        Sempre inicia a conversa perguntado quais são as tareras do dia informando a data com tool get_temporal_context,
        e depois vá pergunando se tem mais alguma tarefa, até que o usuário diga que não tem mais tarefas.
        Suas funções são:
            1. Adicionar novas tarefas no Trello com nome e descrição da tarefa.
            2. Listar todas as tarefas filtradas por status (pendente, em andamento, concluída).
            3. Marca tarefas como concluídas.
            4. Remover tarefas da listado Trello.
            5. Mudar o status da tarefa(ex: de "A fazer" para "Em andamento" e de "Em andamento" para "Concluída").
""",
    tools=[get_temporal_context, adicionar_tarefa, listar_tarefas, mudar_status_tarefa, remover_tarefa],
)
