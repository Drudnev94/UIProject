# UIProject

A Playwright-based UI automation testing project for the Action-Press website.

## Project Structure

```
UIProject/
├── pages/              # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py    # Base page with common functionality
│   ├── header.py       # Header page object
│   └── main_page.py    # Main page object
├── test/               # Test files
│   ├── __init__.py
│   ├── conftest.py     # Pytest fixtures and configuration
│   └── test_search_page.py
├── data.py             # Test data module
└── README.md
```

## Requirements

- Python 3.8+
- Playwright
- pytest

## Installation

1. Install dependencies:
```bash
pip install playwright pytest
playwright install
```

2. Run tests:
```bash
pytest test/
```

## Usage

The project uses the Page Object Model (POM) design pattern for maintainable UI tests.

Example test:
```python
from pages.header import HeaderPage

def test_search(header: HeaderPage):
    header.search("search query")
```