FROM python:3.8-slim-buster

WORKDIR /project

COPY ./data /project/data
COPY ./notebooks /project/notebooks
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]

