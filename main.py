import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL

dadosBcb = requestApiBcb("20191")
# salvarCsv(dadosBcb, "C:/Users/Aluno/Documents/TADS034/etlBCB-main/src/datasets/meiosPagamentosTri.csv", ";", ".")

salvarSQLite(dadosBcb, "src/datasets/etlBCB.db", "meios_pagamentos_tri")

#salvarMySQL(dadosBcb, "root", "teste", "localhost", "etlbcb", "meios_pagamentos_tri")
