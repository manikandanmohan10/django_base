FROM python:3.10.13-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /code

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]