import logging
import os

import azure.functions as func
import pyodbc


app = func.FunctionApp()


def extract_table(table_name: str) -> None:
    """
    Extrai os dados de uma tabela do SQL Server.
    """

    logging.info(f"Iniciando extração da tabela itsm.{table_name}")

    sql_server = os.getenv("HOST")
    sql_database = os.getenv("DATABASE")
    sql_user = os.getenv("USER")
    sql_pass = os.getenv("PASSWORD")

    # Valida as variáveis de ambiente
    if not all([sql_server, sql_database, sql_user, sql_pass]):
        raise ValueError(
            "Uma ou mais variáveis de conexão com o SQL Server não foram configuradas."
        )

    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pass};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()

            query = f"SELECT * FROM itsm.{table_name}"

            cursor.execute(query)

            rows = cursor.fetchall()

            logging.info(
                f"Tabela itsm.{table_name}: "
                f"{len(rows)} registros encontrados."
            )

    except Exception:
        logging.exception(
            f"Erro ao ler a tabela itsm.{table_name}"
        )
        raise


# =====================================================
# TIMER TRIGGER - CHAMADO
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_chamado(myTimer: func.TimerRequest) -> None:
    extract_table("chamado")


# =====================================================
# TIMER TRIGGER - CATEGORIA
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_categoria(myTimer: func.TimerRequest) -> None:
    extract_table("categoria")


# =====================================================
# TIMER TRIGGER - ANALISTA
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_analista(myTimer: func.TimerRequest) -> None:
    extract_table("analista")


# =====================================================
# TIMER TRIGGER - CHAMADO SLA
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_chamado_sla(myTimer: func.TimerRequest) -> None:
    extract_table("chamado_sla")


# =====================================================
# TIMER TRIGGER - CHAMADO STATUS HISTORICO
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_chamado_status_historico(myTimer: func.TimerRequest) -> None:
    extract_table("chamado_status_historico")


# =====================================================
# TIMER TRIGGER - CLIENTE ORGANIZACAO
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_cliente_organizacao(myTimer: func.TimerRequest) -> None:
    extract_table("cliente_organizacao")


# =====================================================
# TIMER TRIGGER - CSAT AVALIACAO
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_csat_avaliacao(myTimer: func.TimerRequest) -> None:
    extract_table("csat_avaliacao")


# =====================================================
# TIMER TRIGGER - FILA
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_fila(myTimer: func.TimerRequest) -> None:
    extract_table("fila")


# =====================================================
# TIMER TRIGGER - SLA
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_sla(myTimer: func.TimerRequest) -> None:
    extract_table("sla")


# =====================================================
# TIMER TRIGGER - SOLICITANTE
# =====================================================

@app.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_solicitante(myTimer: func.TimerRequest) -> None:
    extract_table("solicitante")