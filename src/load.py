import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str = ';', decimal: str = ',') -> None:
    """
    Salva o DataFrame em um arquivo CSV.

    Parâmetros:
    -----------
    df : pd.DataFrame
        O DataFrame a ser salvo.
    nome_arquivo : str
        O nome ou caminho do arquivo onde o DataFrame será salvo.
    separador : str, opcional
        O separador a ser usado no arquivo CSV (padrão é ';').
    decimal : str, opcional
        O caractere utilizado para representar decimais (padrão é ',').

        PS: Esta função não retorna nada, ela apenas salva o DataFrame em um arquivo CSV.
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return
