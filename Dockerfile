
FROM python:3.9.9

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 app.py