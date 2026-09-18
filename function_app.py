import logging
import azure.functions as func
import requests

app = func.FunctionApp()


# Timer Trigger
@app.timer_trigger(
    schedule="*/10 * * * * *",
    arg_name="myTimer",
    use_monitor=False
)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    logging.info("TAPRA-2026: Timer Trigger executada!")

    # URL do HTTP Trigger
    url = "https://funcapp-tapra-rafaela-amb5hmgscsena7bs.canadacentral-01.azurewebsites.net/api/http_trigger"

    # JSON que será enviado no body
    data = {
        "name": "Atividade 3"
    }

    try:
        # Faz POST para o HTTP Trigger
        response = requests.post(
            url,
            json=data
        )

        logging.info(f"HTTP Status: {response.status_code}")
        logging.info(f"Resposta do HTTP Trigger: {response.text}")

    except Exception as e:
        logging.error(f"Erro ao chamar o HTTP Trigger: {e}")


# HTTP Trigger
@app.route(
    route="http_trigger",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=["POST"]
)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("TAPRA-2026: HTTP Trigger executada!")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Body JSON inválido.",
            status_code=400
        )

    name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully.",
            status_code=200
        )

    return func.HttpResponse(
        "O campo 'name' é obrigatório.",
        status_code=400
    )
