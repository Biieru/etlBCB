# etlBCB · ETL e análise de dados do Banco Central

Pipeline em **Python** que extrai dados abertos de meios de pagamento do **Banco Central do Brasil**, trata com **pandas** e grava em **SQLite** ou **MySQL**. Depois, notebooks fazem a análise exploratória e testam modelos de previsão (**Prophet** e **Random Forest**) para o gasto com cartão de crédito.

## 🔎 O que o projeto faz

1. **Extract:** consulta a API OData de dados abertos do BCB (Meios de Pagamento Trimestrais) por trimestre
2. **Transform:** normaliza o JSON em DataFrame e converte a coluna de data
3. **Load:** grava o resultado em CSV, SQLite ou MySQL (via SQLAlchemy)
4. **Análise:** estatística descritiva, médias e medianas (Pix, cartões), correlação entre variáveis e modelos de previsão

## 🛠️ Tecnologias

Python · requests · pandas · SQLite · MySQL · SQLAlchemy · PyMySQL · Matplotlib · Seaborn · scikit-learn · Prophet · Jupyter

## 📁 Estrutura

```
etlBCB/
├── main.py                    # roda o ETL (extrai um trimestre e grava no SQLite)
├── src/
│   ├── extractTransform.py    # requestApiBcb(): chamada à API e tratamento
│   ├── load.py                # salvarCsv(), salvarSqlite(), salvarMySql()
│   └── datasets/              # CSV e bancos SQLite gerados
├── Relatorio.ipynb            # análise exploratória dos meios de pagamento
├── analise_pagamentos.ipynb   # médias, medianas e estatística descritiva
├── analise_cartoes.ipynb      # análise das transações com cartão
├── MachineLearning.ipynb      # correlação, Random Forest e Prophet
└── requirements.txt
```

## ▶️ Como rodar

```bash
git clone https://github.com/Biieru/etlBCB.git
cd etlBCB
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

O `main.py` baixa o trimestre `20191` e grava em `src/datasets/etlbcb.db`. Para outro trimestre, troque o parâmetro (formato `AAAAT`, ex.: `20234`). Depois, abra os notebooks com `jupyter notebook`.

## 📈 Principais análises

- Estrutura e qualidade dos dados (tipos, valores faltantes, conversão de datas)
- Médias e medianas por meio de pagamento, com destaque para Pix
- Correlação entre variáveis para escolher preditores do gasto com cartão de crédito
- Random Forest com importância das variáveis
- Série temporal com Prophet

<!-- Dica: coloque aqui 1 ou 2 prints dos gráficos dos notebooks. Arraste a imagem para o editor do GitHub que ele gera o link. -->

## 🔜 Próximos passos

- [ ] Buscar vários trimestres em sequência no `main.py`
- [ ] Ler usuário e senha do MySQL de variáveis de ambiente (`.env`)
- [ ] Testes com `pytest` para extração e carga

## 👤 Autor

**Gabriel Coelho de Araújo** · [dev.to](https://dev.to/bordercansado) · coleho.biel@gmail.com
