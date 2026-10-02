import logging
import azure.functions as func
import os

import pyodbc

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def extract_chamado(myTimer: func.TimerRequest) -> None:

    host_sql = os.getenv("HOST")
    database_sql = os.getenv("DATABASE")
    user_sql = os.getenv("USER")
    pass_sql = os.getenv("PASSWORD")

    #como montar uma string de conexão com o pyodbc azure database sql 

    string_conexao = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host_sql};DATABASE={database_sql};UID={user_sql};PWD={pass_sql}"

conexao = pyodbc.connect(string_conexao)

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM itsm.chamado")

    dados = cursor.fetchall()

    for dado in dados:
        logging.info(dado)

    conexao.close()