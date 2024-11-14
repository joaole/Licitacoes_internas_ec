## Estruturação do Projeto

Licitacoes_internar_ec/
├──licitacao_scraper
│   ├── models/
│   │   ├── database.py          # Conexão e configuração do banco SQL
│   │   └── data_models.py       # Classes que representam os dados
│   ├── spiders/
│   │   ├── site1_spider.py      # Spider 1
│   │   ├── site2_spider.py      # Spider 2
│   │   └── ...                  # Demais spiders
│   ├── controllers/
│   │   ├── data_processor.py    # Módulo de tratamento e limpeza dos dados
│   │   └── database_inserter.py # Módulo para inserir dados no SQL
│   ├── main.py                  # Script principal para iniciar o scraping
|   |──     pipelines.py
|   |──     middlewares.py
│   └── settings.py              # Configurações do Scrapy e projeto
├── venv
└── readne.md

### models/database.py
Esse arquivo é responsável por configurar a conexão com o banco de dados e fornecer uma função para recuperar a conexão sempre que necessário.
- A função get_connection() retorna uma conexão ativa se a conexão for bem-sucedida.
    - Se houver um erro, ele exibe a mensagem e retorna None.

### models/data_models.py
Este arquivo contem funções que representam operações de banco de dados para cada uma das tabelas.

## ntegre o Pipeline de Exportação no Scrapy:

No arquivo settings.py do Scrapy, defina o pipeline de exportação para usar a função de inserção no banco de dados:


### requiments
scrapy, mysql.connection, selenium, webdriver-manger