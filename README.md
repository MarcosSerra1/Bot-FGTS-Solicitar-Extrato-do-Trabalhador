# Automatização de Tarefas com Python e PyAutoGUI

Este projeto visa automatizar tarefas específicas relacionadas ao Conectividade Social usando Python e a biblioteca PyAutoGUI para interação com a interface gráfica.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install pyautogui
```

## Estrutura do Projeto

- [main.py](main.py): Módulo principal que contém o menu principal e chama as funções relacionadas.
- [extrato_fgts.py](extrato_fgts.py): Módulo responsável por extrair o extrato do FGTS.
- [pasta_util.py](pasta_util.py): Módulo com funções utilitárias relacionadas a pastas.

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o código principal:

```bash
python main.py
```

## Funcionalidades

### `main.py`

- Menu principal para extrair dados do Conectividade Social.
- Chama funções relacionadas ao extrato do FGTS e à chave do FGTS.

### `extrato_fgts.py`

- Função `extratoFGTS` para extrair o extrato do FGTS interagindo com a interface gráfica.

### `pasta_util.py`

- Função `criar_pasta` para criar uma pasta se ela não existir.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Autor

[Seu Nome]

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.
