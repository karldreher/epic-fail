FROM python:3.12.6-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# TODO: Non-urgently, switch to waitress or similar
# TODO: fix user
CMD ["fastapi", "run", "main.py"]