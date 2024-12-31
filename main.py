from typing import Union
import os
from fastapi import FastAPI
from pydantic_models import Exit, Fibonacci

app = FastAPI()


@app.post("/api/exit")
def api_exit(exit_code: Exit):
    # TODO: consider the use of sys.exit() instead of os._exit().  
    # Or, extend the model to allow failing in many different ways.
    # It just has to be chaotic.
    os._exit(exit_code.code)
    return {"exit_code": exit_code}


fibs = []
@app.post("/api/fibonacci")
def api_fibonacci(length: Fibonacci):
    """
    Add a fibbonaci sequence of length `length` to the global list of fibonacci sequences.
    Return the list of lists of fibonacci sequences.

    This will certainly run the app out of memory if you keep adding to it.
    """
    # TODO: Uniquely identify the fibonacci sequence by timestamp or some other unique identifier.
    global fibs
    fib = [0, 1]
    if length.length == 0:
        fib = []
    elif length.length == 1:
        fib = [0]
    else:
        while len(fib) < length.length:
            fib.append(fib[-1] + fib[-2])
    fibs.append(fib)
    return {"sequences":fibs}

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
