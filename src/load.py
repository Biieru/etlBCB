import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str = ';', decimal: str = ',') -> None:
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return