# GreenTrade

O GreenTrade, uma iniciativa inovadora em prol da sustentabilidade, foi concebido com o objetivo de transformar a reciclagem em uma experiência colaborativa e recompensadora. Esta plataforma busca endereçar os desafios ambientais contemporâneos, estabelecendo uma ponte entre empresas e consumidores para promover o consumo e produção responsáveis, alinhados com os Objetivos de Desenvolvimento Sustentável (ODS), especialmente o ODS 12 - Consumo e Produção Responsáveis.

## Necessário para rodar o projeto
- `Python`: Instale o python em [https://www.python.org/downloads/]
- `Mongodb`: Instale o mongodb em [https://www.mongodb.com/try/download/community]

## Como executar o projeto

### Ambiente Windows:

```console
git clone https://github.com/wkauan/GreenTrade.git
cd GreenTrade
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
cd code
python manage.py runserver
```

Se encontrar dificuldades ao iniciar a virtual environment (venv), execute o seguinte comando no terminal: `Set-ExecutionPolicy -scope Process -ExecutionPolicy Bypass`

### Ambiente Linux:

```console
git clone https://github.com/wkauan/GreenTrade.git
cd GreenTrade
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd code
python manage.py runserver
```

### Integrantes

- [Beatriz Honorato](https://github.com/BeatrizHonorato)
- [Kauan Bomfim](https://github.com/wkauan)
- [Larissa Volsi](https://github.com/Lvolsi)
- [Lucas Theodoro](https://github.com/LucasTheodoroSilva)
- [Marcel Araujo](https://github.com/araujomarcel)

### Funções

- Scrum Master: Beatriz Honorato
- Documentação: Larissa Volsi
- Desenvolvedor Back-End: Marcel Araujo
- Desenvolvedor Front-End: Kauan Bomfim
- Banco de dados: Larissa Volsi e Lucas Theodoro
