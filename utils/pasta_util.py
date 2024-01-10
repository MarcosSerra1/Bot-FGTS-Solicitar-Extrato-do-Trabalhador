# pasta_util.py
import os


def criar_pasta(caminho_pasta):
    '''
    Função para criar uma pasta se ela não existir.

    Args:
        caminho_pasta (str): Caminho completo para a pasta.

    Returns:
        bool: True se a pasta foi criada ou já existia,
        False se ocorreu um erro.
    '''
    try:
        # Verifica se a pasta já existe
        if not os.path.exists(caminho_pasta):
            # Se não existir, cria a pasta
            os.makedirs(caminho_pasta)
            print(f"Pasta criada em '{caminho_pasta}'")
        else:
            print(f"A pasta já existe em '{caminho_pasta}'")
        return True
    except Exception as e:
        print(f"Erro ao criar a pasta: {e}")
        return False
