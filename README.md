# Epic-Fail

Epic Fail is an application *designed to fail*.  it can be used as a learning tool, to help appreciate failure modes and simulate incident response and debugging. 


# Architecture
This application is *designed to fail*.  It is a FastAPI web service, and features will be added over time, but the main architectural driver is that *all endpoints should produce a failure mode* with the exception of `/healthz`.  We want the app to be healthy enough to start (usually) but otherwise, API endpoints should exhibit *fantastic, utterly catastrophic failure*.  

# Why would anyone do this? 
![Chaos.](https://media1.tenor.com/m/VlJ2MvxQbL0AAAAd/the-dark-knight-heath-ledger.gif)

# Getting Started
```
pip install -r requirements.txt
fastapi run main.py
```

# API Docs (Swagger)
As a first-class FastAPI application, docs are available on the `/docs` endpoint.
