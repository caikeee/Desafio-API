import requests
import json
from colorama import init, Fore, Style

# Inicializa colorama com autoreset
init(autoreset=True)

# URL base da API
BASE_URL = 'http://127.0.0.1:5000/atividades'

# função que tenta listar as atividades e se der errado o erro ja exibe a mensagem
def listar_atividades():
    try:
        # Envia uma solicitação GET para pegar os dados
        response = requests.get(BASE_URL)
        # se falhar essa solicitação ja gera um 'HTTP erro', pra entender onde esta o erro
        response.raise_for_status()
        # Caso a solicitação de certo ai ja converte as informações do json em uma lista
        atividades = response.json()
        # e aqui exibe essa lista
       # print('Atividades:', atividades)
        print(Fore.GREEN+'atividades:', json.dumps(atividades, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        # Imprime o erro caso a solicitação falhe
        print(f'Erro ao listar atividades: {e}')

def criar_atividade():
    # Dados da nova atividade a ser criada
    nova_atividade = {
        'nome': 'Natação',
        'detalhes': 'Treino na piscina',
        'tipo': 'natação',
        'km': 1.5,
        'esforço': 'alto'
    }
    try:
        # Envia uma solicitação POST com os dados da nova atividade
        response = requests.post(BASE_URL, json=nova_atividade)
        # Levanta uma exceção se a solicitação falhar
        response.raise_for_status()
        # Imprime a resposta da criação da atividade
        print(Fore.GREEN+'Atividade criada com sucesso:', response.json())
    except requests.exceptions.RequestException as e:
        # Imprime o erro caso a solicitação falhe
        print(f'Erro ao criar atividade: {e}')


# pega a informação da atividade selecionando por ID
def obter_atividade(id):
    try:
        # Envia uma solicitação GET para obter uma atividade específica pelo ID
        response = requests.get(f'{BASE_URL}/{id}')
        # Levanta uma exceção se a solicitação falhar
        response.raise_for_status()
        # Converte a resposta JSON em dicionário 
        atividade = response.json()
        # Imprime a atividade
        print(Fore.GREEN+'Atividade:', atividade)
    except requests.exceptions.RequestException as e:
        # Imprime o erro caso a solicitação falhe
        print(f'Erro ao obter atividade: {e}')

def deletar_atividade(id):
    try:
        # Envia uma solicitação DELETE para deletar uma atividade específica pelo ID
        response = requests.delete(f'{BASE_URL}/{id}')
        # Levanta uma exceção se a solicitação falhar
        response.raise_for_status()
        # Imprime a mensagem de sucesso da deleção
        print(Fore.GREEN+'Atividade deletada com sucesso')
    except requests.exceptions.RequestException as e:
        # Imprime o erro caso a solicitação falhe
        print(f'Erro ao deletar atividade: {e}')


#método de uso 
def menu():
    while True:
        print('''
        Menu de requisições da API:

        1 - Listar todas as atividades
        2 - Criar nova atividade
        3 - Selecionar atividade por ID
        4 - Deletar atividade
        5 - Sair
        ''')
        op = int(input('Digite a opção desejada: '))

        if op == 1:
            listar_atividades()
        elif op == 2:
            criar_atividade()
        elif op == 3:
            id = int(input('Digite o ID da atividade: '))
            obter_atividade(id)
        elif op == 4:
            id = int(input('Digite o ID da atividade: '))
            deletar_atividade(id)
        elif op == 5:
            print('Saindo...')
            break
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()