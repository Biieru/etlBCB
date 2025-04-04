import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(
    df: pd.DataFrame, nome_arquivo: str, separador: str = ";", decimal: str = ","
) -> None:
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


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
    return
