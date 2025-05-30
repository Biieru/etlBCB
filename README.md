# ETLBCB - Extração, Transformação e Análise de Dados do Banco Central do Brasil

Este projeto realiza a extração, transformação e análise de dados do Banco Central do Brasil (BCB), com foco em análise de séries temporais e machine learning.

## 📋 Descrição

O ETLBCB é um projeto que automatiza a coleta de dados do Banco Central do Brasil, realiza transformações necessárias e permite análises avançadas utilizando técnicas de machine learning e séries temporais.

## 🚀 Funcionalidades

- Extração automática de dados do BCB
- Transformação e limpeza dos dados
- Análise exploratória de dados
- Previsões usando Prophet (Facebook)
- Visualizações interativas
- Análise de correlações
- Machine Learning para previsões

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Pandas
- Prophet (Facebook)
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- PyMySQL

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Biieru/etlBCB.git
cd etlBCB
```

2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📊 Estrutura do Projeto

```
etlBCB/
├── src/                    # Código fonte
├── .venv/                  # Ambiente virtual
├── main.py                 # Script principal
├── requirements.txt        # Dependências do projeto
├── MachineLearning.ipynb   # Notebook de Machine Learning
├── Relatorio.ipynb         # Notebook de Análise
└── analise_cartoes.ipynb   # Notebook de Análise de Cartões
```

## 🎯 Como Usar

1. Execute o script principal:
```bash
python main.py
```

2. Para análises mais detalhadas, abra os notebooks Jupyter:
- `MachineLearning.ipynb`: Análises de machine learning e previsões
- `Relatorio.ipynb`: Relatórios e análises gerais
- `analise_cartoes.ipynb`: Análises específicas de cartões

## 📈 Exemplos de Análises

O projeto inclui diversos tipos de análises:
- Previsões de séries temporais usando Prophet
- Análise de correlações entre variáveis
- Visualizações interativas com Plotly
- Modelos de machine learning para previsões

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Autor

[Gabriel Coelho de Araujo] - [business.coleho@gmail.com]
