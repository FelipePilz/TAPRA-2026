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

    url = "https://funcapp-tapra-rafaela-amb5hmgscsena7bs.canadacentral-01.azurewebsites.net/api/http_trigger"

    params = {
        "name": "CHAMADO PELA APP FUNCTION"
    }

    try:
        response = requests.get(
            url,
            params=params
        )

        logging.info(f"Resposta do HTTP Trigger: {response.text}")

    except Exception as e:
        logging.error(f"Erro ao chamar o HTTP Trigger: {e}")


# HTTP Trigger
@app.route(
    route="http_trigger",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=["GET"]
)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("TAPRA-2026: HTTP Trigger executada!")

    name = req.params.get("name")

    if name:
        return func.HttpResponse(
            f"Olá, {name}!",
            status_code=200
        )

    return func.HttpResponse(
        "O parâmetro 'name' é obrigatório.",
        status_code=400
    )

