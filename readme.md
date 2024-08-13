# Web Scraping Project

Este é um projeto de web scraping avançado em Python.

## Estrutura do Projeto
webscraping_project/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   ├── processor.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   └── test_processor.py
├── requirements.txt
├── README.md
└── .gitignore

## Como Executar

1. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. Execute os testes:
    ```bash
    pytest
    ```

3. Execute o scraper:
    ```python
    from src.scraper import WebScraper
    from src.processor import DataProcessor

    url = 'http://example.com'
    scraper = WebScraper(url)
    content = scraper.fetch_content()
    data = scraper.parse_content(content)

    processor = DataProcessor(data)
    df = processor.process_data()
    processor.save_data(df, 'data/processed/data.csv')
    ```

## Contribuições

Sinta-se à vontade para contribuir com este projeto. Faça um fork e envie um pull request.

