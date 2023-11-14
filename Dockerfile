FROM python:3.6.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./app /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]