FROM cr.yandex/crp5qi8v0ihlm4d39hkf/public/python:3.12.2-slim-bullseye

WORKDIR /code

RUN pip install poetry==1.5.1

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root

COPY main.py main.py

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
