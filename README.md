# 📊 ETL - Banco Central do Brasil

Este projeto realiza a **extração, transformação e carga (ETL)** de dados da API pública do Banco Central do Brasil. O objetivo é obter informações sobre meios de pagamento trimestrais e armazená-las em um arquivo **CSV** para posterior análise.


## 📝 Estrutura do Projeto e Arquivos

### Principais arquivos do projeto.

| Arquivo                  | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `main.py`                | Arquivo principal que orquestra o processo ETL.                           |
| `extractTransform.py`    | Responsável pela extração de dados da API.                               |
| `load.py`                | Responsável por salvar os dados em um arquivo CSV.                        |
| `datasets/`              | Pasta onde os arquivos CSV serão armazenados.                            |
| `requeriments.txt`       | Lista as dependências do projeto (requests, pandas).                      |



# 📖 Dicionário
Apenas dos valores principais, para mais detalhes sobre a API, consulte a [documentação oficial](https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/documentacao).
Coluna                   | Tipo      | Descrição
-------------------------|----------|---------------------------------------------
datatrimestre            | datetime | Data do trimestre referenciado
id                       | int      | Identificador único do registro
meioPagamento            | str      | Meio de pagamento (ex: Cartão de Crédito, Pix)
valorTransacionado       | float    | Valor total transacionado no período
quantidadeTransacoes     | int      | Quantidade total de transações no período

### ✒️ Desenvolvido por @Bordercansado


