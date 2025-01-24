FROM python:3.12

WORKDIR /project

COPY . /project

RUN pip install poetry

RUN poetry install --no-root

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]