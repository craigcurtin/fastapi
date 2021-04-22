# FROM artifacts-scm.dstcorp.net/docker-repos/centos/python-36-centos7

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
