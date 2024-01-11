## Bot-FGTS

Este projeto consiste em um bot para interagir com o Conectividade Social, realizando a extração de dados, como Extrato FGTS e Chave FGTS.

### Estrutura do Projeto

```markdown
bot-fgts
│
├── utils
│   ├── __init__.py
│   ├── escolha.py
│   ├── extrato_fgts.py
│   ├── chave_fgts.py
│   └── pasta_util.py
│
├── main.py
│
└── requirements.txt
```

### Configuração

Antes de executar o script, certifique-se de ter todas as dependências instaladas. Para isso, utilize o comando:

```bash
pip install -r requirements.txt
```

### Uso

1. Execute o script `main.py` para acessar o menu principal.
2. Escolha a opção desejada (Extrato FGTS, Chave FGTS, etc.).
3. Siga as instruções apresentadas na tela para fornecer os dados necessários.
4. O bot realizará as interações necessárias no Conectividade Social e extrairá os dados.

### Notas Importantes

- Certifique-se de ter o Google Chrome instalado.

### Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
