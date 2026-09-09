import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(
    schedule="*/10 * * * * *",
    arg_name="myTimer",
    use_monitor=False
)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    logging.info("TAPRA-2026: Timer Trigger executada!")