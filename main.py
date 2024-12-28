from typing import Union
import os
from fastapi import FastAPI
from pydantic_models import Exit

app = FastAPI()


@app.post("/api/exit")
def api_exit(exit_code: Exit):
    # TODO: consider the use of sys.exit() instead of os._exit().  
    # Or, extend the model to allow failing in many different ways.
    # It just has to be chaotic.
    os._exit(exit_code.code)
    return {"exit_code": exit_code}

@app.get("/healthz")
def healthz():
    """
    Used to test the health check of the application.  This is a good health check. 😇
    """
    return {"status": "ok"}

@app.get("/unhealthz", status_code=500)
def evil_healthz():
    """
    Used to test the health check of the application.  In an evil way.
    This assuredly wouldn't work as a healthcheck for very long.

    """
    return {"status": "ok"}
