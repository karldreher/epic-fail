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
